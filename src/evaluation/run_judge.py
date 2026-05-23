"""
LLM-as-Judge evaluation entry point.
Supports concurrent execution, checkpoint resume, and error isolation.

Usage: run_judge.sh <dataset> <paradigm> <model> [--prompt MODE] [--workers N] [--max-records N]
       Built-in checkpoint resume — safe to re-run.

Paradigm mapping:
  pointwise → PointwiseJudge   (deepresearch_bench, realdr, verify_bench_hard)
  pairwise  → PairwiseJudge    (wp_bench, ma)
  listwise  → ListwiseJudge    (surge)
"""
import json
import sys
import time
import argparse
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.judge.api_clients.base_client import load_api_config, get_model_interfaces
from src.judge.api_clients.openai_client import OpenAIClient
from src.judge.pointwise_judge import PointwiseJudge
from src.judge.pairwise_judge import PairwiseJudge
from src.judge.listwise_judge import ListwiseJudge
from src.evaluation.datasets import get_dataset_module
from src.evaluation.prompts.get_prompt import get_prompt
from src.utils.io_utils import load_jsonl
from collections import defaultdict

import yaml

# ── Judge class mapping ──
JUDGE_CLASSES = {
    "pointwise": PointwiseJudge,
    "pairwise": PairwiseJudge,
    "listwise": ListwiseJudge,
}

_write_lock = threading.Lock()


def get_output_path(dataset: str, prompt_mode: str, model_name: str) -> Path:
    """Output path: outputs/judge_results/{model_name}/{dataset}/{prompt_mode}.jsonl"""
    out_dir = BASE_DIR / "outputs" / "judge_results" / model_name / dataset
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{prompt_mode}.jsonl"


def dedup_file(output_path: Path, paradigm: str, dataset: str = None) -> int:
    """
    Remove duplicate judge results in-place.
    - pointwise: keep 1 per (data_id, model)
    - pairwise (wp_bench/ma): keep last 2 per canonical key (debiased A/B swap)
    - pairwise (other): keep 1 per canonical key
    - listwise: keep 1 per data_id
    Returns number of removed duplicates.
    """
    if not output_path.exists() or output_path.stat().st_size == 0:
        return 0

    records = []
    with open(output_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not records:
        return 0

    before = len(records)

    if paradigm == "pointwise":
        seen = set()
        deduped = []
        for r in records:
            key = (str(r.get("data_id", "")), str(r.get("model", "")))
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        records = deduped
    elif paradigm == "listwise":
        seen = set()
        deduped = []
        for r in records:
            key = (str(r.get("data_id", "")),)
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        records = deduped
    else:  # pairwise
        if dataset in ("wp_bench", "ma"):
            # Debiased: keep 2 per canonical key (orig + swapped)
            key_groups = defaultdict(list)
            for r in records:
                resp_a = r.get("response_a", "")
                resp_b = r.get("response_b", "")
                m0, m1 = sorted([str(resp_a), str(resp_b)])
                key = (str(r.get("data_id", "")), m0, m1)
                key_groups[key].append(r)
            records = []
            for group in key_groups.values():
                records.extend(group[-2:])  # keep last 2 (most recent judgments)
        else:
            seen = set()
            deduped = []
            for r in records:
                resp_a = r.get("response_a", "")
                resp_b = r.get("response_b", "")
                m0, m1 = sorted([str(resp_a), str(resp_b)])
                key = (str(r.get("data_id", "")), m0, m1)
                if key not in seen:
                    seen.add(key)
                    deduped.append(r)
            records = deduped

    after = len(records)
    if after < before:
        with open(output_path, "w", encoding="utf-8") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    return before - after


def load_completed_keys(output_path: Path, paradigm: str = "pointwise",
                        dataset: str = None) -> set:
    """
    Load set of completed key tuples from existing output file (checkpoint resume).

    - pointwise: 1 result per response, key = (data_id, model)
    - listwise: 1 result per record, key = (data_id,)
    - pairwise: canonical key = (data_id, sorted_model_a, sorted_model_b)
    - wp_bench/ma (debiased): needs 2 rows per canonical key
    """
    if not output_path.exists():
        return set()
    keys = set()
    key_count = {}  # track line count per key (for debiased detection)
    with open(output_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue

            did = record.get("data_id")
            if did is None:
                continue

            if paradigm == "pointwise":
                model = record.get("model")
                if model is not None:
                    keys.add((str(did), str(model)))
            elif paradigm == "listwise":
                # listwise: one output row per record, key = data_id
                keys.add((str(did),))
            else:
                # pairwise: canonical key = (data_id, sorted_model_a, sorted_model_b)
                resp_a = record.get("response_a", "")
                resp_b = record.get("response_b", "")
                m0, m1 = sorted([str(resp_a), str(resp_b)])
                key = (str(did), m0, m1)

                if dataset in ("wp_bench", "ma"):
                    # Debiased: count canonical key occurrences (should be 2)
                    key_count[key] = key_count.get(key, 0) + 1
                else:
                    keys.add(key)

    # Debiased pairwise: each canonical key needs 2 rows (orig+swapped) to be complete
    if dataset in ("wp_bench", "ma") and paradigm == "pairwise":
        for key, count in key_count.items():
            if count >= 2:
                keys.add(key)
        missing = sum(1 for c in key_count.values() if c < 2)
        if missing:
            print(f"  [断点续跑] {dataset} debiased: {missing} 条记录只有 1 行结果，需要补跑")

    # token_exceed records are also treated as completed (never retried)
    te_path = output_path.parent / f"{output_path.stem}_token_exceed{output_path.suffix}"
    if te_path.exists():
        with open(te_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                did = rec.get("data_id")
                if did is None:
                    continue
                if paradigm == "pointwise":
                    models = rec.get("models", [])
                    for m in models:
                        keys.add((str(did), str(m)))
                else:
                    keys.add((str(did),))

    # content_filter records are also treated as completed (never retried)
    cf_path = output_path.parent / f"{output_path.stem}_content_filter{output_path.suffix}"
    if cf_path.exists():
        with open(cf_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                did = rec.get("data_id")
                if did is None:
                    continue
                if paradigm == "pointwise":
                    models = rec.get("models", [])
                    for m in models:
                        keys.add((str(did), str(m)))
                else:
                    keys.add((str(did),))

    return keys


def save_result(result: dict, output_path: Path):
    """Thread-safe append to output file."""
    with _write_lock:
        with open(output_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")


def get_error_path(output_path: Path) -> Path:
    """Error log path: xxx_errors.jsonl (same directory)."""
    return output_path.parent / f"{output_path.stem}_errors{output_path.suffix}"


def load_error_ids(error_path: Path) -> set:
    """Load failed data_ids from error file (skips empty/invalid lines)."""
    if not error_path.exists() or error_path.stat().st_size == 0:
        return set()
    errors = set()
    with open(error_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if rec.get("data_id") is not None:
                    errors.add(str(rec["data_id"]))
            except json.JSONDecodeError:
                continue
    return errors


def save_error(error_rec: dict, error_path: Path):
    """Thread-safe append to error file."""
    with _write_lock:
        with open(error_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(error_rec, ensure_ascii=False) + "\n")


def get_token_exceed_path(output_path: Path) -> Path:
    """Path for max_prompt_tokens exceeded records."""
    return output_path.parent / f"{output_path.stem}_token_exceed{output_path.suffix}"


def get_content_filter_path(output_path: Path) -> Path:
    """Path for content safety filter (data_inspection_failed) records."""
    return output_path.parent / f"{output_path.stem}_content_filter{output_path.suffix}"


def process_one_record(
    item: dict,
    judge,
    paradigm: str,
    prompt_mode: str,
    prompt: dict,
    output_path: Path,
    error_path: Path,
    completed_keys: set,
    judge_model: str = None,
    dataset: str = None,
    reference_map: dict = None,
    criteria_map: dict = None,
) -> int:
    """Process a single record. Returns number of new results. Skips if completed."""
    data_id = str(item.get("id", item.get("data_id", "")))
    if not data_id:
        return 0

    # ── Checkpoint resume: skip completed responses ──
    if paradigm == "pointwise":
        responses = item.get("responses", [])
        pending = [r for r in responses if (data_id, str(r["model"])) not in completed_keys]
        if not pending:
            return 0
        responses_param = pending
    elif paradigm == "listwise":
        if (data_id,) in completed_keys:
            return 0
        responses_param = item.get("responses", [])
    else:
        resps = item.get("responses", [])
        m0 = str(resps[0].get("model", "")) if len(resps) > 0 else ""
        m1 = str(resps[1].get("model", "")) if len(resps) > 1 else ""
        pair_key = (data_id, min(m0, m1), max(m0, m1))
        if pair_key in completed_keys:
            return 0
        responses_param = resps

    # WP-Bench rubric: dynamic genre-based prompt rendering
    if dataset == "wp_bench" and "rubric" in prompt_mode:
        tag = item.get("meta", {}).get("tag", "")
        prompt = get_prompt(dataset, prompt_mode, tag=tag)

    try:
        # Debiased: evaluate both (A,B) and (B,A) orderings then average
        judge_kwargs = {}
        if paradigm == "pairwise" and dataset in ("wp_bench", "ma"):
            judge_kwargs["debiased"] = True

        # Build format_kwargs for extra template placeholders: reference, criteria_list, dimension
        format_kwargs = {}
        if reference_map:
            ref_key = data_id
            # MA reference key is "paper_{id}" while data_id is the full path
            if dataset == "ma" and ref_key not in reference_map:
                paper_key = "_".join(ref_key.split("_")[:2])  # "paper_115"
                if paper_key in reference_map:
                    ref_key = paper_key
            if ref_key in reference_map:
                format_kwargs["reference"] = reference_map[ref_key]
                # MA structure dimension uses its own structural outline reference
                if dataset == "ma":
                    dim = item.get("meta", {}).get("dimension", "")
                    if dim == "structure":
                        struct_key = ref_key + "_structure"
                        if struct_key in reference_map:
                            format_kwargs["reference"] = reference_map[struct_key]
        if criteria_map and data_id in criteria_map:
            format_kwargs["criteria_list"] = criteria_map[data_id]
        if dataset == "ma":
                format_kwargs["dimension"] = dim
        judge_kwargs["format_kwargs"] = format_kwargs

        results = judge.judge(
            instruction=item.get("instruction", ""),
            responses=responses_param,
            prompt_template=prompt,
            data_id=data_id,
            **judge_kwargs,
        )
        new_count = 0
        for r in results:
            r["dataset"] = item.get("dataset", "")
            r["paradigm"] = paradigm
            r["prompt_mode"] = prompt_mode
            r["judge_model"] = judge_model or judge.model_name
            save_result(r, output_path)
            new_count += 1
            # Update completed_keys to prevent duplicates within the same run (retry, etc.)
            if paradigm == "pointwise":
                completed_keys.add((data_id, str(r["model"])))
        # pairwise/listwise: mark complete only after all results are written
        if new_count > 0:
            if paradigm == "listwise":
                completed_keys.add((data_id,))
            elif paradigm == "pairwise" and pair_key:
                completed_keys.add(pair_key)
        return new_count
    except Exception as e:
        error_str = str(e)
        error_record = {"data_id": data_id, "error": error_str}
        if any(kw in error_str for kw in ("exceeded max_prompt_tokens", "maximum context length",
                                           "context_length_exceeded", "Range of input length")):
            te_path = get_token_exceed_path(output_path)
            # Token exceed: treat as valid output, record and mark completed (no retry)
            if paradigm == "pointwise":
                failed_models = [str(r["model"]) for r in responses_param]
                error_record["models"] = failed_models
                for m in failed_models:
                    completed_keys.add((data_id, m))
            else:
                completed_keys.add((data_id,))
            with _write_lock:
                with open(te_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(error_record, ensure_ascii=False) + "\n")
            print(f"  [token超限] data_id={data_id}: max_prompt_tokens 超出，不再重试")
        elif any(kw in error_str for kw in ("inappropriate content", "data_inspection_failed")):
            cf_path = get_content_filter_path(output_path)
            # Content filter: treat as valid outcome, record and mark completed (no retry)
            if paradigm == "pointwise":
                failed_models = [str(r["model"]) for r in responses_param]
                error_record["models"] = failed_models
                for m in failed_models:
                    completed_keys.add((data_id, m))
            else:
                completed_keys.add((data_id,))
            with _write_lock:
                with open(cf_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(error_record, ensure_ascii=False) + "\n")
            print(f"  [内容限制] data_id={data_id}: 内容违反安全策略，不再重试")
        else:
            save_error(error_record, error_path)
            print(f"  [错误] data_id={data_id}: {e}")
        return 0


def run_evaluation(
    dataset: str,
    paradigm: str,
    model_name: str,
    prompt_mode: str = "vanilla",
    num_workers: int = 8,
    max_records: int = None,
):
    """Main evaluation pipeline."""
    print(f"数据集:     {dataset}")
    print(f"范式:       {paradigm}")
    print(f"Prompt:     {prompt_mode}")
    print(f"模型:       {model_name}")
    print(f"并发数:     {num_workers}")
    print(f"断点续跑:   默认启用")

    # ── 1. Validate paradigm ──
    judge_cls = JUDGE_CLASSES.get(paradigm)
    if not judge_cls:
        print(f"错误: 不支持的范式 '{paradigm}'，可选: {list(JUDGE_CLASSES.keys())}")
        sys.exit(1)

    # SurGE uses ListwiseJudge for batch scoring; supports legacy pointwise calls
    if dataset == "surge" and paradigm == "pointwise":
        from src.judge.listwise_judge import ListwiseJudge
        judge_cls = ListwiseJudge

    # ── 2. Get dataset module ──
    try:
        mod = get_dataset_module(dataset)
    except KeyError as e:
        print(f"错误: {e}")
        sys.exit(1)

    ds_paradigm = mod.get_paradigm()
    if paradigm != ds_paradigm:
        print(f"警告: {dataset} 默认范式为 {ds_paradigm}，当前使用 {paradigm}，请确保 extract_metrics 兼容")

    # ── 3. Load API config ──
    api_config = load_api_config()
    interfaces = get_model_interfaces(api_config, target_models=[model_name])
    if not interfaces:
        print(f"错误: 未找到模型 {model_name} 的 API 配置")
        sys.exit(1)
    model_info = interfaces[0]
    print(f"API 接口:   {model_info['name']} @ {model_info['api_base']}")

    # ── 4. Load evaluation config ──
    with open(BASE_DIR / "config" / "judge_config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    eval_cfg = config.get("evaluation", {})

    # Model-specific max_tokens overrides global config
    model_mt = model_info.get("max_tokens")
    if model_mt:
        eval_cfg = {**eval_cfg, "max_tokens": model_mt}
        print(f"  max_tokens: {model_mt} (模型专属)")

    # ── 5. Load prompt template ──
    prompt = get_prompt(dataset, prompt_mode)
    print(f"提示词:     config/prompts/{dataset}/{prompt_mode}.yaml")

    # ── 6. Initialize client and Judge ──
    model_mpt = model_info.get("max_prompt_tokens",
                                eval_cfg.get("max_prompt_tokens", 120000))
    client = OpenAIClient(api_base=model_info["api_base"], api_key=model_info["api_key"],
                          max_prompt_tokens=model_mpt,
                          extra_body=model_info.get("extra_body", {}),
                          api_model=model_info.get("api_model"))
    judge = judge_cls(model_name, client, eval_cfg)

# ── 7. Load data (handled by dataset module) ──
    data = mod.load_data()
    print(f"数据:       {len(data)} 条")

    if max_records and max_records < len(data):
        data = data[:max_records]
        print(f"  限制: 取前 {max_records} 条")

    # Load reference and criteria data for format_kwargs injection
    reference_map = {}
    ref_path = BASE_DIR / "data_standardized" / f"{dataset}_reference.jsonl"
    if ref_path.exists():
        for entry in load_jsonl(ref_path):
            reference_map[str(entry.get("id", ""))] = entry.get("reference", "")

    criteria_map = {}
    crit_path = BASE_DIR / "data_standardized" / f"{dataset}_criteria.jsonl"
    if crit_path.exists():
        for entry in load_jsonl(crit_path):
            criteria_map[str(entry.get("id", ""))] = entry.get("criteria_text", "")

    # ── 8. Dedup + load existing output (checkpoint resume, skip completed) ──
    output_path = get_output_path(dataset, prompt_mode, model_name)
    error_path = get_error_path(output_path)
    removed = dedup_file(output_path, paradigm, dataset=dataset)
    if removed:
        print(f"  清理了 {removed} 条重复记录")
    completed_keys = load_completed_keys(output_path, paradigm, dataset=dataset)
    if completed_keys:
        print(f"  已有 {len(completed_keys)} 条已完成，跳过")

    # ── 9. Concurrent execution ──
    print(f"\n开始评测 ...")
    start_time = time.time()
    total_new = 0

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {
            executor.submit(
                process_one_record,
                item,
                judge,
                paradigm,
                prompt_mode,
                prompt,
                output_path,
                error_path,
                completed_keys,
                model_name,
                dataset,
                reference_map=reference_map,
                criteria_map=criteria_map,
            ): item
            for item in data
        }

        done_count = 0
        total = len(data)
        for future in as_completed(futures):
            done_count += 1
            try:
                n = future.result()
                total_new += n
            except Exception as e:
                print(f"  [线程错误] {e}")
            if done_count % max(1, total // 10) == 0 or done_count == total:
                elapsed = time.time() - start_time
                print(f"  进度: {done_count}/{total} ({elapsed:.0f}s)")

    elapsed = time.time() - start_time
    total_count = total_new
    print(f"\n完成！")
    print(f"  新增结果: {total_new} 条")
    print(f"  总耗时:   {elapsed:.1f}s")
    print(f"  输出文件: {output_path}")

    # ── 10. Auto-retry failed records ──
    max_retries = 1
    for retry in range(1, max_retries + 1):
        error_ids = load_error_ids(error_path)
        if not error_ids:
            break

        # Clear error file; retry results will be re-written
        error_path.write_text("")

        retry_data = []
        for item in data:
            item_id = str(item.get("id", item.get("data_id", "")))
            if item_id in error_ids:
                retry_data.append(item)

        if not retry_data:
            break

        print(f"\n=== 第 {retry} 轮重试（{len(retry_data)} 条）===")
        retry_start = time.time()
        retry_new = 0

        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = {
                executor.submit(
                    process_one_record,
                    item, judge, paradigm, prompt_mode, prompt,
                    output_path, error_path, completed_keys,
                    model_name, dataset,
                    reference_map=reference_map,
                    criteria_map=criteria_map,
                ): item
                for item in retry_data
            }

            done_count = 0
            rtotal = len(retry_data)
            for future in as_completed(futures):
                done_count += 1
                try:
                    n = future.result()
                    retry_new += n
                    total_count += n
                except Exception as e:
                    print(f"  [线程错误] {e}")
                if done_count == rtotal or done_count % max(1, rtotal // 5) == 0:
                    elapsed_retry = time.time() - retry_start
                    print(f"  进度: {done_count}/{rtotal} ({elapsed_retry:.0f}s)")

        r_elapsed = time.time() - retry_start
        remaining = load_error_ids(error_path)
        if remaining:
            print(f"  第 {retry} 轮: 新增 {retry_new} 条, 仍有 {len(remaining)} 条失败 ({r_elapsed:.1f}s)")
        else:
            print(f"  第 {retry} 轮: 新增 {retry_new} 条, 全部成功 ({r_elapsed:.1f}s)")

    # Token exceed & content filter summary
    te_path = get_token_exceed_path(output_path)
    te_count = 0
    if te_path.exists():
        with open(te_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    te_count += 1

    cf_path = get_content_filter_path(output_path)
    cf_count = 0
    if cf_path.exists():
        with open(cf_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    cf_count += 1

    final_errors = load_error_ids(error_path)
    summary_parts = [f"总计 {total_count} 条"]
    if te_count > 0:
        summary_parts.append(f"token超限 {te_count} 条")
    if cf_count > 0:
        summary_parts.append(f"内容限制 {cf_count} 条")
    if final_errors:
        summary_parts.append(f"其他错误 {len(final_errors)} 条")

    print(f"\n  {' | '.join(summary_parts)}")
    if te_count > 0:
        print(f"  → token超限明细: {te_path.name}")
    if cf_count > 0:
        print(f"  → 内容限制明细: {cf_path.name}")
    if final_errors:
        print(f"\n警告: 仍有 {len(final_errors)} 条记录因其他错误失败，请检查网络后重新运行")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="LLM-as-Judge 评测")
    parser.add_argument("dataset", help="数据集名称 (deepresearch_bench / realdr / surge / wp_bench / ma / verify_bench_hard)")
    parser.add_argument("paradigm", help="Judge 范式 (pointwise / pairwise / listwise)")
    parser.add_argument("model", help="Judge 模型名称 (如 gpt-4o-mini)")
    parser.add_argument("--prompt", default="vanilla", help="Prompt 模式 (默认: vanilla)")
    parser.add_argument("--workers", type=int, default=8, help="并发线程数 (default: 8)")
    parser.add_argument("--max-records", type=int, default=None, help="限制处理条数（测试用）")

    args = parser.parse_args()

    run_evaluation(
        dataset=args.dataset,
        paradigm=args.paradigm,
        model_name=args.model,
        prompt_mode=args.prompt,
        num_workers=args.workers,
        max_records=args.max_records,
    )


if __name__ == "__main__":
    main()

"""
Reliability computation: compare judge outputs against ground truth.
Computes ACC, Spearman, Kendall via per-dataset extract_metrics().

Pointwise / Listwise → ACC + Spearman + Kendall
Pairwise → ACC only

Usage: python src/evaluation/compute_reliability.py <dataset> <paradigm> <model> --prompt <mode>
"""
import json
import sys
from pathlib import Path

import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.reliability.agreement_metrics import (
    #compute_all_metrics,
    average_per_query_metrics,  # per-query
    average_per_query_accuracy,  # per-query
    pairwise_accuracy,
    spearman_corr,
    kendalls_tau,
)
from src.utils.io_utils import load_jsonl
from src.evaluation.datasets import get_dataset_module
from src.evaluation.run_judge import dedup_file


def compute_group_metrics(group_data: dict, per_query_data: dict = None, extra_zero_pairs: int = 0) -> dict:
    """Compute metrics for one (gt, pred) group.

    Args:
        group_data: {"gt": [...], "pred": [...]}
        per_query_data: {query_id: {"gt": [...], "pred": [...]}} — if provided, ACC is per-query aggregated
    """
    gt = group_data.get("gt", [])
    pred = group_data.get("pred", [])
    if len(gt) < 2:
        return {"n": len(gt), "accuracy": None, "spearman": None, "kendall": None}

    # Auto-detect binary data (all values ∈ {0,1}) → use simple ACC
    all_vals = set(gt) | set(pred)
    is_binary = all_vals.issubset({0, 1})

    # ACC: per-query aggregated if per_query_data provided, else global
    if per_query_data:
        if is_binary:
            # Binary per_query: simple ACC
            total_correct = 0
            total_samples = 0
            for data in per_query_data.values():
                qgt = data.get("gt", [])
                qpred = data.get("pred", [])
                for g, p in zip(qgt, qpred):
                    total_correct += (1 if g == p else 0)
                    total_samples += 1
            accuracy = round(total_correct / total_samples, 4) if total_samples > 0 else None
            acc_correct, acc_total = total_correct, total_samples
        else:
            acc_metrics = average_per_query_accuracy(per_query_data)
            accuracy = acc_metrics["accuracy"]
            acc_correct = acc_metrics["correct"]
            acc_total = acc_metrics["total"]
    elif is_binary:
        # Binary global: simple ACC
        correct = sum(1 for g, p in zip(gt, pred) if g == p)
        total = len(gt)
        accuracy = round(correct / total, 4) if total > 0 else None
        acc_correct, acc_total = correct, total
    else:
        gt_arr = np.array(gt)
        pred_arr = np.array(pred)
        acc, correct, total = pairwise_accuracy(gt_arr, pred_arr)
        accuracy = round(acc, 4) if not np.isnan(acc) else None
        acc_correct, acc_total = correct, total

    # ── Error adjustment: token_exceed / content_filter contribute 0-correct pairs ──
    if extra_zero_pairs > 0:
        acc_total += extra_zero_pairs
        accuracy = round(acc_correct / acc_total, 4) if acc_total > 0 else None

    # Spearman / Kendall — skip binary data (ranking is meaningless for correct/incorrect)
    sp = kt = None
    if not is_binary:
        unique_gt = len(set(gt))
        unique_pred = len(set(pred))
        if unique_gt >= 2 and unique_pred >= 2:
            sp = round(spearman_corr(gt, pred), 4)
            kt = round(kendalls_tau(gt, pred), 4)

    return {
        "n": len(gt),
        "accuracy": accuracy,
        "accuracy_correct": acc_correct,
        "accuracy_total": acc_total,
        "spearman": sp,
        "kendall": kt,
    }


def save_reliability_results(results: dict, output_path: Path):
    """Save reliability results to JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"  Saved: {output_path}")


def compute(dataset: str, prompt_mode: str, model_name: str):
    """Compute reliability metrics for one (dataset, prompt_mode, model) tuple."""
    paradigm_map = {
        "deepresearch_bench": "pointwise",
        "realdr": "pointwise",
        "surge": "listwise",
        "wp_bench": "pairwise",
        "ma": "pairwise",
        "verify_bench_hard": "pointwise",
    }

    result_path = BASE_DIR / "outputs" / "judge_results" / model_name / dataset / f"{prompt_mode}.jsonl"
    if not result_path.exists():
        print(f"[跳过] 文件不存在: {result_path}")
        return

    paradigm = paradigm_map.get(dataset, "pointwise")

    # Dedup before loading to avoid duplicate records skewing metrics
    removed = dedup_file(result_path, paradigm, dataset=dataset)
    if removed:
        print(f"  去重: 清理了 {removed} 条重复记录")

    judge_results = load_jsonl(result_path)
    if not judge_results:
        print(f"[跳过] 无有效结果: {result_path}")
        return

    gt_path = BASE_DIR / "ground_truth" / f"{dataset}_gt.jsonl"
    gt_data = load_jsonl(gt_path)
    if not gt_data:
        print(f"[跳过] 真值文件为空: {gt_path}")
        return

    # ── Token exceed & content filter statistics ──
    te_count = 0
    te_path = BASE_DIR / "outputs" / "judge_results" / model_name / dataset / f"{prompt_mode}_token_exceed.jsonl"
    if te_path.exists():
        te_data = load_jsonl(te_path)
        te_count = len(te_data)

    cf_count = 0
    cf_path = BASE_DIR / "outputs" / "judge_results" / model_name / dataset / f"{prompt_mode}_content_filter.jsonl"
    if cf_path.exists():
        cf_data = load_jsonl(cf_path)
        cf_count = len(cf_data)

    total_with_errors = len(judge_results) + te_count + cf_count
    te_error_rate = round(te_count / total_with_errors, 4) if total_with_errors > 0 else 0.0
    cf_error_rate = round(cf_count / total_with_errors, 4) if total_with_errors > 0 else 0.0

    print(f"\n=== {dataset} ({paradigm}, {prompt_mode}, {model_name}) ===")
    print(f"  Judge 结果: {len(judge_results)} 条")
    if te_count > 0:
        print(f"  token超限:  {te_count} 条 (error_rate={te_error_rate})")
    if cf_count > 0:
        print(f"  内容限制:  {cf_count} 条 (error_rate={cf_error_rate})")
    print(f"  真值:       {len(gt_data)} 条")

    # Extract metrics via dataset module
    mod = get_dataset_module(dataset)
    extracted = mod.extract_metrics(judge_results, gt_data)

    # Build output structure
    out = {
        "dataset": dataset,
        "paradigm": paradigm,
        "prompt_mode": prompt_mode,
        "judge_model": model_name,
        "groups": {},
        "token_exceed": {
            "count": te_count,
            "total_success": len(judge_results),
            "error_rate": te_error_rate,
        },
        "content_filter": {
            "count": cf_count,
            "total_success": len(judge_results),
            "error_rate": cf_error_rate,
        },
    }

    # Read per-query data if available
    per_query_raw = extracted.get("per_query", {})

    # Iterate groups (shared by pairwise/pointwise/listwise)
    groups = extracted.get("groups", {})

    # ── Error adjustment: derive expected entries per query from GT, count missing as 0-correct pairs ──
    error_extra_pairs = {}
    if per_query_raw:
        from collections import Counter
        # Build GT → expected entry count per query
        gt_expected = {}
        if dataset == "surge":
            for g in gt_data:
                gid = str(g["id"])
                n = len(g.get("structure_ranking", {})) - 1  # always exclude GT → 3 models → 3 pairs
                if n >= 2:
                    gt_expected[gid] = n
        elif dataset == "deepresearch_bench":
            for g in gt_data:
                gid = str(g["id"])
                n = len(g.get("aggregated", {}))  # expected number of models per topic
                if n >= 2:
                    gt_expected[gid] = n
        elif dataset == "realdr":
            task_counts = Counter()
            for g in gt_data:
                task_counts[str(g["task_id"])] += 1
            for tid, n in task_counts.items():
                if n >= 2:
                    gt_expected[tid] = n

        if gt_expected:
            for group_name, pq in per_query_raw.items():
                gd = groups.get(group_name, {})
                # Only adjust groups with actual data (exclude empty groups from prompt mismatch)
                if len(gd.get("gt", [])) < 2:
                    continue
                total_extra = 0
                for qkey, exp_n in gt_expected.items():
                    actual_n = len(pq.get(qkey, {}).get("gt", []))
                    if actual_n < exp_n:
                        k = exp_n - actual_n
                        extra = k * (2 * exp_n - k - 1) // 2  # C(exp,2) - C(act,2)
                        total_extra += extra
                if total_extra > 0:
                    error_extra_pairs[group_name] = total_extra

    for group_name, group_data in sorted(groups.items()):
        pq_for_group = per_query_raw.get(group_name)
        # Pairwise datasets return pre-computed metrics, no gt/pred arrays
        if "gt" not in group_data:
            metrics = group_data
        else:
            metrics = compute_group_metrics(group_data, pq_for_group, extra_zero_pairs=error_extra_pairs.get(group_name, 0))
        out["groups"][group_name] = metrics
        status = ""
        n = metrics.get("n", 0)
        if n >= 2 and metrics.get("accuracy") is not None:
            acc_label = "perQ ACC" if pq_for_group else "ACC"
            status = f"{acc_label}={metrics['accuracy']:.4f}"
            if metrics.get("accuracy_total"):
                status += f" ({metrics['accuracy_correct']}/{metrics['accuracy_total']})"
            if metrics.get("spearman") is not None:
                status += f", Sp={metrics['spearman']:.4f}, τ={metrics['kendall']:.4f}"
        else:
            status = "样本不足"

        # Per-query Spearman/Kendall
        pq = per_query_raw.get(group_name)
        if pq:
            pq_metrics = average_per_query_metrics(pq)
            out.setdefault("per_query", {})[group_name] = pq_metrics
            if pq_metrics["spearman"] is not None:
                status += f" | perQ Sp={pq_metrics['spearman']:.4f}, τ={pq_metrics['kendall']:.4f}"
            elif pq_metrics["n_queries_spearman"] > 0:
                status += f" | perQ n={pq_metrics['n_queries_spearman']} (all <3 pts)"

        print(f"  [{group_name}] n={n}, {status}")

    # Save results
    out_path = BASE_DIR / "outputs" / "reliability_scores" / model_name / dataset / f"{prompt_mode}.json"
    save_reliability_results(out, out_path)


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Compute LLM-Judge reliability metrics")
    parser.add_argument("dataset", nargs="?", default=None, help="Dataset name")
    parser.add_argument("paradigm", nargs="?", default=None, help="Judge paradigm (for output only; determined by dataset)")
    parser.add_argument("model", nargs="?", default=None, help="Model name (without prompt_mode prefix)")
    parser.add_argument("--prompt", default="vanilla", help="Prompt mode (default: vanilla)")

    args = parser.parse_args()

    all_datasets = ["deepresearch_bench", "surge", "wp_bench", "realdr",
                     "ma", "verify_bench_hard"]

    if args.dataset:
        compute(args.dataset, args.prompt, args.model or "gpt-4o-mini")
    else:
        for ds in all_datasets:
            judge_base = BASE_DIR / "outputs" / "judge_results"
            if not judge_base.exists():
                continue
            for model_dir in sorted(judge_base.iterdir()):
                if not model_dir.is_dir():
                    continue
                ds_dir = model_dir / ds
                if not ds_dir.exists():
                    continue
                for fpath in sorted(ds_dir.glob("*.jsonl")):
                    if fpath.stem.endswith("_errors") or fpath.stem.endswith("_token_exceed"):
                        continue
                    prompt_mode = fpath.stem  # filename is the prompt_mode
                    model = model_dir.name
                    compute(ds, prompt_mode, model)


if __name__ == "__main__":
    main()

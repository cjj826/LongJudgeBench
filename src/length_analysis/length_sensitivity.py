# -*- coding: utf-8 -*-
"""
Length Sensitivity Analysis
============================
For each dataset, bucket pairwise comparisons by average token length
of two candidate outputs, and report ACC per bucket.

Two bucketing modes:
  1. Fixed buckets (default): <3K / 3-8K / 8-16K / >16K
  2. Adaptive buckets (--adaptive): 4 equal-sized buckets by quartile

Usage:
    python -m src.length_analysis.length_sensitivity qwen3-max vanilla
    python -m src.length_analysis.length_sensitivity qwen3-max vanilla --adaptive
"""
import json
import sys
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl
from src.utils.token_counter import count_tokens

FIXED_BUCKETS = [(0, 3000), (3000, 8000), (8000, 16000), (16000, float("inf"))]
FIXED_NAMES = ["<3K", "3-8K", "8-16K", ">16K"]


def get_fixed_bucket(avg_len: int) -> int:
    for i, (lo, hi) in enumerate(FIXED_BUCKETS):
        if lo <= avg_len < hi:
            return i
    return len(FIXED_BUCKETS) - 1


def build_content_length_map(dataset: str) -> dict:
    """Load standardized data and build {(data_id, model): token_count} mapping."""
    path = BASE_DIR / "data_standardized" / f"{dataset}.jsonl"
    res = {}
    for rec in load_jsonl(path):
        did = str(rec["id"])
        for resp in rec.get("responses", []):
            res[(did, resp.get("model", ""))] = count_tokens(resp.get("content", ""))
    return res


def to_buckets(pairs: list, adaptive: bool) -> dict:
    """
    Bucket pairs by avg_len.

    Args:
        pairs: [(avg_len, is_correct), ...]
        adaptive: True for 4 equal-sized quartile buckets, False for fixed boundaries.
    Returns:
        {name: {"accuracy": float or None, "correct": int, "total": int, "range": (lo, hi)}}
    """
    def _safe_range(r):
        """Convert float('inf') to None for JSON-safe serialization."""
        return tuple(None if v == float("inf") else v for v in r)

    if not pairs:
        return {n: {"accuracy": None, "correct": 0, "total": 0, "range": (0, 0)}
                for n in (FIXED_NAMES if not adaptive else ["Q1", "Q2", "Q3", "Q4"])}

    if not adaptive:
        buckets = {i: {"correct": 0, "total": 0} for i in range(4)}
        for avg_len, corr in pairs:
            b = get_fixed_bucket(avg_len)
            buckets[b]["total"] += 1
            if corr:
                buckets[b]["correct"] += 1
        return {
            FIXED_NAMES[i]: {
                "accuracy": round(buckets[i]["correct"] / buckets[i]["total"], 4) if buckets[i]["total"] >= 5 else None,
                "correct": buckets[i]["correct"],
                "total": buckets[i]["total"],
                "range": _safe_range(FIXED_BUCKETS[i]),
            }
            for i in range(4)
        }

    # ── Adaptive bucketing: split into 4 equal parts by avg_len ──
    pairs.sort(key=lambda x: x[0])
    n = len(pairs)
    splits = [n * i // 4 for i in range(5)]
    names = ["Q1", "Q2", "Q3", "Q4"]
    result = {}
    for i in range(4):
        segment = pairs[splits[i]:splits[i + 1]]
        total = len(segment)
        correct = sum(1 for _, corr in segment if corr)
        lo = segment[0][0] if segment else 0
        hi = segment[-1][0] if segment else 0
        result[names[i]] = {
            "accuracy": round(correct / total, 4) if total >= 5 else None,
            "correct": correct,
            "total": total,
            "range": (lo, hi),
        }
    return result


# ──────────────────────────────────────────────
# Dataset processors → return [(avg_len, is_correct), ...]
# ──────────────────────────────────────────────

def process_deepresearch_bench(model: str, prompt_mode: str) -> list:
    pairs = []
    judge_path = BASE_DIR / "outputs" / "judge_results" / model / "deepresearch_bench" / f"{prompt_mode}.jsonl"
    gt_path = BASE_DIR / "ground_truth" / "deepresearch_bench_gt.jsonl"
    length_map = build_content_length_map("deepresearch_bench")

    gt_map = {}
    for g in load_jsonl(gt_path):
        gid = str(g["id"])
        for mname, scores in g.get("aggregated", {}).items():
            gt_map[(gid, mname)] = scores.get("weighted_total", 0) / 10.0

    per_query = defaultdict(dict)
    for jr in load_jsonl(judge_path):
        did = str(jr.get("data_id", ""))
        m = jr.get("model", "")
        score = jr.get("judge_result", {}).get("overall_score")
        if score is not None:
            per_query[did][m] = float(score)

    for did, pred_scores in per_query.items():
        models = sorted(pred_scores.keys())
        for i in range(len(models)):
            for j in range(i + 1, len(models)):
                mi, mj = models[i], models[j]
                ki, kj = (did, mi), (did, mj)
                if ki not in gt_map or kj not in gt_map or ki not in length_map or kj not in length_map:
                    continue
                g = gt_map[ki] - gt_map[kj]
                p = pred_scores[mi] - pred_scores[mj]
                if g == 0:
                    continue
                avg_len = (length_map[ki] + length_map[kj]) // 2
                pairs.append((avg_len, (g > 0 and p > 0) or (g < 0 and p < 0)))
    return pairs


def process_realdr(model: str, prompt_mode: str) -> list:
    pairs = []
    judge_path = BASE_DIR / "outputs" / "judge_results" / model / "realdr" / f"{prompt_mode}.jsonl"
    gt_path = BASE_DIR / "ground_truth" / "realdr_gt.jsonl"
    length_map = build_content_length_map("realdr")

    did_length = {}
    for (lk_did, _), v in length_map.items():
        did_length[lk_did] = v

    gt_map = {}
    did_to_task = {}
    for g in load_jsonl(gt_path):
        gid = str(g["id"])
        gt_map[gid] = float(g["weighted_total"])
        did_to_task[gid] = g.get("task_id")

    task_scores = defaultdict(dict)
    for jr in load_jsonl(judge_path):
        did = str(jr.get("data_id", ""))
        if did not in gt_map:
            continue
        tid = did_to_task[did]
        score = jr.get("judge_result", {}).get("overall_score")
        if score is None:
            jr_res = jr.get("judge_result", {})
            if isinstance(jr_res, dict):
                for sk in ("overall_quality_score", "quality_score", "score"):
                    if sk in jr_res:
                        score = float(jr_res[sk])
                        break
        if score is not None:
            task_scores[tid][did] = float(score)

    for tid, dids_scores in task_scores.items():
        dids = sorted(dids_scores.keys())
        for i in range(len(dids)):
            for j in range(i + 1, len(dids)):
                di, dj = dids[i], dids[j]
                if di not in gt_map or dj not in gt_map:
                    continue
                li, lj = did_length.get(di), did_length.get(dj)
                if not li or not lj:
                    continue
                g = gt_map[di] - gt_map[dj]
                p = dids_scores[di] - dids_scores[dj]
                if g == 0:
                    continue
                avg_len = (li + lj) // 2
                pairs.append((avg_len, (g > 0 and p > 0) or (g < 0 and p < 0)))
    return pairs


def _surge_by_dim(model: str, prompt_mode: str, dim: str) -> list:
    """SurGE dimension processor (content / structure)."""
    pairs = []
    # score key: content → content_score, structure → structural_score
    score_key = "content_score" if dim == "content" else "structural_score"
    judge_path = BASE_DIR / "outputs" / "judge_results" / model / "surge" / f"{dim}_{prompt_mode}.jsonl"
    gt_path = BASE_DIR / "ground_truth" / "surge_gt.jsonl"
    length_map = build_content_length_map("surge")

    gt_rank_map = {}
    for g in load_jsonl(gt_path):
        gid = str(g["id"])
        gt_rank_map[gid] = g.get(f"{dim}_ranking", {})

    per_query_scores = defaultdict(dict)
    for jr in load_jsonl(judge_path):
        did = str(jr.get("data_id", ""))
        jr_res = jr.get("judge_result", {})
        models = jr.get("models", [])
        letters = ["A", "B", "C", "D"]
        for letter, mname in zip(letters, models):
            mdata = jr_res.get(letter, {})
            if isinstance(mdata, dict):
                score = mdata.get(score_key)
                if score is not None:
                    per_query_scores[did][mname] = float(score)

    for did, pred_scores in per_query_scores.items():
        if did not in gt_rank_map:
            continue
        gt_ranks = gt_rank_map[did]
        models = sorted(pred_scores.keys())
        for i in range(len(models)):
            for j in range(i + 1, len(models)):
                mi, mj = models[i], models[j]
                if mi not in gt_ranks or mj not in gt_ranks:
                    continue
                ki, kj = (did, mi), (did, mj)
                if ki not in length_map or kj not in length_map:
                    continue
                g = gt_ranks[mj] - gt_ranks[mi]   # positive = GT prefers i
                p = pred_scores[mi] - pred_scores[mj]  # positive = judge prefers i
                if g == 0:
                    continue
                avg_len = (length_map[ki] + length_map[kj]) // 2
                pairs.append((avg_len, (g > 0 and p > 0) or (g < 0 and p < 0)))
    return pairs


def process_surge_content(model: str, prompt_mode: str) -> list:
    return _surge_by_dim(model, prompt_mode, "content")


def process_surge_structure(model: str, prompt_mode: str) -> list:
    return _surge_by_dim(model, prompt_mode, "structure")


def process_verify_bench_hard(model: str, prompt_mode: str) -> list:
    pairs = []
    judge_path = BASE_DIR / "outputs" / "judge_results" / model / "verify_bench_hard" / f"{prompt_mode}.jsonl"
    gt_path = BASE_DIR / "ground_truth" / "verify_bench_hard_gt.jsonl"
    length_map = build_content_length_map("verify_bench_hard")

    did_length = {}
    for (lk_did, _), v in length_map.items():
        did_length[lk_did] = v

    gt_map = {}
    for g in load_jsonl(gt_path):
        gt_map[str(g["id"])] = 1 if g.get("gold_correct") else 0

    for jr in load_jsonl(judge_path):
        did = str(jr.get("data_id", ""))
        if did not in gt_map:
            continue
        jr_res = jr.get("judge_result", {})
        if not isinstance(jr_res, dict):
            continue
        score_val = jr_res.get("score")
        if score_val is not None:
            pred = 1 if float(score_val) == 1 else 0
        else:
            verdict = str(jr_res.get("verdict", "")).strip().lower()
            pred = 1 if verdict in ("yes", "correct") else 0
        item_len = did_length.get(did, 0)
        if item_len == 0:
            continue
        # verify has no pairs; each doc is a single "pair" (pointwise accuracy)
        pairs.append((item_len, pred == gt_map[did]))
    return pairs


def process_wp_bench(model: str, prompt_mode: str) -> list:
    pairs = []
    judge_path = BASE_DIR / "outputs" / "judge_results" / model / "wp_bench" / f"{prompt_mode}.jsonl"
    data_path = BASE_DIR / "data_standardized" / "wp_bench.jsonl"

    data_content = {}
    gt_label = {}
    for rec in load_jsonl(data_path):
        did = str(rec["id"])
        data_content[did] = {}
        gt_label[did] = {}
        for r in rec.get("responses", []):
            m = r.get("model", "")
            data_content[did][m] = r.get("content", "")
            raw = r.get("label", "")
            gt_label[did][m] = int(raw) if raw in ("0", "1", 0, 1) else -1

    for jr in load_jsonl(judge_path):
        did = str(jr.get("data_id", ""))
        if did not in data_content:
            continue
        jr_res = jr.get("judge_result", {})
        if not isinstance(jr_res, dict):
            continue
        preferred = jr_res.get("preferred_response", "")
        if preferred not in ("A", "B"):
            continue
        resp_a_model = jr.get("response_a", "")
        resp_b_model = jr.get("response_b", "")
        preferred_model = resp_a_model if preferred == "A" else resp_b_model
        gt_a = gt_label[did].get(resp_a_model, -1)
        gt_b = gt_label[did].get(resp_b_model, -1)
        if gt_a < 0 or gt_b < 0:
            continue
        judge_correct = (preferred_model == resp_a_model and gt_a == 1) or \
                        (preferred_model == resp_b_model and gt_b == 1)
        len_a = count_tokens(data_content[did].get(resp_a_model, ""))
        len_b = count_tokens(data_content[did].get(resp_b_model, ""))
        pairs.append(((len_a + len_b) // 2, judge_correct))
    return pairs


def _ma_by_dim(model: str, prompt_mode: str, dim: str) -> list:
    """MA dimension processor (insights / structure)."""
    pairs = []
    judge_path = BASE_DIR / "outputs" / "judge_results" / model / "ma" / f"{dim}_{prompt_mode}.jsonl"
    gt_path = BASE_DIR / "ground_truth" / "ma_gt.jsonl"
    length_map = build_content_length_map("ma")

    # GT: id → preferred (A/B)
    gt_pref = {}
    for g in load_jsonl(gt_path):
        if g.get("dimension") != dim:
            continue
        gid = str(g["id"])
        gt_pref[gid] = g["preferred"]

    for jr in load_jsonl(judge_path):
        did = str(jr.get("data_id", ""))
        if did not in gt_pref:
            continue
        jr_res = jr.get("judge_result", {})
        if not isinstance(jr_res, dict):
            continue

        # preferred key: preferred_{dim}_consistency for insights, preferred_{dim}_quality for structure
        pref_key = f"preferred_{dim}_consistency" if dim == "insights" else f"preferred_{dim}_quality"
        pred_pref = jr_res.get(pref_key, "")
        if pred_pref not in ("A", "B"):
            continue

        resp_a = jr.get("response_a", "")
        resp_b = jr.get("response_b", "")

        judge_correct = pred_pref == gt_pref[did]
        len_a = length_map.get((did, resp_a), 0)
        len_b = length_map.get((did, resp_b), 0)
        if len_a == 0 or len_b == 0:
            # fallback: try without dimension suffix (unlikely needed)
            continue
        pairs.append(((len_a + len_b) // 2, judge_correct))
    return pairs


def process_ma_insights(model: str, prompt_mode: str) -> list:
    return _ma_by_dim(model, prompt_mode, "insights")




# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

PROCESSORS = {
    "deepresearch_bench": process_deepresearch_bench,
    "realdr": process_realdr,
    "surge_content": process_surge_content,
    "surge_structure": process_surge_structure,
    "verify_bench_hard": process_verify_bench_hard,
    "wp_bench": process_wp_bench,
    "ma_insights": process_ma_insights,
}

DATASET_ORDER = ["deepresearch_bench", "realdr", "surge_content", "surge_structure",
                 "verify_bench_hard", "wp_bench", "ma_insights"]


def print_table(all_results: dict, bucket_names: list):
    header = f"{'Dataset':<22}"
    for bn in bucket_names:
        header += f" | {bn:<7}"
    print(header)
    print("-" * len(header))

    for ds in DATASET_ORDER:
        buckets = all_results.get(ds, {})
        row = f"{ds:<22}"
        for bn in bucket_names:
            b = buckets.get(bn, {})
            acc = b.get("accuracy")
            row += f" | {acc:.4f}" if acc is not None else " | -"
        print(row)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Length Sensitivity Analysis")
    parser.add_argument("model", help="Judge model name")
    parser.add_argument("prompt_mode", nargs="?", default="vanilla", help="Prompt mode (default: vanilla)")
    parser.add_argument("--adaptive", action="store_true", help="Enable adaptive bucketing (quartile-based)")

    args = parser.parse_args()

    print(f"\n=== Length Sensitivity Analysis ===")
    print(f"Judge: {args.model}, Prompt: {args.prompt_mode}")
    print(f"Mode: {'Adaptive (Q1/Q2/Q3/Q4)' if args.adaptive else 'Fixed (<3K/3-8K/8-16K/>16K)'}\n")

    bucket_names = FIXED_NAMES if not args.adaptive else ["Q1", "Q2", "Q3", "Q4"]

    all_results = {}
    for ds in DATASET_ORDER:
        pairs = PROCESSORS[ds](args.model, args.prompt_mode)
        buckets = to_buckets(pairs, args.adaptive)
        all_results[ds] = buckets
        # Print length ranges in adaptive mode
        if args.adaptive:
            ranges = []
            for i in range(4):
                r = buckets[bucket_names[i]].get("range", (0, 0))
                ranges.append(f"{r[0]}-{r[1]}")
            print(f"  {ds} ranges: {', '.join(ranges)}")

    print_table(all_results, bucket_names)

    # Save JSON
    suffix = "_adaptive" if args.adaptive else ""
    out_dir = BASE_DIR / "outputs" / "length_sensitivity"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.model}_{args.prompt_mode}{suffix}.json"

    # Strip range from output (it's bulky; save separately if needed)
    out_data = {}
    for ds in DATASET_ORDER:
        out_data[ds] = {}
        for bn in bucket_names:
            b = all_results[ds].get(bn, {})
            out_data[ds][bn] = {
                "accuracy": b.get("accuracy"),
                "correct": b.get("correct"),
                "total": b.get("total"),
                "range": b.get("range"),
            }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

"""
Analysis 3: Score Distribution & Compression Analysis (deepresearch_bench, realdr).

Goal: Compare judge score distributions vs GT distributions to quantify
score compression bias. Are judges using the full scale?

Findings feed into FP2: Score Compression.
"""
import sys
from pathlib import Path
from collections import defaultdict
import math

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl


def analyze_score_distribution(judge_path: str, gt_path: str, dataset: str, model_name: str, prompt_mode: str):
    """Compare judge score distribution vs GT distribution."""
    judge_data = load_jsonl(judge_path)
    gt_data = load_jsonl(gt_path)

    # Build GT map
    if dataset == "deepresearch_bench":
        gt_map = {}
        for g in gt_data:
            gid = str(g["id"])
            for model_name_gt, scores in g.get("aggregated", {}).items():
                gt_map[(gid, model_name_gt)] = scores.get("overall", 0) / 10.0
    else:  # realdr
        gt_map = {}
        for g in gt_data:
            gid = str(g["id"])
            gt_map[gid] = g.get("weighted_total", 0)

    judge_scores = []
    gt_scores_matched = []
    score_diffs = []

    for r in judge_data:
        jr = r.get("judge_result", {})
        if not isinstance(jr, dict):
            continue

        if dataset == "deepresearch_bench":
            key = (str(r.get("data_id", "")), r.get("model", ""))
            gt_val = gt_map.get(key)
            judge_val = jr.get("overall_score")
        else:  # realdr
            key = str(r.get("data_id", ""))
            gt_val = gt_map.get(key)
            judge_val = jr.get("overall_score")

        if gt_val is not None and judge_val is not None:
            judge_scores.append(float(judge_val))
            gt_scores_matched.append(float(gt_val))
            score_diffs.append(float(judge_val) - float(gt_val))

    if not judge_scores:
        print(f"  No scores found for {model_name}/{dataset}/{prompt_mode}")
        return

    n = len(judge_scores)
    judge_mean = sum(judge_scores) / n
    gt_mean = sum(gt_scores_matched) / n
    judge_std = math.sqrt(sum((s - judge_mean) ** 2 for s in judge_scores) / n)
    gt_std = math.sqrt(sum((s - gt_mean) ** 2 for s in gt_scores_matched) / n)
    bias = judge_mean - gt_mean
    mae = sum(abs(d) for d in score_diffs) / n

    # Score histogram (judge vs GT)
    bins = [(0, 2), (2, 4), (4, 6), (6, 8), (8, 10)]
    judge_hist = [sum(1 for s in judge_scores if lo <= s < hi) for lo, hi in bins]
    gt_hist = [sum(1 for s in gt_scores_matched if lo <= s < hi) for lo, hi in bins]

    # Range usage
    judge_min, judge_max = min(judge_scores), max(judge_scores)
    gt_min, gt_max = min(gt_scores_matched), max(gt_scores_matched)

    print(f"\n{'='*70}")
    print(f"ANALYSIS 3: Score Distribution — {model_name} / {dataset} / {prompt_mode}")
    print(f"{'='*70}")
    print(f"  N: {n}")
    print(f"  Judge scores:  mean={judge_mean:.2f}, std={judge_std:.2f}, range=[{judge_min}, {judge_max}]")
    print(f"  GT scores:     mean={gt_mean:.2f}, std={gt_std:.2f}, range=[{gt_min}, {gt_max}]")
    print(f"  Bias (J-GT):   {bias:+.2f}")
    print(f"  MAE:           {mae:.2f}")
    print(f"\n  Score Distribution:")
    print(f"  {'Bucket':<15} {'Judge':<12} {'GT':<12} {'Diff':<12}")
    print(f"  {'─'*51}")
    for (lo, hi), jc, gc in zip(bins, judge_hist, gt_hist):
        label = f"[{lo}-{hi})"
        diff = jc - gc
        bar_j = "█" * (jc * 30 // max(max(judge_hist), 1))
        bar_g = "█" * (gc * 30 // max(max(gt_hist), 1))
        print(f"  {label:<15} {jc:<4}({bar_j:<30}) {gc:<4}({bar_g:<30}) {diff:+d}")

    if abs(bias) > 0.5:
        if bias > 0:
            print(f"\n  → Judge systematically OVER-SCORES by {bias:.2f} points")
        else:
            print(f"\n  → Judge systematically UNDER-SCORES by {abs(bias):.2f} points")

    if judge_std < gt_std * 0.7:
        print(f"  → Score COMPRESSION detected (judge std {judge_std:.2f} vs GT std {gt_std:.2f})")

    return {
        "n": n,
        "judge_mean": judge_mean,
        "gt_mean": gt_mean,
        "bias": bias,
        "mae": mae,
        "judge_std": judge_std,
        "gt_std": gt_std,
        "judge_range": (judge_min, judge_max),
        "gt_range": (gt_min, gt_max),
    }


def main():
    base = BASE_DIR / "outputs" / "judge_results"
    models = ["gpt-5.2", "gpt-4o-mini", "deepseek-v4-flash", "qwen3-max",
              "qwen3-32b", "qwen3-32b-nothinking", "kimi-k2.6", "glm-5.1"]

    dr_gt = BASE_DIR / "ground_truth" / "deepresearch_bench_gt.jsonl"
    realdr_gt = BASE_DIR / "ground_truth" / "realdr_gt.jsonl"

    print(f"\n{'='*70}")
    print(f"SCORE DISTRIBUTION ACROSS MODELS - deepresearch_bench")
    print(f"{'='*70}")

    dr_results = {}
    for model in models:
        path = base / model / "deepresearch_bench" / "vanilla.jsonl"
        if path.exists():
            res = analyze_score_distribution(str(path), str(dr_gt), "deepresearch_bench", model, "vanilla")
            dr_results[model] = res

    # Summary table
    print(f"\n{'='*70}")
    print(f"SUMMARY TABLE: deepresearch_bench vanilla")
    print(f"{'='*70}")
    print(f"{'Model':<25} {'Judge μ':>8} {'GT μ':>8} {'Bias':>8} {'MAE':>8} {'J σ':>6} {'GT σ':>6}")
    print(f"{'─'*65}")
    for model in models:
        r = dr_results.get(model)
        if r:
            print(f"{model:<25} {r['judge_mean']:>8.2f} {r['gt_mean']:>8.2f} "
                  f"{r['bias']:>+8.2f} {r['mae']:>8.2f} {r['judge_std']:>6.2f} {r['gt_std']:>6.2f}")


if __name__ == "__main__":
    main()

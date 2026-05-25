"""
Analysis 5: Rubric vs Vanilla Dimension-Level Comparison (deepresearch_bench).

Goal: Compare judge accuracy across dimensions in rubric mode.
Which dimensions are hardest? Which models handle which dimensions best?

Findings feed into FP6: Dimension Understanding Mismatch.
"""
import sys
from pathlib import Path
from collections import defaultdict
import math

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl

DIMS = ["comprehensiveness", "insight", "instruction_following", "readability"]
DIM_LABELS = {
    "comprehensiveness": "Comprehensiveness",
    "insight": "Insight",
    "instruction_following": "Instruction Following",
    "readability": "Readability",
}


def extract_dim_scores(jr: dict) -> dict:
    """Extract per-dimension average scores from rubric judge result."""
    dim_scores = {}
    for dim in DIMS:
        entries = jr.get(dim, [])
        if isinstance(entries, list) and len(entries) > 0:
            scores = [float(item["target_score"]) for item in entries
                     if isinstance(item, dict) and "target_score" in item]
            if scores:
                dim_scores[dim] = sum(scores) / len(scores)
        elif isinstance(entries, (int, float)):
            dim_scores[dim] = float(entries)
    return dim_scores


def analyze_dimension_level(judge_path: str, gt_path: str, model_name: str, prompt_mode: str):
    """Analyze per-dimension accuracy for rubric mode."""
    judge_data = load_jsonl(judge_path)
    gt_data = load_jsonl(gt_path)

    # Build GT map with dimension scores
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        for model_name_gt, scores in g.get("aggregated", {}).items():
            dims = {k: v / 10.0 for k, v in scores.get("dimensions", {}).items()}
            gt_map[(gid, model_name_gt)] = dims

    # Per-dimension error collection
    dim_data = defaultdict(lambda: {"judge": [], "gt": [], "diffs": []})
    total_pairs = 0

    for r in judge_data:
        key = (str(r.get("data_id", "")), r.get("model", ""))
        if key not in gt_map:
            continue
        jr = r.get("judge_result", {})
        if not isinstance(jr, dict):
            continue

        judge_dims = extract_dim_scores(jr)
        gt_dims = gt_map[key]

        if not judge_dims:
            continue

        total_pairs += 1
        for dim in DIMS:
            jv = judge_dims.get(dim)
            gv = gt_dims.get(dim)
            if jv is not None and gv is not None:
                dim_data[dim]["judge"].append(jv)
                dim_data[dim]["gt"].append(gv)
                dim_data[dim]["diffs"].append(abs(jv - gv))

    print(f"\n{'='*70}")
    print(f"ANALYSIS 5: Dimension-Level Accuracy — {model_name} / {prompt_mode}")
    print(f"{'='*70}")
    print(f"  Total matched pairs: {total_pairs}")

    print(f"\n  {'Dimension':<30} {'N':>5} {'Judge μ':>8} {'GT μ':>8} {'Bias':>8} {'MAE':>8} {'Std Err':>8}")
    print(f"  {'─'*75}")
    for dim in DIMS:
        d = dim_data.get(dim)
        if not d or not d["judge"]:
            continue
        n = len(d["judge"])
        j_mean = sum(d["judge"]) / n
        g_mean = sum(d["gt"]) / n
        bias = j_mean - g_mean
        mae = sum(d["diffs"]) / n
        std_err = math.sqrt(sum((x - j_mean)**2 for x in d["judge"]) / n) / math.sqrt(n)
        print(f"  {DIM_LABELS.get(dim, dim):<30} {n:>5} {j_mean:>8.2f} {g_mean:>8.2f} "
              f"{bias:>+8.2f} {mae:>8.2f} {std_err:>8.3f}")

    # Best and worst dimensions
    dim_maes = {dim: sum(dim_data[dim]["diffs"]) / len(dim_data[dim]["diffs"])
                for dim in DIMS if dim_data[dim]["diffs"]}
    if dim_maes:
        best = min(dim_maes, key=dim_maes.get)
        worst = max(dim_maes, key=dim_maes.get)
        print(f"\n  Most accurate dimension:   {DIM_LABELS.get(best, best)} (MAE={dim_maes[best]:.2f})")
        print(f"  Least accurate dimension: {DIM_LABELS.get(worst, worst)} (MAE={dim_maes[worst]:.2f})")

    return dim_data


def main():
    base = BASE_DIR / "outputs" / "judge_results"
    gt_path = BASE_DIR / "ground_truth" / "deepresearch_bench_gt.jsonl"

    models = ["gpt-5.2", "gpt-4o-mini", "deepseek-v4-flash", "qwen3-max",
              "qwen3-32b", "kimi-k2.6", "glm-5.1"]

    print(f"\n{'='*70}")
    print(f"DIMENSION-LEVEL ANALYSIS (rubric_reference mode)")
    print(f"{'='*70}")

    all_dim_stats = {}

    for model in models:
        path = base / model / "deepresearch_bench" / "vanilla_rubric_reference.jsonl"
        if not path.exists():
            print(f"  SKIP: {path}")
            continue
        dim_data = analyze_dimension_level(str(path), str(gt_path), model, "vanilla_rubric_reference")
        all_dim_stats[model] = {
            dim: {
                "mae": sum(dim_data[dim]["diffs"]) / len(dim_data[dim]["diffs"]) if dim_data[dim]["diffs"] else 0,
                "bias": (sum(dim_data[dim]["judge"]) / len(dim_data[dim]["judge"]) -
                         sum(dim_data[dim]["gt"]) / len(dim_data[dim]["gt"])) if dim_data[dim]["judge"] else 0,
            }
            for dim in DIMS if dim_data[dim]["diffs"]
        }

    # Cross-model dimension difficulty
    print(f"\n{'='*70}")
    print(f"CROSS-MODEL: Dimension Difficulty (MAE)")
    print(f"{'='*70}")
    header = f"{'Model':<25}"
    for dim in DIMS:
        header += f" {DIM_LABELS.get(dim, dim)[:12]:>12}"
    print(f"  {header}")
    print(f"  {'─'*75}")
    for model in models:
        if model not in all_dim_stats:
            continue
        row = f"{model:<25}"
        for dim in DIMS:
            mae = all_dim_stats[model].get(dim, {}).get("mae", 0)
            row += f" {mae:>12.2f}"
        print(f"  {row}")


if __name__ == "__main__":
    main()

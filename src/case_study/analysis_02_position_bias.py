"""
Analysis 2: Position Bias Analysis (wp_bench, ma).

Goal: Quantify position bias in pairwise evaluation by comparing original vs swapped
order consistency.

Findings feed into FP1: Position Bias.
"""
import sys
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl


def analyze_pairwise_position_bias(judge_path: str, gt_path: str, dataset: str, model_name: str, prompt_mode: str, dim_key: str = None):
    """Analyze position bias in pairwise judgments.

    Args:
        judge_path: Path to judge results JSONL
        gt_path: Path to ground truth JSONL
        dataset: Dataset name
        model_name: Judge model name
        prompt_mode: Prompt mode name
        dim_key: Dimension-specific key in judge_result (e.g., "preferred_insights_consistency")
                  None for wp_bench which uses "preferred_response"
    """
    judge_data = load_jsonl(judge_path)
    gt_data = load_jsonl(gt_path) if gt_path else []

    # Build GT map
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        preferred = g.get("preferred", g.get("preference", {}).get("chosen_model", None))
        gt_map[gid] = {"preferred": preferred}

    # Group by data_id, collecting original and swapped
    pairs = defaultdict(lambda: {"original": None, "swapped": None})
    pref_key = dim_key if dim_key else "preferred_response"

    for r in judge_data:
        did = str(r.get("data_id", ""))
        jr = r.get("judge_result", {})
        if not isinstance(jr, dict):
            continue
        swap_pos = jr.get("swap_position", "original")
        preference = jr.get(pref_key)
        pairs[did][swap_pos] = preference

    # Analyze consistency
    consistent = 0
    inconsistent = 0
    total = 0
    inconsistent_cases = []

    for did, pair in pairs.items():
        orig = pair.get("original")
        swap = pair.get("swapped")
        if orig is None or swap is None:
            continue
        total += 1
        # In debiased mode: original and swapped should agree after inverting swapped
        # If orig == "A" and swap == "B", after inverting swap → "A", they agree
        # If orig == "A" and swap == "A", after inverting swap → "B", they disagree
        def invert(p):
            if p == "A":
                return "B"
            elif p == "B":
                return "A"
            return "tie"

        swap_inverted = invert(swap)

        if orig == swap_inverted:
            consistent += 1
        else:
            inconsistent += 1
            inconsistent_cases.append({
                "data_id": did,
                "original": orig,
                "swapped": swap,
                "swapped_inverted": swap_inverted,
                "gt_preferred": gt_map.get(did, {}).get("preferred", "unknown"),
            })

    consistency_rate = consistent / total * 100 if total > 0 else 0

    print(f"\n{'='*70}")
    print(f"ANALYSIS 2: Position Bias — {model_name} / {dataset} / {prompt_mode}")
    print(f"{'='*70}")
    print(f"  Total pairs: {total}")
    print(f"  Consistent:  {consistent} ({consistency_rate:.1f}%)")
    print(f"  Inconsistent: {inconsistent} ({100-consistency_rate:.1f}%)")
    print(f"  Random baseline consistency: 50%")

    if inconsistent_cases:
        print(f"\n  TOP INCONSISTENT CASES:")
        # Find cases with response length info
        for case in inconsistent_cases[:10]:
            gt = case["gt_preferred"]
            print(f"    data_id={case['data_id']}: orig={case['original']}, "
                  f"swapped={case['swapped']}, inverted_swap={case['swapped_inverted']}, "
                  f"GT={gt}")

        # Analyze: does position bias correlate with identifiable features?
        # Check if judge favors first position (A in original, B in swapped → always picks A)
        first_pos_bias = sum(1 for c in inconsistent_cases
                            if c["original"] == "A" and c["swapped"] == "A")
        second_pos_bias = sum(1 for c in inconsistent_cases
                             if c["original"] == "B" and c["swapped"] == "B")
        print(f"\n  Position bias pattern:")
        print(f"    Always picks 'A' (strong first-position bias): {first_pos_bias}")
        print(f"    Always picks 'B' (strong second-position bias): {second_pos_bias}")
        other = inconsistent - first_pos_bias - second_pos_bias
        print(f"    Other inconsistency pattern: {other}")

    return {"consistent": consistent, "inconsistent": inconsistent, "total": total}


def main():
    base = BASE_DIR / "outputs" / "judge_results"
    models = ["gpt-5.2", "gpt-4o-mini", "deepseek-v4-flash", "qwen3-max",
              "qwen3-32b", "qwen3-32b-nothinking", "kimi-k2.6", "glm-5.1"]

    wp_gt = BASE_DIR / "ground_truth" / "wp_bench_gt.jsonl"
    ma_gt = BASE_DIR / "ground_truth" / "ma_gt.jsonl"

    print(f"\n{'='*70}")
    print(f"POSITION BIAS ACROSS ALL MODELS")
    print(f"{'='*70}")

    # Collect results for summary table
    wp_results = {}
    ma_results = {}

    for model in models:
        # wp_bench
        wp_path = base / model / "wp_bench" / "vanilla.jsonl"
        if wp_path.exists():
            res = analyze_pairwise_position_bias(str(wp_path), str(wp_gt), "wp_bench", model, "vanilla")
            wp_results[model] = res

        # ma
        ma_path = base / model / "ma" / "insights_vanilla.jsonl"
        if ma_path.exists():
            res = analyze_pairwise_position_bias(
                str(ma_path), str(ma_gt), "ma", model, "insights_vanilla",
                dim_key="preferred_insights_consistency"
            )
            ma_results[model] = res

    # Summary table
    print(f"\n{'='*70}")
    print(f"SUMMARY: Position Bias Across Models")
    print(f"{'='*70}")
    print(f"{'Model':<25} {'WP-Bench':>15} {'MA-Insights':>15}")
    print(f"{'─'*55}")
    for model in models:
        wp = wp_results.get(model, {})
        ma = ma_results.get(model, {})
        wp_str = f"{wp.get('consistent', 0)}/{wp.get('total', 0)}" if wp else "N/A"
        ma_str = f"{ma.get('consistent', 0)}/{ma.get('total', 0)}" if ma else "N/A"
        wp_rate = f"({wp['consistent']/wp['total']*100:.0f}%)" if wp and wp['total'] > 0 else ""
        ma_rate = f"({ma['consistent']/ma['total']*100:.0f}%)" if ma and ma['total'] > 0 else ""
        print(f"{model:<25} {wp_str+wp_rate:>15} {ma_str+ma_rate:>15}")


if __name__ == "__main__":
    main()

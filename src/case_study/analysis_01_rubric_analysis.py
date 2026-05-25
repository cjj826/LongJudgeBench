"""
Analysis 1: Rubric Mode Analysis Text Extraction (deepresearch_bench).

Goal: Extract judge's per-criterion analysis text for "bad cases" where
judge scores differ significantly from ground truth. This allows qualitative
analysis of WHY the judge made errors by reading its reasoning.

Findings feed into:
  - FP2: Score Compression (judge scores vs GT)
  - FP5: Long document info aggregation failure
  - FP6: Dimension-level understanding mismatch
"""
import json
import sys
from pathlib import Path
from collections import defaultdict

# Add project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl

# deepresearch_bench dimensions
DIMS = ["comprehensiveness", "insight", "instruction_following", "readability"]

# Simple English labels for dimensions
DIM_LABELS = {
    "comprehensiveness": "Comprehensiveness",
    "insight": "Insight",
    "instruction_following": "Instruction Following",
    "readability": "Readability",
}


def extract_judge_dim_scores(judge_result: dict) -> dict:
    """Extract per-dimension average scores from rubric judge result."""
    dim_scores = {}
    for dim in DIMS:
        entries = judge_result.get(dim, [])
        if isinstance(entries, list) and len(entries) > 0:
            scores = []
            for item in entries:
                if isinstance(item, dict):
                    score = item.get("target_score")
                    if score is None:
                        score = item.get("article_2_score")
                    if score is not None:
                        scores.append(float(score))
            if scores:
                dim_scores[dim] = sum(scores) / len(scores)
    return dim_scores


def build_gt_map(gt_data: list) -> dict:
    """Build {(data_id, model): gt_dict} from ground truth."""
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        for model_name, scores in g.get("aggregated", {}).items():
            gt_map[(gid, model_name)] = {
                "overall": scores.get("overall", 0) / 10.0,  # 0-100 → 0-10
                "weighted_total": scores.get("weighted_total", 0) / 10.0,
                "dimensions": {k: v / 10.0 for k, v in scores.get("dimensions", {}).items()},
            }
    return gt_map


def analyze_rubric_mode(judge_path: str, gt_path: str, model_name: str, prompt_mode: str):
    """Analyze rubric mode judge results and find bad cases with analysis text."""
    judge_data = load_jsonl(judge_path)
    gt_data = load_jsonl(gt_path)
    gt_map = build_gt_map(gt_data)

    # Collect per-entry errors
    bad_cases = []  # Cases with large score discrepancy
    all_diffs = []

    for r in judge_data:
        key = (str(r.get("data_id", "")), r.get("model", ""))
        if key not in gt_map:
            continue
        jr = r.get("judge_result", {})
        if not isinstance(jr, dict):
            continue

        gt_entry = gt_map[key]
        judge_dims = extract_judge_dim_scores(jr)

        if not judge_dims:
            continue

        # Compute overall score (weighted average across dims)
        judge_overall = sum(judge_dims.values()) / len(judge_dims)
        gt_overall = gt_entry.get("overall", 0)

        diff = abs(judge_overall - gt_overall)
        all_diffs.append(diff)

        if diff >= 2.0:  # Bad case: judge differs from GT by >= 2 points (on 0-10 scale)
            # Collect per-criterion analysis text
            dim_details = {}
            for dim in DIMS:
                entries = jr.get(dim, [])
                if isinstance(entries, list):
                    dim_details[dim] = []
                    for item in entries:
                        if isinstance(item, dict) and "analysis" in item:
                            dim_details[dim].append({
                                "criterion": item.get("criterion", ""),
                                "analysis": item.get("analysis", ""),
                                "score": item.get("target_score") or item.get("article_2_score"),
                            })

            bad_cases.append({
                "data_id": key[0],
                "model": key[1],
                "judge_overall": round(judge_overall, 2),
                "gt_overall": round(gt_overall, 2),
                "diff": round(diff, 2),
                "summary": r.get("response", "")[:200],  # First 200 chars of raw response
                "dim_scores": {k: round(v, 2) for k, v in judge_dims.items()},
                "dim_details": dim_details,
            })

    # Sort by discrepancy (largest first)
    bad_cases.sort(key=lambda x: x["diff"], reverse=True)

    print(f"\n{'='*70}")
    print(f"ANALYSIS 1: Rubric Mode Bad Cases — {model_name} / {prompt_mode}")
    print(f"{'='*70}")
    print(f"Total judge entries: {len(judge_data)}")
    print(f"Bad cases (diff >= 2.0): {len(bad_cases)}")
    if all_diffs:
        print(f"Mean |judge - GT|: {sum(all_diffs)/len(all_diffs):.2f}")
        print(f"Max |judge - GT|: {max(all_diffs):.2f}")

    # Print top bad cases with full analysis text
    print(f"\n{'─'*70}")
    print(f"TOP 10 WORST CASES (Full Analysis Text)")
    print(f"{'─'*70}")

    for i, case in enumerate(bad_cases[:10]):
        print(f"\n{'='*70}")
        print(f"CASE {i+1}: data_id={case['data_id']}, model={case['model']}")
        print(f"  Judge overall: {case['judge_overall']} | GT overall: {case['gt_overall']} | Diff: {case['diff']}")
        print(f"  Dimension scores: {case['dim_scores']}")

        for dim in DIMS:
            details = case["dim_details"].get(dim, [])
            if not details:
                continue

            gt_dim = None
            # We need to look up GT dimension scores; we can infer from context
            print(f"\n  ┌─ {DIM_LABELS[dim]} ({len(details)} sub-criteria)")
            for item in details:
                criterion = item["criterion"]
                score = item["score"]
                analysis = item["analysis"]
                # Truncate analysis for readability
                if len(analysis) > 300:
                    analysis = analysis[:300] + "..."
                print(f"  ├─ [{score}] {criterion}")
                print(f"  │  {analysis}")
            print(f"  └─")

    # Summary statistics
    print(f"\n{'─'*70}")
    print(f"SUMMARY: Score Discrepancy Distribution")
    print(f"{'─'*70}")

    if bad_cases:
        bins = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 10)]
        for lo, hi in bins:
            count = sum(1 for c in bad_cases if lo <= c["diff"] < hi)
            if count > 0:
                print(f"  Diff {lo}-{hi}: {count} cases")

    # Model-level breakdown
    model_diffs = defaultdict(list)
    for case in bad_cases:
        model_diffs[case["model"]].append(case["diff"])
    print(f"\n  Per-model avg diff:")
    for m, diffs in sorted(model_diffs.items()):
        print(f"    {m}: avg diff = {sum(diffs)/len(diffs):.2f} (n={len(diffs)})")

    return bad_cases


def main():
    base = BASE_DIR / "outputs" / "judge_results"

    # Focus on qwen3-max rubric_reference mode (richest analysis)
    models_prompts = [
        ("qwen3-max", "vanilla_rubric_reference"),
        ("qwen3-max", "vanilla_rubric"),
        ("qwen3-32b", "vanilla_rubric_reference"),
        ("gpt-5.2", "vanilla_rubric_reference"),
    ]

    gt_path = BASE_DIR / "ground_truth" / "deepresearch_bench_gt.jsonl"

    all_bad_cases = {}
    for model, prompt_mode in models_prompts:
        judge_path = base / model / "deepresearch_bench" / f"{prompt_mode}.jsonl"
        if not judge_path.exists():
            print(f"SKIP: {judge_path} not found")
            continue
        cases = analyze_rubric_mode(
            str(judge_path),
            str(gt_path),
            model,
            prompt_mode,
        )
        all_bad_cases[f"{model}/{prompt_mode}"] = cases

    # Cross-model agreement on bad cases
    print(f"\n{'='*70}")
    print(f"CROSS-MODEL: Bad Cases Overlap")
    print(f"{'='*70}")

    # Find cases that are bad across ALL models
    case_keys = None
    for key, cases in all_bad_cases.items():
        this_set = {(c["data_id"], c["model"]) for c in cases}
        if case_keys is None:
            case_keys = this_set
        else:
            case_keys = case_keys & this_set

    if case_keys:
        print(f"\n  Cases that are consistently bad across ALL models: {len(case_keys)}")
        for did, model in sorted(case_keys)[:5]:
            print(f"    data_id={did}, model={model}")
    else:
        print("  No case is consistently bad across all models.")
        # Show intersection of just 2 models
        keys = list(all_bad_cases.keys())
        if len(keys) >= 2:
            s1 = {(c["data_id"], c["model"]) for c in all_bad_cases[keys[0]]}
            s2 = {(c["data_id"], c["model"]) for c in all_bad_cases[keys[1]]}
            overlap = s1 & s2
            print(f"  Overlap between {keys[0]} and {keys[1]}: {len(overlap)} cases")


if __name__ == "__main__":
    main()

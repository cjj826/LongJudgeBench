"""
Analysis 4: "All Models Wrong" Case Analysis (verify_bench_hard).

Goal: Identify cases where ALL judge models disagree with ground truth,
indicating genuinely hard or ambiguous cases. Analyze their characteristics.

Findings feed into FP3: Task-Specific Blind Spots.
"""
import sys
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl


def analyze_all_wrong_cases():
    """Find verify_bench_hard cases where ALL 8 judge models disagree with GT."""
    base = BASE_DIR / "outputs" / "judge_results"
    models = ["gpt-5.2", "gpt-4o-mini", "deepseek-v4-flash", "qwen3-max",
              "qwen3-32b", "qwen3-32b-nothinking", "kimi-k2.6", "glm-5.1"]

    gt_path = BASE_DIR / "ground_truth" / "verify_bench_hard_gt.jsonl"
    gt_data = load_jsonl(gt_path)

    # Build GT map
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        gt_map[gid] = {
            "gold_correct": g.get("gold_correct", False),
            "answer_type": g.get("answer_type", ""),
            "answer_subtype": g.get("answer_subtype", ""),
            "source": g.get("source", ""),
            "completion_model": g.get("completion_model", ""),
        }

    # Load vanilla judge results for each model
    model_verdicts = defaultdict(dict)  # {data_id: {model: verdict_bool}}
    for model in models:
        path = base / model / "verify_bench_hard" / "vanilla.jsonl"
        if not path.exists():
            continue
        for r in load_jsonl(path):
            did = str(r.get("data_id", ""))
            jr = r.get("judge_result", {})
            if isinstance(jr, dict):
                verdict = jr.get("score", jr.get("verdict"))
                if verdict is not None:
                    if isinstance(verdict, str):
                        verdict = 1 if verdict.lower() in ("yes", "correct", "true") else 0
                    model_verdicts[did][model] = int(verdict)

    # Classify each case
    all_data_ids = set(model_verdicts.keys())
    all_models_set = set(models)

    all_correct = []
    all_wrong = []
    mixed = []

    for did in all_data_ids:
        available_models = set(model_verdicts[did].keys())
        gt = gt_map.get(did, {}).get("gold_correct", False)
        gt_int = 1 if gt else 0

        agrees = sum(1 for m in available_models if model_verdicts[did].get(m) == gt_int)
        disagrees = len(available_models) - agrees

        if disagrees == 0:
            all_correct.append(did)
        elif agrees == 0:
            all_wrong.append(did)
        else:
            mixed.append((did, agrees, disagrees))

    # Stats
    total = len(all_data_ids)
    n_all_correct = len(all_correct)
    n_all_wrong = len(all_wrong)
    n_mixed = len(mixed)

    print(f"\n{'='*70}")
    print(f"ANALYSIS 4: All Models Wrong — verify_bench_hard")
    print(f"{'='*70}")
    print(f"Total cases: {total}")
    print(f"All 8 models correct: {n_all_correct} ({n_all_correct/total*100:.1f}%)")
    print(f"All 8 models WRONG:   {n_all_wrong} ({n_all_wrong/total*100:.1f}%)")
    print(f"Mixed agreement:      {n_mixed} ({n_mixed/total*100:.1f}%)")

    # Characterize "all wrong" cases
    if all_wrong:
        print(f"\n{'─'*70}")
        print(f"CHARACTERISTICS OF 'ALL WRONG' CASES")
        print(f"{'─'*70}")

        # Answer type breakdown
        type_counts = defaultdict(int)
        subtype_counts = defaultdict(int)
        source_counts = defaultdict(int)

        for did in all_wrong:
            info = gt_map.get(did, {})
            type_counts[info.get("answer_type", "unknown")] += 1
            subtype_counts[info.get("answer_subtype", "unknown")] += 1
            source_counts[info.get("source", "unknown")] += 1

        print(f"\n  By Answer Type:")
        for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"    {t}: {c} cases")

        print(f"\n  By Answer Subtype:")
        for t, c in sorted(subtype_counts.items(), key=lambda x: -x[1]):
            print(f"    {t}: {c} cases")

        print(f"\n  By Source:")
        for t, c in sorted(source_counts.items(), key=lambda x: -x[1]):
            print(f"    {t}: {c} cases")

        # Compare with "all correct" cases
        print(f"\n{'─'*70}")
        print(f"COMPARISON: 'All Wrong' vs 'All Correct'")
        print(f"{'─'*70}")
        wrong_types = defaultdict(int)
        correct_types = defaultdict(int)
        for did in all_wrong:
            wrong_types[gt_map[did]["answer_type"]] += 1
        for did in all_correct:
            correct_types[gt_map[did]["answer_type"]] += 1

        all_types = set(list(wrong_types.keys()) + list(correct_types.keys()))
        print(f"\n  {'Answer Type':<25} {'Wrong':>8} {'Correct':>8} {'Error Rate':>12}")
        print(f"  {'─'*53}")
        for t in sorted(all_types):
            wc = wrong_types.get(t, 0)
            cc = correct_types.get(t, 0)
            total_t = wc + cc
            rate = wc / total_t * 100 if total_t > 0 else 0
            print(f"  {t:<25} {wc:>8} {cc:>8} {rate:>11.1f}%")

        # Print detailed examples
        print(f"\n{'─'*70}")
        print(f"TOP 10 'ALL WRONG' CASE DETAILS")
        print(f"{'─'*70}")
        for did in all_wrong[:10]:
            info = gt_map.get(did, {})
            print(f"\n  data_id={did}")
            print(f"    Answer type: {info.get('answer_type', '?')} / {info.get('answer_subtype', '?')}")
            print(f"    Source: {info.get('source', '?')}")
            print(f"    Completion model: {info.get('completion_model', '?')}")
            print(f"    Gold correct: {info.get('gold_correct', '?')}")
            # Show what each model predicted
            ver_str = ", ".join(f"{m}:{model_verdicts[did].get(m, '?')}" for m in models)
            print(f"    Model verdicts: [{ver_str}]")

    return {
        "total": total,
        "all_correct": n_all_correct,
        "all_wrong": n_all_wrong,
        "mixed": n_mixed,
        "all_wrong_ids": all_wrong,
    }


def main():
    analyze_all_wrong_cases()


if __name__ == "__main__":
    main()

"""WP-Bench dataset module."""
from pathlib import Path
from collections import defaultdict, OrderedDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from src.utils.io_utils import load_jsonl


def get_paradigm() -> str:
    return "pairwise"


def load_data(data_dir: str = None) -> list[dict]:
    """Load from data_standardized/wp_bench.jsonl"""
    path = Path(data_dir) if data_dir else BASE_DIR / "data_standardized" / "wp_bench.jsonl"
    return load_jsonl(path)


def extract_metrics(judge_results: list, gt_data: list) -> dict:
    """
    Judge: {data_id, response_a, response_b, judge_result: {preferred_response, swap_position, debiased}}
    GT:    {id, preference: {chosen_model}}

    In debiased mode, each data_id may have 2 rows (original + swapped),
    each judge_result compared independently against GT.
    Swapped results have A↔B reversed before comparison.

    Returns: {"accuracy": ..., "correct": N, "total": N}  (pairwise has no sub-groups)
    """
    gt_map = defaultdict(list)
    for g in gt_data:
        gid = str(g["id"])
        pref = g.get("preference", {})
        gt_map[gid].append({
            "chosen_model": pref.get("chosen_model", ""),
            "rejected_model": pref.get("rejected_model", ""),
        })

    # Group by data_id
    by_id = OrderedDict()
    for r in judge_results:
        did = str(r.get("data_id", ""))
        if did in gt_map:
            by_id.setdefault(did, []).append(r)

    correct = 0
    total = 0

    for did, results in by_id.items():
        r0 = results[0]
        response_a = r0.get("response_a", "")
        response_b = r0.get("response_b", "")

        # Determine GT answer (single ground truth per pair)
        gt_answer = None
        for gt_entry in gt_map[did]:
            gt_chosen = gt_entry["chosen_model"]
            gt_rejected = gt_entry.get("rejected_model", "")
            if gt_chosen == gt_rejected:
                continue
            if gt_chosen == response_a:
                gt_answer = "A"
                break
            elif gt_chosen == response_b:
                gt_answer = "B"
                break
        if gt_answer is None:
            continue

        # Each judge_result compared independently against GT
        for r in results:
            pref = str(r.get("judge_result", {}).get("preferred_response", "")).strip().upper()
            if r.get("judge_result", {}).get("error"):
                continue  # parse error, skip

            total += 1  # all outputs (including tie, missing) counted in denominator

            if pref not in ("A", "B"):
                continue  # tie or missing → 0 correct, 1 total

            is_swapped = r.get("judge_result", {}).get("swap_position") == "swapped"
            if is_swapped:
                # swapped: A=original response_1, B=original response_0 → invert
                judge_val = "B" if pref == "A" else "A"
            else:
                judge_val = pref

            if judge_val == gt_answer:
                correct += 1

    acc = correct / total if total > 0 else 0
    return {
        "accuracy": acc,
        "correct": correct,
        "total": total,
        "groups": {"all": {"n": total, "accuracy": acc, "spearman": None, "kendall": None}},
    }

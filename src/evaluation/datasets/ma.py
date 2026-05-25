"""MA dataset module.
Judge: pairwise (compare two systems)
GT:    pairwise_preference (A/B/tie aggregated from 8 annotators)
extract_metrics: compare judge preference vs GT preference, compute ACC
Supports debiased (position swap debiasing) and tie output
"""
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from src.utils.io_utils import load_jsonl

DIMS = ["insights"]
DIM_KEY_MAP = {
    "insights": "preferred_insights_consistency",
}


def get_paradigm() -> str:
    return "pairwise"


def load_data(data_dir: str = None) -> list[dict]:
    """Load from data_standardized/ma.jsonl"""
    path = Path(data_dir) if data_dir else BASE_DIR / "data_standardized" / "ma.jsonl"
    return load_jsonl(path)


def extract_metrics(judge_results: list, gt_data: list) -> dict:
    """
    Judge: {data_id, response_a, response_b,
            judge_result: {preferred_insights_consistency,
                           swap_position (optional, debiased)}}
           LLM may output "A" / "B" / "tie"

    GT:    {id, dimension, preferred, system_a, system_b}

    Supports debiased (position swap debiasing):
      - Same data_id has 2 records (original + swapped)
      - Each judge_result compared independently against GT
      - Swapped results have A↔B reversed before comparison (TIE unchanged)

    Returns: groups grouped by dimension
    """
    # Build GT mapping
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        gt_map[gid] = {
            "dimension": g.get("dimension", ""),
            "preferred": g.get("preferred", "tie"),
            "system_a": g.get("system_a", ""),
            "system_b": g.get("system_b", ""),
        }

    # Group judge results by data_id (supports debiased: 2 rows per data_id)
    by_id = defaultdict(list)
    for r in judge_results:
        did = str(r.get("data_id", ""))
        if did in gt_map:
            by_id[did].append(r)

    # Aggregate by dimension
    dim_results = defaultdict(lambda: {"correct": 0, "total": 0})

    for did, results in by_id.items():
        gt_entry = gt_map[did]
        dim = gt_entry["dimension"]
        if dim not in DIMS:
            continue

        # GT preference (can be A/B/TIE)
        gt_pref = gt_entry.get("preferred", "tie").strip().upper()

        # Each judge_result compared independently against GT
        for r in results:
            pref = str(r.get("judge_result", {}).get(DIM_KEY_MAP[dim], "")).strip().upper()
            if pref not in ("A", "B", "TIE"):
                continue  # LLM did not output this dimension, skip

            is_swapped = r.get("judge_result", {}).get("swap_position") == "swapped"
            if is_swapped:
                # swapped: swap A↔B, TIE unchanged
                judge_val = {"A": "B", "B": "A", "TIE": "TIE"}.get(pref, pref)
            else:
                judge_val = pref

            dim_results[dim]["total"] += 1
            if judge_val == gt_pref:
                dim_results[dim]["correct"] += 1

    # Build output
    groups = {}
    per_query = {}
    total_correct = 0
    total_all = 0
    for dim in DIMS:
        res = dim_results[dim]
        correct = res["correct"]
        total = res["total"]
        acc = correct / total if total > 0 else 0
        groups[dim] = {
            "n": total,
            "accuracy": acc,
            "spearman": None,
            "kendall": None,
        }
        total_correct += correct
        total_all += total

    groups["all"] = {
        "n": total_all,
        "accuracy": total_correct / total_all if total_all > 0 else 0,
        "spearman": None,
        "kendall": None,
    }

    return {
        "accuracy": total_correct / total_all if total_all > 0 else 0,
        "correct": total_correct,
        "total": total_all,
        "groups": groups,
        "per_query": per_query,
    }

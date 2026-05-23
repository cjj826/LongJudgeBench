"""VerifyBench-Hard dataset module.
Judge: pointwise (binary Yes/No)
GT:    pointwise_binary (gold_correct)
extract_metrics: binary ACC, grouped by answer_type / answer_subtype / source breakdown

Note: this file is self-contained; verify_bench.py is deprecated.
"""
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from src.utils.io_utils import load_jsonl


def get_paradigm() -> str:
    return "pointwise"


def load_data(data_dir: str = None) -> list[dict]:
    """Load from data_standardized/verify_bench_hard.jsonl"""
    path = Path(data_dir) if data_dir else BASE_DIR / "data_standardized" / "verify_bench_hard.jsonl"
    return load_jsonl(path)


def extract_metrics(judge_results: list, gt_data: list) -> dict:
    """
    Judge: {data_id, judge_result: {verdict: "Yes"/"No"/"Correct"/"Incorrect", score: 0/1}}

    GT: {id, gold_correct: bool, answer_type, answer_subtype, source}

    Returns: groups containing global and per-breakdown ACC
    Note: pred values are 0/1, compute_group_metrics auto-switches to simple ACC
    """
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        gt_map[gid] = g

    # Collect by each breakdown group
    groups = defaultdict(lambda: {"gt": [], "pred": []})

    for r in judge_results:
        did = str(r.get("data_id", ""))
        if did not in gt_map:
            continue
        jr = r.get("judge_result", {})
        if not jr or isinstance(jr, dict) and jr.get("error"):
            continue

        gt = gt_map[did]
        gold = gt.get("gold_correct")
        if gold is None:
            continue

        gold_int = 1 if gold else 0

        # Prefer score field (more reliable), fall back to parsing verdict
        score_val = jr.get("score")
        if score_val is not None:
            pred = 1 if float(score_val) == 1 else 0
        else:
            verdict = str(jr.get("verdict", "")).strip().lower()
            pred = 1 if verdict in ("yes", "correct") else 0

        # Global
        groups["all"]["gt"].append(gold_int)
        groups["all"]["pred"].append(pred)

        # By answer_type
        at = gt.get("answer_type", "unknown")
        groups[f"type_{at}"]["gt"].append(gold_int)
        groups[f"type_{at}"]["pred"].append(pred)

        # By answer_subtype
        ast = gt.get("answer_subtype", "unknown")
        groups[f"subtype_{ast}"]["gt"].append(gold_int)
        groups[f"subtype_{ast}"]["pred"].append(pred)

        # By source
        src = gt.get("source", "unknown")
        groups[f"source_{src}"]["gt"].append(gold_int)
        groups[f"source_{src}"]["pred"].append(pred)

    return {"groups": dict(groups), "per_query": {}}

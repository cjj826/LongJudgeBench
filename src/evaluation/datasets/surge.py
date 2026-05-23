"""SurGE dataset module.
Judge: listwise (batch scoring → ranking, compared against human ranking)
GT:    listwise (rank 1-4)
extract_metrics: converts pointwise scores to rankings and compares with GT.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from src.utils.io_utils import load_jsonl


def get_paradigm() -> str:
    return "listwise"


def load_data(data_dir: str = None) -> list[dict]:
    """Load from data_standardized/surge.jsonl"""
    path = Path(data_dir) if data_dir else BASE_DIR / "data_standardized" / "surge.jsonl"
    return load_jsonl(path)


def _scores_to_ranks(scores_dict: dict) -> dict:
    """Convert {model: score} to {model: rank}, using average rank for ties."""
    sorted_models = sorted(scores_dict.items(), key=lambda x: x[1], reverse=True)
    ranks = {}
    n = len(sorted_models)
    i = 0
    while i < n:
        # Find tied-score segment
        j = i
        while j < n and sorted_models[j][1] == sorted_models[i][1]:
            j += 1
        avg_rank = (i + 1 + j) / 2  # average rank for ties
        for k in range(i, j):
            ranks[sorted_models[k][0]] = avg_rank
        i = j
    return ranks


def extract_metrics(judge_results: list, gt_data: list, exclude_gt: bool = False) -> dict:
    """
    Judge output: {data_id, model: model_name, judge_result: {structural_score: N, content_score: N}}
    or listwise format: {data_id, models: [A,B,C,D], judge_result: {A: {structural_score:, content_score:}, ...}}

    GT: {id, structure_ranking: {model: rank}, content_ranking: {model: rank}}
    Returns groups: {structure: {gt,pred}, content: {gt,pred}}

    Args:
        exclude_gt: True = always exclude GT (3 pairs); False = exclude GT only in reference mode (default)
    """
    gt_map = {}
    for g in gt_data:
        gid = str(g["id"])
        gt_map[gid] = {
            "structure": g.get("structure_ranking", {}),
            "content": g.get("content_ranking", {}),
        }

    groups = {
        "structure": {"gt": [], "pred": []},
        "content": {"gt": [], "pred": []},
    }

    # Aggregate scores by data_id
    paper_scores = {}
    for r in judge_results:
        did = str(r.get("data_id", ""))
        if did not in gt_map:
            continue
        jr = r.get("judge_result", {})
        if not jr:
            continue

        # Support two output formats
        if did not in paper_scores:
            paper_scores[did] = {"structure": {}, "content": {}}

        # Format 1: pointwise single output {data_id, model, judge_result: {structural_score, content_score}}
        model = r.get("model", "")
        if model:
            if isinstance(jr, dict):
                struct_score = jr.get("structural_score")
                content_score = jr.get("content_score")
                if struct_score is not None:
                    paper_scores[did]["structure"][model] = float(struct_score)
                if content_score is not None:
                    paper_scores[did]["content"][model] = float(content_score)

        # Format 2: batch output {data_id, models: [A,B,C,D], judge_result: {A: {structural_score:, content_score:}, ...}}
        models_list = r.get("models", [])
        if models_list and isinstance(jr, dict):
            letter_keys = ["A", "B", "C", "D"]
            for i, m in enumerate(models_list):
                key = letter_keys[i] if i < len(letter_keys) else m
                m_data = jr.get(key, {})
                if not isinstance(m_data, dict):
                    m_data = jr.get(m, {})
                if isinstance(m_data, dict):
                    struct_score = m_data.get("structural_score")
                    content_score = m_data.get("content_score")
                    if struct_score is not None:
                        paper_scores[did]["structure"][m] = float(struct_score)
                    if content_score is not None:
                        paper_scores[did]["content"][m] = float(content_score)

    # Convert paper scores to rankings, compare with GT
    # If GT exists in GT ranking but not in predicted scores (reference mode),
    # auto-assign highest score → rank 1, and record ref_dims for GT exclusion in ACC
    from collections import defaultdict
    ref_dims = defaultdict(set)
    for did, dims in paper_scores.items():
        for dim in ["structure", "content"]:
            scores = dims.get(dim, {})
            gt_ranks = gt_map[did][dim]
            if "GT" not in scores and "GT" in gt_ranks:
                scores["GT"] = 5.1  # exceeds 0-5 scale to guarantee rank 1
                ref_dims[did].add(dim)
    per_query = {"structure": {}, "content": {}}
    for did, dims in paper_scores.items():
        for dim in ["structure", "content"]:
            scores = dims.get(dim, {})
            if len(scores) < 2:
                continue
            pred_ranks = _scores_to_ranks(scores)
            gt_ranks = gt_map[did][dim]
            # Collect per-query data (exclude GT in reference mode or when exclude_gt=True)
            gt_list, pred_list = [], []
            for m in scores:
                if m == "GT" and (exclude_gt or dim in ref_dims.get(did, set())):
                    continue  # GT injected as rank 1 → pairs containing GT are not meaningful
                if m in gt_ranks:
                    gt_list.append(float(gt_ranks[m]))
                    pred_list.append(float(pred_ranks[m]))
            if gt_list:
                per_query[dim][did] = {"gt": gt_list, "pred": pred_list}
            # Global groups (also exclude GT)
            for m in scores:
                if m == "GT" and (exclude_gt or dim in ref_dims.get(did, set())):
                    continue
                if m in gt_ranks:
                    groups[dim]["gt"].append(float(gt_ranks[m]))
                    groups[dim]["pred"].append(float(pred_ranks[m]))

    return {"groups": groups, "per_query": per_query}

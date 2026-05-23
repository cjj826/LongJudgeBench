"""DeepResearch-Bench dataset module.
Supports vanilla (overall_score) and rubric (per-dimension) output formats.

Rubric mode: criteria.jsonl defines per-criterion weights.
LLM outputs per-criterion scores, then weighted-average aggregates into dimension scores.
"""
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from src.utils.io_utils import load_jsonl

# Sub-dimension list (rubric mode)
DIMS = ["comprehensiveness", "insight", "instruction_following", "readability"]


def get_paradigm() -> str:
    return "pointwise"


def load_data(data_dir: str = None) -> list[dict]:
    """Load from data_standardized/deepresearch_bench.jsonl"""
    path = Path(data_dir) if data_dir else BASE_DIR / "data_standardized" / "deepresearch_bench.jsonl"
    return load_jsonl(path)


def load_criteria_map() -> dict:
    """Load sub-criterion weights from raw criteria.jsonl.

    Returns:
        {id_str: {"criterions": {"comprehensiveness": [{criterion, weight}, ...], ...}}}
    """
    path = BASE_DIR / "data" / "DeepResearch-Bench-Dataset" / "criteria.jsonl"
    result = {}
    for entry in load_jsonl(path):
        result[str(entry["id"])] = {
            "criterions": entry.get("criterions", {}),
        }
    return result


def _extract_dim_scores(jr: dict, sub_criterions: dict = None) -> dict:
    """Extract dimension scores from judge_result, supporting weighted aggregation.

    Rubric reference format (vanilla_rubric_reference):
      {"comprehensiveness": [{"criterion": "...", "analysis": "...",
                              "article_1_score": 8.0, "article_2_score": 7.5}, ...]}
      Uses article_2_score (target article) weighted by sub-criterion weights.

    Rubric simple format (vanilla_rubric):
      {"comprehensiveness": [{"criterion": "...", "analysis": "...",
                              "target_score": 7.5}, ...]}
      Uses target_score weighted by sub-criterion weights.

    Rubric flat format (legacy):
      {"comprehensiveness": 8.5}
    Vanilla format:
      {"overall_score": 7.5}
    """
    dim_scores = {}
    for dim in DIMS:
        val = jr.get(dim)
        if val is None:
            continue
        if isinstance(val, list) and len(val) > 0:
            # Per-sub-criterion array format: extract scores
            scores = []
            for item in val:
                if not isinstance(item, dict):
                    continue
                score = item.get("article_2_score") or item.get("target_score")
                if score is not None:
                    scores.append(float(score))

            if not scores:
                continue

            # Weighted average using sub-criterion weights
            sub_weights = None
            if sub_criterions and dim in sub_criterions:
                sub_list = sub_criterions[dim]
                sub_weights = [c.get("weight", 1.0) for c in sub_list]

            if sub_weights and len(sub_weights) == len(scores):
                total_weight = sum(sub_weights)
                if total_weight > 0:
                    dim_scores[dim] = sum(s * w for s, w in zip(scores, sub_weights)) / total_weight
                else:
                    dim_scores[dim] = sum(scores) / len(scores)
            else:
                dim_scores[dim] = sum(scores) / len(scores)
        else:
            # Flat numeric format (legacy compatibility)
            dim_scores[dim] = float(val)
    return dim_scores


def extract_metrics(judge_results: list, gt_data: list) -> dict:
    """
    Judge vanilla:  {data_id, model, judge_result: {overall_score}}
    Judge rubric:  {data_id, model, judge_result: {comprehensiveness: [{criterion, analysis, target_score}, ...], ...}}

    GT: {id, aggregated: {model: {weighted_total, overall, dimensions}}}
    Matches by (data_id, model). Returns groups for "all" and each dimension.
    """
    gt_map = {}
    dim_weight_map = {}  # {id_str: {dim: weight}}
    for g in gt_data:
        gid = str(g["id"])
        dw = g.get("dimension_weights", {})
        if dw:
            dim_weight_map[gid] = dw
        for model_name, scores in g.get("aggregated", {}).items():
            gt_map[(gid, model_name)] = {
                "weighted_total": scores.get("weighted_total", 0) / 10.0,
                "overall": scores.get("overall", 0) / 10.0,
                "dimensions": scores.get("dimensions", {}),
            }

    # Load sub-criterion weights (for rubric mode weighted aggregation)
    criteria_map = load_criteria_map()

    groups = defaultdict(lambda: {"gt": [], "pred": []})
    # per_query[group_name][did] = {"gt": [...], "pred": [...]}
    per_query = defaultdict(lambda: defaultdict(lambda: {"gt": [], "pred": []}))

    for r in judge_results:
        key = (str(r.get("data_id", "")), r.get("model", ""))
        if key not in gt_map or "judge_result" not in r:
            continue
        jr = r["judge_result"]
        if not isinstance(jr, dict):
            continue

        did = str(r.get("data_id", ""))
        baseline = r["model"]
        gt_entry = gt_map[key]

        # 1) overall_score (vanilla mode)
        if "overall_score" in jr:
            pred_val = float(jr["overall_score"])
            gt_overall = gt_entry["overall"]
            groups[baseline]["gt"].append(gt_overall)
            groups[baseline]["pred"].append(pred_val)
            groups["all"]["gt"].append(gt_overall)
            groups["all"]["pred"].append(pred_val)
            per_query["all"][did]["gt"].append(gt_overall)
            per_query["all"][did]["pred"].append(pred_val)

        # 2) Sub-dimension scores (rubric mode)
        criteria_entry = criteria_map.get(did, {})
        sub_criterions = criteria_entry.get("criterions", {})
        dim_scores = _extract_dim_scores(jr, sub_criterions)
        gt_dims = gt_entry.get("dimensions", {})
        if dim_scores:
            dim_weights = dim_weight_map.get(did, {})
            wsum_gt = 0.0
            wsum_pred = 0.0
            tw = 0.0
            for dim, pred_val in dim_scores.items():
                gt_dim = gt_dims.get(dim, 0) / 10.0  # GT sub-dimension 0-100 → 0-10
                groups[f"dim_{dim}"]["gt"].append(gt_dim)
                groups[f"dim_{dim}"]["pred"].append(pred_val)
                per_query[f"dim_{dim}"][did]["gt"].append(gt_dim)
                per_query[f"dim_{dim}"][did]["pred"].append(pred_val)
                w = dim_weights.get(dim, 1.0)
                wsum_gt += gt_dim * w
                wsum_pred += pred_val * w
                tw += w
            # Weighted average by criteria dimension weights → "all" group (total score)
            # (total derived from sub-scores × dimension_weight, not directly output)
            if tw > 0:
                groups["all"]["gt"].append(wsum_gt / tw)
                groups["all"]["pred"].append(wsum_pred / tw)
                per_query["all"][did]["gt"].append(wsum_gt / tw)
                per_query["all"][did]["pred"].append(wsum_pred / tw)

    # Convert per_query from nested defaultdict to plain dict
    per_query_out = {k: dict(v) for k, v in per_query.items()}
    return {"groups": dict(groups), "per_query": per_query_out}


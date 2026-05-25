"""RealDR dataset module — loads from data_standardized."""
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
from src.utils.io_utils import load_jsonl


def get_paradigm() -> str:
    return "pointwise"


def load_data(data_dir: str = None) -> list[dict]:
    """
    Load from data_standardized/realdr.jsonl.
    Returns list of standardized records.
    """
    path = Path(data_dir) if data_dir else BASE_DIR / "data_standardized" / "realdr.jsonl"
    return load_jsonl(path)


def extract_metrics(judge_results: list, gt_data: list) -> dict:
    """
    Judge vanilla: {overall_score} → overall score
    Judge rubric:  {logical_structure_score, expression_score, bias_check_score} → dimension scores
    GT: {weighted_total, dimensions: {逻辑结构, 表达形式, 偏见检查}, weights: {...}}
    Matches by data_id. Returns groups: all, model:{name}, task:{id}, dim:{name}.
    """
    DIM_KEYS = ("logical_structure_score", "expression_score", "bias_check_score")
    # Dataset-internal dimension name keys (used in ground truth JSON):
    DIM_NAMES = ("逻辑结构", "表达形式", "偏见检查")  # logical_structure, expression, bias_check
    DIM_NAMES_EN = ("logical_structure", "expression", "bias_check")

    gt_map = {str(g["id"]): g for g in gt_data}

    groups = defaultdict(lambda: {"gt": [], "pred": []})
    per_task = defaultdict(lambda: {"gt": [], "pred": []})
    per_dim = defaultdict(lambda: defaultdict(lambda: {"gt": [], "pred": []}))

    for r in judge_results:
        did = str(r.get("data_id", ""))
        if did not in gt_map or "judge_result" not in r:
            continue
        jr = r["judge_result"]
        if not isinstance(jr, dict):
            continue

        baseline = r.get("model", "unknown")
        task_id = str(gt_map[did].get("task_id", "unknown"))
        gt_entry = gt_map[did]
        gt_dims = gt_entry.get("dimensions", {})
        dim_weights = gt_entry.get("weights", {})

        # ── 1) overall_score — used by both vanilla and rubric ──
        score_key = next((k for k in ("overall_score", "overall_quality_score", "quality_score", "score") if k in jr), None)
        if score_key is not None:
            overall_pred = float(jr[score_key])
            gt_total = float(gt_entry["weighted_total"])
            groups["all"]["gt"].append(gt_total)
            groups["all"]["pred"].append(overall_pred)
            groups[f"model:{baseline}"]["gt"].append(gt_total)
            groups[f"model:{baseline}"]["pred"].append(overall_pred)
            groups[f"task:{task_id}"]["gt"].append(gt_total)
            groups[f"task:{task_id}"]["pred"].append(overall_pred)
            per_task[task_id]["gt"].append(gt_total)
            per_task[task_id]["pred"].append(overall_pred)

        # ── 2) Dimension scores ──
        #    rubric → use model output dimension scores; vanilla → use overall_score as proxy
        for dim_key, dim_name in zip(DIM_KEYS, DIM_NAMES):
            if dim_key in jr:
                pred_val = float(jr[dim_key])
            elif score_key is not None:
                pred_val = overall_pred
            else:
                continue
            gt_val = float(gt_dims.get(dim_name, 0))
            groups[f"dim_{dim_name}"]["gt"].append(gt_val)
            groups[f"dim_{dim_name}"]["pred"].append(pred_val)
            per_dim[f"dim_{dim_name}"][task_id]["gt"].append(gt_val)
            per_dim[f"dim_{dim_name}"][task_id]["pred"].append(pred_val)

        # ── 3) Weighted total (rubric mode) ──
        rubric_scores = {dim_name: float(jr[dim_key])
                         for dim_key, dim_name in zip(DIM_KEYS, DIM_NAMES)
                         if dim_key in jr}
        if len(rubric_scores) == 3:
            w_pred = sum(rubric_scores[d] * dim_weights.get(d, 1.0) for d in rubric_scores)
            w_gt = sum(gt_dims.get(d, 0) * dim_weights.get(d, 1.0) for d in rubric_scores)
            tw = sum(dim_weights.get(d, 1.0) for d in rubric_scores)
            if tw > 0:
                wa_pred = w_pred / tw
                wa_gt = w_gt / tw
                groups["all"]["gt"].append(wa_gt)
                groups["all"]["pred"].append(wa_pred)
                groups[f"model:{baseline}"]["gt"].append(wa_gt)
                groups[f"model:{baseline}"]["pred"].append(wa_pred)
                groups[f"task:{task_id}"]["gt"].append(wa_gt)
                groups[f"task:{task_id}"]["pred"].append(wa_pred)
                per_task[task_id]["gt"].append(wa_gt)
                per_task[task_id]["pred"].append(wa_pred)

    per_query = {"all": dict(per_task)}
    for dim_key, data in per_dim.items():
        per_query[dim_key] = dict(data)
    return {"groups": dict(groups), "per_query": per_query}

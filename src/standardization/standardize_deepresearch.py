"""
Standardize DeepResearch-Bench-Dataset
Input:
  - data/DeepResearch-Bench-Dataset/generated_reports/{model}.jsonl  (4 models)
  - data/DeepResearch-Bench-Dataset/Deepresearch_GT.jsonl  (3 annotators)
  - data/DeepResearch-Bench-Dataset/criteria.jsonl  (dimension weights)
Output:
  - data_standardized/deepresearch_bench.jsonl
  - ground_truth/deepresearch_bench_gt.jsonl
"""

from pathlib import Path
from collections import defaultdict

from src.standardization.utils import (
    BASE_DIR, ensure_output_dirs, save_jsonl, clear_jsonl, load_jsonl, count_tokens
)

# ── Paths ───────────────────────────────────────────────────
DATA_DIR = BASE_DIR / "data" / "DeepResearch-Bench-Dataset"
GEN_REPORTS_DIR = DATA_DIR / "generated_reports"
GT_PATH = DATA_DIR / "Deepresearch_GT.jsonl"
CRITERIA_PATH = DATA_DIR / "criteria.jsonl"

MODELS = ["openai-deepresearch", "gemini-2.5-pro-deepresearch",
          "grok-deeper-search", "perplexity-Research"]

OUT_DATA = BASE_DIR / "data_standardized" / "deepresearch_bench.jsonl"
OUT_GT = BASE_DIR / "ground_truth" / "deepresearch_bench_gt.jsonl"
OUT_CRITERIA = BASE_DIR / "data_standardized" / "deepresearch_bench_criteria.jsonl"


def load_criteria():
    """Load dimension weights and full criterion descriptions {id: {dim: weight, criterions: [...]}}"""
    criteria = {}
    for entry in load_jsonl(CRITERIA_PATH):
        criteria[entry["id"]] = {
            "dimension_weight": entry.get("dimension_weight", {}),
            "criterions": entry.get("criterions", {}),
        }
    return criteria


def format_criteria_text(eid: int, criteria_data: dict) -> str:
    """Format dimension + criterion + sub-weight from criteria.jsonl into readable text for {criteria_list} injection."""
    dim_weight = criteria_data.get("dimension_weight", {})
    criterions = criteria_data.get("criterions", {})
    lines = []
    for dim_name in ["comprehensiveness", "insight", "instruction_following", "readability"]:
        weight = dim_weight.get(dim_name, 0)
        dim_label = dim_name.replace("_", " ").title()
        lines.append(f"Dimension: {dim_label} (dimension_weight: {weight})")
        for c in criterions.get(dim_name, []):
            c_weight = c.get("weight", "")
            weight_tag = f"[Weight: {c_weight}] " if c_weight else ""
            lines.append(f"  - {weight_tag}{c['criterion']}: {c['explanation']}")
        lines.append("")
    return "\n".join(lines)


def load_generated_reports():
    """Load output from 4 models {id: {model: article}}"""
    reports = defaultdict(dict)  # {id: {model: article}}
    prompts = {}                 # {id: prompt}

    for model in MODELS:
        fpath = GEN_REPORTS_DIR / f"{model}.jsonl"
        for entry in load_jsonl(fpath):
            eid = entry["id"]
            if eid <= 50:                          # take only first 50
                reports[eid][model] = entry.get("article", "")
                if eid not in prompts:
                    prompts[eid] = entry.get("prompt", "")
    return reports, prompts


def load_ground_truth():
    """Load ground truth {id: [annotation, ...]}"""
    gt = defaultdict(list)
    for entry in load_jsonl(GT_PATH):
        gt[entry["id"]].append(entry)
    return gt


# Raw annotation dimension name → normalized name mapping
DIM_NAME_MAP = {
    "Comprehensiveness": "comprehensiveness",
    "depth": "insight",
    "instruction following": "instruction_following",
    "readability": "readability",
}


def _map_dim(name: str) -> str:
    """Map raw dimension names from annotations to normalized names."""
    return DIM_NAME_MAP.get(name, name)


def aggregate_scores(scores_list):
    """Average scores across multiple annotators."""
    if not scores_list:
        return {}, 0
    # Collect all models × all dimensions (mapped)
    all_models = set()
    all_dims = set()
    for s in scores_list:
        ds = s.get("dimension_scores", {})
        for model, dims in ds.items():
            all_models.add(model)
            for dim in dims:
                all_dims.add(_map_dim(dim))

    result = {}
    for model in all_models:
        result[model] = {}
        for dim in all_dims:
            # Raw annotation uses unmapped names (e.g. "Comprehensiveness"), need reverse lookup
            raw_dim = {v: k for k, v in DIM_NAME_MAP.items()}.get(dim, dim)
            vals = [s["dimension_scores"][model][raw_dim]
                    for s in scores_list
                    if model in s.get("dimension_scores", {})
                    and raw_dim in s["dimension_scores"][model]]
            result[model][dim] = round(sum(vals) / len(vals), 1) if vals else 0

    # Overall average
    overall_result = {}
    for model in all_models:
        vals = [s["overall_scores"][model]
                for s in scores_list
                if model in s.get("overall_scores", {})]
        overall_result[model] = round(sum(vals) / len(vals), 1) if vals else 0

    return result, overall_result


def main():
    ensure_output_dirs()
    clear_jsonl(OUT_DATA)
    clear_jsonl(OUT_GT)
    clear_jsonl(OUT_CRITERIA)

    print("=" * 60)
    print("DeepResearch-Bench Standardization")
    print("=" * 60)

    # Load data
    criteria = load_criteria()
    reports, prompts = load_generated_reports()
    gt_raw = load_ground_truth()

    print(f"  Models: {len(MODELS)}")
    print(f"  Records: {len(reports)}")
    print(f"  GT entries: {sum(len(v) for v in gt_raw.values())} (annotators: 3)")

    all_ids = sorted(reports.keys())
    for eid in all_ids:
        prompt = prompts.get(eid, "")
        models_data = reports.get(eid, {})
        criteria_entry = criteria.get(eid, {})
        dim_weights = criteria_entry.get("dimension_weight", {})
        gt_entries = gt_raw.get(eid, [])

        # Aggregate ground truth
        dim_avg, overall_avg = aggregate_scores(gt_entries)
        annotators_count = len(gt_entries)

        # Compute weighted total score
        gt_scores = {}
        for model in MODELS:
            if model in dim_avg:
                dims = dim_avg[model]
                weighted = sum(dims.get(d, 0) * dim_weights.get(d, 0)
                               for d in dims)
                gt_scores[model] = {
                    "dimensions": dims,
                    "weighted_total": round(weighted, 1),
                    "overall": overall_avg.get(model, 0),
                }

        # Build responses
        responses = []
        for model in MODELS:
            if model in models_data:
                responses.append({"model": model, "content": models_data[model]})

        # 800-token filter: keep only responses >= 800 tokens (pointwise scores independently)
        THRESHOLD = 800
        responses = [r for r in responses if count_tokens(r["content"]) >= THRESHOLD]
        if not responses:
            continue

        # Save standardized record
        record = {
            "dataset": "deepresearch_bench",
            "id": eid,
            "instruction": prompt,
            "responses": responses,
            "ground_truth": {
                "type": "pointwise_multi_dim",
                "dimension_weights": dim_weights,
                "annotators": annotators_count,
                "scores": gt_scores,
            },
            "meta": {
                "language": "zh",
                "task_type": "pointwise",
                "source": "DeepResearch-Bench-Dataset",
            },
        }
        save_jsonl(record, OUT_DATA)

        # Save ground truth
        gt_record = {
            "dataset": "deepresearch_bench",
            "id": eid,
            "instruction": prompt,
            "dimension_weights": dim_weights,
            "annotators": annotators_count,
            "raw_annotations": [
                {
                    "annotation_id": a["annotation_id"],
                    "dimension_scores": a["dimension_scores"],
                    "overall_scores": a["overall_scores"],
                }
                for a in gt_entries
            ],
            "aggregated": gt_scores,
        }
        save_jsonl(gt_record, OUT_GT)

        # Save criteria text (for rubric mode {criteria_list} injection)
        criteria_text = format_criteria_text(eid, criteria_entry)
        criteria_record = {"id": eid, "criteria_text": criteria_text}
        save_jsonl(criteria_record, OUT_CRITERIA)

    print(f"\n  Output:")
    print(f"    Standardized data: {OUT_DATA} ({len(all_ids)} records)")
    print(f"    Ground truth:      {OUT_GT} ({len(all_ids)} records)")
    print(f"    Criteria:          {OUT_CRITERIA} ({len(all_ids)} records)")
    print("  Done!")


if __name__ == "__main__":
    main()

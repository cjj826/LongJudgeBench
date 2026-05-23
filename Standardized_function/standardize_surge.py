"""
Standardize SurGE
Input:
  - data/SurGE/标注结果.xlsx  (41 topics × rankings)
  - data/SurGE/baselines/{model}/output/{id}/  (4 model outputs)
Output:
  - data_standardized/surge.jsonl
  - ground_truth/surge_gt.jsonl
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import openpyxl
from Standardized_function.utils import (
    BASE_DIR, ensure_output_dirs, save_jsonl, clear_jsonl, count_tokens
)

# ── Paths ───────────────────────────────────────────────────
SURGE_DIR = BASE_DIR / "data" / "SurGE"
XLSX_PATH = SURGE_DIR / "标注结果.xlsx"
BASELINES_DIR = SURGE_DIR / "baselines"

MODELS = ["GT", "Autosurvey", "ID", "Naive"]

OUT_DATA = BASE_DIR / "data_standardized" / "surge.jsonl"
OUT_GT = BASE_DIR / "ground_truth" / "surge_gt.jsonl"
OUT_REF = BASE_DIR / "data_standardized" / "surge_reference.jsonl"

GT_SURVEYS_FILE = SURGE_DIR / "baselines" / "GT_surveys.json"


def read_file_content(filepath):
    """Read file content."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def find_first_file(directory):
    """Return the first file path in a directory."""
    if not directory.exists():
        return None
    for f in directory.iterdir():
        if f.is_file():
            return f
    return None


def main():
    ensure_output_dirs()
    clear_jsonl(OUT_DATA)
    clear_jsonl(OUT_GT)

    print("=" * 60)
    print("SurGE Standardization")
    print("=" * 60)

    # 读取 xlsx
    wb = openpyxl.load_workbook(XLSX_PATH)
    ws = wb["Sheet1"]

    # Columns: data_id(0), Topic(1), structure ranking: GT(2), AutoSurvey(3), ID(4), Naive(5),
    #              content ranking: GT(6), AutoSurvey(7), ID(8), Naive(9)
    # Load GT surveys as reference
    gt_surveys = {}
    if GT_SURVEYS_FILE.exists():
        import json
        with open(GT_SURVEYS_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
        if isinstance(raw, list):
            for item in raw:
                tid = item.get("topic_id", item.get("id", ""))
                gt_surveys[str(tid)] = item.get("full_text", item.get("article", item.get("content", "")))
        elif isinstance(raw, dict):
            gt_surveys = {str(k): v.get("full_text", v.get("article", v.get("content", ""))) for k, v in raw.items()}
    print(f"  GT surveys: {len(gt_surveys)} records")

    clear_jsonl(OUT_REF)
    count = 0
    for row in ws.iter_rows(min_row=2, max_row=42, values_only=True):
        task_id = row[0]
        if task_id is None:
            continue
        task_id = int(task_id)
        topic = str(row[1]).strip() if row[1] else ""

        # Read rankings (key names aligned with MODELS for GT sync)
        structure_ranking = {
            "GT": int(row[2]), "Autosurvey": int(row[3]),
            "ID": int(row[4]), "Naive": int(row[5]),
        }
        content_ranking = {
            "GT": int(row[6]), "Autosurvey": int(row[7]),
            "ID": int(row[8]), "Naive": int(row[9]),
        }

        # Read output content for each model
        responses = []
        for model in MODELS:
            model_dir = BASELINES_DIR / model / "output" / str(task_id)
            fpath = find_first_file(model_dir)
            content = read_file_content(fpath) if fpath else ""
            responses.append({"model": model, "content": content})

        # 800-token filter: keep only responses >= 800 tokens (listwise ranks remaining)
        THRESHOLD = 800
        responses = [r for r in responses if count_tokens(r["content"]) >= THRESHOLD]
        if len(responses) < 2:
            continue

        # Sync GT ranking: keep only models that survived the filter
        kept_models = {r["model"] for r in responses}
        structure_ranking = {m: rank for m, rank in structure_ranking.items() if m in kept_models}
        content_ranking = {m: rank for m, rank in content_ranking.items() if m in kept_models}

        # Standardized data
        record = {
            "dataset": "surge",
            "id": task_id,
            "instruction": topic,
            "responses": responses,
            "ground_truth": {
                "type": "listwise_ranking",
                "structure_ranking": structure_ranking,
                "content_ranking": content_ranking,
            },
            "meta": {
                "language": "en",
                "task_type": "listwise",
                "source": "SurGE",
            },
        }
        save_jsonl(record, OUT_DATA)

        # Ground truth
        gt_record = {
            "dataset": "surge",
            "id": task_id,
            "instruction": topic,
            "structure_ranking": structure_ranking,
            "content_ranking": content_ranking,
            "annotation_type": "listwise_ranking",
        }
        save_jsonl(gt_record, OUT_GT)

        # Save reference (full GT survey text)
        ref_text = gt_surveys.get(str(task_id), "")
        if ref_text:
            save_jsonl({"id": str(task_id), "reference": ref_text}, OUT_REF)
        count += 1

    print(f"  Total: {count} records")
    print(f"  Output:")
    print(f"    Standardized data: {OUT_DATA}")
    print(f"    Ground truth:      {OUT_GT}")
    print(f"    Reference:         {OUT_REF}")
    print("  Done!")


if __name__ == "__main__":
    main()

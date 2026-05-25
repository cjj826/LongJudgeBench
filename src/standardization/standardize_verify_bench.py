"""
Standardize VerifyBench (Hard split only)
Input:
  - data/VerifyBench/data/verify_bench_hard.jsonl
Output:
  - data_standardized/verify_bench_hard.jsonl
  - ground_truth/verify_bench_hard_gt.jsonl
  - data_standardized/verify_bench_hard_reference.jsonl
"""
import json
from pathlib import Path

from src.standardization.utils import (
    BASE_DIR, ensure_output_dirs, save_jsonl, clear_jsonl, count_tokens
)

# ── Paths ──
VB_DIR = BASE_DIR / "data" / "VerifyBench" / "data"

OUT_DATA = BASE_DIR / "data_standardized" / "verify_bench_hard.jsonl"
OUT_GT = BASE_DIR / "ground_truth" / "verify_bench_hard_gt.jsonl"
OUT_REF = BASE_DIR / "data_standardized" / "verify_bench_hard_reference.jsonl"


def standardize_split(src_path: Path, out_data: Path, out_gt: Path, variant: str, out_ref: Path = None):
    """
    Core standardization logic:
    - instruction: question only (wo_ref mode, answer excluded)
    - responses: each completion as one response
    - ground_truth: gold_correct + answer_type/subtype + source + answer (reference)
    - answer is NOT included in instruction (for Judge wo_ref mode)
    """
    records = []
    with open(src_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    print(f"\n  {variant}: {len(records)} records")

    data_count = 0
    gt_count = 0
    for item in records:
        instruction = item.get("question", "")
        content = item.get("completion", "")
        answer = item.get("answer", "")
        gold_correct = item.get("gold_correct", False)

        # response: completion only, no answer (wo_ref)
        responses = [{"model": item.get("completion_model", "unknown"), "content": content}]

        # 800-token filter
        if count_tokens(content) < 800:
            continue

        # Standardized data
        data_record = {
            "dataset": variant,
            "id": f"{item.get('question_id', '')}_{item.get('completion_id', '')}",
            "instruction": instruction,
            "responses": responses,
            "ground_truth": {
                "type": "pointwise_binary",
                "gold_correct": gold_correct,
                "answer_type": item.get("answer_type", ""),
                "answer_subtype": item.get("answer_subtype", ""),
                "source": item.get("source", ""),
                "completion_model": item.get("completion_model", ""),
            },
            "meta": {
                "language": "en",
                "task_type": "pointwise",
                "source": "VerifyBench",
                "variant": variant,
                "question_id": item.get("question_id", ""),
                "completion_id": item.get("completion_id", ""),
                "annotators": item.get("annotator", []),
            },
        }
        save_jsonl(data_record, out_data)
        data_count += 1

        # Ground truth
        data_id = f"{item.get('question_id', '')}_{item.get('completion_id', '')}"
        gt_record = {
            "dataset": variant,
            "id": data_id,
            "gold_correct": gold_correct,
            "answer_type": item.get("answer_type", ""),
            "answer_subtype": item.get("answer_subtype", ""),
            "source": item.get("source", ""),
            "completion_model": item.get("completion_model", ""),
            "answer": answer,
            "annotation_type": "pointwise_binary",
        }
        save_jsonl(gt_record, out_gt)
        gt_count += 1

        # Reference data (for reference prompt mode injecting {reference})
        if out_ref and answer:
            ref_record = {"id": data_id, "reference": answer}
            save_jsonl(ref_record, out_ref)

    return data_count, gt_count


def main():
    ensure_output_dirs()
    clear_jsonl(OUT_DATA)
    clear_jsonl(OUT_GT)
    clear_jsonl(OUT_REF)

    print("=" * 60)
    print("VerifyBench Standardization (Hard split only)")
    print("=" * 60)

    src_hard = VB_DIR / "verify_bench_hard.jsonl"

    print("\n[1/1] verify_bench_hard...")
    n_data, n_gt = standardize_split(src_hard, OUT_DATA, OUT_GT, "verify_bench_hard", out_ref=OUT_REF)

    print(f"\n  Total standardized data: {n_data} records")
    print(f"  Total ground truth:      {n_gt} records")
    print(f"\n  Output:")
    print(f"    Standardized data: {OUT_DATA}")
    print(f"    Ground truth:      {OUT_GT}")
    print("  Done!")


if __name__ == "__main__":
    main()

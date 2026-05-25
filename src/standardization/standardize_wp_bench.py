"""
Standardize Writing-Preference-Bench
Input:
  - data/Writing-Preference-Bench-main/WP_bench_chinese.json
  - data/Writing-Preference-Bench-main/WP_bench_english.json
Output:
  - data_standardized/wp_bench.jsonl
  - ground_truth/wp_bench_gt.jsonl
"""

import json
from pathlib import Path

from src.standardization.utils import (
    BASE_DIR, ensure_output_dirs, save_jsonl, clear_jsonl, count_tokens
)

# ── Paths ───────────────────────────────────────────────────
WP_DIR = BASE_DIR / "data" / "Writing-Preference-Bench-main"
FILES = [
    ("zh", WP_DIR / "WP_bench_chinese.json"),
    ("en", WP_DIR / "WP_bench_english.json"),
]

OUT_DATA = BASE_DIR / "data_standardized" / "wp_bench.jsonl"
OUT_GT = BASE_DIR / "ground_truth" / "wp_bench_gt.jsonl"


def main():
    ensure_output_dirs()
    clear_jsonl(OUT_DATA)
    clear_jsonl(OUT_GT)

    print("=" * 60)
    print("Writing-Preference-Bench Standardization")
    print("=" * 60)

    total = 0
    for lang, fpath in FILES:
        if not fpath.exists():
            print(f"  [Skip] {fpath.name} not found")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"\n  [{lang.upper()}] {fpath.name}: {len(data)} records")

        for entry in data:
            prompt = entry.get("prompt", "")
            prompt_id = entry.get("prompt_id", "")

            chosen = entry.get("chosen", {})
            rejected = entry.get("rejected", {})

            responses = []
            if isinstance(chosen, dict) and chosen.get("response"):
                responses.append({
                    "model": chosen.get("model", "chosen"),
                    "content": chosen["response"],
                    "label": 1,  # chosen = better
                })
            if isinstance(rejected, dict) and rejected.get("response"):
                responses.append({
                    "model": rejected.get("model", "rejected"),
                    "content": rejected["response"],
                    "label": 0,  # rejected = worse
                })

            # 800-token filter: skip if any response < 800
            THRESHOLD = 800
            skip = False
            for resp in responses:
                if count_tokens(resp["content"]) < THRESHOLD:
                    skip = True
                    break
            if skip:
                continue

            # Standardized data
            record = {
                "dataset": "wp_bench",
                "id": prompt_id,
                "instruction": prompt,
                "responses": responses,
                "ground_truth": {
                    "type": "pairwise_preference",
                    "chosen": {
                        "model": chosen.get("model", ""),
                        "score": chosen.get("score"),
                    },
                    "rejected": {
                        "model": rejected.get("model", ""),
                        "score": rejected.get("score"),
                    },
                },
                "meta": {
                    "language": lang,
                    "task_type": "pairwise",
                    "source": "Writing-Preference-Bench",
                    "tag": entry.get("tag", ""),
                },
            }
            save_jsonl(record, OUT_DATA)

            # Ground truth
            gt_record = {
                "dataset": "wp_bench",
                "id": prompt_id,
                "instruction": prompt,
                "preference": {
                    "chosen_model": chosen.get("model", ""),
                    "rejected_model": rejected.get("model", ""),
                },
                "scores": {
                    "chosen": chosen.get("score"),
                    "rejected": rejected.get("score"),
                },
                "annotation_type": "pairwise_preference",
            }
            save_jsonl(gt_record, OUT_GT)
            total += 1

    print(f"\n  Total: {total} records")
    print(f"  Output:")
    print(f"    Standardized data: {OUT_DATA}")
    print(f"    Ground truth:      {OUT_GT}")
    print("  Done!")


if __name__ == "__main__":
    main()

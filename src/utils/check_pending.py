"""
Scan outputs/judge_results/ for all models and list incomplete tasks.

Usage:
  python src/utils/check_pending.py
  python src/utils/check_pending.py --model qwen3-32b
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.utils.io_utils import load_jsonl

# ── Dataset config (synced with run_all.py) ──
DATASETS = [
    ("deepresearch_bench", "pointwise",
     ["vanilla", "vanilla_reference", "vanilla_rubric", "vanilla_rubric_reference"]),
    ("realdr", "pointwise",
     ["vanilla", "vanilla_reference", "vanilla_rubric", "vanilla_rubric_reference"]),
    ("verify_bench_hard", "pointwise",
     ["vanilla", "vanilla_reference", "vanilla_rubric", "vanilla_rubric_reference"]),
    ("wp_bench", "pairwise",
     ["vanilla", "vanilla_rubric"]),
    ("ma", "pairwise",
     ["insights_vanilla", "insights_vanilla_rubric",
      "insights_vanilla_reference", "insights_vanilla_rubric_reference",
      "structure_vanilla", "structure_vanilla_rubric",
      "structure_vanilla_reference", "structure_vanilla_rubric_reference"]),
    ("surge", "listwise",
     ["structure_vanilla", "structure_vanilla_rubric",
      "structure_vanilla_reference", "structure_vanilla_rubric_reference",
      "content_vanilla", "content_vanilla_rubric",
      "content_vanilla_reference", "content_vanilla_rubric_reference"]),
]


def expected_lines(dataset: str) -> int:
    data_path = BASE_DIR / "data_standardized" / f"{dataset}.jsonl"
    if not data_path.exists():
        return 0
    data = load_jsonl(data_path)
    if not data:
        return 0

    for ds, paradigm, _ in DATASETS:
        if ds == dataset:
            if paradigm == "pointwise":
                return sum(len(r.get("responses", [])) for r in data)
            base = len(data)
            if dataset in ("wp_bench", "ma"):
                base *= 2
            return base
    return 0


def count_lines(path):
    if not path.exists():
        return 0
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_models_in_list(path):
    """Count actual models in te/cf files (pointwise has multiple models per line)."""
    if not path.exists() or path.stat().st_size == 0:
        return 0
    import json
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                models = rec.get("models", [])
                total += len(models)
            except json.JSONDecodeError:
                continue
    return total if total > 0 else count_lines(path)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Check incomplete tasks per model")
    parser.add_argument("--model", action="append", default=None, help="only check specified models")
    args = parser.parse_args()

    results_dir = BASE_DIR / "outputs" / "judge_results"
    if not results_dir.exists():
        print("Error: outputs/judge_results/ directory not found")
        sys.exit(1)

    models = sorted(d.name for d in results_dir.iterdir() if d.is_dir())
    if args.model:
        models = [m for m in models if m in args.model]

    total_incomplete = 0
    for model in models:
        print(f"\n{'='*60}")
        print(f"  Model: {model}")
        print(f"{'='*60}")

        model_incomplete = 0
        for ds, paradigm, prompts in DATASETS:
            expected = expected_lines(ds)
            if expected == 0:
                continue

            for pm in prompts:
                judge_file = results_dir / model / ds / f"{pm}.jsonl"
                te_path = results_dir / model / ds / f"{pm}_token_exceed.jsonl"
                cf_path = results_dir / model / ds / f"{pm}_content_filter.jsonl"
                err_path = results_dir / model / ds / f"{pm}_errors.jsonl"

                done = count_lines(judge_file)
                # pointwise: te/cf lines may contain multiple models, expand counts
                if paradigm == "pointwise":
                    te_cnt = count_models_in_list(te_path)
                    cf_cnt = count_models_in_list(cf_path)
                else:
                    te_cnt = count_lines(te_path)
                    cf_cnt = count_lines(cf_path)
                err_cnt = count_lines(err_path)
                total = done + te_cnt + cf_cnt

                # Metrics status
                metric_path = BASE_DIR / "outputs" / "reliability_scores" / model / ds / f"{pm}.json"
                metrics_done = metric_path.exists() and metric_path.stat().st_size > 10

                if total >= expected and metrics_done:
                    continue  # fully completed, skip

                model_incomplete += 1
                total_incomplete += 1

                if total >= expected and not metrics_done:
                    parts = [f"judge_done({done})"]
                    if te_cnt:
                        parts.append(f"te={te_cnt}")
                    if cf_cnt:
                        parts.append(f"cf={cf_cnt}")
                    status = f"[METRICS] {', '.join(parts)}, metrics pending"
                else:
                    parts = [f"{done}/{expected}"]
                    if te_cnt:
                        parts.append(f"te={te_cnt}")
                    if cf_cnt:
                        parts.append(f"cf={cf_cnt}")
                    if err_cnt:
                        parts.append(f"err={err_cnt}")
                    status = f"[JUDGE]  {' '.join(parts)}"

                print(f"  {ds:<22s} {pm:<35s} {status}")

        if model_incomplete == 0:
            print(f"  All complete ✓")
        else:
            print(f"  → {model_incomplete} tasks incomplete")

    print(f"\n{'='*60}")
    print(f"  Total: {total_incomplete} incomplete tasks")
    if total_incomplete == 0:
        print(f"  All models complete!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

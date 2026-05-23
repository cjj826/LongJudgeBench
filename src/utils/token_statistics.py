"""
Token statistics script (based on standardized data).
Reads from data_standardized/ and computes token distribution per dataset.
Metrics: count | Avg / Median / Max / Min Content Tokens
"""
import json
import sys
import statistics
from pathlib import Path
from collections import defaultdict

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

DATA_DIR = BASE_DIR / "data_standardized"

# ── Reuse count_tokens from src/utils/token_counter.py ─────────

from src.utils.token_counter import count_tokens



def load_jsonl(filepath):
    data = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


# Per-dataset analysis functions
def analyze_deepresearch(records):
    print("=" * 65)
    print("[DeepResearch-Bench]")
    print("=" * 65)
    all_inst, all_cont = [], []
    for r in records:
        inst_tok = count_tokens(r["instruction"])
        for resp in r["responses"]:
            all_inst.append(inst_tok)
            all_cont.append(count_tokens(resp["content"]))
    n = len(all_cont)
    return {
        "doc_count": n,
        "avg_instruction": round(sum(all_inst) / n, 1) if n else 0,
        "avg_content": round(sum(all_cont) / n, 1) if n else 0,
        "median_content": round(statistics.median(all_cont), 1) if all_cont else 0,
        "max_content": max(all_cont) if all_cont else 0,
        "min_content": min(all_cont) if all_cont else 0,
    }


def analyze_surge(records):
    print("=" * 65)
    print("[SurGE]")
    print("=" * 65)
    model_responses = defaultdict(list)
    all_inst, all_cont = [], []
    for r in records:
        inst_tok = count_tokens(r["instruction"])
        for resp in r["responses"]:
            model_responses[resp["model"]].append(count_tokens(resp["content"]))
            all_inst.append(inst_tok)
            all_cont.append(count_tokens(resp["content"]))

    by_model = {}
    for model, cont_list in model_responses.items():
        by_model[model] = {
            "doc_count": len(cont_list),
            "avg_instruction": round(sum(all_inst) / len(all_inst), 1) if all_inst else 0,
            "avg_content": round(sum(cont_list) / len(cont_list), 1),
            "median_content": round(statistics.median(cont_list), 1),
            "max_content": max(cont_list),
            "min_content": min(cont_list),
        }
        s = by_model[model]
        print(f"\n  [{model}]")
        print(f"    Documents:         {s['doc_count']}")
        print(f"    Avg. Instruction:  {s['avg_instruction']:>10,} tokens")
        print(f"    Avg. Content:      {s['avg_content']:>10,} tokens")
        print(f"    Max. Content:      {s['max_content']:>10,} tokens")
        print(f"    Min. Content:      {s['min_content']:>10,} tokens")
    return by_model


def analyze_wp_bench(records):
    print("=" * 65)
    print("[Writing-Preference-Bench]")
    print("=" * 65)
    by_lang = defaultdict(lambda: {"inst": [], "cont": []})
    for r in records:
        lang = r["meta"]["language"]
        inst_tok = count_tokens(r["instruction"])
        for resp in r["responses"]:
            by_lang[lang]["inst"].append(inst_tok)
            by_lang[lang]["cont"].append(count_tokens(resp["content"]))

    stats = {}
    for lang, d in by_lang.items():
        n = len(d["cont"])
        stats[f"WP_{lang.upper()}"] = {
            "doc_count": n,
            "avg_instruction": round(sum(d["inst"]) / n, 1) if n else 0,
            "avg_content": round(sum(d["cont"]) / n, 1) if n else 0,
            "median_content": round(statistics.median(d["cont"]), 1) if d["cont"] else 0,
            "max_content": max(d["cont"]) if d["cont"] else 0,
            "min_content": min(d["cont"]) if d["cont"] else 0,
        }
        s = stats[f"WP_{lang.upper()}"]
        print(f"\n  [WP_{lang.upper()}]")
        print(f"    Documents:         {s['doc_count']} (chosen+rejected)")
        print(f"    Avg. Instruction:  {s['avg_instruction']:>10,} tokens")
        print(f"    Avg. Content:      {s['avg_content']:>10,} tokens")
        print(f"    Max. Content:      {s['max_content']:>10,} tokens")
        print(f"    Min. Content:      {s['min_content']:>10,} tokens")
    return stats


def analyze_ma(records):
    """MA: each paper has 4 system outputs; same output may appear in multiple pairs, deduplicate."""
    print("=" * 65)
    print("[MA]")
    print("=" * 65)
    seen = {}
    inst_tok_map = {}
    for r in records:
        pid = r.get("meta", {}).get("paper_id", "")
        inst_tok = count_tokens(r.get("instruction", ""))
        for resp in r["responses"]:
            key = (pid, resp["model"])
            if key not in seen:
                seen[key] = count_tokens(resp["content"])
                inst_tok_map[key] = inst_tok
    vals = list(seen.values())
    inst_vals = list(inst_tok_map.values())
    n = len(vals)
    return {
        "doc_count": n,
        "avg_instruction": round(sum(inst_vals) / n, 1) if n else 0,
        "avg_content": round(sum(vals) / n, 1) if n else 0,
        "median_content": round(statistics.median(vals), 1) if vals else 0,
        "max_content": max(vals) if vals else 0,
        "min_content": min(vals) if vals else 0,
    }


def analyze_verify_bench_hard(records):
    """verify_bench_hard: single response per record."""
    print("=" * 65)
    print("[Verify-Bench-Hard]")
    print("=" * 65)
    inst_tok_list = [count_tokens(r["instruction"]) for r in records]
    cont_tok_list = [count_tokens(r["responses"][0]["content"]) if r["responses"] else 0 for r in records]
    n = len(records)
    return {
        "doc_count": n,
        "avg_instruction": round(sum(inst_tok_list) / n, 1) if n else 0,
        "avg_content": round(sum(cont_tok_list) / n, 1) if n else 0,
        "median_content": round(statistics.median(cont_tok_list), 1) if cont_tok_list else 0,
        "max_content": max(cont_tok_list) if cont_tok_list else 0,
        "min_content": min(cont_tok_list) if cont_tok_list else 0,
    }


def analyze_realdr(records):
    print("=" * 65)
    print("[RealDR]")
    print("=" * 65)
    inst_tok_list = [count_tokens(r["instruction"]) for r in records]
    cont_tok_list = [count_tokens(r["responses"][0]["content"]) if r["responses"] else 0 for r in records]
    n = len(records)
    return {
        "doc_count": n,
        "avg_instruction": round(sum(inst_tok_list) / n, 1) if n else 0,
        "avg_content": round(sum(cont_tok_list) / n, 1) if n else 0,
        "median_content": round(statistics.median(cont_tok_list), 1) if cont_tok_list else 0,
        "max_content": max(cont_tok_list) if cont_tok_list else 0,
        "min_content": min(cont_tok_list) if cont_tok_list else 0,
    }


# Additional features: Token filter & ratio statistics

def compute_sample_tokens(record: dict) -> int:
    """Total tokens for one sample (instruction + all response content)."""
    total = count_tokens(record.get("instruction", ""))
    for resp in record.get("responses", []):
        total += count_tokens(resp.get("content", ""))
    return total


def filter_short_samples_and_report(records, threshold=800):
    """
    Filter samples with token count < threshold.
    For paired data (wp_bench), if one side < threshold, both (entire record) are removed.
    Returns: (filtered_records, removed_count)
    """
    kept = []
    removed = 0
    for r in records:
        tokens = compute_sample_tokens(r)
        if tokens < threshold:
            removed += 1
        else:
            kept.append(r)

    # For paired datasets, if one response in a record is below threshold but another is >= threshold,
    # we keep it as-is (the entire record is removed).
    # For wp_bench (one record = two responses), the above logic already removes the entire record.
    return kept, removed


def report_token_ratio(records, threshold=1000):
    """
    Compute ratio of samples with token count >= threshold.
    """
    total = len(records)
    if total == 0:
        return 0.0, 0
    above = sum(1 for r in records if compute_sample_tokens(r) >= threshold)
    return round(above / total * 100, 1), above


def run_token_filter_analysis(datasets_data):
    """Run token filter & ratio statistics."""
    print("\n" + "=" * 65)
    print("[Token Filter & Ratio Stats]")
    print("=" * 65)

    for name, records in datasets_data.items():
        if not records:
            continue

        if name in ("ma",):
            # MA: same paper appears in multiple pairs, deduplicate by (paper_id, model)
            seen = {}
            for r in records:
                pid = r.get("meta", {}).get("paper_id", "")
                for resp in r["responses"]:
                    key = (pid, resp["model"])
                    if key not in seen:
                        t = count_tokens(r.get("instruction", "")) + count_tokens(resp["content"])
                        seen[key] = t
            all_tokens = list(seen.values())
            below_800 = sum(1 for t in all_tokens if t < 800)
            above_1000 = sum(1 for t in all_tokens if t >= 1000)
            ratio_above = round(above_1000 / len(all_tokens) * 100, 1) if all_tokens else 0
            print(f"\n  [{name}] (deduplicated)")
            print(f"    Total samples:     {len(all_tokens)}")
            print(f"    Token < 800:        {below_800} ({round(below_800/len(all_tokens)*100,1)}%)")
            print(f"    Token >= 1000:      {above_1000} ({ratio_above}%)")
        else:
            if name == "surge":
                # SurGE: each record has 4 responses, count separately
                below_800_total = 0
                above_1000_total = 0
                grand_total = 0
                for r in records:
                    for resp in r["responses"]:
                        t = count_tokens(r["instruction"]) + count_tokens(resp["content"])
                        grand_total += 1
                        if t < 800:
                            below_800_total += 1
                        if t >= 1000:
                            above_1000_total += 1
                ratio_above = round(above_1000_total / grand_total * 100, 1) if grand_total else 0
                print(f"\n  [{name}] (per-sample granularity)")
                print(f"    Total samples:     {grand_total}")
                print(f"    Token < 800:        {below_800_total} ({round(below_800_total/grand_total*100,1)}%)")
                print(f"    Token >= 1000:      {above_1000_total} ({ratio_above}%)")
            else:
                # deepresearch_bench / realdr: each response is an independent sample
                all_cont = []
                for r in records:
                    inst = count_tokens(r["instruction"])
                    for resp in r["responses"]:
                        all_cont.append(inst + count_tokens(resp["content"]))
                below_800 = sum(1 for t in all_cont if t < 800)
                above_1000 = sum(1 for t in all_cont if t >= 1000)
                ratio_above = round(above_1000 / len(all_cont) * 100, 1) if all_cont else 0
                print(f"\n  [{name}] (per-sample granularity)")
                print(f"    Total samples:     {len(all_cont)}")
                print(f"    Token < 800:        {below_800} ({round(below_800/len(all_cont)*100,1)}%)")
                print(f"    Token >= 1000:      {above_1000} ({ratio_above}%)")


# Main

def print_stats(name, stats):
    avg_inst = stats.get('avg_instruction', 0)
    print(f"  {name:<35} {stats['doc_count']:<8} {avg_inst:<12,} "
          f"{stats['avg_content']:<12,} {stats['median_content']:<12,} "
          f"{stats['max_content']:<12,} {stats['min_content']:<12,}")


def main():
    # ── Load standardized data ──
    datasets_files = {
        "deepresearch_bench": DATA_DIR / "deepresearch_bench.jsonl",
        "surge": DATA_DIR / "surge.jsonl",
        "wp_bench": DATA_DIR / "wp_bench.jsonl",
        "realdr": DATA_DIR / "realdr.jsonl",
        "ma": DATA_DIR / "ma.jsonl",
        "verify_bench_hard": DATA_DIR / "verify_bench_hard.jsonl",
    }

    all_data = {}
    for name, fpath in datasets_files.items():
        if fpath.exists():
            all_data[name] = load_jsonl(fpath)
            print(f"[Loaded] {name}: {len(all_data[name])} records")
        else:
            print(f"[Skip] {name}: file not found")
    print()

    # ── Per-dataset statistics ──
    dr_stats = analyze_deepresearch(all_data.get("deepresearch_bench", []))
    surge_stats = analyze_surge(all_data.get("surge", []))
    wp_stats = analyze_wp_bench(all_data.get("wp_bench", []))
    bd_stats = analyze_realdr(all_data.get("realdr", []))
    ma_stats = analyze_ma(all_data.get("ma", []))
    vbh_stats = analyze_verify_bench_hard(all_data.get("verify_bench_hard", []))
    # ── Summary comparison ──
    print("\n" + "=" * 65)
    print("[Summary Comparison]")
    print("=" * 65)
    print(f"  {'Dataset':<35} {'Count':<8} {'Avg.Inst':<12} {'Avg.Cont':<12} {'Med.Cont':<12} {'Max.Cont':<12} {'Min.Cont':<12}")
    print(f"  {'-' * 103}")

    print_stats("DeepResearch-Bench (total)", dr_stats)

    for model, s in surge_stats.items():
        print_stats(f"  SurGE/{model}", s)

    for lang, s in wp_stats.items():
        print_stats(f"  WP-Bench/{lang}", s)

    print_stats("RealDR (total)", bd_stats)
    print_stats("MA (total)", ma_stats)
    print_stats("Verify-Bench-Hard (total)", vbh_stats)
    # ── Token filter & ratio stats ──
    run_token_filter_analysis(all_data)

    print()
    print("Done!")


if __name__ == "__main__":
    main()

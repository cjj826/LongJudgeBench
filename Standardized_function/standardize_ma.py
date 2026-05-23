"""
Standardize MA (Meta-Analysis Paper Generation Benchmark)
Paradigm: Pairwise (LLM compares two system outputs → preference)
GT: Human pairwise preference (A2/A1/tie/B1/B2), 8 annotators aggregated
Dimensions: insights (3 comparisons × 30 papers) + structure (1 comparison × 30 papers)
Input:
  - data/MA/metasyn_evaluation_complete.json
  - data/MA/human_annotation_subset/baseline_results/*/paper_{id}/report.md
Output:
  - data_standardized/ma.jsonl
  - ground_truth/ma_gt.jsonl
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from Standardized_function.utils import (
    BASE_DIR, ensure_output_dirs, save_jsonl, clear_jsonl, count_tokens
)

# ── Paths ──
MAP_DIR = BASE_DIR / "data" / "MA"
ANNOTATION_FILE = MAP_DIR / "metasyn_evaluation_complete.json"
BASELINE_DIR = MAP_DIR / "human_annotation_subset" / "baseline_results"

OUT_DATA = BASE_DIR / "data_standardized" / "ma.jsonl"
OUT_GT = BASE_DIR / "ground_truth" / "ma_gt.jsonl"
OUT_REF = BASE_DIR / "data_standardized" / "ma_reference.jsonl"

GT_PAPERS_FILE = MAP_DIR / "human_annotation_subset" / "gt" / "papers_annotated_30.json"

# Keep only LLM-as-Judge dimensions
DIMENSIONS = ["insights", "structure"]

# System name → directory mapping
SYSTEM_DIR_MAP = {
    "gpt5_bm25": "gpt_researcher_gpt5_bm25",
    "gpt5_dense": "gpt_researcher_gpt5_dense_trained",
    "glm5_bm25": "gpt_researcher_glm_5_bm25",
    "dsr1_bm25": "gpt_researcher_deepseek_r1_bm25",
    "auto_bm25": "autometa_gpt5_bm25",
    "auto_dense": "autometa_gpt5_dense_trained",
}

SYSTEM_LABELS = {
    "gpt5_bm25": "GPT-Researcher (GPT-5) / BM25",
    "gpt5_dense": "GPT-Researcher (GPT-5) / Dense-FT",
    "glm5_bm25": "GPT-Researcher (GLM-5) / BM25",
    "dsr1_bm25": "GPT-Researcher (DeepSeek-R1) / BM25",
    "auto_bm25": "AutoMeta (GPT-5) / BM25",
    "auto_dense": "AutoMeta (GPT-5) / Dense-FT",
}

# Rating string → integer mapping
RATING_MAP_INT = {"A2": 0, "A1": 1, "tie": 2, "B1": 3, "B2": 4}


def load_system_output(paper_id: str, system_name: str) -> str:
    """Read system output report.md from baseline_results."""
    dir_name = SYSTEM_DIR_MAP.get(system_name)
    if not dir_name:
        return ""
    report_path = BASELINE_DIR / dir_name / f"paper_{paper_id}" / "report.md"
    if report_path.exists():
        try:
            return report_path.read_text(encoding="utf-8")
        except Exception:
            return ""
    return ""


def load_annotation_data():
    with open(ANNOTATION_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_gt_papers() -> dict:
    """Load GT paper data, return {paper_id: paper}."""
    with open(GT_PAPERS_FILE, "r", encoding="utf-8") as f:
        papers = json.load(f)
    return {str(p["ID"]): p for p in papers}


def filter_tasks_by_dimension(tasks: list) -> list:
    """Keep only insights and structure dimensions."""
    return [t for t in tasks if t.get("dimension_id") in DIMENSIONS]


def get_instruction(paper: dict) -> str:
    """Build instruction from paper title + abstract."""
    title = paper.get("Title", "")
    abstract = paper.get("Abstract", "")
    return f"Write a systematic review and meta-analysis section for the following paper.\n\nTitle: {title}\n\nAbstract: {abstract}"


def aggregate_pairwise_annotations(tasks: list) -> dict:
    """
    Aggregate 8 annotators' ratings per pair×dim.
    Returns: {(pair_id, dim): {"mean_rating": float, "preferred": "A/B/tie", ...}}
    Only processes insights and structure dimensions.
    """
    results = {}
    for task in tasks:
        dim_id = task.get("dimension_id")
        if dim_id not in DIMENSIONS:
            continue
        pair_id = task["pair_id"]
        key = (pair_id, dim_id)

        annotations = task.get("human_annotations", {})
        ratings = []
        for ann in annotations.values():
            rating_str = ann.get("rating", "")
            if rating_str in RATING_MAP_INT:
                ratings.append(RATING_MAP_INT[rating_str])

        if not ratings:
            continue

        mean_rating = sum(ratings) / len(ratings)
        if mean_rating < 2.0:
            preferred = "A"
        elif mean_rating > 2.0:
            preferred = "B"
        else:
            preferred = "tie"

        results[key] = {
            "mean_rating": round(mean_rating, 4),
            "preferred": preferred,
            "n": len(ratings),
            "system_a": task["system_a"],
            "system_b": task["system_b"],
            "ratings": ratings,
        }
    return results


def construct_structure_outline(paper: dict) -> str:
    """Build per-paper structure outline from metadata for Structure Reference."""
    lines = []
    lines.append("## Expected Structure Outline")
    lines.append("")

    rq = paper.get("Research_Question", "")
    if rq:
        lines.append(f"**Research Question**: {rq}")
        lines.append("")

    topic = paper.get("Topic", "")
    abstract = paper.get("Abstract", "")
    lines.append("**Background/Introduction**:")
    if topic:
        lines.append(f"This report should introduce the clinical context of {topic}.")
    if abstract:
        lines.append(f"Context: {abstract[:300]}...")
    lines.append("")

    lines.append("**Methods — The report should specify:**")
    for field, label in [("Population", "Population"), ("Intervention", "Intervention"),
                          ("Comparison", "Comparison"), ("Outcome", "Outcome")]:
        val = paper.get(field, "")
        if val:
            lines.append(f"- {label}: {val}")

    strategies = paper.get("search_strategies", [])
    if strategies:
        db_names = [s.get("db", "") for s in strategies if isinstance(s, dict) and s.get("db")]
        if db_names:
            lines.append(f"- Search databases: {', '.join(db_names)}")

    inc = paper.get("inclusion_criteria", "")
    if inc:
        lines.append(f"- Inclusion criteria: {inc[:200]}")
    exc = paper.get("exclusion_criteria", "")
    if exc:
        lines.append(f"- Exclusion criteria: {exc[:200]}")
    lines.append("")

    lines.append("**Results**:")
    ed = paper.get("Effect_Direction", "")
    est = paper.get("Effect_Size_Type", "")
    esv = paper.get("Effect_Size_Value", "")
    if ed or est:
        parts = []
        if ed:
            parts.append(f"direction: {ed}")
        if est:
            parts.append(f"effect size ({est} = {esv})" if esv else f"effect size: {est}")
        lines.append(f"Report the {'; '.join(parts)}.")
    het = paper.get("Heterogeneity_Level", "")
    if het:
        lines.append(f"Heterogeneity: {het}.")
    lines.append("")

    lines.append("**Discussion**: Interpret the evidence, discuss limitations, heterogeneity, and clinical implications.")
    lines.append("")

    cs = paper.get("Conclusion_Summary", "")
    if cs:
        lines.append(f"**Conclusion**: {cs}")

    return "\n".join(lines)


def main():
    ensure_output_dirs()
    clear_jsonl(OUT_DATA)
    clear_jsonl(OUT_GT)
    clear_jsonl(OUT_REF)

    print("=" * 60)
    print("MA Standardization (Pairwise, insights + structure only)")
    print("=" * 60)

    # Load data
    print("\n[1/4] Loading annotation data...")
    data = load_annotation_data()
    per_task_data = data["per_task_data"]
    print(f"  Total tasks: {len(per_task_data)}")

    print("\n[2/4] Loading GT papers...")
    gt_papers = load_gt_papers()
    print(f"  GT papers: {len(gt_papers)}")

    # Group by paper_id
    paper_tasks = {}
    for task in per_task_data.values():
        pid = task["paper_id"]
        dim_id = task.get("dimension_id")
        if dim_id not in DIMENSIONS:
            continue
        if pid not in paper_tasks:
            paper_tasks[pid] = []
        paper_tasks[pid].append(task)

    paper_ids = sorted(paper_tasks.keys())
    print(f"  Papers with insights/structure annotations: {len(paper_ids)}")
    print(f"  Paper IDs: {paper_ids}")

    # Build reference map
    ref_map = {}
    for pid_str, p in gt_papers.items():
        ref_map[pid_str] = p.get("conclusion_paragraph", "")

    THRESHOLD = 800
    data_count = 0
    gt_count = 0
    ref_count = 0

    for pid in paper_ids:
        tasks = paper_tasks[pid]
        paper = gt_papers.get(pid, {})
        paper_title = paper.get("Title", tasks[0].get("paper_title", ""))

        instruction = get_instruction(paper)

        # Collect system outputs (lazy load, only those appearing in pairs)
        needed_systems = set()
        for task in tasks:
            needed_systems.add(task["system_a"])
            needed_systems.add(task["system_b"])

        system_content = {}
        all_ok = True
        for sys_name in needed_systems:
            content = load_system_output(pid, sys_name)
            tok_count = count_tokens(content) if content else 0
            if tok_count < THRESHOLD:
                print(f"  [Filter] {pid}/{sys_name}: {tok_count} tokens < {THRESHOLD}")
                all_ok = False
                break
            if content:
                system_content[sys_name] = content

        if not all_ok or not system_content:
            continue

        # Aggregate pairwise annotations
        agg = aggregate_pairwise_annotations(tasks)
        if not agg:
            continue

        # Generate one record per pair×dim combination
        pairwise_records = {}  # {(pair_id, dim): {...}}
        for (pair_id, dim_id), ar in agg.items():
            key = (pair_id, dim_id)
            sa, sb = ar["system_a"], ar["system_b"]
            content_a = system_content.get(sa, "")
            content_b = system_content.get(sb, "")
            if not content_a or not content_b:
                continue

            pair_label = dim_id  # insights / structure
            record_id = f"paper_{pid}_{pair_id}_{dim_id}"

            record = {
                "dataset": "ma",
                "id": record_id,
                "instruction": instruction,
                "responses": [
                    {"model": sa, "content": content_a},
                    {"model": sb, "content": content_b},
                ],
                "ground_truth": {
                    "type": "pairwise_preference",
                    "pair_id": pair_id,
                    "dimension": dim_id,
                    "preferred": ar["preferred"],
                    "mean_rating": ar["mean_rating"],
                    "n_annotators": ar["n"],
                    "system_a": sa,
                    "system_b": sb,
                },
                "meta": {
                    "language": "en",
                    "task_type": "pairwise",
                    "source": "MAP",
                    "paper_title": paper_title,
                    "paper_id": pid,
                    "pair_id": pair_id,
                    "dimension": dim_id,
                },
            }
            save_jsonl(record, OUT_DATA)
            data_count += 1

            # GT record
            gt_record = {
                "dataset": "ma",
                "id": record_id,
                "paper_id": pid,
                "paper_title": paper_title,
                "pair_id": pair_id,
                "dimension": dim_id,
                "annotation_type": "pairwise_preference",
                "preferred": ar["preferred"],
                "mean_rating": ar["mean_rating"],
                "n_annotators": ar["n"],
                "system_a": sa,
                "system_b": sb,
            }
            save_jsonl(gt_record, OUT_GT)
            gt_count += 1

        # Reference output (one per paper)
        # Insights: conclusion_paragraph
        if pid in ref_map:
            ref_record = {
                "id": f"paper_{pid}",
                "reference": ref_map[pid],
            }
            save_jsonl(ref_record, OUT_REF)
            ref_count += 1

        # Structure: per-paper structural outline
        structure_outline = construct_structure_outline(paper)
        ref_struct = {
            "id": f"paper_{pid}_structure",
            "reference": structure_outline,
        }
        save_jsonl(ref_struct, OUT_REF)
        ref_count += 1

    print(f"\n  Standardized data: {data_count} records (pair)")
    print(f"  Ground truth:      {gt_count} records")
    print(f"  Reference:         {ref_count} records")
    print(f"  Output:")
    print(f"    Standardized data: {OUT_DATA}")
    print(f"    Ground truth:      {OUT_GT}")
    print(f"    Reference:         {OUT_REF}")
    print("  Done!")


if __name__ == "__main__":
    main()

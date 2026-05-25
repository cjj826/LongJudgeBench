"""
Orchestrator: Run all case study analyses and generate summary report.

Usage:
  python src/case_study/run_all_analyses.py
"""
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.case_study.analysis_01_rubric_analysis import main as run_analysis_1
from src.case_study.analysis_02_position_bias import main as run_analysis_2
from src.case_study.analysis_03_score_distribution import main as run_analysis_3
from src.case_study.analysis_04_all_wrong_cases import main as run_analysis_4
from src.case_study.analysis_05_dimension_level import main as run_analysis_5


def print_header(text: str):
    print(f"\n\n{'#'*80}")
    print(f"# {text}")
    print(f"{'#'*80}")


def main():
    start = time.time()

    print_header("RUNNING ALL CASE STUDY ANALYSES")
    print(f"Output directory: {BASE_DIR / 'src' / 'case_study'}")

    # Analysis 1: Rubric Mode Analysis Text
    t1 = time.time()
    print_header("ANALYSIS 1: Rubric Text Analysis (deepresearch_bench)")
    run_analysis_1()
    print(f"\n  ✓ Completed in {time.time() - t1:.1f}s")

    # Analysis 2: Position Bias
    t2 = time.time()
    print_header("ANALYSIS 2: Position Bias (wp_bench, ma)")
    run_analysis_2()
    print(f"\n  ✓ Completed in {time.time() - t2:.1f}s")

    # Analysis 3: Score Distribution
    t3 = time.time()
    print_header("ANALYSIS 3: Score Distribution (deepresearch_bench)")
    run_analysis_3()
    print(f"\n  ✓ Completed in {time.time() - t3:.1f}s")

    # Analysis 4: All Models Wrong
    t4 = time.time()
    print_header("ANALYSIS 4: All Models Wrong (verify_bench_hard)")
    run_analysis_4()
    print(f"\n  ✓ Completed in {time.time() - t4:.1f}s")

    # Analysis 5: Dimension-Level
    t5 = time.time()
    print_header("ANALYSIS 5: Dimension-Level Comparison (deepresearch_bench rubric)")
    run_analysis_5()
    print(f"\n  ✓ Completed in {time.time() - t5:.1f}s")

    # Summary
    total = time.time() - start
    print_header("ALL ANALYSES COMPLETE")
    print(f"Total time: {total:.1f}s")
    print(f"\nKey findings summary:")
    print(f"  - Rubric mode analysis text extracted for qualitative case study")
    print(f"  - Position bias quantified for all 8 models on pairwise datasets")
    print(f"  - Score distribution compared between judge and GT")
    print(f"  - 'All models wrong' cases identified and characterized")
    print(f"  - Dimension-level accuracy compared across models")
    print(f"\nAnalysis complete. Review outputs above.")


if __name__ == "__main__":
    main()

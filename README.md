<div align="right">
  <a href="README.zh.md">中文</a> | <b>English</b>
</div>

<br>

<div align="center">
  <h1>LongJudgeBench</h1>
  <p>
    <b>A Benchmark for Evaluating LLM-as-a-Judge on Long-Form Outputs</b>
  </p>
  <p>
    <img src="https://img.shields.io/badge/python-3.10+-blue" alt="Python 3.10+">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
    <img src="https://img.shields.io/badge/datasets-6-orange" alt="6 Datasets">
    <img src="https://img.shields.io/badge/paradigms-pointwise_|_pairwise_|_listwise-purple" alt="3 Paradigms">
  </p>
</div>

---

**LongJudgeBench** is a comprehensive meta-evaluation benchmark for assessing LLM-as-a-Judge reliability on **long-form outputs** (1K–68K chars). Unlike existing benchmarks focused on short responses, LongJudgeBench targets real-world scenarios — deep research reports, scientific surveys, and long-chain reasoning — where judges must assess global structure, long-range coherence, and sustained readability.

<p align="center">
  <img src="images/LongJudgeBench.png" alt="LongJudgeBench Overview" width="85%">
  <br>
  <em>Figure 1: LongJudgeBench overview — task formalization, construction pipeline, and evaluation framework.</em>
</p>

## Table of Contents

- [Key Features](#key-features)
- [Benchmark Statistics](#benchmark-statistics)
- [Key Findings](#key-findings)
- [Quick Start](#quick-start)
- [Evaluation Paradigms](#evaluation-paradigms)
- [Prompt Modes](#prompt-modes)
- [Data Format](#data-format)
- [Project Structure](#project-structure)
- [Output Format](#output-format)
- [Citation](#citation)

## Key Features

- **6 diverse datasets** covering pointwise, pairwise, and listwise judging protocols
- **Bilingual** support (Chinese and English tasks)
- **4 prompt variants** per dataset: vanilla, rubric, reference, rubric+reference
- **8 judge models** evaluated: GPT-5.2, GPT-4o-mini, DeepSeek-V4-Flash, Qwen3-Max, Qwen3-32B, Qwen3-32B (no-thinking), Kimi-K2.6, GLM-5.1
- **3 agreement metrics**: pairwise ACC, Spearman, Kendall's τ
- **Length sensitivity analysis**: bucketed accuracy by output length (fixed + adaptive quartile bins)
- **Case study analysis**: systematic identification of judge failure patterns with root cause analysis
- **Checkpoint resume**: safe to re-run, automatically skips completed items

## Benchmark Statistics

| Dataset            | Paradigm  | Language | Documents               | Avg Tokens | Task                                                  |
| ------------------ | --------- | -------- | ----------------------- | ---------- | ----------------------------------------------------- |
| deepresearch_bench | pointwise | zh       | 200                     | 18,013     | Deep research report scoring (4 weighted dimensions)  |
| realdr             | pointwise | en/zh    | 640                     | 10,131     | Document quality scoring (3 weighted dimensions)      |
| verify_bench_hard  | pointwise | en       | 316                     | 3,053      | Binary verification (Yes/No)                          |
| wp_bench           | pairwise  | en/zh    | 526 (263 pairs × 2)    | 3,509      | Writing preference comparison                         |
| ma                 | pairwise  | en       | 120                     | 4,764      | Medical meta-analysis comparison (insights dimension) |
| surge              | listwise  | en       | 164 (41 topics × 4)    | 28,758     | CS survey generation ranking                          |

### Length Sensitivity Analysis

<p align="center">
  <img src="images/length_sensitivity.png" alt="Length Sensitivity Analysis" width="85%">
  <br>
  <em>Figure 2: Judge accuracy across output length buckets — longer outputs are generally harder to evaluate reliably, with the longest quartile showing significantly lower agreement.</em>
</p>

## Key Findings

Our experiments across 8 LLM judges on 6 datasets reveal:

- **Reliability varies sharply by model and dataset**: Pairwise accuracy ranges from ~55% (near random) to ~85% across models and datasets. No single judge is universally reliable.
- **Length is a systematic difficulty factor**: Judge accuracy drops consistently in the longest output quartile across most datasets. The effect is most pronounced on realdr and verify_bench_hard, where the longest quartile accuracy falls below 60%.
- **Rubrics and references help — but not always**: Reference mode improves accuracy on verify_bench_hard (70.9% → 82.3%) but can hurt on wp_bench (75.3% → 65.2%). The effectiveness depends on task characteristics.
- **Three failure patterns** explain most judge-human disagreements:
  - *(a) Coarse Semantic Granularity*: Judges match keywords rather than verify conceptual identity. In long texts, abundant peripheral content drowns out core concept mismatches (e.g., confusing "Streamable HTTP" with "Messages API streaming").
  - *(b) Specialized Evaluation Needs Misalignment*: Judges evaluate surface-level topic coverage while humans evaluate precise task completion. Long responses can be "on topic" without being "on task."
  - *(c–e) Additional patterns*: Rubric rigidity (checklist thinking), position bias in pairwise evaluation (up to 95% for some models), and score compression (model-specific, not universal).
- **Score compression is model-specific**: Only GPT-4o-mini shows severe compression (σ=0.55 vs GT σ=1.22). Reference mode broadens its range to σ=1.00.
- **Task-specific blind spots**: On verify_bench_hard, 14.9% of cases have all 8 judges disagree with ground truth. Semantic understanding tasks (D2-Semantic) show a 66.7% collective error rate.

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API

Edit `config/api_config.json` with your API endpoints and keys.

### 3. Run a single evaluation

```bash
bash scripts/run_judge.sh <dataset> <paradigm> <model> [--prompt MODE] [--workers N]
```

Example:

```bash
# Pointwise evaluation
bash scripts/run_judge.sh deepresearch_bench pointwise gpt-4o-mini --prompt vanilla

# Pairwise with dimension prefix (surge/ma require dimension prefix)
bash scripts/run_judge.sh surge listwise gpt-4o-mini --prompt structure_vanilla
```

### 4. Batch evaluation

```bash
# Run all datasets
bash scripts/run_all.sh

# Run specific model
bash scripts/run_all.sh --model gpt-4o-mini --prompt vanilla
```

### 5. Parallel evaluation

```bash
bash scripts/run_parallel.sh --model qwen3-32b --model deepseek-v4-flash --workers 4
```

### 6. Compute reliability metrics

```bash
python src/evaluation/compute_reliability.py <dataset> <paradigm> <model> --prompt <mode>
```

### 7. Export results to xlsx

```bash
# Export all results to a single xlsx summary
python src/evaluation/export_results_xlsx.py

# Export with specific models only
python src/evaluation/export_results_xlsx.py --models gpt-4o-mini qwen3-32b
```

Results are saved to `outputs/reliability_summary.xlsx` (or a custom path).

> **Note:** All commands support checkpoint resume — repeat a command and it automatically skips completed items.

## Evaluation Paradigms

| Paradigm            | Description                              | Metrics                              |
| ------------------- | ---------------------------------------- | ------------------------------------ |
| **pointwise** | Score each response independently        | pairwise ACC, Spearman, Kendall's τ |
| **pairwise**  | Compare two responses, select preference | ACC (preference agreement)           |
| **listwise**  | Rank multiple responses                  | Spearman, Kendall's τ, pairwise ACC |

All paradigms support per-query aggregated metrics to prevent long-tail data from dominating.

## Prompt Modes

Each dataset supports 4 prompt variants:

| Mode                 | Description                            |
| -------------------- | -------------------------------------- |
| `vanilla`          | Basic scoring instruction              |
| `rubric`           | Dimensional scoring with criteria list |
| `reference`        | Reference article provided for scoring |
| `rubric_reference` | Rubric + reference combined            |

For surge (listwise) and ma (pairwise), modes are prefixed by the evaluation dimension:

| Dataset | Available Prompt Modes                                                                                                                                                                                                                             |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| surge   | `content_vanilla`, `structure_vanilla`, `content_vanilla_reference`, `structure_vanilla_reference`, `content_vanilla_rubric`, `structure_vanilla_rubric`, `content_vanilla_rubric_reference`, `structure_vanilla_rubric_reference` |
| ma      | `insights_vanilla`, `insights_vanilla_reference`, `insights_vanilla_rubric`, `insights_vanilla_rubric_reference`                                                                                                                           |

## Data Format

Standardized data uses a unified JSONL schema (`data_standardized/{dataset}.jsonl`):

```json
{
  "dataset": "dataset_name",
  "id": "unique_id",
  "instruction": "task prompt",
  "responses": [{"model": "name", "content": "full text"}],
  "ground_truth": { /* format-specific */ },
  "meta": {"language": "zh/en", "task_type": "pointwise/pairwise/listwise", "source": "origin"}
}
```

### Ground Truth Formats

| Paradigm  | ground_truth format                                               | Metrics                              |
| --------- | ----------------------------------------------------------------- | ------------------------------------ |
| pointwise | `{"type": "pointwise_...", "scores": {model: score}}`           | pairwise ACC, Spearman, Kendall's τ |
| pairwise  | `{"type": "pairwise_preference", "preferred": "A/B/tie"}`       | ACC (preference agreement)           |
| listwise  | `{"type": "listwise_ranking", "dimension_name": {model: rank}}` | Spearman, Kendall's τ, pairwise ACC |

Reference files (`{dataset}_reference.jsonl`) contain ground-truth reference texts used by the reference prompt mode.

## Project Structure

```
├── config/                    # Evaluation config & prompt templates
│   ├── judge_config.yaml       # Judge parameters (temperature, max_tokens)
│   ├── prompts/{dataset}/      # Prompt templates (vanilla/rubric/reference variants)
│   └── dataset_registry.json   # Dataset metadata
├── data/                       # Raw datasets (original formats)
├── data_standardized/          # Standardized JSONL data
├── ground_truth/               # Ground truth labels
├── src/
│   ├── evaluation/             # Evaluation pipeline & dataset adapters
│   │   ├── run_judge.py        # Judge entry point
│   │   ├── compute_reliability.py  # Reliability metric computation
│   │   └── datasets/           # Dataset adapters
│   ├── judge/                  # Judge implementations
│   │   ├── base_judge.py       # Base class (JSON parsing, error handling)
│   │   ├── pointwise_judge.py
│   │   ├── pairwise_judge.py
│   │   ├── listwise_judge.py
│   │   └── api_clients/        # API client (OpenAI-compatible)
│   ├── reliability/            # Agreement metrics
│   │   └── agreement_metrics.py    # ACC / Spearman / Kendall's τ
│   ├── standardization/        # Data standardization scripts
│   ├── length_analysis/        # Length sensitivity analysis
│   ├── case_study/             # Failure pattern case study
│   └── utils/                  # IO, token counting
├── scripts/                    # Shell launchers
├── outputs/                    # Evaluation outputs (generated at runtime)
│   ├── judge_results/          # Raw judge outputs (JSONL)
│   ├── reliability_scores/     # Reliability scores (JSON)
│   └── length_sensitivity/     # Length analysis results (JSON)
├── images/                     # Figures and diagrams
├── requirements.txt
└── LICENSE
```

## Output Format

### Judge Output (`outputs/judge_results/{model}/{dataset}/{mode}.jsonl`)

Each line is one judge scoring result:

```json
{
  "data_id": "record_id",
  "model": "model_name",
  "judge_result": { "overall_score": 8.5, ... },
  "response": "Raw judge response text"
}
```

Error records are written to `{mode}_errors.jsonl` and `{mode}_token_exceed.jsonl` in the same directory.

## Citation

```bibtex
@article{longjudgebench,
  title={LongJudgeBench: A Benchmark for Evaluating LLM-as-a-Judge on Long-Form Outputs},
  author={},
  journal={},
  year={2026}
}
```

## License

This project is licensed under the [MIT License](LICENSE).

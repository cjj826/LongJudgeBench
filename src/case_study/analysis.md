# Case Study Analysis: LLM-as-Judge Failure Patterns

## Overview

This analysis examines **why LLM judges make mistakes** when evaluating long-form content, using rubric-mode outputs where judges provide per-criterion reasoning. We analyze 8 judge models across 6 datasets, focusing on the deepresearch_bench dataset where rubric mode produces rich analysis text.

**Key finding**: Two fundamental failure patterns explain most judge-human disagreements:

1. **(a) Coarse Semantic Granularity**: Judges operate at a keyword-matching level, confusing professional concepts that share surface-level terminology but differ substantively — amplified by long texts.

2. **(b) Specialized Evaluation Needs Misalignment**: Long-text generation tasks often have narrow, context-specific evaluation criteria that judges fail to recognize. Judges evaluate surface-level topical alignment while humans judge precise task completion.

---

## Pattern (a): Coarse Semantic Granularity — Judge Confuses Professional Concept Boundaries in Long Texts

### Mechanism

LLM judges exhibit a fundamental flaw in long-text evaluation: **coarse semantic granularity leads to blurred professional concept boundaries**. Judges operate at a keyword-matching level — when a response contains terms that superficially resemble the instruction's key concepts, the judge treats them as equivalent, failing to recognize substantive differences that domain experts would easily spot. This flaw is amplified in long texts, where abundant peripheral content about related concepts "drowns out" the core conceptual mismatch.

### Case Study A1: Streamable HTTP (id=20)

| Item | Value |
|------|-------|
| **Instruction** | "研究Anthropic最新发布的Streamable HTTP的具体实现方案" (Research the specific implementation of Anthropic's newly released Streamable HTTP) |
| **Response** | gemini-2.5-pro-deepresearch, 21,439 chars |
| **Judge (qwen3-max)** | 8.85 overall |
| **GT (human)** | 5.37 overall (instruction_following: 3.67, comprehensiveness: 5.33) |

**Judge's rubric analysis (excerpts)**:

> Comprehensiveness [1] score=9.5: "对核心技术机制和工作流程的解析极为出色...详细描述了从message_start到message_stop的完整事件序列"

> Instruction_following [0] score=10.0: "文章严格围绕Anthropic Messages API的流式实现（即其'Streamable HTTP'）展开"

> Insight [0] score=9.5: "对核心机制的阐释极具深度...展现了超越表面文档的深刻理解"

**What went wrong**: The judge confuses "Messages API SSE streaming" (an existing feature enabled by `stream: true`) with "Streamable HTTP" (a distinct MCP protocol specification). These are related but technically distinct — they share keywords like "Anthropic," "streaming," "SSE," and "events," but differ in their protocol design, use case, and technical details. The judge's keyword-matching semantic cannot distinguish them. The 21K-char response, which thoroughly covers Messages API streaming, provides enough keyword overlap to trigger a false positive on every rubric criterion. Human annotators with domain expertise instantly recognize the mismatch, giving instruction_following only 3.67.

**Failure mechanism**: Concept confusion caused by coarse semantic granularity. The judge matches surface-level keywords instead of verifying conceptual identity. Long texts amplify this flaw by providing abundant peripheral content that reinforces the keyword overlap.

---

## Pattern (b): Specialized Evaluation Needs Misalignment

### Mechanism

Long-text generation tasks often involve **narrow, context-specific evaluation needs** that general-purpose rubric criteria fail to capture. The fundamental misalignment: **judges evaluate surface-level topic coverage, while humans evaluate precise task completion**. A response can be "on topic" without actually answering the specific question asked — and in long-form evaluation, judges consistently fail to distinguish these two.

### Case Study B1: Gaussian Electric Fields (id=9)

The instruction_following dimension shows the largest gap across all analyzed cases:

| Dimension | Judge Avg | GT Avg | Gap |
|-----------|-----------|--------|-----|
| instruction_following | 9.83 | 4.83 | **+5.00** |
| comprehensiveness | 9.08 | 6.67 | +2.41 |
| readability | 9.33 | 6.00 | +3.33 |
| insight | 8.83 | 5.93 | +2.90 |

The judge's rubric criteria check: "Does the response stay within the topic domain?" "Does it mention the challenge?" "Does it cover multiple methods?" — surface-level topical coverage that the 17K-char response easily satisfies. But human evaluators apply a stricter standard: the response should directly answer the specific question about orientation uncertainty, not provide a general lecture on computational electrochemistry.

**Root cause**: In long-text evaluation, "instruction following" is interpreted by judges as topical relevance, but by humans as task completion. This gap widens with response length — longer responses can be more "on topic" while being less "on task."

### Case Study B2: Pipa Music Evolution Under-Scoring (id=37)

| Item | Value |
|------|-------|
| **Instruction** | 研究爵士钢琴在现代/当代音乐中的创新与风格演变 (Research jazz piano innovation and style evolution in modern/contemporary music) |
| **Response** | perplexity-Research, 8,925 chars |
| **Judge (qwen3-max)** | 4.93 overall |
| **GT (human)** | 8.87 overall (insight: 8.83, comprehensiveness: 8.83) |

**Judge's rubric analysis**:

> Comprehensiveness [0] score=4.5: "对1950年前的关键风格缺乏系统梳理，未能为现代演变提供清晰的历史参照系"

> Insight [0] score=3.0: "分析流于表象，缺乏对关键转折点的机制性解释"

> Instruction_following [2] score=5.0: "未系统对比经典与现代在钢琴技法上的具体差异，回应不够充分"

**What went wrong**: The judge applies **rigid academic standards** — expects systematic historical coverage, deep music-theoretic analysis, specific performer citations. The 9K-char response offers a more focused, selective discussion. But the GT (8.87) shows humans found it excellent.

The key insight: **different evaluators have different expectations**. The rubric criteria were designed by academics expecting exhaustive coverage. Professional musicians (the likely human annotators) value selectivity and insight over exhaustive coverage. The judge over-penalizes for missing "standard" content.

**Failure mechanism**: Rubric criteria encode one evaluation philosophy (exhaustive academic), but the task's real evaluation needs are different (selective insight). The judge faithfully applies the rubric and gets the wrong answer.

### Cross-Model Pattern: Consistent Instruction Following Gap

Analysis across all 8 models on deepresearch_bench rubric mode reveals:

| Model | instruction_following MAE | insight MAE | comprehensiveness MAE | readability MAE |
|-------|------------------------|-------------|----------------------|-----------------|
| qwen3-max | 1.66 | 1.48 | 1.33 | 1.24 |
| deepseek-v4-flash | 1.35 | 2.54 | 2.00 | 1.20 |
| gpt-5.2 | 1.27 | 1.79 | 1.72 | 1.26 |
| gpt-4o-mini | 1.47 | 1.38 | 1.10 | 1.16 |

**Insight** is consistently the hardest dimension (highest MAE across all models), while **readability** is the easiest. instruction_following shows high variance — some models (gpt-5.2) handle it better than others (deepseek-v4-flash).

---

## Additional Failure Patterns

### Pattern (c): Rubric Rigidity — Checklist Evaluation vs. Holistic Judgment

When judges use rubric mode, they tend to apply criteria as a rigid checklist, penalizing responses that don't exactly match each sub-criterion. This is especially visible with deepseek-v4-flash, which **systematically under-scores** on rubric mode (all top-15 discrepancies are negative).

**Example**: deepseek-v4-flash on id=2 (insurance company comparison)
- **Judge**: 2.48 → GT: 7.07 (diff: -4.59)
- The judge harshly penalizes for: not using proper rankings, not covering all 10 companies equally, lacking financial data
- But humans found the response decent (7.07) — it has useful information even if not perfectly structured

The rubric encourages an **exhaustive, academic standard** that doesn't match the pragmatic standard humans apply.

### Pattern (d): Position Bias in Pairwise Evaluation

On pairwise tasks (wp_bench, ma), position bias is severe:

| Model | WP-Bench Inconsistency | MA Inconsistency | Pattern |
|-------|----------------------|-----------------|---------|
| glm-5.1 | 46.4% | **94.9%** | Always picks first position (37/39 cases) |
| gpt-4o-mini | **79.1%** | 20.5% | Random-like on wp_bench |
| gpt-5.2 | 47.5% | 33.3% | Moderate bias |
| qwen3-max | 21.6% | 12.8% | Least biased |

glm-5.1 shows extreme first-position bias on MA: 37 out of 39 inconsistent cases always pick response A regardless of content. This suggests the judge isn't evaluating content at all for these cases.

### Pattern (e): Score Compression in Pointwise Evaluation

Score compression is **not universal** across judges — it is highly model-specific and prompt-mode-dependent.

**Vanilla mode** (judge outputs a single overall score, 0–10):

| Model | Judge μ | GT μ | Judge σ | GT σ | Bias | Compression |
|-------|--------|------|---------|------|------|-------------|
| gpt-4o-mini | 8.60 | 7.20 | **0.55** | 1.22 | +1.40 | **Severe** |
| qwen3-32b-nothinking | 7.66 | 7.20 | **0.89** | 1.22 | +0.46 | Mild |
| qwen3-32b | 7.54 | 7.20 | **0.98** | 1.22 | +0.34 | Mild |
| gpt-5.2 | 6.25 | 7.20 | 1.47 | 1.22 | -0.95 | No |
| kimi-k2.6 | 6.26 | 7.20 | 1.52 | 1.22 | -0.94 | No |
| qwen3-max | 7.95 | 7.20 | 1.54 | 1.22 | +0.75 | No |
| deepseek-v4-flash | 7.76 | 7.20 | 1.76 | 1.22 | +0.56 | No |
| glm-5.1 | 8.20 | 7.20 | 2.28 | 1.22 | +1.00 | No (over-dispersed) |

Only **gpt-4o-mini** shows severe compression (σ=0.55), using less than half the range. qwen3-32b variants show mild compression. Most judges actually use a wider range than humans, not narrower.

**Reference mode** (same format, but with reference info) **reduces compression**:

| Model | Judge μ | Judge σ | Bias | Change from Vanilla |
|-------|--------|---------|------|--------------------|
| gpt-4o-mini | 7.14 | **1.00** | -0.06 | σ 0.55→1.00, mean 8.60→7.14 |
| deepseek-v4-flash | 6.01 | 2.00 | -1.19 | σ 1.76→2.00 |
| gpt-5.2 | 6.03 | 1.56 | -1.17 | σ 1.47→1.56 |

Providing reference information shifts judge scores closer to GT distribution and significantly broadens the score range for compressed models.

### Pattern (f): Task-Specific Blind Spots

On verify_bench_hard, 14.9% of cases have ALL 8 judges disagreeing with ground truth:

| Answer Type | Error Rate |
|-------------|-----------|
| D2-Semantic | **66.7%** |
| C4-Finite state | 53.3% |
| A3-Float | 57.5% |
| B2-List | 27.3% |

D2-Semantic tasks (requiring semantic understanding of long outputs) consistently fool all judges, suggesting a fundamental blind spot in LLM-as-Judge for semantic evaluation.

---

## Inter-Failure Pattern Correlation

### Long-Text Amplification × Coarse Semantic Granularity

Patterns (a) and (b) both manifest coarse semantic granularity, and long texts amplify this flaw:

- **Pattern (a)** — Streamable HTTP: 21K chars of SSE protocol discussion mask the concept confusion between "Messages API streaming" and "Streamable HTTP"
- **Pattern (b)** — Gaussian Electric Fields: 90% of the 17K-char response is a general survey, with only a few paragraphs addressing the actual question

In both cases, longer texts provide abundant surface-level keyword overlap, making it harder for the judge to recognize that the response does not precisely fulfill the task requirement.

### Position Bias × Task Type

Position bias in pairwise tasks shows a model×dataset interaction effect:

- glm-5.1 shows 94.9% bias on MA but only 46.4% on WP-Bench (extreme first-position preference on MA)
- gpt-4o-mini shows 79.1% bias on WP-Bench but only 20.5% on MA

This indicates position bias is not a fixed model attribute but a function of the interaction between model and task characteristics.

---

## Implications for Future Improvement

### 1. Toward Concept-Verification Evaluation
Pattern (a) reveals that judges match keywords rather than verify concepts. Future prompt designs should include explicit "concept verification" criteria: require the judge to confirm that the response discusses the *exact* concept in the instruction, not merely a related one. For technical domains, providing concise concept definitions in the rubric could help.

### 2. Task-Specific Instruction Following
Pattern (b) shows judges interpret "instruction following" as topical relevance, while humans mean task completion. The instruction_following dimension needs refinement for long-text tasks: generic topical alignment is insufficient. Judges should evaluate whether the response *accomplishes* what was asked, not just whether it stays "on topic."

### 3. Rubric Design: Balance Structure with Flexibility
Patterns (c) and (a) both implicate rubric design. Rubrics can help (by providing structure) and hurt (by encouraging checklist thinking without concept verification). Future designs should:
- Include a "holistic quality" assessment alongside checklist items
- Allow partial credit and reasonable selectivity
- Avoid overly fine-grained criteria (more than 5–6 sub-criteria may backfire)

### 4. Domain Expertise Integration
Across all failure patterns, judges lack the domain knowledge to detect subtle conceptual errors. Reference-based evaluation (providing key facts) helps partially, but does not solve coarse semantic granularity. Multi-judge voting or domain-adapted judges could reduce individual blind spots.

### 5. Position Bias: Mandatory Debiasing
Pattern (d) shows position bias in pairwise evaluation is severe for some models (glm-5.1: 95%). Debiased evaluation (averaging original and swapped positions) should be mandatory. Models with extreme bias should be flagged as unreliable for pairwise judgments.

---

## Methodology

### Data Sources
- **Judge results**: `outputs/judge_results/{model}/deepresearch_bench/vanilla_rubric_reference.jsonl`
- **Ground truth**: `ground_truth/deepresearch_bench_gt.jsonl`
- **Original responses**: `data_standardized/deepresearch_bench.jsonl`

### Analysis Approach
1. Identify cases with largest judge-GT discrepancy (|diff| ≥ 2.0 on 0-10 scale)
2. Read judge's per-criterion analysis text (rubric mode)
3. Compare judge's reasoning with actual response content
4. Classify failure mechanism
5. Cross-validate with other models and datasets

### GT Selection for Rubric Mode
The GT file contains two overall scores: `overall` (human holistic rating) and `weighted_total` (weighted average of 4 dimension scores using `dimension_weights`). For rubric mode analysis, we use **`weighted_total`** as the GT, since both judge and GT scores are derived from dimension-level evaluations. `overall` is only used for vanilla mode evaluation.

### Models Analyzed
gpt-5.2, gpt-4o-mini, deepseek-v4-flash, qwen3-max, qwen3-32b, qwen3-32b-nothinking, kimi-k2.6, glm-5.1

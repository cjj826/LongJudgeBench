# Case Study Analysis: LLM-as-Judge Failure Patterns

## Overview

This analysis examines **why LLM judges make mistakes** when evaluating long-form content, using rubric-mode outputs where judges provide per-criterion reasoning. We analyze 8 judge models across 6 datasets, focusing on the deepresearch_bench dataset where rubric+reference mode produces rich analysis text.

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
| **Response** | gemini-2.5-pro-deepresearch, 14,340 tokens |
| **Judge (qwen3-max, rubric+reference)** | 8.85 overall |
| **GT (human)** | 5.37 overall (instruction_following: 3.67, comprehensiveness: 5.33) |

**Judge's rubric analysis (excerpts)**:

> Comprehensiveness [1] score=9.5: "对核心技术机制和工作流程的解析极为出色...详细描述了从message_start到message_stop的完整事件序列"

> Instruction_following [0] score=10.0: "文章严格围绕Anthropic Messages API的流式实现（即其'Streamable HTTP'）展开"

> Insight [0] score=9.5: "对核心机制的阐释极具深度...展现了超越表面文档的深刻理解"

**What went wrong**: The judge confuses "Messages API SSE streaming" (an existing feature enabled by `stream: true`) with "Streamable HTTP" (a distinct MCP protocol specification). These are related but technically distinct — they share keywords like "Anthropic," "streaming," "SSE," and "events," but differ in their protocol design, use case, and technical details. The judge's keyword-matching semantic cannot distinguish them. The ~14K token response, which thoroughly covers Messages API streaming, provides enough keyword overlap to trigger a false positive on every rubric criterion. Human annotators with domain expertise instantly recognize the mismatch, giving instruction_following only 3.67.

**Failure mechanism**: Concept confusion caused by coarse semantic granularity. The judge matches surface-level keywords instead of verifying conceptual identity. Long texts amplify this flaw by providing abundant peripheral content that reinforces the keyword overlap.

---

## Pattern (b): Specialized Evaluation Needs Misalignment

### Mechanism

Long-text generation tasks often involve **narrow, context-specific evaluation needs** that general-purpose rubric criteria fail to capture. The fundamental misalignment: **judges evaluate surface-level topic coverage, while humans evaluate precise task completion**. A response can be "on topic" without actually answering the specific question asked — and in long-form evaluation, judges consistently fail to distinguish these two.

### Case Study B1: Gaussian Electric Fields (id=9)

The instruction_following dimension shows the largest gap across all analyzed cases:

| Dimension | Judge (qwen3-max, rubric+reference) | GT Avg | Gap |
|-----------|-----------|--------|-----|
| instruction_following | 9.88 | 4.83 | **+5.05** |
| comprehensiveness | 9.08 | 6.67 | +2.41 |
| readability | 9.33 | 6.00 | +3.33 |
| insight | 8.92 | 5.93 | +2.99 |

The judge's rubric criteria check: "Does the response stay within the topic domain?" "Does it mention the challenge?" "Does it cover multiple methods?" — surface-level topical coverage that the ~13K token response easily satisfies. But human evaluators apply a stricter standard: the response should directly answer the specific question about orientation uncertainty, not provide a general lecture on computational electrochemistry.

**Root cause**: In long-text evaluation, "instruction following" is interpreted by judges as topical relevance, but by humans as task completion. This gap widens with response length — longer responses can be more "on topic" while being less "on task."

### Case Study B2: Pipa Music Evolution Under-Scoring (id=37)

| Item | Value |
|------|-------|
| **Instruction** | 研究爵士钢琴在现代/当代音乐中的创新与风格演变 (Research jazz piano innovation and style evolution in modern/contemporary music) |
| **Response** | perplexity-Research, 8,320 tokens |
| **Judge (qwen3-max, rubric+reference)** | 4.93 overall |
| **GT (human)** | 8.87 overall (insight: 8.83, comprehensiveness: 8.83) |

**Judge's rubric analysis**:

> Comprehensiveness [0] score=4.5: "对1950年前的关键风格缺乏系统梳理，未能为现代演变提供清晰的历史参照系"

> Insight [0] score=3.0: "分析流于表象，缺乏对关键转折点的机制性解释"

> Instruction_following [2] score=5.0: "未系统对比经典与现代在钢琴技法上的具体差异，回应不够充分"

**What went wrong**: The judge applies **rigid academic standards** — expects systematic historical coverage, deep music-theoretic analysis, specific performer citations. The ~8K token response offers a more focused, selective discussion. But the GT (8.87) shows humans found it excellent.

The key insight: **different evaluators have different expectations**. The rubric criteria were designed by academics expecting exhaustive coverage. Professional musicians (the likely human annotators) value selectivity and insight over exhaustive coverage. The judge over-penalizes for missing "standard" content.

**Failure mechanism**: Rubric criteria encode one evaluation philosophy (exhaustive academic), but the task's real evaluation needs are different (selective insight). The judge faithfully applies the rubric and gets the wrong answer.

### Cross-Model Pattern: Consistent Instruction Following Gap

Analysis across all 8 models on deepresearch_bench rubric+reference mode reveals:

| Model | instruction_following MAE | insight MAE | comprehensiveness MAE | readability MAE |
|-------|------------------------|-------------|----------------------|-----------------|
| qwen3-max | 1.67 | 1.48 | 1.33 | 1.24 |
| deepseek-v4-flash | 1.36 | 2.53 | 2.00 | 1.19 |
| gpt-5.2 | 1.27 | 1.79 | 1.72 | 1.26 |
| gpt-4o-mini | 1.47 | 1.38 | 1.10 | 1.16 |
| qwen3-32b | 1.15 | 1.31 | 1.31 | 1.23 |
| qwen3-32b-nothinking | 1.30 | 1.32 | 1.32 | 1.22 |
| glm-5.1 | 1.50 | 2.16 | 1.79 | 1.33 |
| kimi-k2.6 | **2.20** | **2.91** | **2.67** | **2.45** |

**Insight** is consistently the hardest dimension (highest MAE across all models), while **readability** is the easiest. instruction_following shows high variance — some models (gpt-5.2) handle it better than others (deepseek-v4-flash).

---

## Additional Failure Patterns

### Pattern (c): Rubric Rigidity — Checklist Evaluation vs. Holistic Judgment

When judges use rubric mode, they tend to apply criteria as a rigid checklist, penalizing responses that don't exactly match each sub-criterion. This is especially visible with deepseek-v4-flash, which **systematically under-scores** on rubric mode (all top-15 discrepancies are negative).

**Example**: deepseek-v4-flash (rubric mode) on id=2 (insurance company comparison)
- **Judge**: 3.70 → GT: 7.07 (diff: -3.37)
- The judge harshly penalizes for: not using proper rankings, not covering all 10 companies equally, lacking financial data
- But humans found the response decent (7.07) — it has useful information even if not perfectly structured

The rubric encourages an **exhaustive, academic standard** that doesn't match the pragmatic standard humans apply.

### Pattern (d): Position Bias in Pairwise Evaluation

On pairwise tasks (wp_bench, ma), position bias is severe (evaluated in vanilla mode):

| Model | WP-Bench Inconsistency (vanilla) | MA Inconsistency (vanilla) | WP-Bench Pattern | MA Pattern |
|-------|----------------------|-----------------|-----------------|------------|
| glm-5.1 | 47/263 (17.9%) | 30/90 (33.3%) | First-pos bias | First-pos bias (28/30) |
| gpt-4o-mini | 207/263 (**78.7%**) | 44/90 (48.9%) | First-pos bias | Mixed |
| gpt-5.2 | 121/263 (46.0%) | 50/90 (55.6%) | First-pos bias | First-pos bias |
| deepseek-v4-flash | 163/263 (62.0%) | 41/90 (45.6%) | First-pos bias | Mixed |
| qwen3-max | 113/263 (43.0%) | 35/90 (38.9%) | First-pos bias | First-pos bias |
| qwen3-32b | 56/263 (21.3%) | 34/90 (37.8%) | First-pos bias | Mixed |
| qwen3-32b-nothinking | 42/263 (16.0%) | 19/90 (21.1%) | Mixed | Mixed |
| kimi-k2.6 | 28/263 (10.6%) | 21/90 (23.3%) | Mixed | Mixed |

Position bias varies significantly by model and dataset. WP-Bench (263 total pairs across 158 instructions) and MA (90 pairs) show different patterns. For example, glm-5.1 on MA shows 30/90 pairs (33.3%) inconsistent when A/B positions are swapped — of those, 28/30 (93.3%) always pick the first position, indicating extreme first-position bias. Conversely, gpt-4o-mini shows 207/263 (78.7%) inconsistency on WP-Bench but only 44/90 (48.9%) on MA. The inconsistency rate measures **how often** position flips change the result; the "always-A" ratio measures the **direction** of the bias. Both are needed: high inconsistency without directional bias suggests randomness, while high inconsistency with strong directional bias (≥80%) signals systematic position preference.

### Pattern (e): Score Compression in Pointwise Evaluation

Score compression is **not universal** across judges — it is highly model-specific and prompt-mode-dependent.

**Vanilla mode** (judge outputs a single overall score, 0–10):

| Model | Judge μ | GT μ | Judge σ | GT σ | Bias | Compression |
|-------|--------|------|---------|------|------|-------------|
| gpt-4o-mini | 8.60 | 7.24 | **0.55** | 1.22 | +1.36 | **Severe** |
| qwen3-32b-nothinking | 7.77 | 7.24 | **0.95** | 1.22 | +0.53 | Mild |
| qwen3-32b | 7.65 | 7.24 | **1.00** | 1.22 | +0.40 | Mild |
| gpt-5.2 | 6.25 | 7.24 | 1.47 | 1.22 | -0.99 | No |
| kimi-k2.6 | 6.28 | 7.24 | 1.54 | 1.22 | -0.96 | No |
| qwen3-max | 8.00 | 7.24 | 1.55 | 1.22 | +0.76 | No |
| deepseek-v4-flash | 7.77 | 7.24 | 1.76 | 1.22 | +0.53 | No |
| glm-5.1 | 8.22 | 7.24 | 2.29 | 1.22 | +0.99 | No (over-dispersed) |

Only **gpt-4o-mini** shows severe compression (σ=0.55), using less than half the range. qwen3-32b variants show mild compression. Most judges actually use a wider range than humans, not narrower.

**Reference mode** (same format, but with reference info) **reduces compression**:

| Model | Judge μ | Judge σ | Bias | Change from Vanilla |
|-------|--------|---------|------|--------------------|
| gpt-4o-mini | 7.15 | **0.99** | -0.09 | σ 0.55→0.99, mean 8.60→7.15 |
| deepseek-v4-flash | 6.02 | 2.00 | -1.22 | σ 1.76→2.00 |
| gpt-5.2 | 6.05 | 1.57 | -1.19 | σ 1.47→1.57 |

Providing reference information shifts judge scores closer to GT distribution and significantly broadens the score range for compressed models.

### Pattern (f): Task-Specific Blind Spots

On verify_bench_hard, 14.9% of cases have ALL 8 judges disagreeing with ground truth:

| Metric | Value |
|--------|-------|
| Total cases | 316 |
| All judges correct | ~27.8% |
| **All judges wrong** | **~14.9%** |
| Mixed | ~57.3% |

| Answer Type | Error Rate | Description |
|-------------|-----------|-------------|
| **A3-Float** | **57.5%** | Floating-point precision |
| C4-Finite state | 53.3% | Finite state verification |
| D2-Semantic | 50.0% | Semantic understanding tasks |
| B2-Equation | 50.0% | Equation verification |
| A2-Constant | 50.0% | Constant verification |
| A1-Integer | 35.6% | Integer verification |

A3-Float (floating-point precision) shows the highest error rate at 57.5%, while D2-Semantic tasks reach 50.0%, indicating blind spots in LLM-as-Judge for both numerical precision and semantic evaluation.

**Case 6A (A3-Float, id=860bb1...)**：Instruction: "Write $x^2+1500x+1500$ as $(x+b)^2+c$, find $c/b$." The response correctly completes the square: $b=750, c=-561000, c/b=-748$. Yet all 8 judges judge it as incorrect (NO). Reason: the computation involves large-number arithmetic ($1500^2=2,250,000$, $-561,000/750=-748$) that judges cannot reliably track.

**Case 6B (D2-Semantic, id=4b0b45...)**：Instruction: "In $\triangle ABC$, $a=\sqrt{3}, b=\sqrt{2}, B=45^{\circ}$, find $A, C$ and side $c$." By the Law of Sines, $\sin A = \sqrt{3}/2$, so $A=60^{\circ}$ or $120^{\circ}$ (SSA ambiguous case — both are valid). The response gives only $A=60^{\circ}$. However, 3/8 judges incorrectly say YES, failing to recognize the missing second solution, which requires geometric semantic understanding.

---

## Inter-Failure Pattern Correlation

### Long-Text Amplification × Coarse Semantic Granularity

Patterns (a) and (b) both manifest coarse semantic granularity, and long texts amplify this flaw:

- **Pattern (a)** — Streamable HTTP: ~14K tokens of SSE protocol discussion mask the concept confusion between "Messages API streaming" and "Streamable HTTP"
- **Pattern (b)** — Gaussian Electric Fields: 90% of the ~13K token response is a general survey, with only a few paragraphs addressing the actual question

In both cases, longer texts provide abundant surface-level keyword overlap, making it harder for the judge to recognize that the response does not precisely fulfill the task requirement.

### Position Bias × Task Type

Position bias in pairwise tasks shows a model×dataset interaction effect:

- glm-5.1 shows 33.3% inconsistency on MA (93.3% always-first among inconsistent pairs) but only 17.9% on WP-Bench
- gpt-4o-mini shows 78.7% inconsistency on WP-Bench (always-first) but only 48.9% on MA (mixed direction)

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
Pattern (d) shows position bias in pairwise evaluation is severe for some models (glm-5.1: 93.3% of inconsistent pairs always pick the first position). Debiased evaluation (averaging original and swapped positions) should be mandatory. Models with extreme bias should be flagged as unreliable for pairwise judgments.

---

## Methodology

### Data Sources
- **Judge results**: `outputs/judge_results/{model}/deepresearch_bench/vanilla_rubric_reference.jsonl`
- **Ground truth**: `ground_truth/deepresearch_bench_gt.jsonl`
- **Original responses**: `data_standardized/deepresearch_bench.jsonl`

### Analysis Approach
1. Identify cases with largest judge-GT discrepancy (|diff| ≥ 2.0 on 0-10 scale)
2. Read judge's per-criterion analysis text (rubric+reference mode)
3. Compare judge's reasoning with actual response content
4. Classify failure mechanism
5. Cross-validate with other models and datasets

### GT Selection for Rubric+Reference Mode
The GT file contains two overall scores: `overall` (human holistic rating) and `weighted_total` (weighted average of 4 dimension scores using `dimension_weights`). For rubric+reference mode analysis, we use **`weighted_total`** as the GT, since both judge and GT scores are derived from dimension-level evaluations. `overall` is only used for vanilla mode evaluation.

### Models Analyzed
gpt-5.2, gpt-4o-mini, deepseek-v4-flash, qwen3-max, qwen3-32b, qwen3-32b-nothinking, kimi-k2.6, glm-5.1

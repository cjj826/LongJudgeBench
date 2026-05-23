# Standardized_function (部分)— 数据集标准化处理

## 概述

将 5 个原始数据集标准化为统一 JSONL 格式，方便后续交由 LLM-as-Judge 评测及计算可靠性。

标准化后的数据输出到：

- `data_standardized/` — 标准化数据（含 instruction + responses + ground_truth）
- `ground_truth/` — 纯真值（便于直接对比）

---

## 文件说明

| 文件                            | 功能                                             |
| ------------------------------- | ------------------------------------------------ |
| `utils.py`                    | 共享工具函数（路径定义、JSONL 读写、token 计数） |
| `standardize_deepresearch.py` | DeepResearch-Bench 标准化                        |
| `standardize_surge.py`        | SurGE 标准化                                     |
| `standardize_wp_bench.py`     | Writing-Preference-Bench 标准化                  |
| `standardize_realdr.py`       | RealDR 标准化                                    |
| ..                              | .....                                            |

---

## 1. DeepResearch-Bench

### 原始数据位置

| 数据            | 路径                                                                |
| --------------- | ------------------------------------------------------------------- |
| 4 个模型输出    | `data/DeepResearch-Bench-Dataset/generated_reports/{model}.jsonl` |
| 真值 (3 人标注) | `data/DeepResearch-Bench-Dataset/Deepresearch_GT.jsonl`           |
| 维度权重        | `data/DeepResearch-Bench-Dataset/criteria.jsonl`                  |

### 处理过程

1. 从 `criteria.jsonl` 加载每个 id 的维度权重
2. 从 4 个模型的 jsonl 读取 `id <= 50` 的条目，以 `id` 为键聚合
3. 从 `Deepresearch_GT.jsonl` 读取每个 id 的 3 条标注
4. 取 3 人各维度均值，按权重计算加权总分

### 输出字段

| 字段                                           | 说明                                                                                                              |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `dataset`                                    | 固定为 `"deepresearch_bench"`                                                                                   |
| `id`                                         | 1-50                                                                                                              |
| `instruction`                                | prompt 文本                                                                                                       |
| `responses[].model`                          | 模型名：`openai-deepresearch`, `gemini-2.5-pro-deepresearch`, `grok-deeper-search`, `perplexity-Research` |
| `responses[].content`                        | article 全文                                                                                                      |
| `ground_truth.type`                          | `"pointwise_multi_dim"`                                                                                         |
| `ground_truth.dimension_weights`             | 4 维权重 (readability/insight/comprehensiveness/instruction_following)                                            |
| `ground_truth.scores.{model}.dimensions`     | 各维度均值                                                                                                        |
| `ground_truth.scores.{model}.weighted_total` | 加权总分                                                                                                          |
| `ground_truth.scores.{model}.overall`        | 原始 overall 均值                                                                                                 |
| `ground_truth.annotators`                    | 3                                                                                                                 |

### 真值格式 (`ground_truth/deepresearch_bench_gt.jsonl`)

| 字段                | 说明                                                                           |
| ------------------- | ------------------------------------------------------------------------------ |
| `raw_annotations` | 3 条原始标注（含 `annotation_id`、`dimension_scores`、`overall_scores`） |
| `aggregated`      | 聚合后的各模型各维度均值 + 加权总分                                            |

---

## 2. SurGE

### 原始数据位置

| 数据         | 路径                                                           |
| ------------ | -------------------------------------------------------------- |
| 标注结果     | `data/SurGE/标注结果.xlsx`                                   |
| 4 个系统输出 | `data/SurGE/baselines/{Autosurvey,GT,ID,Naive}/output/{id}/` |

### 处理过程

1. 从 xlsx 读取 41 条 topic 及排序（结构排序 + 内容排序）
2. 对每个 topic，从 4 个系统目录读取对应输出文件
3. 结构排序和内容排序各自保留，不合并

### 输出字段

| 字段                               | 说明                                      |
| ---------------------------------- | ----------------------------------------- |
| `dataset`                        | `"surge"`                               |
| `id`                             | 0-40                                      |
| `instruction`                    | Topic 标题                                |
| `responses[].model`              | `GT`, `AutoSurvey`, `ID`, `Naive` |
| `responses[].content`            | 模型输出全文                              |
| `ground_truth.type`              | `"listwise_ranking"`                    |
| `ground_truth.structure_ranking` | 结构质量排序 (1=最好, 4=最差)             |
| `ground_truth.content_ranking`   | 内容质量排序 (1=最好, 4=最差)             |

---

## 3. Writing-Preference-Bench

### 原始数据位置

| 数据 | 路径                                                         |
| ---- | ------------------------------------------------------------ |
| 中文 | `data/Writing-Preference-Bench-main/WP_bench_chinese.json` |
| 英文 | `data/Writing-Preference-Bench-main/WP_bench_english.json` |

### 处理过程

1. 读取 JSON，每条含 `prompt` + `chosen` + `rejected`
2. `chosen.response` 标记为 label=1（更好），`rejected.response` 标记为 label=0（更差）
3. 模型名称保持原始命名

### 输出字段

| 字段                      | 说明                                    |
| ------------------------- | --------------------------------------- |
| `dataset`               | `"wp_bench"`                          |
| `id`                    | `prompt_id` (UUID)                    |
| `instruction`           | `prompt` 文本                         |
| `responses[].model`     | 原始模型名（如 `OpenAI-gpt4.1-mini`） |
| `responses[].content`   | response 文本                           |
| `responses[].label`     | 1 = chosen, 0 = rejected                |
| `ground_truth.type`     | `"pairwise_preference"`               |
| `ground_truth.chosen`   | 被选中回复的 model + score              |
| `ground_truth.rejected` | 被拒绝回复的 model + score              |
| `meta.language`         | `"zh"` 或 `"en"`                    |

---

## 4. RealDR (our_data)

### 原始数据位置

| 数据        | 路径                                                              |
| ----------- | ----------------------------------------------------------------- |
| 文档        | `data/our_data/task{1..40}/Doc_*.docx` (640 个)                 |
| 映射 + 权重 | `data/our_data/GT/checklist_mapping_key_T1_T40_1771971296.xlsx` |
| 标注员1     | `data/our_data/GT/Human_result1.xlsx`                           |
| 标注员2     | `data/our_data/GT/Human_result2.xlsx`                           |
| Instruction | `task_prompt/task{id}.jsonl` → `prompt{Pos}.context`         |

### 处理过程

1. 从 mapping xlsx 读取每个 `Blind ID` 的 (`Task ID`, `Model`, `PromptPos`, `Weight1/2/3`)
2. 读取对应 docx 的文本内容
3. 从 `task_prompt` 读取对应 `prompt{Pos}.context` 作为 instruction
4. 读取两人打分，各维度取均值
5. 计算加权总分：`逻辑结构×W1 + 表达形式×W2 + 偏见检查×W3`
6. 无排除，40 个 task 全部纳入

### 评分维度

| 维度     | 权重来源    | 说明         |
| -------- | ----------- | ------------ |
| 逻辑结构 | `Weight1` | 文档结构质量 |
| 表达形式 | `Weight2` | 语言表达质量 |
| 偏见检查 | `Weight3` | 偏见/公平性  |

### 输出字段

| 字段                            | 说明                                 |
| ------------------------------- | ------------------------------------ |
| `dataset`                     | `"realdr"`                         |
| `id`                          | `"Doc_001"` 格式                   |
| `instruction`                 | 对应的 prompt context                |
| `responses[].model`           | 模型名（如 `Gemini`, `Mita` 等） |
| `responses[].content`         | docx 全文文本                        |
| `ground_truth.type`           | `"pointwise_multi_dim_weighted"`   |
| `ground_truth.dimensions`     | 各维度两人均值                       |
| `ground_truth.weights`        | 各维度权重                           |
| `ground_truth.weighted_total` | 加权总分                             |
| `ground_truth.annotators`     | 2                                    |

---

## 统一 Schema

所有数据集共用以下顶层结构：

```json
{
  "dataset": "deepresearch_bench | surge | wp_bench | realdr | writing_prompts",
  "id": "<全局唯一 ID>",
  "instruction": "<指令文本>",
  "responses": [
    {"model": "<模型名>", "content": "<回复内容>"}
  ],
  "ground_truth": { /* 各数据集特有格式 */ },
  "meta": {
    "language": "zh | en",
    "task_type": "pointwise | pairwise | listwise",
    "source": "原始数据集名"
  }
}
```

---

## 运行方式

```bash
# 在项目根目录下运行

# DeepResearch-Bench
& D:/Anaconda/envs/tensorflow/python.exe Standardized_function/standardize_deepresearch.py

# SurGE
& D:/Anaconda/envs/tensorflow/python.exe Standardized_function/standardize_surge.py

# Writing-Preference-Bench
& D:/Anaconda/envs/tensorflow/python.exe Standardized_function/standardize_wp_bench.py

# RealDR
& D:/Anaconda/envs/tensorflow/python.exe Standardized_function/standardize_realdr.py

.......

# 或一键运行所有
& D:/Anaconda/envs/tensorflow/python.exe -m Standardized_function.utils
```

## 依赖

```
tiktoken         # token 计数（可选，不安装则用空格分词）
openpyxl         # 读取 xlsx
python-docx      # 读取 docx
```

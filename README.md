# LongJudgeBench

LongJudgeBench 是一个面向长文本生成的 LLM-as-Judge 评测框架，支持 **pointwise**（逐点评分）、**pairwise**（成对比较）、**listwise**（排序比较）三种评测范式，覆盖研究报告、文档质量、写作偏好、综述生成等多种任务场景。

## 项目结构

├── config/                   # 评测配置 & prompt 模板
│   ├── judge_config.yaml     # 评测参数（temperature, max_tokens 等）
│   ├── prompts/{dataset}/    # 各数据集 prompt 模板（vanilla/rubric/reference 变体）
│   └── dataset_registry.json # 数据集注册信息
├── data/                     # 各数据集原始数据格式
├── data_standardized/        # 标准化后的 JSONL 格式数据
│   ├── {dataset}.jsonl       # 评测数据
│   ├── {dataset}_reference.jsonl  # 参考文章
│   └── {dataset}_criteria.jsonl   # 评分标准
├── ground_truth/             # 真值文件
├── src/
│   ├── evaluation/           # 评测主流程
│   │   ├── run_judge.py      # Judge 运行入口
│   │   ├── compute_reliability.py  # 可靠性指标计算
│   │   └── datasets/         # 各数据集适配模块
│   ├── judge/                # Judge 实现
│   │   ├── base_judge.py     # 基类（JSON 解析、错误处理）
│   │   ├── pointwise_judge.py
│   │   ├── pairwise_judge.py
│   │   └── listwise_judge.py
│   ├── reliability/          # 指标计算
│   │   └── agreement_metrics.py  # ACC / Spearman / Kendall
│   └── utils/                # 工具类
├── scripts/                  # 运行脚本
│   ├── run_all.sh            # 全量实验启动
│   ├── run_judge.sh          # 单任务 Judge
│   ├── run_parallel.sh     # 并行调度
│   └── export_results_xlsx.sh # 结果导出
└── outputs/                  # 评测输出
    ├── judge_results/        # Judge 原始输出（JSONL）
    └── reliability_scores/   # 可靠性计算结果（JSON）

## 评测范式

| 范式                | 说明                                       | 适用数据集                                    |
| ------------------- | ------------------------------------------ | --------------------------------------------- |
| **pointwise** | 对每个 model 的回复独立评分（0-10 或 0/1） | deepresearch_bench, realdr, verify_bench_hard |
| **pairwise**  | 比较两个回复，选偏好 A/B                   | wp_bench, ma                                  |
| **listwise**  | 对多个回复排序（pointwise 打分后转排序）   | surge                                         |

## 数据集

| 数据集             | 范式      | 语言         | 记录数              | 回复数 | 任务                                                                                       |
| ------------------ | --------- | ------------ | ------------------- | ------ | ------------------------------------------------------------------------------------------ |
| deepresearch_bench | pointwise | zh           | 50 topics×4 models | 200    | 深度研究报告评分（comprehensiveness/insight/instruction_following/readability 四维度加权） |
| realdr             | pointwise | zh           | 40 tasks×16 models | 640    | 文档质量评分（逻辑结构/表达形式/偏见检查 三维度加权）                                      |
| verify_bench_hard  | pointwise | en           | 316                 | 316    | 二分类验证（Yes/No）                                                                       |
| wp_bench           | pairwise  | multilingual | 263                 | 526    | 写作偏好比较（debiased 正反各评一次）                                                      |
| ma                 | pairwise  | en           | 120                 | 240    | 多智能体写作比较（insights + structure 两维度×8 标注者）                                  |
| surge              | listwise  | en           | 41                  | 164    | 综述生成排序（4 系统，structure + content 两维度排名）                                     |

### Prompt 模式

每个数据集支持以下 prompt 模式变体：

| 模式                       | 说明                                  |
| -------------------------- | ------------------------------------- |
| **vanilla**          | 基础评分指令                          |
| **rubric**           | 带评分标准（criteria_list）的维度评分 |
| **reference**        | 提供参考文章辅助评分                  |
| **rubric_reference** | 评分标准 + 参考文章                   |

Pairwise 数据集（ma）和 listwise 数据集（surge）额外按评分维度加前缀：

- ma: `insights_vanilla`, `structure_vanilla`, `insights_vanilla_reference` 等
- surge: `structure_vanilla`, `content_vanilla`, `structure_vanilla_reference` 等

## 数据格式

标准化评测数据统一为 JSONL 格式（`data_standardized/{dataset}.jsonl`）：

```json
{
  "dataset": "数据集名",
  "id": "唯一 ID",
  "instruction": "任务指令 / prompt",
  "responses": [
    {"model": "模型名", "content": "模型回复全文"}
  ],
  "ground_truth": { /* 真值，格式见下 */ },
  "meta": {
    "language": "zh / en",
    "task_type": "pointwise / pairwise / listwise",
    "source": "数据来源"
  }
}
```

参考文件（`{dataset}_reference.jsonl`）包含 reference 提示词模式所需的参考文本。

### 真值格式

| 范式      | ground_truth 格式                                                 | 指标                                 |
| --------- | ----------------------------------------------------------------- | ------------------------------------ |
| pointwise | `{"type": "pointwise_...", "scores": {model: score}}`           | pairwise ACC, Spearman, Kendall's τ |
| pairwise  | `{"type": "pairwise_preference", "preferred": "A/B/tie"}`       | ACC（偏好一致性）                    |
| listwise  | `{"type": "listwise_ranking", "dimension_name": {model: rank}}` | Spearman, Kendall's τ, pairwise ACC |

## 运行方式

```bash
# 1. 单任务运行
bash scripts/run_judge.sh <dataset> <paradigm> <model> [--prompt MODE] [--workers N]

# 示例：deepresearch_bench pointwise 评测
bash scripts/run_judge.sh deepresearch_bench pointwise gpt-4o-mini --prompt vanilla

# 2. 全量实验（自动跳过已有结果）
python scripts/run_all.py
python scripts/run_all.py --model gpt-4o-mini --prompt vanilla

# 3. 仅计算可靠性指标（Judge 已完成时）
python src/evaluation/compute_reliability.py <dataset> <paradigm> <model> --prompt <mode>

# 4. 结果导出
python scripts/export_results_xlsx.py outputs/reliability_summary.xlsx
```

### 断点续跑

所有运行方式均内置断点续跑：重复执行同一任务会自动跳过已完成项，从断点继续。删除 `outputs/judge_results/{model}/{dataset}/{mode}.jsonl` 后可强制重跑。

## 输出格式

### Judge 输出（`outputs/judge_results/{model}/{dataset}/{mode}.jsonl`）

每行一条 Judge 评分结果：

```json
{
  "data_id": "记录 ID",
  "model": "模型名",
  "judge_result": { "overall_score": 8.5, ... },
  "response": "Judge 原始回复内容"
}
```

错误记录输出到同目录下的 `{mode}_errors.jsonl`、`{mode}_token_exceed.jsonl`。

### 可靠性分数（`outputs/reliability_scores/{model}/{dataset}/{mode}.json`）

```json
{
  "dataset": "surge",
  "paradigm": "listwise",
  "prompt_mode": "structure_vanilla",
  "judge_model": "gpt-4o-mini",
  "groups": {
    "structure": {
      "n": 123,
      "accuracy": 0.7654,
      "spearman": 0.8123,
      "kendall": 0.7345,
      "accuracy_correct": 94,
      "accuracy_total": 123
    }
  },
  "token_exceed": { "count": 2, "error_rate": 0.016 },
  "per_query": { "structure": { "spearman": 0.82, "kendall": 0.74 } }
}
```

## 指标说明

- **pairwise ACC**：对所有 C(n,2) 对比较 GT 和 Pred 中排序是否一致，同分不计入分母
- **Spearman**：秩相关系数，衡量排序一致性
- **Kendall's τ**：Kendall 秩相关系数，能处理同分情况
- **per query 指标**：分 query 计算 Spearman/Kendall 后取平均，避免长尾数据主导

## 关键配置

评测参数在 `config/judge_config.yaml` 中：

- `temperature: 0.0` — 确定性输出（评测标准设定）
- `max_tokens: 24576` — Judge 最大生成长度（实验设定）
- `max_prompt_tokens: 131072` — 最大输入长度（实验设定）

Prompt 模板在 `config/prompts/{dataset}/` 下，使用 YAML 格式定义评分指令和输出格式。

## 自定义数据集

1. 在 `Standardized_function/` 中添加标准化脚本，输出到 `data_standardized/{dataset}.jsonl` 和 `ground_truth/{dataset}_gt.jsonl`
2. 在 `src/evaluation/datasets/` 中添加数据集模块（实现 `extract_metrics()`）
3. 在 `config/prompts/{dataset}/` 中添加 prompt 模板 YAML
4. 在 `config/dataset_registry.json` 中注册

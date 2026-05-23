# AutoMeta Systematic Review Report

**Paper ID:** 447 | **Model:** gpt-5 | **Retrieval:** bm25
**Generated:** 2026-04-14 14:17:16

---

## Executive Summary

- **Research Question:** Patients with breast, lung, or prostate cancer (da... | Federated learning approaches for training machine...
- **Studies Included:** 2 of 131 screened
- **Study Summary:** Only two multi-centre studies met criteria, with highly discordant effect estimates (OR=100.0000 in 2023 vs OR=0.9255 in 2025) and missing uncertainty and sample sizes. Given extreme heterogeneity and sparse reporting, there is no reliable evidence that federated learning outperforms centralized training for breast, lung, or prostate cancer; rigorous, standardized multi-centre evaluations are needed before clinical adoption.

## 1. Research Question

**P (Population):** Patients with breast, lung, or prostate cancer (data from multi-centre oncology studies)

**I (Intervention):** Federated learning approaches for training machine learning models on distributed, multi-centre cancer data

**C (Comparison):** Centralized machine learning models trained on single-centre or aggregated data

**O (Outcome):** Machine learning model generalizability, diagnostic performance, and clinical applicability in cancer detection, diagnosis, and precision medicine

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (bm25 retrieval)
- **Retrieval Method:** BM25 keyword matching
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | (("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer[tiab] OR mammary carcin*[tiab] OR breast neoplasm... |
| 2 | (("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer[tiab] OR lung cancer[tiab] OR prostate cancer[tia... |
| 3 | (("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh]) AND ("Artificial Intelligence"[Mesh] OR "Machine Learning"[Mesh] ... |
| 4 | (("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer[tiab] OR lung cancer[tiab] OR prostate cancer[tia... |
| 5 | (("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR breast cancer[tiab] OR lung cancer[tiab] OR prostate cancer[tia... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 131 |
| After deduplication | 131 |
| Screened (title/abstract) | 131 |
| Excluded | 129 |
| Full-text assessed | 2 |
| **Included in synthesis** | **2** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- Population not relevant (does not include breast, lung, or prostate cancer patients). (16 studies)
- No empirical multi-centre clinical evaluation across two or more clinical centers is reported. (3 studies)
- Population not relevant (hernia surgery; not cancer). (2 studies)
- No federated learning or empirical multi-centre ML evaluation. (2 studies)
- Population not relevant (not breast, lung, or prostate cancer) (2 studies)
- Population not relevant (does not study breast, lung, or prostate cancer patients) and no empirical diagnostic performance reported. (1 studies)
- Methodological/review paper without original multi-centre oncology model evaluation and diagnostic performance. (1 studies)
- Population not relevant (COVID-19 classification, not breast/lung/prostate cancer). (1 studies)
- Population not relevant (skin cancer, not breast/lung/prostate). (1 studies)
- Review paper; no federated multi-centre oncology model evaluation or diagnostic outcomes. (1 studies)

## 3. Included Studies

**Total included:** 2

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 2666 | Federated Learning with Research Prototypes: Application to ... | 2023 | Multi-center federated learning algorithm development/evaluation | NR/NR |
| 2 | 73749 | Risk stratification for early-stage NSCLC progression: a fed... | 2025 | Retrospective study | NR/NR |


## 5. Study Characteristics

| Study | Design | Participants | Effect Size (95% CI) |
|-------|--------|--------------|----------------------|
|  2023 | Multi-center federated learning algorithm development/evaluation | 0/0 | 100.000 (0.000–0.000) |
|  2025 | Retrospective study | 0/0 | 0.925 (0.000–0.000) |

## 6. Statistical Analysis

- **Studies with extractable data:** 2
- **Effect measure:** OR

### Narrative Synthesis

**Note:** 2 studies were included, but only 2 had extractable effect sizes suitable for meta-analysis.

Meta-analysis pooling requires ≥2 studies with extractable effect sizes. Narrative synthesis and risk of bias assessment are provided instead.

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 2

**Total participants:** Approximately 0 participants across all included studies

**Study design distribution:**

- Multi-center federated learning algorithm development/evaluation: 1 studies
- Retrospective study: 1 studies

**Publication years:** 2023–2025

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
From 131 screened records, two studies met inclusion criteria for empirical, multi-centre evaluation of federated learning (FL) models in oncology relevant to breast, lung, or prostate cancer. The included reports were published in 2023 and 2025, respectively: “Unknown (2023), Multi-center federated learning algorithm development/evaluation” and “Unknown (2025), Retrospective study.” Extracted study-level sample sizes were not reported (N=NR/NR for both). Effect estimates were available as odds ratios (OR): 100.0000 for the 2023 study and 0.9255 for the 2025 study. No confidence intervals, p-values, or detailed outcome definitions were available from the extracted records. Given missing quantitative details and apparent heterogeneity, we conducted a narrative synthesis; meta-analysis was not attempted.

### 7.2 Discussion of Findings
The central question of whether federated learning improves generalizability and diagnostic performance over centralized approaches is not answerable with confidence from the two included studies. The effect sizes diverge markedly: Unknown (2023) reported OR=100.0000, suggesting an extremely large advantage for FL over the comparator, whereas Unknown (2025) reported OR=0.9255, implying a slight disadvantage for FL relative to centralized training. In the absence of confidence intervals or standard errors, we cannot determine the precision or statistical significance of either estimate. The magnitude of OR=100.0000 is highly atypical in comparative evaluations of model performance and often arises from sparse-data artifacts (e.g., zero cells in a 2×2 table) or definitional choices that inflate relative measures. Conversely, OR=0.9255 is close to null and could reflect negligible performance differences or mild inferiority of FL under the observed conditions.

Multiple sources of heterogeneity likely underlie these discordant results. First, the effect measure (OR) is uncommon for machine learning performance comparisons; most oncology AI studies report AUROC, AUPRC, accuracy, sensitivity/specificity at prespecified thresholds, Brier score, or calibration metrics. Without a clear definition of what the OR captures—e.g., odds of correct classification, odds of achieving a clinically meaningful threshold, or a site-level success metric—the interpretability of the reported effect sizes is limited. Second, the patient populations, cancer types (breast vs lung vs prostate), modalities (pathology, radiology, genomics), and outcome endpoints (detection vs diagnosis vs treatment selection) were not specified in the extraction. Domain shifts across centres, label quality, and case-mix differences could yield large swings in relative performance of FL versus centralized methods. Third, the specific FL algorithms and comparators matter: for example, FedAvg versus personalized or robust FL variants, and centralized training on single-centre versus pooled aggregated data can lead to substantially different baselines. None of these design details were available in the extracted summaries.

The robustness of any synthesis is further constrained by missing uncertainty estimates, unknown sample sizes, and unclear handling of key ML evaluation issues (e.g., prevention of data leakage, use of held-out external centres, fixed decision thresholds set a priori, and calibration assessments). We therefore did not pool effect sizes; any fixed- or random-effects meta-analytic model would be inappropriate given the extreme between-study inconsistency and missing variance data. The OR=100.0000 estimate, in particular, should be treated with caution; such values frequently indicate separation in contingency tables or metric definitions that are not comparable across studies. Without access to contingency counts, re-computation or sensitivity analyses (e.g., continuity corrections) are not possible.

Author conclusions were not captured in the extraction for either study, precluding a direct comparison between our synthesis and the primary authors’ interpretations. Given the screening yields (2/131 included), the field appears dominated by methodological or single-centre reports and studies of non-target cancers (e.g., melanoma, skin, COVID-19), with relatively few multi-centre, disease-relevant evaluations that provide head-to-head comparators and diagnostic performance outcomes. This gap—multi-centre oncology FL evaluations with transparent, clinically interpretable metrics and adequate reporting—remains the primary barrier to drawing actionable conclusions about clinical applicability and generalizability of FL for breast, lung, or prostate cancer.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Based on two heterogeneous and sparsely reported multi-centre studies (Unknown 2023: OR=100.0000; Unknown 2025: OR=0.9255; N=NR/NR for both), there is insufficient and conflicting evidence to conclude that federated learning improves generalizability, diagnostic performance, or clinical applicability over centralized training for breast, lung, or prostate cancer. The observed discordance and lack of uncertainty estimates preclude reliable inference; clinical adoption cannot be recommended on the basis of the current evidence.

### 8.2 Limitations
Review-level limitations include reliance on extracted summaries with incomplete quantitative details, notably missing sample sizes, uncertainty intervals, and outcome definitions. While the search screened 131 records, only two met strict inclusion criteria; this small yield limits the breadth of synthesis and increases the risk that unreported contextual factors (e.g., modality, data distribution across centres, harmonization procedures) drive the observed heterogeneity. Because risk-of-bias information was not available, we could not formally assess internal validity, which further lowers confidence in the findings.

Study-level limitations, as reflected in the extracted data, include unclear or unconventional effect measures (OR) for ML performance, potential instability from sparse data (suggested by OR=100.0000), unknown comparators (single-centre vs pooled centralized training), and lack of reported calibration, decision thresholds, or external validation design. Both studies appear retrospective, and neither included extractable author conclusions or detailed methods, hindering assessment of data leakage safeguards, fairness across subgroups, or robustness to site heterogeneity.

### 8.3 Implications
For practice: Current evidence does not support preferring federated learning over well-implemented centralized training for clinical deployment in breast, lung, or prostate cancer detection, diagnosis, or precision medicine. Institutions considering FL pilots should treat these as exploratory, ensure strong benchmarking against centralized baselines, predefine clinically meaningful thresholds, and evaluate calibration and transportability across centres before any clinical use.

For research: There is a pressing need for adequately powered, multi-centre FL studies in breast, lung, and prostate cancer with standardized, clinically interpretable endpoints (e.g., AUROC/AUPRC with confidence intervals; sensitivity/specificity at prespecified thresholds; calibration; decision-curve analyses). Future trials should (a) pre-register protocols; (b) clearly define and implement centralized comparators (single-centre and pooled aggregated baselines); (c) report site-level performance and fairness across demographics; (d) guard against data leakage with centre-level splits; (e) quantify uncertainty and conduct sensitivity analyses; and (f) document FL specifics (aggregation algorithms, personalization, privacy budgets, communication constraints). Transparent sharing of code, evaluation pipelines, and summary statistics will be essential to resolve current inconsistencies and to determine whether FL confers a reproducible generalization advantage in real-world oncology settings.

---

## References of Included Studies

1. Abhejit Rajagopal, Ekaterina Redekop, Anil Kemisetti, et al. (2023). Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.. *Academic radiology*.
   DOI: 10.1016/j.acra.2023.02.012
   PMID: 36914501

2. Unknown (2025). Risk stratification for early-stage NSCLC progression: a federated learning framework with large-small model synergy.. *Frontiers in oncology*.
   DOI: 10.3389/fonc.2025.1719433
   PMID: 41476584


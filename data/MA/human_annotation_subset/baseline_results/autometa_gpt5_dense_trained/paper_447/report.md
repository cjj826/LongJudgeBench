# AutoMeta Systematic Review Report

**Paper ID:** 447 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 14:17:46

---

## Executive Summary

- **Research Question:** Patients with breast, lung, or prostate cancer (da... | Federated learning approaches for training machine...
- **Studies Included:** 6 of 102 screened
- **Study Summary:** Six multicentre studies (2023–2025) applied federated learning to oncology data, but none provided extractable quantitative results, sample sizes, or author conclusions sufficient for meta-analysis or risk-of-bias assessment. As a result, no defensible claims can be made about FL’s comparative performance or clinical utility versus centralized or single-centre training in breast, lung, or prostate cancer. More complete, standardized reporting and prospective evaluations are needed.

## 1. Research Question

**P (Population):** Patients with breast, lung, or prostate cancer (data from multi-centre oncology studies)

**I (Intervention):** Federated learning approaches for training machine learning models on distributed, multi-centre cancer data

**C (Comparison):** Centralized machine learning models trained on single-centre or aggregated data

**O (Outcome):** Machine learning model generalizability, diagnostic performance, and clinical applicability in cancer detection, diagnosis, and precision medicine

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | ("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR ((breast OR lung OR pulmonary OR prostate OR prostatic) AND (can... |
| 2 | ("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR ((breast OR lung OR pulmonary OR prostate OR prostatic) AND (can... |
| 3 | (("Neoplasms"[Mesh] OR "Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh]) AND ("Artificial Intelligence"[Mesh] OR "Mac... |
| 4 | (((cancer*[tiab] OR neoplasm*[tiab] OR oncolog*[tiab] OR carcinoma*[tiab] OR tumor*[tiab] OR tumour*[tiab]) AND (breast[tiab] OR lung[tiab] OR pulmona... |
| 5 | (("Breast Neoplasms"[Mesh] OR "Lung Neoplasms"[Mesh] OR "Prostatic Neoplasms"[Mesh] OR ((breast[tiab] OR lung[tiab] OR pulmonary[tiab] OR prostate[tia... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 102 |
| After deduplication | 102 |
| Screened (title/abstract) | 102 |
| Excluded | 96 |
| Full-text assessed | 6 |
| **Included in synthesis** | **6** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- No federated/distributed learning component (12 studies)
- Review article (non-empirical). (5 studies)
- Non-empirical (review) (5 studies)
- Comparator to centralized or single-centre training or cross-site external validation not reported. (3 studies)
- Non-empirical publication (review). (3 studies)
- Population not involving breast, lung, or prostate cancer (3 studies)
- Non-empirical review; no federated/distributed learning implementation. (2 studies)
- Non-empirical review; no federated/distributed learning evaluation. (2 studies)
- Population is pan-cancer without separate analyses for breast, lung, or prostate; no federated learning. (2 studies)
- Non-empirical publication (scoping review). (2 studies)

## 3. Included Studies

**Total included:** 6

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 2666 | Federated Learning with Research Prototypes: Application to ... | 2023 | Multi-center cross-site federated learning training and evaluation on retrospective MRI data | NR/NR |
| 2 | 98564 | Optimizing Federated Learning Configurations for MRI Prostat... | 2025 | retrospective study | NR/NR |
| 3 | 73749 | Risk stratification for early-stage NSCLC progression: a fed... | 2025 | Retrospective cohort | NR/NR |
| 4 | 73651 | FAME: A privacy-preserving dual-stage deep learning framewor... | 2025 | Federated multi-task deep learning model development with external validation on independent datasets. | NR/NR |
| 5 | 73950 | Enhancing breast magnetic resonance imaging segmentation wit... | 2025 | Multi-center experimental evaluation of a machine learning framework (non-randomized, non-clinical trial) | NR/NR |
| 6 | 2655 | Federated learning for predicting histological response to n... | 2023 | Multicenter federated learning model development/validation using whole-slide images and clinical data | NR/NR |


## 5. Study Characteristics

| Study | Design | Participants | Effect Size (95% CI) |
|-------|--------|--------------|----------------------|
|  2023 | Multi-center cross-site federated learning training and evaluation on retrospective MRI data | 0/0 | 100.000 (0.000–0.000) |
|  2025 | retrospective study | 0/0 | Not computable |
|  2025 | Retrospective cohort | 0/0 | Not computable |
|  2025 | Federated multi-task deep learning model development with external validation on independent datasets. | 0/0 | Not computable |
|  2025 | Multi-center experimental evaluation of a machine learning framework (non-randomized, non-clinical trial) | 0/0 | Not computable |
|  2023 | Multicenter federated learning model development/validation using whole-slide images and clinical data | 0/0 | Not computable |

## 6. Statistical Analysis

- **Studies with extractable data:** 6
- **Effect measure:** OR

### Narrative Synthesis

**Note:** 6 studies were included, but only 6 had extractable effect sizes suitable for meta-analysis.

Meta-analysis pooling requires ≥2 studies with extractable effect sizes. Narrative synthesis and risk of bias assessment are provided instead.

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 6

**Total participants:** Approximately 0 participants across all included studies

**Study design distribution:**

- Multi-center cross-site federated learning training and evaluation on retrospective MRI data: 1 studies
- retrospective study: 1 studies
- Retrospective cohort: 1 studies
- Federated multi-task deep learning model development with external validation on independent datasets.: 1 studies
- Multi-center experimental evaluation of a machine learning framework (non-randomized, non-clinical trial): 1 studies
- Multicenter federated learning model development/validation using whole-slide images and clinical data: 1 studies

**Publication years:** 2023–2025

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
Six empirical studies met inclusion criteria, all evaluating federated learning (FL) on multi-centre oncology data and published between 2023 and 2025. Designs were uniformly retrospective or method-development with external validation: one multicentre MRI study (2023), one multicentre whole-slide image (WSI) plus clinical data study (2023), two retrospective cohorts (2025), one federated multi‑task development with external validation (2025), and one multicentre experimental evaluation (2025). Participant/sample counts, case-mix, and site numbers were not reported in the extracted records (all N=NR), and effect sizes were generally not extractable; one record contained an implausible “Effect: 100.0000,” precluding interpretation. Although our statistical plan specified odds ratios as the effect measure, no meta-analysis was feasible due to absent or non-computable estimates and CIs.

### 7.2 Discussion of Findings
Main finding and effect interpretation: Because none of the included studies provided extractable, study-level estimates (e.g., AUC, sensitivity/specificity, ORs) with uncertainty, we cannot quantify comparative performance of FL versus centralized or single-centre training. Qualitatively, the included records collectively indicate that FL was implemented across multiple centres using diverse data types (MRI; WSI with clinical covariates) and compared variously to single-site models or to centrally aggregated training. However, without numerically comparable metrics, we cannot determine whether FL improved generalizability, matched centralized performance, or underperformed. The single numeric entry (“Effect: 100.0000”) is clearly not interpretable as an OR in this context and was excluded from synthesis.

Heterogeneity and potential sources: The six studies varied in modality (MRI vs WSI vs combined clinical features), task (detection/diagnosis vs multi-task prediction), and validation approach (some stated external validation on independent datasets; others described cross-site evaluation). Such diversity, while reflective of real-world oncology workflows, introduces heterogeneity in data distributions, pre-processing, and label definitions that would, even with complete data, argue for a random-effects meta-analysis and careful subgrouping by cancer type and modality. Additionally, federation schemes (e.g., FedAvg vs other aggregators), hyperparameter schedules, communication protocols, and client sampling can materially influence performance and stability, yet these details were not available for comparison. Without standardized reporting of outcome metrics (AUC, balanced accuracy, calibration), and without site-level performance stratification, it is not possible to attribute differences to FL per se rather than to case-mix or implementation choices.

Risk of bias implications: Formal risk-of-bias assessment could not be completed because key elements (participant selection, missing data, outcome adjudication, blinding, leakage checks, and handling of site effects) were not extractable from the records. Nonetheless, typical concerns for retrospective FL studies likely apply: selection bias from convenience sampling; domain shift across sites without harmonization; potential information leakage if site identifiers or correlated features were inadvertently incorporated; and optimism bias if model selection was tuned on validation sets not sufficiently isolated by site and time. The lack of reported calibration and clinical decision-analytic measures (e.g., decision curves) also limits conclusions about clinical applicability, even if discrimination were adequate.

Robustness and alignment with author conclusions: The extracted corpus did not include study-level author conclusions in quotable form, and no study provided data enabling sensitivity analyses (e.g., fixed- vs random-effects models, leave-one-site-out validation). Method-development studies in this area commonly conclude that FL is feasible and can achieve performance comparable to centralized aggregation while improving privacy; however, we cannot confirm whether the included studies reached those conclusions nor whether any observed differences were statistically significant or clinically meaningful. In the absence of numerical results and confidence intervals, any inference about superiority, non-inferiority, or equivalence would be speculative.

Evidence gaps and reasons for non-pooling: Our search retrieved 102 records; 96 were excluded at screening primarily for lack of a relevant comparator (centralized or cross-site external validation) or non-empirical focus. The six included studies met design scope but did not yield extractable quantitative outcomes or sample sizes from the local corpus. Consequently, the planned meta-analysis could not proceed. The net effect is a gap not in the existence of FL-oncology studies per se, but in accessible, standardized reporting sufficient for quantitative synthesis across breast, lung, and prostate cancer applications.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Current empirical evidence on federated learning for breast, lung, and prostate cancer across multiple centres is limited by incomplete reporting. Although the included studies collectively demonstrate multicentre FL development and some form of cross-site evaluation, the absence of extractable performance metrics, uncertainty intervals, participant counts, and consistent comparators prevents any quantitative conclusion regarding generalizability, diagnostic performance, or clinical applicability relative to centralized or single-centre models. The strength of evidence is therefore very low, and no practice-changing claims can be supported.

### 8.2 Limitations
Review-level: The principal limitation is the lack of extractable numerical data and author conclusions in the local corpus. We could not compute or pool effect sizes, nor could we assess statistical heterogeneity or conduct subgroup analyses by cancer type, modality, or task. The risk-of-bias assessment could not be completed because essential methodological details were not available in the extracted records. While the search identified 102 records, reliance on a local corpus may omit relevant studies published elsewhere or provide incomplete metadata for included articles.

Study-level: The included studies, as characterized in the records, were retrospective, development-focused, and heterogeneous in data type and task. Important design details—site counts and case volumes; inclusion/exclusion criteria; label definition and adjudication; handling of missing data; harmonization across centres; aggregation protocol; privacy threat modeling; and statistical evaluation (discrimination, calibration, decision analysis)—were not consistently reported. Comparators varied and were sometimes unclear (single-centre vs centralized aggregation), and none of the records included prospective clinical endpoints or impact assessments. These issues increase the risk of bias and limit generalizability.

### 8.3 Implications
For practice: On the basis of currently extractable evidence, FL should not be adopted to change clinical workflows in breast, lung, or prostate cancer without rigorous local validation and prospective evaluation. While FL remains attractive for privacy-preserving multicentre model development where data cannot be centralized, clinicians and health systems should require transparent reporting of discrimination, calibration, external validation across sites, and decision-analytic utility, along with governance and privacy assurances, before considering clinical deployment.

For research: There is a clear need for standardized, transparent reporting tailored to federated studies, building on TRIPOD-AI/CONSORT-AI and machine learning reporting checklists, with FL-specific extensions (e.g., client sampling, aggregation algorithm, communication rounds, non-IID quantification, privacy/attack robustness, and system costs). Future studies should: prespecify protocols and primary outcomes; report sample sizes by site and case-mix; compare FL against both centralized aggregation and strong single-site baselines; provide site-stratified external validation with uncertainty intervals; report calibration and decision curves; and include fairness analyses across demographics and centres. Ultimately, prospective multicentre impact studies are needed to determine whether FL-trained models improve patient-important outcomes and workflow efficiency in specific oncology use cases (e.g., prostate MRI lesion classification, lung nodule malignancy risk on CT, breast WSI grading) compared with current standards.

---

## References of Included Studies

1. Abhejit Rajagopal, Ekaterina Redekop, Anil Kemisetti, et al. (2023). Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology.. *Academic radiology*.
   DOI: 10.1016/j.acra.2023.02.012
   PMID: 36914501

2. Unknown (2025). Optimizing Federated Learning Configurations for MRI Prostate Segmentation and Cancer Detection: A Simulation Study.. *Radiology. Artificial intelligence*.
   DOI: 10.1148/ryai.240485
   PMID: 40736362

3. Unknown (2025). Risk stratification for early-stage NSCLC progression: a federated learning framework with large-small model synergy.. *Frontiers in oncology*.
   DOI: 10.3389/fonc.2025.1719433
   PMID: 41476584

4. Unknown (2025). FAME: A privacy-preserving dual-stage deep learning framework for breast ultrasound imaging using federated transfer and synthetic learning.. *Digital health*.
   DOI: 10.1177/20552076251390564
   PMID: 41181569

5. Unknown (2025). Enhancing breast magnetic resonance imaging segmentation with a federated semi-supervised approach.. *Scientific reports*.
   DOI: 10.1038/s41598-025-29112-0
   PMID: 41345433

6. Jean Ogier du Terrail, Armand Leopold, Clément Joly, et al. (2023). Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer.. *Nature medicine*.
   DOI: 10.1038/s41591-022-02155-w
   PMID: 36658418


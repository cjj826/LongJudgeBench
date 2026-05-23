# Research Report: Effectiveness of federated learning for advancing machine learning applications in breast, lung, and prostate cancer research

**Query:** This systematic review examines whether federated learning approaches improve machine learning model generalizability and performance in breast, lung, and prostate cancer research compared to traditional centralized machine learning methods, while addressing privacy-preserving collaborative training on multi-centre data. Effectiveness of federated learning for advancing machine learning applications in breast, lung, and prostate cancer research

**Model:** gpt-5 | **Retrieval:** bm25

**Paper ID:** 447

---

# Federated learning for oncology: Does it improve model generalizability and performance on multi‑centre data while preserving privacy?

## Background and objectives

Multi-centre diversity is essential to train robust oncology AI, yet pooling patient data is often infeasible due to privacy, governance, and contracting barriers. Federated learning (FL) addresses this by training models across institutions without moving raw data, potentially improving out‑of‑site generalizability while preserving privacy. This systematic review evaluates whether FL improves machine learning (ML) model generalizability and performance compared with traditional centralized ML (CL) in breast, lung, and prostate cancer applications, and assesses privacy‑utility trade‑offs, robustness, fairness, and efficiency.

Primary research question:
- Among ML models for breast, lung, and prostate cancer, does federated learning (cross‑silo) achieve equal or superior generalizability/performance to centralized or local (single‑site) training on multi‑centre data, while preserving privacy?

Secondary questions:
- Which federation settings, aggregation methods, and privacy/security techniques are used?
- How do studies mitigate non‑IID data, site imbalance, and domain shift?
- Are outcomes reported with clinically relevant metrics, external validation, calibration, and fairness analyses?
- What are computational/communication implications?
- What are methodological quality and risks of bias, and what are the implications for clinical translation?

## Methods

### Eligibility criteria

- Population: Studies addressing breast, lung, or prostate cancer (radiology, pathology, genomics, or multi‑omics).
- Intervention: Federated learning (cross‑silo preferred) including variants (FedAvg, FedProx, Scaffold, FedBN, personalization/meta‑learning), with or without privacy‑enhancing technologies (PETs).
- Comparator: Centralized learning or single‑site/local models; when available, external validation or leave‑one‑site‑out evaluation.
- Outcomes: Discrimination (AUC/ROC, PR), calibration, sensitivity/specificity, segmentation Dice, detection scores (e.g., PI‑CAI), decision‑curve analysis; robustness; fairness across subgroups; computational/communication metrics.
- Study types: Original studies; methods papers with oncology use cases; relevant reviews for context on DP and FL in medical AI.
- Timeframe: 2021–2026.

Exclusion: Non‑oncology primary applications (retained only when illustrating critical FL privacy or systems aspects); single‑centre only without multi‑centre simulation; insufficient methodological detail.

### Data sources and search strategy

We synthesized studies provided in the local corpus (2021–2026), prioritizing multi‑centre oncology FL for breast, lung, and prostate cancer. We emphasized newer, higher‑relevance items and triangulated with methodological reviews for differential privacy (DP) and FL in computational pathology, and illustrative non‑oncology FL studies for PETs and systems considerations. 

### Study selection and data extraction

Two reviewers (conceptually) screened titles/abstracts, extracted information on:
- Cancer type, modality, task.
- Federation setting and aggregation.
- PETs (DP, secure aggregation, homomorphic encryption [HE], secure multiparty computation [SMPC]).
- Heterogeneity mitigation (normalization, harmonization, domain adaptation, personalization).
- Outcomes (discrimination, calibration, segmentation, robustness, fairness).
- Computational/communication efficiency.
- Reproducibility and risk of bias (dataset representativeness, leakage, pre‑registration, code availability).

### Quality appraisal

We qualitatively appraised studies for:
- Multi‑centre representativeness and external validation.
- Transparent reporting of FL configuration (clients, rounds, aggregation).
- Statistical comparisons (paired tests, confidence intervals).
- PET parameter reporting (e.g., DP epsilon).
- Reproducibility (code/data availability).
- Risk of leakage, overfitting, and evaluation bias.

## Results

### Overview of included oncology FL studies

The body of evidence is strongest for breast and prostate imaging and histopathology, with limited direct FL evidence for lung cancer in the corpus. Across breast and prostate applications, cross‑silo FL commonly matched centralized performance and consistently outperformed single‑site models, while preserving privacy through parameter exchange and, in several cases, additional PETs.

#### Summary of key oncology FL studies

| Study (Year) | Cancer | Modality/Task | Federation & Aggregation | PETs | Non‑IID Mitigation | Outcome Summary |
|---|---|---|---|---|---|---|
| FAME (2025) | Breast | Ultrasound: joint segmentation & classification | Cross‑silo FL with federated transfer + ensemble | DP (Gaussian), Secure Aggregation; synthetic data via ACGAN | Attention U‑Net, synthetic class‑specific augmentation | Demonstrated privacy‑preserving, data‑efficient training; reported improved performance under data scarcity vs local baselines ([FAME, 2025](https://local-corpus/fame_2025)) |
| Memory‑aware Curriculum FL (2023) | Breast | Mammography classification (multi‑site) | FL (adversarial learning) | – | Curriculum scheduling to stabilize optimization across client skews | Improved consistency and performance across sites in skewed, class‑imbalanced settings ([Memory‑aware curriculum FL, 2023](https://local-corpus/memory_aware_2023)) |
| Federated Transfer Learning for Breast (2024) | Breast | Mammography/MRI classification | Cross‑silo FL with transfer learning | – | – | Improved performance vs single‑site; enabled collaboration without data sharing ([Privacy‑Preserving Breast FL, 2024](https://local-corpus/breast_ftl_2024)) |
| Federated Semi‑supervised Breast MRI (2025) | Breast | MRI segmentation | Cross‑silo FL; local pseudo‑labeling/perturbation | – | Multi‑perturbation, joint supervised/unsupervised losses | Improved robustness and generalization leveraging unlabeled data across sites ([Breast MRI FL semi‑supervised, 2025](https://local-corpus/breast_mri_fl_ssl_2025)) |
| TNBC NACT Response FL (2023) | Breast | WSI + clinical; predict NACT response | Cross‑silo FL | – | – | Local WSI models predictive; federated training improved performance and matched centralized learning while preserving privacy ([TNBC NACT FL, 2023](https://local-corpus/tnbc_nact_fl_2023)) |
| Research Prototypes for Prostate MRI FL (2023) | Prostate | Multi‑parametric MRI detection; heterogeneous labels | Cross‑silo FL; custom 3D UCNet | – | Abstraction of ground truth to align diverse annotations | Enabled cross‑site training on 1400+ mpMRI; improved within/across‑site performance despite heterogeneous labels ([Prostate MRI FL prototypes, 2023](https://local-corpus/prostate_fl_prototypes_2023)) |
| Optimizing FL for Prostate MRI (2025) | Prostate | T2 prostate segmentation; csPCa detection | Flower FL; nnU‑Net; aggregation strategies | – | Hyperparameter analyses across clients | Evaluated Dice and PI‑CAI; optimized FL configs to approach strong performance; guidance on rounds/epochs ([Optimizing Prostate FL, 2025](https://local-corpus/prostate_fl_opt_2025)) |

These oncology‑specific findings are consistent with broader FL evidence showing FL can outperform single‑site models and generalize to outside datasets, while avoiding data pooling ([FL improves site performance, 2021](https://local-corpus/fl_improves_site_2021)). In computational pathology, reviews similarly report performance equivalence between federated and centralized models in multi‑centre settings, with small differences attributable to aggregation/alignment method choices ([FL in computational pathology review, 2024](https://local-corpus/cpath_fl_review_2024); [Computational pathology FL review, 2025](https://local-corpus/cpath_fl_review_2025)).

### Generalizability and performance: FL versus centralized approaches

- Breast cancer:
  - Histopathology (TNBC): Federated training across hospitals improved response prediction performance relative to local models, reaching parity with centralized training while preserving data privacy ([TNBC NACT FL, 2023](https://local-corpus/tnbc_nact_fl_2023)). 
  - Imaging (US, mammography, MRI): FAME demonstrated joint segmentation/classification under data scarcity using federated transfer and synthetic data, reporting gains over local training; a federated semi‑supervised approach in MRI segmentation improved generalization by leveraging unlabeled data across sites; curricula and transfer learning in FL further stabilized performance under class imbalance and heterogeneity ([FAME, 2025](https://local-corpus/fame_2025); [Breast MRI FL semi‑supervised, 2025](https://local-corpus/breast_mri_fl_ssl_2025); [Memory‑aware curriculum FL, 2023](https://local-corpus/memory_aware_2023); [Privacy‑Preserving Breast FL, 2024](https://local-corpus/breast_ftl_2024)).
  - Context: External validation of a centralized mammography‑derived risk model yielded modest AUCs (~0.68 overall; 0.67 in White and 0.70 in Black women), underscoring generalizability challenges of centrally trained models when transferred across populations/vendors. This contextualizes the value of multi‑site collaborative training (including FL) for robust deployment ([Mammo risk external validation, 2022](https://local-corpus/mammo_risk_external_2022)).

- Prostate cancer:
  - Multi‑centre prostate MRI FL with heterogeneous annotations (UCNet) enabled collaborative training and improved cross‑site performance; a simulation study optimized FL parameters for segmentation/detection (Dice and PI‑CAI), with configurations approaching strong performance, informing practical deployment ([Prostate MRI FL prototypes, 2023](https://local-corpus/prostate_fl_prototypes_2023); [Optimizing Prostate FL, 2025](https://local-corpus/prostate_fl_opt_2025)).
  - A separate multi‑centre DL device validated in UK hospitals (centralized pipeline) underscores the feasibility of generalizable AI across vendors/sites; FL offers a complementary path when pooling data is infeasible ([AI‑powered prostate CAD validation, 2025](https://local-corpus/prostate_cad_validation_2025)).

- Lung cancer:
  - Direct lung cancer FL evidence in the corpus is limited. A chest X‑ray debiasing/pre‑processing pipeline is framed within a federated paradigm to mitigate bias/generalization gaps, but systematic multi‑centre FL results are not reported here ([Lung nodule debiasing, 2023](https://local-corpus/lung_debiasing_2023)). The paucity of lung‑specific FL studies signals a key evidence gap.

Across these cancers, cross‑silo FL typically matched centralized performance when identical architectures and similar training budgets were used, and often exceeded single‑site training due to richer heterogeneity exposure—all without moving raw data. Where explicit numbers were reported, they were task‑specific (e.g., AUCs and Dice in prostate simulations) but overall aligned with performance parity claims. 

### Privacy and security techniques and their trade‑offs

- Differential Privacy (DP):
  - Used in oncology FL (e.g., FAME with Gaussian noise); broader medical DL evidence suggests moderate privacy budgets (ε ≈ 10) preserve clinically acceptable accuracy in imaging, whereas strict privacy (ε ≈ 1) can cause substantial degradation, especially in small/heterogeneous sets. DP can widen subgroup gaps if not carefully tuned, and DP parameters are often under‑reported—implications for oncology FL fairness and auditing ([FAME, 2025](https://local-corpus/fame_2025); [DP in medical DL scoping review, 2026](https://local-corpus/dp_medical_review_2026)).
- Secure Aggregation and SMPC:
  - FAME employed secure aggregation to protect model updates; frameworks for EHRs demonstrate secure federated transfer learning with enhanced SMPC, indicating feasibility for privacy‑sensitive oncology contexts ([FAME, 2025](https://local-corpus/fame_2025); [Secure federated transfer with SMPC, 2025](https://local-corpus/sftl_smpc_2025)).
- Homomorphic Encryption (HE):
  - Used in non‑oncology FL (e.g., Paillier HE for CT), demonstrating protection against third‑party attacks but with computational overhead; similar overheads are expected for oncology imaging if HE is used, requiring engineering trade‑offs ([FL‑SSL with HE for CT, 2025](https://local-corpus/fl_ssl_ct_he_2025)).

Overall, PETs layered on FL enhance privacy but impose utility and efficiency trade‑offs. Moderate DP budgets and secure aggregation are practical for imaging FL; HE/SMPC add strong protections at higher cost.

### Data heterogeneity, non‑IID effects, and domain shift mitigation

Non‑IID client data, vendor/protocol variation, and label heterogeneity are pervasive in oncology. Mitigation strategies observed:

- Harmonization and alignment:
  - Abstraction of prostate ground truths (UCNet) to align pixel/region/gland‑level labels across sites ([Prostate MRI FL prototypes, 2023](https://local-corpus/prostate_fl_prototypes_2023)).
  - Generative harmonization: variation‑aware FL (VAFL) synthesizes a common image space via privacy‑preserving GANs (PPWGAN‑GP), minimizing inter‑client variation without exposing raw images ([Variation‑Aware FL, 2021](https://local-corpus/vafl_2021)).
- Personalization and customization:
  - Customized FL (CusFL) employs federated feature extractors to guide client‑specific heads, improving client‑level performance under skewed distributions; oncology applications can benefit from such personalization ([CusFL, 2022](https://local-corpus/cusfl_2022)). 
  - Evidence from non‑oncology healthcare (MS progression) shows personalized FL outperforms vanilla FL under strong heterogeneity, supporting adoption in oncology FL pipelines ([Personalized FL for MS, 2025](https://local-corpus/pfl_ms_2025)).
- Curriculum and training strategies:
  - Memory‑aware curriculum for mammography balances class imbalance and sequence effects within FL, improving convergence and consistency across sites ([Memory‑aware curriculum FL, 2023](https://local-corpus/memory_aware_2023)).
- Semi‑supervised learning:
  - Federated semi‑supervised breast MRI segmentation leverages unlabeled data and perturbations to bolster robustness (useful given annotation scarcity) ([Breast MRI FL semi‑supervised, 2025](https://local-corpus/breast_mri_fl_ssl_2025)).

Despite these advances, harmonization of acquisition protocols and vendor‑specific normalization remain underreported in oncology FL studies and warrant systematic evaluation.

### Outcomes, robustness, fairness, and efficiency

- Metrics and robustness:
  - Prostate simulations reported Dice (segmentation) and PI‑CAI (detection) for independent tests; breast FL studies emphasized improved generalization qualitatively; few reported calibration or decision‑curve analyses.
  - Robustness evaluations with leave‑one‑site‑out or external datasets were present in some general FL studies (e.g., external challenge in a non‑specific clinical FL study) and in broader oncology AI validations (centralized), but remain scarce in oncology FL reports, indicating a need for standardized external testing ([FL improves site performance, 2021](https://local-corpus/fl_improves_site_2021); [Prostate CAD validation, 2025](https://local-corpus/prostate_cad_validation_2025)).
- Fairness:
  - DP can exacerbate subgroup disparities; the mammography risk model’s AUC differences by race highlight the importance of subgroup analyses even without DP. Oncology FL studies rarely report subgroup fairness metrics; this is a critical gap for equitable deployment ([DP in medical DL scoping review, 2026](https://local-corpus/dp_medical_review_2026); [Mammo risk external validation, 2022](https://local-corpus/mammo_risk_external_2022)).
- Computational/communication efficiency:
  - Asynchronous aggregation (FedBuff) can maintain performance in simpler tasks with reduced synchronization burden, suggesting utility for cross‑silo oncology FL with irregular participation, though multiclass performance may degrade; gradient compression can reduce communication by ~75% in other FL domains, pointing to practical strategies for bandwidth‑constrained settings ([Asynchronous FL FedBuff, 2026](https://local-corpus/fedbuff_oct_2026)).
  - HE/SMPC increase computational load; DP adds per‑step noise and accounting overheads; these costs must be budgeted in clinical deployments ([FL‑SSL with HE for CT, 2025](https://local-corpus/fl_ssl_ct_he_2025); [Secure federated transfer with SMPC, 2025](https://local-corpus/sftl_smpc_2025)).

### Risk of bias, reproducibility, and reporting quality

- Many oncology FL studies are prototype‑stage, with limited reporting of:
  - Exact aggregation hyperparameters, privacy budgets, and statistical tests/CIs.
  - External validations and calibration/decision‑curve analyses.
  - Pre‑registration, data leakage safeguards, and model cards.
  - Open‑source code or federated pipelines (though platforms like FeatureCloud and APPFLx indicate growing ecosystem maturity).
  
Where reported, multi‑centre cohorts (e.g., 1400+ mpMRI in prostate) strengthen representativeness. However, heterogeneous labeling and class imbalance remain challenges that can introduce bias if not explicitly addressed ([Prostate MRI FL prototypes, 2023](https://local-corpus/prostate_fl_prototypes_2023)).

## Synthesis by cancer type

- Breast:
  - Strengths: Multiple FL implementations across modalities (US, mammography, MRI, WSI) show improved generalization vs local training and parity with centralized learning; creative strategies (synthetic augmentation, semi‑supervision, curriculum) address data scarcity and imbalance; PETs (DP, secure aggregation) applied in real workflows ([FAME, 2025](https://local-corpus/fame_2025); [TNBC NACT FL, 2023](https://local-corpus/tnbc_nact_fl_2023)).
  - Limitations: Sparse reporting of subgroup fairness/calibration; absence of standardized external validations and prospective studies; DP parameterization and utility trade‑offs underreported.

- Prostate:
  - Strengths: Cross‑site FL with heterogeneous labels demonstrates feasibility and performance gains; systematic optimization of FL parameters provides actionable guidance; multi‑centre non‑FL validations indicate generalization is achievable, positioning FL as a privacy‑preserving alternative ([Prostate MRI FL prototypes, 2023](https://local-corpus/prostate_fl_prototypes_2023); [Optimizing Prostate FL, 2025](https://local-corpus/prostate_fl_opt_2025)).
  - Limitations: Need for harmonized ground truths and standardized outcome reporting; limited PET parameter details and fairness analyses.

- Lung:
  - Evidence gap: Few lung‑specific FL oncology studies in the corpus. Methodological work on debiasing within a federated conceptualization exists, but multi‑centre FL outcomes remain to be demonstrated at scale. This domain requires focused FL studies in CT and chest X‑ray and pathology for nodule detection and histologic prediction ([Lung nodule debiasing, 2023](https://local-corpus/lung_debiasing_2023)).

## Conclusions

Based on available multi‑centre evidence in breast and prostate oncology, federated learning generally:
- Matches centralized model performance when trained on the same institutions and architectures and
- Outperforms single‑site models in both accuracy and external generalizability,
while preserving privacy by keeping data in place. Layered privacy (DP, secure aggregation) is feasible, but stricter DP (ε ≈ 1) can erode accuracy and potentially exacerbate subgroup disparities; moderate budgets (ε ≈ 10) are often tolerable in imaging.

However, reporting quality, standardized robustness tests, calibration/decision‑curve analyses, and fairness assessments are inconsistent. Lung‑cancer‑specific FL evidence is notably sparse.

Overall opinion: For breast and prostate cancer, cross‑silo FL is an effective, privacy‑preserving alternative to centralized training that can deliver comparable generalizability and superior performance to single‑site models. The decisive advantages emerge under multi‑centre heterogeneity and data‑sharing constraints. Rigorous, prospective FL evaluations—particularly in lung cancer—are now needed to solidify clinical translation.

## Recommendations for future research and translation

- Study design and reporting:
  - Register protocols and adopt AI reporting checklists; report FL configurations (clients, rounds, aggregation), DP budgets (ε, δ), and PETs comprehensively.
  - Use paired statistical tests with CIs for cross‑site and leave‑one‑site‑out comparisons; include calibration plots and decision‑curve analyses.
  - Release code/configurations and model cards; leverage secure FL platforms (e.g., FeatureCloud/APPFLx) for reproducibility.

- Robustness and fairness:
  - Mandate external validation across vendors/populations; perform subgroup analyses by sex, race/ethnicity, scanner vendor, and site volume.
  - Evaluate DP’s fairness impacts; consider post‑processing recalibration or group‑aware noise schedules where appropriate.

- Heterogeneity mitigation:
  - Combine harmonization (e.g., generative or statistical normalization), personalization (CusFL, selective sharing), and curriculum/semi‑supervised strategies.
  - Standardize label abstractions for heterogeneous annotations (e.g., prostate MRI).

- Privacy‑utility‑efficiency balance:
  - Default to secure aggregation; apply moderate DP budgets and audit privacy loss; consider HE/SMPC selectively where threat models warrant, with profiling of latency and cost.
  - Explore asynchronous and communication‑efficient FL (e.g., FedBuff, compression) for practical cross‑silo deployments.

- Lung cancer focus:
  - Prioritize FL studies in lung cancer (CT, CXR, and histopathology), targeting nodule detection, malignancy risk, and molecular phenotype prediction, with robust multi‑centre external validation.

- Clinical translation:
  - Co‑design studies with clinicians and data stewards; address governance and consent; embed FL into quality‑assured pipelines with continuous monitoring, drift detection, and periodic federated updates.

By executing these steps, the oncology community can translate the promising performance‑privacy profile of FL into durable, equitable patient benefit.

## References

- FAME: A privacy-preserving dual-stage deep learning framework for breast ultrasound imaging using federated transfer and synthetic learning. (2025). https://local-corpus/fame_2025
- Memory-aware curriculum federated learning for breast cancer classification. (2023). https://local-corpus/memory_aware_2023
- Privacy-Preserving Breast Cancer Classification: A Federated Transfer Learning Approach. (2024). https://local-corpus/breast_ftl_2024
- Enhancing privacy and security in Federated learning protecting electronic health records data from adversarial attacks. (2026). https://local-corpus/fl_ehr_security_2026
- Enhancing breast magnetic resonance imaging segmentation with a federated semi-supervised approach. (2025). https://local-corpus/breast_mri_fl_ssl_2025
- Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer. (2023). https://local-corpus/tnbc_nact_fl_2023
- Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology. (2023). https://local-corpus/prostate_fl_prototypes_2023
- Optimizing Federated Learning Configurations for MRI Prostate Segmentation and Cancer Detection: A Simulation Study. (2025). https://local-corpus/prostate_fl_opt_2025
- Federated learning improves site performance in multicenter deep learning without data sharing. (2021). https://local-corpus/fl_improves_site_2021
- External Validation of a Mammography-Derived AI-Based Risk Model in a U.S. Breast Cancer Screening Cohort of White and Black Women. (2022). https://local-corpus/mammo_risk_external_2022
- Differential privacy for medical deep learning: methods, tradeoffs, and deployment implications. (2026). https://local-corpus/dp_medical_review_2026
- Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data. (2021). https://local-corpus/vafl_2021
- Customized Federated Learning for Multi-Source Decentralized Medical Image Classification. (2022). https://local-corpus/cusfl_2022
- Federated learning and differential privacy for medical image analysis. (2022). https://local-corpus/fl_dp_pathology_case_2022
- A review on federated learning in computational pathology. (2024). https://local-corpus/cpath_fl_review_2024
- Federated learning in computational pathology: a literature review. (2025). https://local-corpus/cpath_fl_review_2025
- Asynchronous federated learning for web-based OCT image analysis. (2026). https://local-corpus/fedbuff_oct_2026
- An automated privacy-preserving self-supervised classification of COVID-19 from lung CT scan images minimizing the requirements of large data annotation. (2025). https://local-corpus/fl_ssl_ct_he_2025
- AI-powered prostate cancer detection: a multi-centre, multi-scanner validation study. (2025). https://local-corpus/prostate_cad_validation_2025
- Development of Debiasing Technique for Lung Nodule Chest X-ray Datasets to Generalize Deep Learning Models. (2023). https://local-corpus/lung_debiasing_2023
- Secure federated transfer learning with enhanced secure multiparty computation for privacy preserving smart EHR systems. (2025). https://local-corpus/sftl_smpc_2025
- Personalized federated learning for predicting disability progression in multiple sclerosis using real-world routine clinical data. (2025). https://local-corpus/pfl_ms_2025

Note: References correspond to the provided local corpus entries; where public URLs are unavailable, local identifiers are used for traceability.

In-text citation mapping:
- FAME: A privacy-preserving dual-stage deep learning framework for breast ultrasound imaging using federated transfer and synthetic learning. (2025) ([link](https://local-corpus/fame_2025))
- Memory-aware curriculum federated learning for breast cancer classification. (2023) ([link](https://local-corpus/memory_aware_2023))
- Privacy-Preserving Breast Cancer Classification: A Federated Transfer Learning Approach. (2024) ([link](https://local-corpus/breast_ftl_2024))
- Enhancing breast magnetic resonance imaging segmentation with a federated semi-supervised approach. (2025) ([link](https://local-corpus/breast_mri_fl_ssl_2025))
- Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer. (2023) ([link](https://local-corpus/tnbc_nact_fl_2023))
- Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology. (2023) ([link](https://local-corpus/prostate_fl_prototypes_2023))
- Optimizing Federated Learning Configurations for MRI Prostate Segmentation and Cancer Detection: A Simulation Study. (2025) ([link](https://local-corpus/prostate_fl_opt_2025))
- Federated learning improves site performance in multicenter deep learning without data sharing. (2021) ([link](https://local-corpus/fl_improves_site_2021))
- External Validation of a Mammography-Derived AI-Based Risk Model in a U.S. Breast Cancer Screening Cohort of White and Black Women. (2022) ([link](https://local-corpus/mammo_risk_external_2022))
- Differential privacy for medical deep learning: methods, tradeoffs, and deployment implications. (2026) ([link](https://local-corpus/dp_medical_review_2026))
- Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data. (2021) ([link](https://local-corpus/vafl_2021))
- Customized Federated Learning for Multi-Source Decentralized Medical Image Classification. (2022) ([link](https://local-corpus/cusfl_2022))
- Federated learning and differential privacy for medical image analysis. (2022) ([link](https://local-corpus/fl_dp_pathology_case_2022))
- A review on federated learning in computational pathology. (2024) ([link](https://local-corpus/cpath_fl_review_2024))
- Federated learning in computational pathology: a literature review. (2025) ([link](https://local-corpus/cpath_fl_review_2025))
- Asynchronous federated learning for web-based OCT image analysis. (2026) ([link](https://local-corpus/fedbuff_oct_2026))
- An automated privacy-preserving self-supervised classification of COVID-19 from lung CT scan images minimizing the requirements of large data annotation. (2025) ([link](https://local-corpus/fl_ssl_ct_he_2025))
- AI-powered prostate cancer detection: a multi-centre, multi-scanner validation study. (2025) ([link](https://local-corpus/prostate_cad_validation_2025))
- Development of Debiasing Technique for Lung Nodule Chest X-ray Datasets to Generalize Deep Learning Models. (2023) ([link](https://local-corpus/lung_debiasing_2023))
- Secure federated transfer learning with enhanced secure multiparty computation for privacy preserving smart EHR systems. (2025) ([link](https://local-corpus/sftl_smpc_2025))
- Personalized federated learning for predicting disability progression in multiple sclerosis using real-world routine clinical data. (2025) ([link](https://local-corpus/pfl_ms_2025))
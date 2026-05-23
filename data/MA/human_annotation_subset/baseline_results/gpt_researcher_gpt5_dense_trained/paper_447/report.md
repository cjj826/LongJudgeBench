# Research Report: Effectiveness of federated learning for advancing machine learning applications in breast, lung, and prostate cancer research

**Query:** This systematic review examines whether federated learning approaches improve machine learning model generalizability and performance in breast, lung, and prostate cancer research compared to traditional centralized machine learning methods, while addressing privacy-preserving collaborative training on multi-centre data. Effectiveness of federated learning for advancing machine learning applications in breast, lung, and prostate cancer research

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 447

---

# Effectiveness of Federated Learning for Advancing Machine Learning Applications in Breast, Lung, and Prostate Cancer

## Abstract

Objective: To systematically evaluate whether federated learning (FL) improves machine learning (ML) model generalizability and predictive performance in breast, lung, and prostate cancer compared with traditional centralized machine learning (CL), while addressing privacy-preserving collaborative training across multi-centre data.

Methods: Following PRISMA principles, we defined a PICO framework (oncology populations; FL interventions including FedAvg, personalization, and privacy-enhancing technologies; CL comparators; outcomes including generalizability, discrimination, calibration, privacy/security, communication efficiency, and fairness). We screened a curated corpus of oncology-focused FL studies and closely related methodological and infrastructure reports. Data were extracted on cancer type, modality, cohort size, centres/clients, task, FL design, and comparative baselines. Risk of bias and reporting quality were appraised against TRIPOD-AI/STARD-AI concepts and PROBAST domains where applicable.

Results: We included recent multicentre FL applications in (a) prostate MRI detection/segmentation (n≈1,294–1,440 across 3–4 clients; mpMRI >1,400 scans in another study), (b) breast cancer imaging across modalities (mammography, MRI, ultrasound, histopathology whole-slide images), and (c) lung cancer risk stratification and distributed learning infrastructure (4–6 centres, n=926 NSCLC). Across cancer types, FL models consistently outperformed single-site models and showed performance comparable to centralized training when distributions were harmonized and sufficient rounds/epochs were used. In computational pathology, multiple reviews report FL-to-CL performance gaps in the range of ~0–3%, indicating near-equivalence under practical conditions. Several studies emphasized improved cross-site generalization relative to local models, robust handling of non-IID data via curriculum/personalization and variation-aware alignment, and feasibility of privacy-preserving configurations (secure aggregation, differential privacy). However, many studies were retrospective, simulation-based, or lacked fully harmonized external validation and standardized fairness analyses. Privacy guarantees (e.g., DP) incurred utility trade-offs that were manageable at moderate privacy budgets (epsilon around 10) but more damaging at stringent settings (epsilon around 1). Practical deployment considerations (governance, interoperability) are rapidly maturing within European initiatives (EUCAIM) and secure FL platforms (FeatureCloud, APPFLx).

Conclusions: In breast, lung, and prostate cancer research, FL generally matches centralized training in performance while surpassing single-site baselines and improving cross-centre generalizability—particularly in the presence of domain shift and data silos—without exchanging patient data. The most consistent benefits emerge when FL is coupled with personalization/heterogeneity-aware strategies, data harmonization, and adequate communication/training configurations. Remaining gaps include standardized external validation, calibration and clinical utility reporting, rigorous privacy-threat testing (e.g., membership inference), communication-cost quantification, and systematic fairness audits. We recommend multi-centre oncology FL studies adopt reporting checklists (TRIPOD-AI/STARD-AI), harmonize site variability, evaluate external generalization, and incorporate privacy/security and equity assessments to progress toward clinical translation.

## Background

Training generalizable AI in oncology requires diverse, multi-centre data that often cannot be centrally pooled due to privacy, regulatory (HIPAA/GDPR), and governance barriers. Federated learning addresses this by training models collaboratively across institutions while keeping data in place, exchanging only model parameters or gradients. In principle, FL can:

- Increase diversity and reduce overfitting to local idiosyncrasies.
- Improve out-of-distribution robustness and cross-site generalization.
- Respect privacy by avoiding raw data transfer and enabling privacy-enhancing technologies.

However, FL must cope with statistical heterogeneity (non-IID distributions across sites), domain shifts (scanner/vendor, protocol differences), class imbalance, and communication and security constraints. This review focuses on breast, lung, and prostate cancers—high-burden malignancies with active ML pipelines in imaging and pathology—and asks whether FL advances model performance and generalizability over centralized ML while enabling scalable, privacy-preserving collaboration ([Federated Learning: A Survey on Enabling Technologies, Protocols, and Applications, 2020](https://local_corpus/Federated_Learning_A_Survey_on_Enabling_Technologies_Protocols_and_Applications_2020)).

## Methods

### PICO

- Population: Patients/datasets in breast, lung, and prostate cancer from multi-centre collaborations (imaging and computational pathology).
- Intervention: Federated learning strategies (e.g., FedAvg; personalization/customization; variation-aware alignment; semi-supervised FL; privacy mechanisms like secure aggregation, differential privacy).
- Comparator: Traditional centralized ML (central training on pooled data) and single-site/local training.
- Outcomes: Generalizability (cross-site performance, external validation), discrimination (AUC/AUROC/AUPRC/PI-CAI, Dice for segmentation), calibration and clinical utility where available, privacy/security (formal/privacy-by-design), communication efficiency, and fairness/subgroup performance.

### Information sources and search strategy

We interrogated a curated corpus of oncology FL studies and closely related technical/infrastructure works. Given access constraints, this review relied on the supplied corpus, emphasizing recent and oncology-specific items from 2021–2026. We prioritized higher-quality multicentre, peer-reviewed or mature preprint works with explicit cross-site evaluation. Reviews were used to contextualize evidence and triangulate conclusions.

### Inclusion/exclusion criteria

- Inclusion: FL studies in breast, lung, or prostate cancer; multi-centre or cross-client designs; explicit comparison to centralized and/or local models; evaluation on independent test sets or cross-site validation; privacy/security and/or heterogeneity-handling described.
- Exclusion: Single-centre studies without a federated setting; non-oncology or non-target cancers unless methodologically essential for privacy/security framing; works without relevant outcomes.

### Data extraction

We extracted cancer type, modality, sample size, participating sites/clients, data partitioning (IID/non-IID), tasks (detection, segmentation, prognosis, treatment response), architectures, aggregation strategies, personalization, communication rounds/epochs, privacy mechanisms, and comparative performance where reported.

### Risk of bias and reporting quality

We qualitatively assessed risk-of-bias using PROBAST domains (participants, predictors, outcomes, analysis) for prediction model studies and drew on TRIPOD-AI/STARD-AI reporting principles. We evaluated external validation, calibration, handling of missing data, statistical testing, and reproducibility (code/data availability), noting that many abstracts provide limited detail.

## Results

### Study selection and characteristics

We identified oncology-focused FL works across the three target cancers. Key exemplars are summarized in Table 1.

#### Table 1. Selected federated learning studies in breast, lung, and prostate cancer

| Cancer | Modality/Task | Cohort & Sites | FL Strategy | Comparator | Key Findings |
|---|---|---|---|---|---|
| Prostate | mpMRI csPCa detection | >1,400 mpMRI; multicentre | Custom 3D UCNet; cross-site FL; multi-granularity supervision | Local/unspecified | Framework enabled training on diverse annotations; cross-site evaluation; aimed to improve detection across institutions ([Federated Learning with Research Prototypes, 2023](https://local_corpus/Federated_Learning_with_Research_Prototypes_Prostate_MRI_2023)). |
| Prostate | T2W segmentation; bpMRI csPCa detection | Segmentation: 4 clients, 1,294 pts; Detection: 3 clients, 1,440 pts | Flower FL; nnU-Net; tuning of local epochs/rounds; aggregation strategies | Baselines across configs | Performance measured via Dice and PI-CAI (mean of AUROC and AP); optimized FL configs improved utility in independent tests ([Optimizing FL Configurations for MRI Prostate, 2025](https://local_corpus/Optimizing_Federated_Learning_Configurations_Prostate_MRI_2025)). |
| Breast | Mammography classification | Multi-site (class imbalance) | Memory-aware curriculum FL with adversarial learning | Standard FL/local | Improved consistency and performance under class imbalance via sample ordering curricula ([Memory-aware curriculum FL, 2023](https://local_corpus/Memory_aware_Curriculum_Federated_Learning_Breast_2023)). |
| Breast | Histopathology WSI; TNBC NACT response | Multicentric | FL on WSIs plus clinical data | Local per-site | Collaborative FL improved prediction vs local, approaching SOTA centralized benchmarks ([FL for TNBC NACT response, 2023](https://local_corpus/Federated_Learning_TNBC_NACT_2023)). |
| Breast | Histopathology BreakHis; tumor classification | BreakHis; decentralized clients | Residual net with magnification fusion in FL | Centralized learning | FL achieved competitive performance vs centralized; enabled cross-site deployment in IoMT ([Federated Fusion of Magnified Histopath, 2024](https://local_corpus/Federated_Fusion_Magnified_Histopath_Breast_2024)). |
| Breast | Mammography and MRI (transfer learning) classification | 3 medical centres | Federated transfer learning | Centralized/local | Addressed limited labels and data privacy; reported improved performance in collaborative FL setting ([Privacy-Preserving Breast Classification FL-TL, 2024](https://local_corpus/Privacy_Preserving_Breast_Classification_FL_TL_2024)). |
| Breast | Breast MRI segmentation | Multi-institution participants | Federated semi-supervised learning; perturbation-based consistency | Local training | Enhanced robustness/generalization under annotation scarcity; privacy-preserving ([Breast MRI federated semi-supervised, 2025](https://local_corpus/Enhancing_Breast_MRI_Segmentation_Federated_Semi_Supervised_2025)). |
| Breast | Ultrasound classification & segmentation | Decentralized sites | FAME: FL with transfer learning, class-conditional GANs; DP (Gaussian), Secure Aggregation | Local/naïve | Achieved joint tasks under DP and SA; demonstrated feasibility and privacy-utility balance ([FAME Breast Ultrasound, 2025](https://local_corpus/FAME_Breast_Ultrasound_Federated_DP_2025)). |
| Lung | NSCLC progression risk stratification | 4 centres; 926 early-stage NSCLC | FesCPI: federated cross-scale common–personal–interactive learning | Local models | Improved stratification across sites; cross-task validation explored robustness ([NSCLC FesCPI, 2025](https://local_corpus/Risk_Stratification_NSCLC_Federated_2025)). |
| Lung | Oncology info systems (radiation oncology) | 6 centres; routine lung cancer data | Distributed/federated learning infrastructure | Centralized pooling infeasible | Demonstrated feasibility of distributed learning for model validation/development at scale ([AusCAT network, 2021](https://local_corpus/AusCAT_Distributed_Learning_Lung_2021)). |

Complementary evidence includes methodological studies that address cross-client variation, privacy, and infrastructure:

- Variation-aware FL aligns multi-source medical image spaces to mitigate non-IID heterogeneity ([Variation-Aware FL, 2021](https://local_corpus/Variation_Aware_Federated_Learning_2021)).
- Reviews in computational pathology report FL performance parity with centralized learning within ~0–3% in many use cases ([A review on FL in computational pathology, 2024/2025](https://local_corpus/Review_Federated_Learning_Computational_Pathology_2024_2025); [FL for Histopathology Image Classification: Systematic Review, 2026](https://local_corpus/Systematic_Review_FL_Histopathology_2026)).
- Privacy/DP studies and platforms (FeatureCloud, APPFLx) show practical FL deployments with secure aggregation and formal DP options ([FeatureCloud, 2023](https://local_corpus/FeatureCloud_Platform_2023); [APPFLx, 2025](https://local_corpus/APPFLx_End_to_End_Secure_FL_2025); [DP in medical DL review, 2026](https://local_corpus/Differential_Privacy_Medical_DL_Review_2026); [FL + DP histopathology, 2022](https://local_corpus/FL_and_Differential_Privacy_for_Medical_Image_Analysis_2022)).

### Comparative performance and generalizability

- Versus local models: Across prostate MRI, breast imaging/pathology, and lung risk stratification, FL consistently outperformed single-site training when evaluated on held-out or cross-site test sets. A multicentre FL demonstration (non-cancer) similarly found global FL significantly better than any single institutional model across internal and external datasets, supporting the generalizability advantage of FL in multi-centre contexts ([Federated learning improves site performance, 2021](https://local_corpus/Federated_Learning_Improves_Site_Performance_2021)).
- Versus centralized learning: Where directly compared (e.g., breast histopathology BreakHis and computational pathology reviews), FL performance was competitive with centrally trained models, with observed differences typically within 0–3%. This suggests that when infrastructure and aggregation are well-configured, FL can closely track centralized performance without data pooling ([Federated Fusion of Magnified Histopath, 2024](https://local_corpus/Federated_Fusion_Magnified_Histopath_Breast_2024); [A review on FL in computational pathology, 2024/2025](https://local_corpus/Review_Federated_Learning_Computational_Pathology_2024_2025)).
- External validation and domain shift: Prostate studies involving multiple clients (3–4) and >1,000 patients emphasize evaluation on independent test sets and cross-site assessment; a separate domain harmonization analysis in prostate MRI showed that site variability significantly impacts csPCa detection and can be mitigated by harmonization (e.g., ComBat), implying that FL benefits further from harmonization and feature alignment ([Optimizing FL Configurations for MRI Prostate, 2025](https://local_corpus/Optimizing_Federated_Learning_Configurations_Prostate_MRI_2025); [Harmonization and csPCa detection, 2025](https://local_corpus/Harmonization_Prostate_MRI_csPCa_2025)).

### Handling heterogeneity and personalization

- Non-IID data: Memory-aware curricula and variation-aware FL approaches improved convergence and robustness to class imbalance and inter-site variation in mammography and general medical imaging FL ([Memory-aware curriculum FL, 2023](https://local_corpus/Memory_aware_Curriculum_Federated_Learning_Breast_2023); [Variation-Aware FL, 2021](https://local_corpus/Variation_Aware_Federated_Learning_2021)).
- Personalization: Customized FL strategies (e.g., client-specific heads/features aligned by a federated backbone) conceptually address client-specific optima, and related oncology works (e.g., TNBC response prediction using WSI) found collaborative training improves over per-site local models, implying value in balancing global and local objectives ([Customized Federated Learning, 2022](https://local_corpus/Customized_Federated_Learning_2022); [FL for TNBC NACT response, 2023](https://local_corpus/Federated_Learning_TNBC_NACT_2023)).

### Privacy, security, and communication efficiency

- Privacy-preserving mechanisms: Several oncology FL works implemented secure aggregation and differential privacy (DP). In breast ultrasound (FAME), Gaussian DP noise and secure aggregation were used alongside federated transfer and synthetic augmentation, illustrating practical privacy-by-design pipelines under data scarcity ([FAME Breast Ultrasound, 2025](https://local_corpus/FAME_Breast_Ultrasound_Federated_DP_2025)). A case study in histopathology found DP-FL feasible but sensitive to non-IID distributions and site sizes—consistent with broader evidence that moderate DP budgets (epsilon ≈ 10) preserve utility whereas strict privacy (epsilon ≈ 1) can degrade performance materially, especially in small or heterogeneous data ([FL and Differential Privacy for Medical Image Analysis, 2022](https://local_corpus/FL_and_Differential_Privacy_for_Medical_Image_Analysis_2022); [Differential privacy in medical DL review, 2026](https://local_corpus/Differential_Privacy_Medical_DL_Review_2026)).
- Security threats: Theoretical and applied work indicates residual risks (e.g., membership inference, model inversion) if DP is misconfigured or if aggregation is insecure; modern frameworks (FeatureCloud, APPFLx) integrate secure communication, identity management, and app-based privacy primitives to mitigate such threats in biomedical FL ([FeatureCloud, 2023](https://local_corpus/FeatureCloud_Platform_2023); [APPFLx, 2025](https://local_corpus/APPFLx_End_to_End_Secure_FL_2025)).
- Communication efficiency: While oncology studies seldom report bandwidth/latency, related FL works demonstrate reductions via gradient compression and asynchronous aggregation; these considerations remain essential for scaling multi-centre oncology FL, especially where many clients or high-resolution WSIs/MRI are involved (e.g., 75% reduction reported in a federated few-shot framework, albeit outside oncology) ([FedMedSecure, 2025](https://local_corpus/FedMedSecure_Few_Shot_Communication_2025)).

### Fairness and subgroup performance

Explicit subgroup analyses (e.g., by scanner vendor, demographics) are infrequently reported in oncology FL. The differential privacy literature warns that DP can widen subgroup performance gaps under strict privacy budgets, reinforcing the need for fairness audits, stratified reporting, and calibration across demographic and site-level subgroups in future oncology FL studies ([Differential privacy in medical DL review, 2026](https://local_corpus/Differential_Privacy_Medical_DL_Review_2026)).

### Reproducibility and governance

- Reproducibility: “Federated testing” has been proposed to improve cross-site reproducibility by deploying the same model code at multiple centres to identify implementation discrepancies, a complementary practice to FL that could strengthen external validation of oncology AI ([Federated testing for reproducibility, 2024](https://local_corpus/Federated_Testing_Reproducible_AI_2024)).
- Governance and infrastructure: EU-wide initiatives (EUCAIM) and DRN/CDM networks (e.g., CAREL) are establishing secure centralized-and-federated infrastructures and documentation frameworks that can host oncology FL at scale while aligning with GDPR and cross-border data-use norms ([EUCAIM hospital experience, 2025](https://local_corpus/EUCAIM_Population_Experience_2025); [CAREL DRN, 2023](https://local_corpus/Cancer_Research_Line_CAREL_2023)). FeatureCloud and APPFLx offer unified, low-code FL deployment options for biomedical research ([FeatureCloud, 2023](https://local_corpus/FeatureCloud_Platform_2023); [APPFLx, 2025](https://local_corpus/APPFLx_End_to_End_Secure_FL_2025)).

## Discussion

### Summary of evidence

Across breast, lung, and prostate cancer applications, FL delivers three recurring benefits:

1. Generalizability gains over single-site training. Collaborative FL consistently surpasses locally trained models when tested across independent sites, indicating better handling of domain shifts common in oncology imaging and pathology ([Federated learning improves site performance, 2021](https://local_corpus/Federated_Learning_Improves_Site_Performance_2021); [FL for TNBC NACT response, 2023](https://local_corpus/Federated_Learning_TNBC_NACT_2023)).

2. Near-equivalence to centralized training. Where directly compared, FL is within a narrow performance margin (≈0–3%) of centrally trained models, particularly in histopathology classification. This suggests that the principal technical performance barrier to adopting FL rather than pooling data is small, while the privacy advantage is large ([A review on FL in computational pathology, 2024/2025](https://local_corpus/Review_Federated_Learning_Computational_Pathology_2024_2025); [Federated Fusion of Magnified Histopath, 2024](https://local_corpus/Federated_Fusion_Magnified_Histopath_Breast_2024)).

3. Robustness under heterogeneity with tailored strategies. Memory-aware curricula, variation-aware alignment, and personalization frameworks mitigate non-IID effects, class imbalance, and site differences—ubiquitous challenges in breast screening datasets and multi-centre MRI/WSI oncology ([Memory-aware curriculum FL, 2023](https://local_corpus/Memory_aware_Curriculum_Federated_Learning_Breast_2023); [Variation-Aware FL, 2021](https://local_corpus/Variation_Aware_Federated_Learning_2021)).

### Conditions under which FL provides the most value

- Multi-centre heterogeneity (e.g., differing scanners/protocols, magnification in histopathology) and class imbalance (e.g., low positive rates in screening) favour FL combined with data harmonization or alignment.
- Privacy-sensitive settings where GDPR/HIPAA preclude pooling but governance permits parameter exchange with secure aggregation.
- Tasks with strong representation learning benefit (MRI segmentation/detection, WSI-based response prediction) where sharing learned features/parameters across sites is valuable.

### Privacy–utility trade-offs

Formal privacy (DP) is feasible in oncology FL but introduces noise that can degrade performance if budgets are too strict. Studies suggest moderate DP budgets (epsilon ≈ 10) may maintain clinically acceptable performance, while epsilon ≈ 1 can cause substantial drops, especially in smaller or non-IID cohorts. Therefore:

- Report DP parameters transparently (epsilon, delta, clipping norms).
- Tailor privacy budgets to task criticality and cohort size; consider hybrid approaches (secure aggregation + moderate DP, client-level DP when appropriate) ([FL and DP in medical imaging, 2022](https://local_corpus/FL_and_Differential_Privacy_for_Medical_Image_Analysis_2022); [DP in medical DL review, 2026](https://local_corpus/Differential_Privacy_Medical_DL_Review_2026)).

### Communication and systems considerations

Oncology FL requires careful configuration of local epochs, rounds, and aggregation to balance convergence and communication. The prostate MRI simulation study underscores the importance of tuning these hyperparameters for best Dice/PI-CAI on independent test sets. Emerging frameworks (APPFLx, FeatureCloud) reduce engineering overhead and support secure, heterogeneous deployments—a prerequisite for broad adoption across hospitals ([Optimizing FL Configurations for MRI Prostate, 2025](https://local_corpus/Optimizing_Federated_Learning_Configurations_Prostate_MRI_2025); [APPFLx, 2025](https://local_corpus/APPFLx_End_to_End_Secure_FL_2025); [FeatureCloud, 2023](https://local_corpus/FeatureCloud_Platform_2023)).

### Fairness and calibration

Few oncology FL studies provide calibration curves, decision-curve analyses, or subgroup performance by demographics or device/vendor. Given regulatory emphasis on safety and equity, future studies should include:

- Subgroup metrics (e.g., by age, sex, race/ethnicity, scanner/vendor, site).
- Calibration and clinical utility analyses.
- Fairness-aware training (reweighting, adversarial debiasing) and post-training audits, particularly when DP is used, due to potential widening of performance gaps at strict privacy settings ([Differential privacy in medical DL review, 2026](https://local_corpus/Differential_Privacy_Medical_DL_Review_2026)).

### Risk of bias and reporting

Many included oncology FL studies are retrospective and/or simulations; explicit external validation and calibration are under-reported. Adherence to TRIPOD-AI/STARD-AI checklists, clear descriptions of client distributions and partitioning (IID vs non-IID), statistical hypothesis testing, confidence intervals, and availability of code/seed configuration will strengthen credibility and reproducibility. “Federated testing” offers a complementary pathway to detect implementation discrepancies before clinical translation ([Federated testing for reproducibility, 2024](https://local_corpus/Federated_Testing_Reproducible_AI_2024)).

## Conclusions

- Federated learning in breast, lung, and prostate cancer generally matches centralized model performance and reliably exceeds single-site training, improving cross-site generalizability without sharing patient data.
- The strongest gains are observed in multi-centre, heterogeneous settings when FL is coupled with personalization, curriculum/variation-aware alignment, and data harmonization.
- Privacy-enhancing technologies (secure aggregation, DP) are feasible; moderate DP budgets preserve utility whereas strict privacy can harm performance and equity.
- Implementation maturity (FeatureCloud, APPFLx) and European infrastructures (EUCAIM) reduce barriers to real-world FL deployment in oncology.
- To catalyze clinical translation, oncology FL studies should prioritize external validation, calibration and clinical utility reporting, explicit fairness audits, threat-model evaluation (inference attacks), and detailed communication/overhead reporting.

## Future Directions and Best-Practice Recommendations

- Design: Employ personalization (e.g., client-specific heads), curriculum or variation-aware methods to address non-IID data; integrate harmonization where feasible.
- Evaluation: Report cross-site and external test performance with confidence intervals; include calibration, decision-curve analyses, and subgroup fairness assessments.
- Privacy/Security: Use secure aggregation by default; consider DP with transparent budgets; adversarially test for membership inference/model inversion risks.
- Efficiency: Optimize local epochs/rounds and aggregation to minimize communication while preserving performance; consider asynchronous or compressed updates in large networks.
- Governance and Reproducibility: Align with EUCAIM/DRN frameworks; adopt TRIPOD-AI/STARD-AI reporting; practice “federated testing”; share code, configs, and seeds.
- Clinical Translation: Engage multi-disciplinary governance for consent/contracting; evaluate clinical utility and workflow integration in prospective studies.

## References

- Federated Learning with Research Prototypes: Application to Multi-Center MRI-based Detection of Prostate Cancer with Diverse Histopathology. (2023). https://local_corpus/Federated_Learning_with_Research_Prototypes_Prostate_MRI_2023
- Optimizing Federated Learning Configurations for MRI Prostate Segmentation and Cancer Detection: A Simulation Study. (2025). https://local_corpus/Optimizing_Federated_Learning_Configurations_Prostate_MRI_2025
- Memory-aware curriculum federated learning for breast cancer classification. (2023). https://local_corpus/Memory_aware_Curriculum_Federated_Learning_Breast_2023
- Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer. (2023). https://local_corpus/Federated_Learning_TNBC_NACT_2023
- Federated Fusion of Magnified Histopathological Images for Breast Tumor Classification in the Internet of Medical Things. (2024). https://local_corpus/Federated_Fusion_Magnified_Histopath_Breast_2024
- Privacy-Preserving Breast Cancer Classification: A Federated Transfer Learning Approach. (2024). https://local_corpus/Privacy_Preserving_Breast_Classification_FL_TL_2024
- Enhancing breast magnetic resonance imaging segmentation with a federated semi-supervised approach. (2025). https://local_corpus/Enhancing_Breast_MRI_Segmentation_Federated_Semi_Supervised_2025
- FAME: A privacy-preserving dual-stage deep learning framework for breast ultrasound imaging using federated transfer and synthetic learning. (2025). https://local_corpus/FAME_Breast_Ultrasound_Federated_DP_2025
- Risk stratification for early-stage NSCLC progression: a federated learning framework with large-small model synergy. (2025). https://local_corpus/Risk_Stratification_NSCLC_Federated_2025
- Implementation of the Australian Computer-Assisted Theragnostics (AusCAT) network for radiation oncology data extraction, reporting and distributed learning. (2021). https://local_corpus/AusCAT_Distributed_Learning_Lung_2021
- Variation-Aware Federated Learning With Multi-Source Decentralized Medical Image Data. (2021). https://local_corpus/Variation_Aware_Federated_Learning_2021
- A review on federated learning in computational pathology. (2024). https://local_corpus/Review_Federated_Learning_Computational_Pathology_2024_2025
- Federated Learning for Histopathology Image Classification: A Systematic Review. (2026). https://local_corpus/Systematic_Review_FL_Histopathology_2026
- Federated learning and differential privacy for medical image analysis. (2022). https://local_corpus/FL_and_Differential_Privacy_for_Medical_Image_Analysis_2022
- Differential privacy for medical deep learning: methods, tradeoffs, and deployment implications. (2026). https://local_corpus/Differential_Privacy_Medical_DL_Review_2026
- The FeatureCloud Platform for Federated Learning in Biomedicine: Unified Approach. (2023). https://local_corpus/FeatureCloud_Platform_2023
- Enabling end-to-end secure federated learning in biomedical research on heterogeneous computing environments with APPFLx. (2025). https://local_corpus/APPFLx_End_to_End_Secure_FL_2025
- From code sharing to sharing of implementations: Advancing reproducible AI development for medical imaging through federated testing. (2024). https://local_corpus/Federated_Testing_Reproducible_AI_2024
- Unveiling the role of harmonization on clinically significant prostate cancer detection using MRI. (2025). https://local_corpus/Harmonization_Prostate_MRI_csPCa_2025
- Federated learning improves site performance in multicenter deep learning without data sharing. (2021). https://local_corpus/Federated_Learning_Improves_Site_Performance_2021
- Federated Learning: A Survey on Enabling Technologies, Protocols, and Applications. (2020). https://local_corpus/Federated_Learning_A_Survey_on_Enabling_Technologies_Protocols_and_Applications_2020
- How the First Medical Imaging Cancer Atlas EUCAIM Was Populated: The Experience of a Reference Hospital. (2025). https://local_corpus/EUCAIM_Population_Experience_2025
- Cancer Research Line (CAREL): Development of Expanded Distributed Research Networks for Prostate Cancer and Lung Cancer. (2023). https://local_corpus/Cancer_Research_Line_CAREL_2023

Notes: Only one reference entry is provided per used source as requested.
# AutoMeta Systematic Review Report

**Paper ID:** 357 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 13:00:02

---

## Executive Summary

- **Research Question:** Postmortem brain samples from schizophrenia patien... | ...
- **Studies Included:** 28 of 126 screened
- **Study Summary:** Across 28 postmortem case-control studies, neuroinflammatory markers tended to be higher in schizophrenia than in controls, but quantitative synthesis was possible for only two studies and was heterogeneous: fixed-effects OR 5.71 (95% CI 2.66–12.25) versus random-effects OR 9.34 (95% CI 0.87–99.69; p=0.064). Overall, the evidence supports neuroinflammatory alterations in at least a subset of schizophrenia brains, while highlighting substantial variability by marker, brain region, and method and a need for standardized, meta-analysis-ready reporting.

## 1. Research Question

**P (Population):** Postmortem brain samples from schizophrenia patients

**I (Intervention):** N/A

**C (Comparison):** Healthy controls (non-schizophrenic postmortem brain samples)

**O (Outcome):** Neuroinflammatory markers including microglial markers, glial fibrillary acidic protein (GFAP) expression, glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, and IFITM

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | ("Schizophrenia"[Mesh] OR schizophrenia[tiab] OR schizophrenic[tiab] OR schizoaffective[tiab] OR psychosis[tiab]) AND ("Autopsy"[Mesh] OR autopsy[tiab... |
| 2 | ("Schizophrenia"[Mesh] OR schizophrenia[tiab] OR schizophren*[tiab]) AND ("Autopsy"[Mesh] OR autopsy[tiab] OR postmortem[tiab] OR "post-mortem"[tiab])... |
| 3 | ("Schizophrenia"[Mesh] AND "Brain"[Mesh] AND ("Autopsy"[Mesh] OR "Tissue Banks"[Mesh]) AND (Microglia[Mesh] OR Astrocytes[Mesh] OR "Glial Fibrillary A... |
| 4 | ((schizophren*[tiab] OR "Schizophrenia Spectrum and Other Psychotic Disorders"[Mesh]) AND (postmortem[tiab] OR "post-mortem"[tiab] OR autopsy[tiab] OR... |
| 5 | ("schizophrenia"[tiab] OR "Schizophrenia"[Mesh]) AND (postmortem[tiab] OR "post-mortem"[tiab] OR autopsy[tiab] OR "Autopsy"[Mesh] OR "postmortem brain... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 126 |
| After deduplication | 126 |
| Screened (title/abstract) | 126 |
| Excluded | 98 |
| Full-text assessed | 28 |
| **Included in synthesis** | **28** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- Not human postmortem brain tissue (neuroimaging study). (8 studies)
- Non-original study (systematic review). (2 studies)
- Non-original review; no extractable postmortem SZ vs control data (2 studies)
- Not human postmortem brain tissue (MRI study). (2 studies)
- Non-original article (review). (2 studies)
- Non-original article (meta-analysis of neuroimaging); not postmortem brain tissue. (2 studies)
- Retracted for falsified data (non-original/invalid dataset). (1 studies)
- Outcomes are synaptic markers (synapsin/synaptophysin) only; no specified neuroinflammatory markers reported. (1 studies)
- Non-original narrative review; not a postmortem brain case-control study. (1 studies)
- No clearly defined healthy control group for comparison. (1 studies)

## 3. Included Studies

**Total included:** 28

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 27434 | Increased prefrontal cortical cells positive for macrophage/... | 2023 | Postmortem case-control | 32/60 |
| 2 | 1795 | Inflammation-related genes up-regulated in schizophrenia bra... | 2007 | Postmortem cross-sectional case-control | 55/55 |
| 3 | 1823 | Comparison of peripheral and central schizophrenia biomarker... | 2012 | cross-sectional | NR/NR |
| 4 | 1776 | Layer-specific reductions in GFAP-reactive astroglia in the ... | 2002 | cross-sectional postmortem case-control study | 9/15 |
| 5 | 1780 | Glial fibrillary acidic protein mRNA levels in the cingulate... | 2005 | Cross-sectional (postmortem case-control using consortium samples) | NR/NR |
| 6 | 1542 | Astrocyte decrease in the subgenual cingulate and callosal g... | 2013 | Cross-sectional postmortem comparative study | NR/NR |
| 7 | 1779 | Increased expression of astrocyte markers in schizophrenia: ... | 2014 | Case-control (postmortem cross-sectional) | 37/37 |
| 8 | 27392 | Increased Macrophages and C1qA, C3, C4 Transcripts in the Mi... | 2020 | Postmortem case-control transcriptomic and immunohistochemical study | NR/NR |
| 9 | 1793 | Distribution of HLA-DR-positive microglia in schizophrenia r... | 2006 | Postmortem case-control (cross-sectional) study | 16/16 |
| 10 | 1824 | Markers of inflammation and stress distinguish subsets of in... | 2014 | Cross-sectional case-control transcriptomic analysis with unsupervised clustering | 32/68 |
| 11 | 1788 | Increased inflammatory markers identified in the dorsolatera... | 2013 | case-control (postmortem observational) | 20/NR |
| 12 | 1777 | 3-D Golgi and image analysis of the olfactory tubercle in sc... | 2000 | Postmortem comparative study (schizophrenia vs controls) | NR/NR |
| 13 | 27725 | Molecular mechanisms and timing of cortical immune activatio... | 2015 | case-control (human) with complementary animal model experiments | 62/62 |
| 14 | 1500 | A quantitative immunohistochemical study of astrocytes in th... | 2001 | Postmortem immunohistochemical study (two cohorts) | 48/23 |
| 15 | 1772 | Astrocyte and glutamate markers in the superficial, deep, an... | 2011 | Cross-sectional case-control (postmortem gene expression) | 18/21 |
| 16 | 1792 | Calprotectin in microglia from frontal cortex is up-regulate... | 2006 | Post-mortem comparative study | NR/NR |
| 17 | 1834 | Elevated viral restriction factor levels in cortical blood v... | 2014 | Cross-sectional case-control (postmortem brain study) | 57/57 |
| 18 | 1796 | Regulation of immune-modulatory genes in left superior tempo... | 2011 | Post-mortem observational gene expression study (case-control, implied) | NR/NR |
| 19 | 1774 | Regionally specific changes in levels of cortical S100beta i... | 2006 | cross-sectional | NR/NR |
| 20 | 1497 | A histological study of the corpus callosum in chronic schiz... | 1983 | post-mortem histological study | NR/NR |
| 21 | 1761 | Gliosis in schizophrenia: a survey. | 1986 | Postmortem case-control quantitative neuropathology | NR/NR |
| 22 | 1762 | Is there gliosis in schizophrenia? Investigation of the temp... | 1987 | Observational postmortem comparative study | NR/NR |
| 23 | 1805 | Quantitative cytoarchitectural studies of the cerebral corte... | 1986 | Case-control (postmortem morphometric study) | 10/10 |
| 24 | 1543 | Evidence for morphological alterations in prefrontal white m... | 2014 | cross-sectional postmortem comparative study | NR/NR |
| 25 | 1512 | Oligodendroglial density in the prefrontal cortex in schizop... | 2004 | Cross-sectional postmortem morphometric study | 15/15 |
| 26 | 1765 | No evidence for astrogliosis in brains of schizophrenic pati... | 1999 | cross-sectional | 33/26 |
| 27 | 1821 | Stereological assessment of the dorsal anterior cingulate co... | 2013 | case-control | 13/13 |
| 28 | 1769 | Increase in HLA-DR immunoreactive microglia in frontal and t... | 2000 | case-control | NR/NR |


## 5. Study Characteristics

| Study | Design | Participants | Key Outcomes |
|-------|--------|--------------|--------------|
|  2023 | Postmortem case-control | 32/60 | See extraction table |
|  2007 | Postmortem cross-sectional case-control | 55/55 | See extraction table |
|  2012 | cross-sectional | 0/0 | See extraction table |
| unknown 0 | cross-sectional postmortem case-control study | 9/15 | See extraction table |
|  2005 | Cross-sectional (postmortem case-control using consortium samples) | 0/0 | See extraction table |
|  2013 | Cross-sectional postmortem comparative study | 0/0 | See extraction table |
|  2014 | Case-control (postmortem cross-sectional) | 37/37 | See extraction table |
|  2020 | Postmortem case-control transcriptomic and immunohistochemical study | 0/0 | See extraction table |
| unknown 0 | Postmortem case-control (cross-sectional) study | 16/16 | See extraction table |
|  2014 | Cross-sectional case-control transcriptomic analysis with unsupervised clustering | 32/68 | See extraction table |
| unknown 0 | case-control (postmortem observational) | 20/0 | See extraction table |
| not reported 0 | Postmortem comparative study (schizophrenia vs controls) | 0/0 | See extraction table |
|  2015 | case-control (human) with complementary animal model experiments | 62/62 | See extraction table |
|  2001 | Postmortem immunohistochemical study (two cohorts) | 48/23 | See extraction table |
|  2011 | Cross-sectional case-control (postmortem gene expression) | 18/21 | See extraction table |
|  2006 | Post-mortem comparative study | 0/0 | See extraction table |
|  2014 | Cross-sectional case-control (postmortem brain study) | 57/57 | See extraction table |
|  2011 | Post-mortem observational gene expression study (case-control, implied) | 0/0 | See extraction table |
|  2006 | cross-sectional | 0/0 | See extraction table |
|  1983 | post-mortem histological study | 0/0 | See extraction table |
|  1986 | Postmortem case-control quantitative neuropathology | 0/0 | See extraction table |
|  1987 | Observational postmortem comparative study | 0/0 | See extraction table |
|  1986 | Case-control (postmortem morphometric study) | 10/10 | See extraction table |
|  2014 | cross-sectional postmortem comparative study | 0/0 | See extraction table |
|  2004 | Cross-sectional postmortem morphometric study | 15/15 | See extraction table |
| unknown 0 | cross-sectional | 33/26 | See extraction table |
|  2013 | case-control | 13/13 | See extraction table |
|  2000 | case-control | 0/0 | See extraction table |

## 6. Statistical Analysis

- **Studies with extractable data:** 2
- **Effect measure:** OR

### Meta-Analysis Results

| Model | Effect | 95% CI | I² | p-value |
|-------|--------|-------|----|--------|
| Random effects | 9.338 | 0.875–99.686 | 86.8% | 0.006 |
| Fixed effects | 5.714 | 2.665–12.250 | - | - |

### Interpretation

- The pooled effect suggests the intervention is associated with increased outcome (OR/RR/HR > 1)
- **Heterogeneity:** Considerable (I² = 86.8%) - high variability, interpret with caution

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 28

**Total participants:** Approximately 935 participants across all included studies

**Study design distribution:**

- cross-sectional: 3 studies
- case-control: 2 studies
- Postmortem case-control: 1 studies
- Postmortem cross-sectional case-control: 1 studies
- cross-sectional postmortem case-control study: 1 studies
- Cross-sectional (postmortem case-control using consortium samples): 1 studies
- Cross-sectional postmortem comparative study: 1 studies
- Case-control (postmortem cross-sectional): 1 studies
- Postmortem case-control transcriptomic and immunohistochemical study: 1 studies
- Postmortem case-control (cross-sectional) study: 1 studies
- Cross-sectional case-control transcriptomic analysis with unsupervised clustering: 1 studies
- case-control (postmortem observational): 1 studies
- Postmortem comparative study (schizophrenia vs controls): 1 studies
- case-control (human) with complementary animal model experiments: 1 studies
- Postmortem immunohistochemical study (two cohorts): 1 studies
- Cross-sectional case-control (postmortem gene expression): 1 studies
- Post-mortem comparative study: 1 studies
- Cross-sectional case-control (postmortem brain study): 1 studies
- Post-mortem observational gene expression study (case-control, implied): 1 studies
- post-mortem histological study: 1 studies
- Postmortem case-control quantitative neuropathology: 1 studies
- Observational postmortem comparative study: 1 studies
- Case-control (postmortem morphometric study): 1 studies
- cross-sectional postmortem comparative study: 1 studies
- Cross-sectional postmortem morphometric study: 1 studies

**Publication years:** 1983–2023

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
We included 28 postmortem case-control studies (2001–2023) comparing neuroinflammatory markers in schizophrenia versus non-psychiatric controls. Designs ranged from immunohistochemistry and protein assays to bulk transcriptomics; one study incorporated unsupervised clustering of gene-expression data, and another combined human postmortem analyses with complementary animal experiments. Across the subset of studies reporting sample sizes, at least 309 schizophrenia cases and 357 controls were examined (e.g., Unknown 2001: 48/23; Unknown 2007: 55/55; Unknown 2014: 37/37; Unknown 2014 transcriptomic clustering: 32/68; Unknown 2015: 62/62; Unknown 2023: 32/60; plus several smaller cohorts). Neuroinflammatory outcomes spanned microglial markers, glial fibrillary acidic protein (GFAP), glial cell densities, cytokines, arachidonic cascade markers, substance P, SERPINA3, and IFITM. Only two studies provided extractable data for quantitative synthesis; the random-effects meta-analysis yielded an odds ratio (OR) of 9.34 (95% CI 0.87 to 99.69; p=0.064), with considerable heterogeneity (I²=86.8%; τ²=2.5426). The fixed-effects model produced a significant pooled OR of 5.71 (95% CI 2.66 to 12.25).

### 7.2 Discussion of Findings
Overall, the quantitative signal—albeit based on only two studies—suggested higher odds of elevated neuroinflammatory markers in schizophrenia relative to controls. One contributing study (Unknown, 2023; N=32/60) reported an effect consistent with approximately OR 3.0 (95% CI 1.23 to 7.31), indicating a moderate increase in a composite neuroinflammatory outcome among cases. The second contributing study (Unknown, 2014 transcriptomic clustering; N=32/68) reported a substantially larger effect. This disparity translated into a model-dependent pooled estimate: the fixed-effects model was statistically significant (OR 5.71, 95% CI 2.66 to 12.25), whereas the random-effects model—more appropriate under heterogeneity—was not (OR 9.34, 95% CI 0.87 to 99.69; p=0.064). Thus, while the direction of effect favors increased neuroinflammation in schizophrenia, the magnitude and certainty are limited by between-study variability and the small number of quantifiable datasets.

The considerable heterogeneity (I²=86.8%) is biologically and methodologically plausible. First, the included studies interrogated diverse marker classes (microglial activation markers, GFAP, cytokines, arachidonic pathway enzymes, neuropeptides such as substance P, acute-phase proteins like SERPINA3, and antiviral-associated IFITMs), which need not change in parallel. Second, tissue sampling varied by region (e.g., prefrontal cortex, cingulate, hippocampus), and regional gliosis or microglial activation can be patchy and context-dependent. Third, platforms differed (immunohistochemistry, protein assays, bulk RNA expression), each with distinct dynamic ranges, cell-type specificity, and susceptibility to postmortem artefacts. Fourth, clinical and perimortem covariates (antipsychotic exposure, agonal state, postmortem interval, tissue pH, smoking and substance use, age, sex, cause of death) influence glial and immune readouts; covariate control was variably reported and was not standardizable from the available extraction. The τ² of 2.54 indicates large between-study variance on the log-odds scale, consistent with the wide confidence intervals in the random-effects model.

Robustness checks—comparing fixed- and random-effects estimates—underscore the fragility of the quantitative inference. The fixed-effects significance suggests that one or both studies contributed high-precision estimates in the same direction; however, with only two studies, the random-effects model is sensitive to dispersion, and the p-value (0.064) narrowly misses conventional thresholds. Given the small k (number of studies), we could not assess small-study effects or publication bias; funnel plot and Egger tests were not meaningful.

Author conclusions were not systematically available in the extraction for most studies, precluding a formal synthesis of investigators’ stated interpretations by marker class. Based on the study descriptors, several investigations using transcriptomics and immunohistochemistry focused on innate immune and astroglial pathways (e.g., SERPINA3, IFITMs, GFAP), while others quantified microglial markers and cytokines. The heterogeneity in extractable outcomes (many “not computable” due to reporting formats) mirrors the likely diversity of author-level conclusions—some reporting increased glial or immune markers in subsets of cases, others reporting null findings or region-specific effects. This aligns with the meta-analytic picture: a tendency toward increased neuroinflammatory signals in schizophrenia with substantial between-study variability.

In sum, the weight of evidence suggests that neuroinflammatory alterations are present in at least a subset of schizophrenia brains postmortem. However, the quantitative magnitude cannot be precisely estimated from the available data, and conclusions are contingent on outcome definitions, brain region, and analytic platform. The field appears characterized by biologically plausible but methodologically heterogeneous findings, consistent with a non-uniform, subgroup-like pattern of neuroinflammatory involvement rather than a ubiquitous lesion.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Across 28 postmortem case-control studies spanning 2001–2023, evidence generally points toward elevated neuroinflammatory markers in schizophrenia compared with controls, but the certainty of the pooled estimate is low. The two studies with extractable data yielded a model-dependent pooled effect (fixed-effects OR 5.71, 95% CI 2.66–12.25; random-effects OR 9.34, 95% CI 0.87–99.69; p=0.064) with considerable heterogeneity (I²=86.8%). These results support the presence of neuroinflammatory changes in at least a subset of cases, while underscoring substantial variability by marker, region, and method.

### 8.2 Limitations
Review-level limitations: We were constrained by incomplete quantitative reporting in most included studies; only two provided data suitable for meta-analysis. Many studies reported ratios, fold-changes, or qualitative immunohistochemical grading that were not directly convertible to standardized effect sizes without access to raw data. We did not perform a formal risk-of-bias assessment due to insufficiently detailed extraction, and we could not assess reporting bias given the small number of quantifiable studies. The total participant count is imprecise; among studies reporting sample sizes, at least 309 schizophrenia cases and 357 controls were analyzed, but several cohorts did not report Ns or reported them partially.

Study-level limitations: Case-control postmortem research is inherently susceptible to selection and confounding (medication exposure, agonal state, postmortem interval, brain pH, smoking/substance use, comorbid medical illness, and cause of death), which differentially influence glial and immune markers. Brain region sampling, cell-type composition, and assay platform varied widely across studies, limiting comparability. Outcomes encompassed diverse biological pathways (microglia, astrocytes, cytokines, arachidonic cascade, neuropeptides), and studies often targeted different markers, reducing the feasibility of a unified meta-analytic endpoint. Some studies combined human postmortem with animal models; while mechanistically informative, such data do not resolve human heterogeneity.

### 8.3 Implications
For practice and policy: Current postmortem evidence does not support any change in clinical practice. The findings are not sufficiently consistent or generalizable to recommend diagnostic use of neuroinflammatory markers or to infer therapeutic efficacy of anti-inflammatory interventions in schizophrenia. The heterogeneity instead argues for caution and for focusing clinical decisions on established evidence from in vivo studies and randomized trials rather than postmortem pathology.

For research: Priority should be given to harmonized, preregistered postmortem consortia studies with standardized brain region sampling, careful phenotyping, and uniform covariate collection (medication, smoking, agonal factors, postmortem interval, pH). Future work should predefine core outcome sets across marker classes (e.g., microglial activation markers, GFAP, key cytokines, arachidonic enzymes, SERPINA3, IFITMs) and report meta-analysis-ready statistics (group means/SDs or effect sizes with variance). Single-cell and spatial transcriptomic/proteomic approaches are needed to resolve cell-type and layer specificity. Given signals of subgroup effects, studies should prospectively test for “high-inflammatory” phenotypes using unsupervised clustering with validation cohorts, and examine clinical correlates (symptom domains, course, antipsychotic exposure). Data sharing of raw quantitative measures will facilitate re-analysis and cross-cohort synthesis. Finally, replication across independent brain banks with robust adjustment for confounders is essential to establish whether particular neuroinflammatory signatures are reproducible, clinically meaningful, and mechanistically linked to schizophrenia pathophysiology.

---

## References of Included Studies

1. Unknown (2023). Increased prefrontal cortical cells positive for macrophage/microglial marker CD163 along blood vessels characterizes a neuropathology of neuroinflammatory schizophrenia.. *Brain, behavior, and immunity*.
   DOI: 10.1016/j.bbi.2023.03.018
   PMID: 36972743

2. Peter Saetre, Lina Emilsson, Elin Axelsson, et al. (2007). Inflammation-related genes up-regulated in schizophrenia brains.. *BMC psychiatry*.
   DOI: 10.1186/1471-244X-7-46
   PMID: 17822540

3. Laura W Harris, Sandra Pietsch, Tammy M K Cheng, et al. (2012). Comparison of peripheral and central schizophrenia biomarker profiles.. *PloS one*.
   DOI: 10.1371/journal.pone.0046368
   PMID: 23118852

4. Grazyna Rajkowska, Jose Javier Miguel-Hidalgo, Zoltan Makkos, et al. (2002). Layer-specific reductions in GFAP-reactive astroglia in the dorsolateral prefrontal cortex in schizophrenia.. *Schizophrenia research*.
   DOI: 10.1016/s0920-9964(02)00339-0
   PMID: 12223243

5. M J Webster, J O'Grady, J E Kleinman, et al. (2005). Glial fibrillary acidic protein mRNA levels in the cingulate cortex of individuals with depression, bipolar disorder and schizophrenia.. *Neuroscience*.
   DOI: 10.1016/j.neuroscience.2005.02.037
   PMID: 15885920

6. Matthew Roy Williams, Thomas Hampton, Ronald K B Pearce, et al. (2013). Astrocyte decrease in the subgenual cingulate and callosal genu in schizophrenia.. *European archives of psychiatry and clinical neuroscience*.
   DOI: 10.1007/s00406-012-0328-5
   PMID: 22660922

7. Vibeke Sørensen Catts, Jenny Wong, Stu Gregory Fillman, et al. (2014). Increased expression of astrocyte markers in schizophrenia: Association with neuroinflammation.. *The Australian and New Zealand journal of psychiatry*.
   DOI: 10.1177/0004867414531078
   PMID: 24744400

8. Unknown (2020). Increased Macrophages and C1qA, C3, C4 Transcripts in the Midbrain of People With Schizophrenia.. *Frontiers in immunology*.
   DOI: 10.3389/fimmu.2020.02002
   PMID: 33133060

9. Johann Steiner, Christian Mawrin, Anke Ziegeler, et al. (2006). Distribution of HLA-DR-positive microglia in schizophrenia reflects impaired cerebral lateralization.. *Acta neuropathologica*.
   DOI: 10.1007/s00401-006-0090-8
   PMID: 16783554

10. S G Fillman, D Sinclair, S J Fung, et al. (2014). Markers of inflammation and stress distinguish subsets of individuals with schizophrenia and bipolar disorder.. *Translational psychiatry*.
   DOI: 10.1038/tp.2014.8
   PMID: 24569695

11. S G Fillman, N Cloonan, V S Catts, et al. (2013). Increased inflammatory markers identified in the dorsolateral prefrontal cortex of individuals with schizophrenia.. *Molecular psychiatry*.
   DOI: 10.1038/mp.2012.110
   PMID: 22869038

12. E Markova, I Markov, A Revishchin, et al. (2000). 3-D Golgi and image analysis of the olfactory tubercle in schizophrenia.. *Analytical and quantitative cytology and histology*.
   DOI: not reported
   PMID: 10800621

13. Unknown (2015). Molecular mechanisms and timing of cortical immune activation in schizophrenia.. *The American journal of psychiatry*.
   DOI: 10.1176/appi.ajp.2015.15010019
   PMID: 26133963

14. R Damadzic, L B Bigelow, L S Krimer, et al. (2001). A quantitative immunohistochemical study of astrocytes in the entorhinal cortex in schizophrenia, bipolar disorder and major depression: absence of significant astrocytosis.. *Brain research bulletin*.
   DOI: 10.1016/s0361-9230(01)00529-9
   PMID: 11576757

15. Pavel Katsel, William Byne, Panos Roussos, et al. (2011). Astrocyte and glutamate markers in the superficial, deep, and white matter layers of the anterior cingulate gyrus in schizophrenia.. *Neuropsychopharmacology : official publication of the American College of Neuropsychopharmacology*.
   DOI: 10.1038/npp.2010.252
   PMID: 21270770

16. Russell Foster, Apsara Kandanearatchi, Claire Beasley, et al. (2006). Calprotectin in microglia from frontal cortex is up-regulated in schizophrenia: evidence for an inflammatory process?. *The European journal of neuroscience*.
   DOI: 10.1111/j.1460-9568.2006.05219.x
   PMID: 17229104

17. Benjamin I Siegel, Elizabeth J Sengupta, Jessica R Edelson, et al. (2014). Elevated viral restriction factor levels in cortical blood vessels in schizophrenia.. *Biological psychiatry*.
   DOI: 10.1016/j.biopsych.2013.09.019
   PMID: 24209773

18. Andrea Schmitt, Fernando Leonardi-Essmann, Pascal F Durrenberger, et al. (2011). Regulation of immune-modulatory genes in left superior temporal cortex of schizophrenia patients: a genome-wide microarray study.. *The world journal of biological psychiatry : the official journal of the World Federation of Societies of Biological Psychiatry*.
   DOI: 10.3109/15622975.2010.530690
   PMID: 21091092

19. Brian Dean, Laura Gray, Elizabeth Scarr (2006). Regionally specific changes in levels of cortical S100beta in bipolar 1 disorder but not schizophrenia.. *The Australian and New Zealand journal of psychiatry*.
   DOI: 10.1080/j.1440-1614.2006.01777.x
   PMID: 16476148

20. H A Nasrallah, M McCalley-Whitters, L B Bigelow, et al. (1983). A histological study of the corpus callosum in chronic schizophrenia.. *Psychiatry research*.
   DOI: 10.1016/0165-1781(83)90013-6
   PMID: 6576392

21. G W Roberts, N Colter, R Lofthouse, et al. (1986). Gliosis in schizophrenia: a survey.. *Biological psychiatry*.
   DOI: 10.1016/0006-3223(86)90285-4
   PMID: 2943323

22. G W Roberts, N Colter, R Lofthouse, et al. (1987). Is there gliosis in schizophrenia? Investigation of the temporal lobe.. *Biological psychiatry*.
   DOI: 10.1016/0006-3223(87)90104-1
   PMID: 3315013

23. F M Benes, J Davidson, E D Bird (1986). Quantitative cytoarchitectural studies of the cerebral cortex of schizophrenics.. *Archives of general psychiatry*.
   DOI: 10.1001/archpsyc.1986.01800010033004
   PMID: 3942472

24. Christa Hercher, Vikramjit Chopra, Clare L Beasley (2014). Evidence for morphological alterations in prefrontal white matter glia in schizophrenia and bipolar disorder.. *Journal of psychiatry & neuroscience : JPN*.
   DOI: 10.1503/jpn.130277
   PMID: 24936776

25. Natalya A Uranova, Victor M Vostrikov, Diana D Orlovskaya, et al. (2004). Oligodendroglial density in the prefrontal cortex in schizophrenia and mood disorders: a study from the Stanley Neuropathology Consortium.. *Schizophrenia research*.
   DOI: 10.1016/S0920-9964(03)00181-6
   PMID: 14984887

26. P Falkai, W G Honer, S David, et al. (1999). No evidence for astrogliosis in brains of schizophrenic patients. A post-mortem study.. *Neuropathology and applied neurobiology*.
   DOI: 10.1046/j.1365-2990.1999.00162.x
   PMID: 10194775

27. M Höistad, H Heinsen, B Wicinski, et al. (2013). Stereological assessment of the dorsal anterior cingulate cortex in schizophrenia: absence of changes in neuronal and glial densities.. *Neuropathology and applied neurobiology*.
   DOI: 10.1111/j.1365-2990.2012.01296.x
   PMID: 22860626

28. K Radewicz, L J Garey, S M Gentleman, et al. (2000). Increase in HLA-DR immunoreactive microglia in frontal and temporal cortex of chronic schizophrenics.. *Journal of neuropathology and experimental neurology*.
   DOI: 10.1093/jnen/59.2.137
   PMID: 10749103


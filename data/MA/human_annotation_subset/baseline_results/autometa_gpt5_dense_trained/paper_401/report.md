# AutoMeta Systematic Review Report

**Paper ID:** 401 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 13:34:15

---

## Executive Summary

- **Research Question:** Breast cancer patients with tissue samples, specif... | ...
- **Studies Included:** 0 of 106 screened
- **Study Summary:** We screened 106 records and excluded all at title/abstract; no eligible human tumor tissue microbiome studies directly comparing TNBC versus non-TNBC were identified. Consequently, we could not estimate effect sizes or evaluate enrichment of specific taxa or functional pathways, highlighting a focused evidence gap and the need for rigorously designed, contamination-controlled, multi-center primary studies.

## 1. Research Question

**P (Population):** Breast cancer patients with tissue samples, specifically comparing TNBC patients to non-TNBC patients (200 samples across four independent cohorts)

**I (Intervention):** N/A

**C (Comparison):** Non-TNBC breast cancer tissue microbiome

**O (Outcome):** Microbial community composition differences, enrichment of specific genera and species (Azospirillum, Gemmiger formicilis, Anaerobutyricum soehngenii), and functional pathway involvement related to chronic inflammation, cellular proliferation, invasion, and metastasis

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | ("Breast Neoplasms"[Mesh] OR breast neoplasm*[tiab] OR breast cancer*[tiab] OR mammary carcinoma*[tiab]) AND ("Microbiota"[Mesh] OR "Microbiome"[Mesh]... |
| 2 | (("Triple Negative Breast Neoplasms"[Mesh] OR TNBC[tiab] OR triple negative[tiab] OR triple-negative[tiab] OR basal-like[tiab] OR (ER-negative[tiab] A... |
| 3 | (("Triple Negative Breast Neoplasms"[Mesh] OR TNBC[tiab] OR triple negative[tiab] OR triple-negative[tiab]) AND (non-triple-negative[tiab] OR non-TNBC... |
| 4 | ("Breast Neoplasms"[Mesh] AND "Triple Negative Breast Neoplasms"[Mesh]) AND ("Microbiota"[Mesh] OR "Microbiome"[Mesh] OR "Metagenomics"[Mesh]) AND ("B... |
| 5 | ((breast[tiab] OR mammary[tiab]) AND (tumor[tiab] OR tumour[tiab] OR tissue[tiab] OR intratumor*[tiab] OR "tumor microenvironment"[tiab] OR "tumour mi... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 106 |
| After deduplication | 106 |
| Screened (title/abstract) | 106 |
| Excluded | 106 |
| Full-text assessed | 0 |
| **Included in synthesis** | **0** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- Not using breast tumor tissue for microbiome profiling (8 studies)
- Non-microbiome assays without bacterial composition or functional pathway data (7 studies)
- No explicit comparison between TNBC and non-TNBC subtypes (3 studies)
- Non-original report (systematic review) (3 studies)
- Non-original report (review). (3 studies)
- Non-original review; not breast tumor tissue microbiome sequencing with TNBC vs non-TNBC comparison. (2 studies)
- No explicit comparison between TNBC and non-TNBC subtypes in breast tumor tissue microbiome. (2 studies)
- Not using breast tumor tissue for microbiome profiling (saliva in oral cancer). (2 studies)
- No explicit comparison between TNBC and non-TNBC within breast tumor tissue microbiome. (2 studies)
- Non-original report (review) (2 studies)

## 3. Included Studies

**Total included:** 0

*No studies included.*

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 0

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
We screened 106 records after deduplication and excluded all 106 at title/abstract level; no records proceeded to full-text review and no studies met inclusion criteria. Consequently, there are no eligible human studies directly comparing the tumor tissue microbiome of triple-negative breast cancer (TNBC) with non-TNBC subtypes and reporting differential community composition, specific taxon enrichment (for example, Azospirillum, Gemmiger formicilis, Anaerobutyricum soehngenii), or functional pathway involvement related to chronic inflammation, cellular proliferation, invasion, or metastasis. This constitutes a clear evidence gap for the prespecified question.

### 7.2 Discussion of Findings
Our main finding is the absence of eligible evidence. Despite an a priori plan to synthesize effect measures (odds ratios) for taxon- or pathway-level differences and, if appropriate, pool across cohorts, the lack of included studies precluded quantitative synthesis. The retrieved literature in the local corpus largely comprised non-original reviews, non-human experimental work, studies focused on non-tissue biospecimens (for example, blood microbiome), and tumor sites other than breast, or breast studies without explicit TNBC versus non-TNBC comparisons in tumor tissue. As a result, none of the 106 screened records provided extractable data on within-tissue microbial community differences between TNBC and non-TNBC patients.

Because there were no eligible studies, we cannot provide estimates, confidence intervals, or p-values for differential abundance of the taxa of interest (Azospirillum, Gemmiger formicilis, Anaerobutyricum soehngenii) or for pathways linked to inflammation or metastatic biology in TNBC versus non-TNBC. Any claims about enrichment of these taxa or functional profiles in TNBC relative to other subtypes are therefore unsupported by the evidence captured here. Similarly, we cannot corroborate or contrast individual author conclusions across studies, as no eligible primary data were available. The author conclusions present in the excluded literature (for example, narrative statements in reviews or findings from animal models or non-tissue biospecimens) do not directly answer the PICO and were excluded by design to maintain clinical and specimen-type relevance.

Although we could not quantify heterogeneity, it is important to recognize the methodological variability likely to impact any future synthesis. Potential sources include: biospecimen type (fresh-frozen versus FFPE tumor tissue), tumor cellularity and microdissection strategy, low-biomass contamination risks and decontamination procedures (negative controls, reagent blanks, and in silico filtering), sequencing modality (16S rRNA gene versus shotgun metagenomics or metatranscriptomics), compositional data handling and differential abundance methods, and clinical covariate imbalance (for example, stage, prior therapy, antibiotic exposure, menopausal status, BMI, race/ethnicity, and batch effects across centers). Even with multiple eligible studies, these factors would warrant careful risk-of-bias assessment and likely favor random-effects models with prespecified subgroup and sensitivity analyses (for example, by sequencing method or contamination control stringency).

Planned statistical procedures (computing study-specific odds ratios and conducting meta-analysis where ≥2 studies reported comparable outcomes) could not be implemented. No fixed- or random-effects comparisons or robustness checks were possible, and there are no author-level conclusions to reconcile with pooled estimates. The key takeaway is not an estimate but the delineation of a targeted evidence gap: among human breast tumor tissue sequencing studies, explicit head-to-head comparisons of TNBC versus non-TNBC microbiomes with organism-level and pathway-level resolution were not identified in this corpus.

Given the biological plausibility that tumor microenvironments might differ by molecular subtype—through immune tone, hypoxia, stromal remodeling, or treatment exposures—it remains an open question whether such differences manifest as reproducible microbial signatures in tumor tissue. However, current evidence identified here does not establish such associations, and the field’s susceptibility to contamination and analytic artifacts underscores the need for rigorous, well-controlled primary studies before any clinical inferences can be drawn.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
No eligible human studies compared the tumor tissue microbiome between TNBC and non-TNBC subtypes with sufficient methodological alignment to our inclusion criteria. As a result, there is no evidence base in this review to support or refute differences in microbial community composition, enrichment of Azospirillum, Gemmiger formicilis, Anaerobutyricum soehngenii, or related functional pathways in TNBC versus non-TNBC.

### 8.2 Limitations
Review-level limitations include reliance on a local corpus, which may not encompass all relevant primary literature, and the fact that all 106 records were excluded at title/abstract screening. While exclusion reasons were documented, the absence of full-text assessment introduces a small risk that potentially eligible studies were misclassified at the screening stage. We also did not perform citation chasing or contact authors for additional data, which might have surfaced otherwise missed tissue-based subtype comparisons.

The broader field has notable study-level challenges that would affect any synthesis: tumor tissue is a low-biomass matrix prone to reagent and environmental contamination; sample processing (FFPE versus fresh-frozen), sequencing approach (16S versus shotgun), and bioinformatic pipelines vary widely; and clinical heterogeneity (for example, neoadjuvant therapy, antibiotic use, comorbidities) can confound microbiome profiles. Absent rigorous negative controls, decontamination protocols, and pre-registered analytic plans with multiple-testing correction, reported associations may be fragile or non-reproducible.

### 8.3 Implications
For practice: There is no current evidence from eligible human tumor tissue sequencing studies to inform clinical decision-making regarding TNBC based on tumor-associated microbiota. No diagnostic, prognostic, or therapeutic use of tumor tissue microbiome features—at the community, genus/species, or pathway level—can be recommended for distinguishing TNBC from non-TNBC.

For research: Targeted, well-powered, multi-center studies are needed to directly compare tumor tissue microbiomes in TNBC versus non-TNBC. Key design features should include: standardized biospecimen collection (preferably fresh-frozen), rigorous contamination control (reagent blanks, environmental controls, spike-ins, and in silico decontamination), shotgun metagenomics and/or metatranscriptomics to enable organism- and pathway-level resolution, and validation by orthogonal assays (qPCR, FISH). Analyses should be pre-registered, use appropriate compositional methods (for example, ANCOM-BC, ALDEx2, Songbird), control for clinical confounders (stage, therapy, antibiotics, BMI, menopausal status), and adjust for multiple testing (for example, FDR). To test hypotheses about enrichment of Azospirillum, Gemmiger formicilis, or Anaerobutyricum soehngenii and pathways related to inflammation and metastasis, studies should ensure sufficient sample size per subtype and replicate findings across independent cohorts with harmonized protocols. Where feasible, paired adjacent normal tissue and longitudinal sampling (pre/post therapy) would strengthen causal inference and functional interpretation.


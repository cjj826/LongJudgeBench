# AutoMeta Systematic Review Report

**Paper ID:** 215 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 09:26:00

---

## Executive Summary

- **Research Question:** pregnant women and their newborns... | ...
- **Studies Included:** 30 of 93 screened
- **Study Summary:** Thirty observational studies (2007–2021) examined prenatal PFOS exposure and birth weight. Multiple cohorts reported modest inverse associations (e.g., −96 to −149 g), and a random-effects meta-analysis of 24 studies using dichotomous outcomes found no statistically significant association (pooled OR=0.8872; 95% CI: 0.7276 to 1.0819; I²=74.4%). Overall, evidence suggests a probable small inverse relationship with substantial heterogeneity and important methodological limitations.

## 1. Research Question

**P (Population):** pregnant women and their newborns

**I (Intervention):** N/A

**C (Comparison):** lower PFOS exposure levels

**O (Outcome):** birth weight (in grams)

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | ("Perfluorooctane Sulfonic Acid"[Supplementary Concept] OR PFOS[tiab] OR "perfluorooctane sulfonic acid"[tiab] OR perfluorooctane sulfonate[tiab] OR p... |
| 2 | (("Perfluorooctane Sulfonic Acid"[Supplementary Concept] OR PFOS[tiab] OR perfluorooctane sulfon*[tiab] OR perfluorooctanesulfon*[tiab] OR perfluorooc... |
| 3 | (("Perfluoroalkyl Substances"[Mesh] OR "Perfluorooctane Sulfonic Acid"[Supplementary Concept]) AND ("Pregnancy"[Mesh] OR "Infant, Newborn"[Mesh]) AND ... |
| 4 | ((PFOS[tiab] OR perfluorooctane sulfon*[tiab] OR perfluorooctanesulfon*[tiab] OR perfluorooctane sulphonic*[tiab] OR "perfluoroalkyl"[tiab] OR "polyfl... |
| 5 | ("Perfluorooctane Sulfonic Acid"[Supplementary Concept] OR PFOS[tiab] OR perfluorooctane sulfon*[tiab] OR perfluorooctane sulphonic*[tiab]) AND ("Bloo... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 93 |
| After deduplication | 93 |
| Screened (title/abstract) | 93 |
| Excluded | 63 |
| Full-text assessed | 30 |
| **Included in synthesis** | **30** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- Exposure assessment study without reporting infant birth weight in grams or data to derive it. (1 studies)
- PFOS-specific exposure estimates not provided; focuses on PFOS alternatives (Cl-PFESAs). (1 studies)
- Outcome is miscarriage; does not report infant birth weight in grams or continuous birth-weight data. (1 studies)
- Does not report infant birth weight in grams or continuous birth-weight data (focus on neonatal growth index/mediation). (1 studies)
- Focuses on trans-placental transfer; does not report infant birth weight in grams or data to derive it. (1 studies)
- Determinants/temporal trends study; does not report infant birth weight in grams or continuous birth-weight data. (1 studies)
- Does not clearly report infant birth weight in grams or data to derive it; neonatal outcomes unspecified. (1 studies)
- Primary outcome is neurodevelopment at 2 years; does not report infant birth weight in grams or continuous birth-weight data. (1 studies)
- Placental transfer study without reporting infant birth weight in grams or continuous birth-weight data. (1 studies)
- Nested case-control focusing on hormonal pathways; does not report infant birth weight in grams or continuous birth-weight data. (1 studies)

## 3. Included Studies

**Total included:** 30

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 3382 | Occurrence of perfluoroalkyl substances in cord serum and as... | 2017 | Observational cross-sectional analysis at birth (cord serum exposure vs. birth outcomes) | NR/NR |
| 2 | 86728 | Associations of Prenatal Exposure to Per- and Polyfluoroalky... | 2021 | Observational exposure-outcome analysis (specific design not reported) | NR/NR |
| 3 | 3401 | Perfluoroalkyl Acids in Maternal Serum and Indices of Fetal ... | 2016 | cohort | NR/NR |
| 4 | 3777 | Perfluorinated chemicals and fetal growth: a study within th... | 2007 | cohort | NR/NR |
| 5 | 88178 | Prenatal Exposure to Perfluoroalkyl Substances and Birth Out... | 2018 | Prospective cohort | NR/NR |
| 6 | 3388 | Maternal exposure to perfluorinated acids and fetal growth. | 2010 | Cohort | NR/NR |
| 7 | 3409 | Perfluorinated compounds in relation to birth weight in the ... | 2012 | cohort | NR/NR |
| 8 | 3393 | Maternal concentrations of polyfluoroalkyl compounds during ... | 2012 | cohort | NR/NR |
| 9 | 3390 | Prenatal exposure to 11 perfluoroalkyl substances and fetal ... | 2020 | Prospective birth cohort | NR/NR |
| 10 | 3778 | Correlations between prenatal exposure to perfluorinated che... | 2009 | Prospective cohort | NR/NR |
| 11 | 70019 | Fetal growth indicators and perfluorinated chemicals: a stud... | 2008 | cohort | NR/NR |
| 12 | 3380 | Maternal exposure to perfluoroalkyl acids measured in whole ... | 2016 | Observational cohort/analytical study of maternal PFAA exposure and birth outcomes | NR/NR |
| 13 | 3383 | Prenatal exposure to chlorinated polyfluoroalkyl ether sulfo... | 2019 | Observational exposure–response analysis using cord blood PFAS concentrations | NR/NR |
| 14 | 3410 | Maternal serum levels of perfluoroalkyl substances in early ... | 2020 | cohort | NR/NR |
| 15 | 3386 | Perfluorinated compounds in umbilical cord blood and adverse... | 2012 | Panel study (prospective birth cohort) | NR/NR |
| 16 | 70016 | The Association of Prenatal Exposure to Perfluorinated Chemi... | 2015 | Birth cohort (observational) | NR/NR |
| 17 | 3405 | Early-Pregnancy Plasma Concentrations of Perfluoroalkyl Subs... | 2018 | Cohort | NR/NR |
| 18 | 3406 | Perfluoroalkyl Mixture Exposure in Relation to Fetal Growth:... | 2022 | cohort | NR/NR |
| 19 | 88584 | Prenatal exposure to perfluoroalkyl and polyfluoroalkyl subs... | 2021 | cohort | NR/NR |
| 20 | 86865 | Association of Early Pregnancy Perfluoroalkyl and Polyfluoro... | 2023 | Prospective cohort | NR/NR |
| 21 | 88064 | Prenatal exposure to legacy and emerging PFAS and sex-specif... | 2025 | cohort | NR/NR |
| 22 | 88597 | Prenatal per- and polyfluoroalkyl substance mixtures and wei... | 2025 | Cohort | NR/NR |
| 23 | 86735 | Association between perfluorinated compound concentrations i... | 2016 | cross-sectional | NR/NR |
| 24 | 69991 | Prenatal exposure to per- and polyfluoroalkyl substances and... | 2019 | cohort | NR/NR |
| 25 | 3381 | Perfluoroalkyl substances in umbilical cord serum and gestat... | 2018 | cohort | NR/NR |
| 26 | 3397 | PFOS, PFOA, estrogen homeostasis, and birth size in Chinese ... | 2019 | cohort | NR/NR |
| 27 | 88826 | Does the timing of sample collection confound the associatio... | 2025 | prospective cohort | NR/NR |
| 28 | 3391 | Prenatal Exposure to Perfluorinated Compounds Affects Birth ... | 2016 | Observational cohort (inferred) | NR/NR |
| 29 | 88687 | Birth Outcomes in Relation to Prenatal Exposure to Per- and ... | 2023 | Prospective cohort (multi-cohort) | NR/NR |
| 30 | 3392 | Prenatal Phthalate, Perfluoroalkyl Acid, and Organochlorine ... | 2016 | cohort | NR/NR |


## 5. Study Characteristics

| Study | Design | Participants | Key Outcomes |
|-------|--------|--------------|--------------|
|  2017 | Observational cross-sectional analysis at birth (cord serum exposure vs. birth outcomes) | 0/0 | See extraction table |
|  2021 | Observational exposure-outcome analysis (specific design not reported) | 0/0 | See extraction table |
|  2016 | cohort | 0/0 | See extraction table |
|  2007 | cohort | 0/0 | See extraction table |
|  2018 | Prospective cohort | 0/0 | See extraction table |
|  2010 | Cohort | 0/0 | See extraction table |
|  2012 | cohort | 0/0 | See extraction table |
|  2012 | cohort | 0/0 | See extraction table |
|  2020 | Prospective birth cohort | 0/0 | See extraction table |
|  2009 | Prospective cohort | 0/0 | See extraction table |
|  2008 | cohort | 0/0 | See extraction table |
|  2016 | Observational cohort/analytical study of maternal PFAA exposure and birth outcomes | 0/0 | See extraction table |
|  2019 | Observational exposure–response analysis using cord blood PFAS concentrations | 0/0 | See extraction table |
|  2020 | cohort | 0/0 | See extraction table |
|  2012 | Panel study (prospective birth cohort) | 0/0 | See extraction table |
|  2015 | Birth cohort (observational) | 0/0 | See extraction table |
|  2018 | Cohort | 0/0 | See extraction table |
|  2022 | cohort | 0/0 | See extraction table |
|  2021 | cohort | 0/0 | See extraction table |
|  2023 | Prospective cohort | 0/0 | See extraction table |
|  2025 | cohort | 0/0 | See extraction table |
|  2025 | Cohort | 0/0 | See extraction table |
|  2016 | cross-sectional | 0/0 | See extraction table |
|  2019 | cohort | 0/0 | See extraction table |
|  2018 | cohort | 0/0 | See extraction table |
|  2019 | cohort | 0/0 | See extraction table |
|  2025 | prospective cohort | 0/0 | See extraction table |
|  2016 | Observational cohort (inferred) | 0/0 | See extraction table |
|  2023 | Prospective cohort (multi-cohort) | 0/0 | See extraction table |
|  2016 | cohort | 0/0 | See extraction table |

## 6. Statistical Analysis

- **Studies with extractable data:** 24
- **Effect measure:** OR

### Meta-Analysis Results

| Model | Effect | 95% CI | I² | p-value |
|-------|--------|-------|----|--------|
| Random effects | 0.887 | 0.728–1.082 | 74.4% | 0.000 |
| Fixed effects | 0.911 | 0.877–0.946 | - | - |

### Interpretation

- The pooled effect suggests the intervention is associated with decreased outcome
- **Heterogeneity:** Substantial (I² = 74.4%) - considerable variability

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 30

**Total participants:** Approximately 0 participants across all included studies

**Study design distribution:**

- cohort: 13 studies
- Prospective cohort: 3 studies
- Cohort: 3 studies
- Observational cross-sectional analysis at birth (cord serum exposure vs. birth outcomes): 1 studies
- Observational exposure-outcome analysis (specific design not reported): 1 studies
- Prospective birth cohort: 1 studies
- Observational cohort/analytical study of maternal PFAA exposure and birth outcomes: 1 studies
- Observational exposure–response analysis using cord blood PFAS concentrations: 1 studies
- Panel study (prospective birth cohort): 1 studies
- Birth cohort (observational): 1 studies
- cross-sectional: 1 studies
- prospective cohort: 1 studies
- Observational cohort (inferred): 1 studies
- Prospective cohort (multi-cohort): 1 studies

**Publication years:** 2007–2025

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
We included 30 observational studies (published 2007–2021) that examined associations between prenatal PFOS exposure and birth weight among pregnant women and their newborns. Designs spanned prospective birth cohorts, general cohort analyses, and cross-sectional analyses at birth using maternal or cord serum PFOS. Exact sample sizes were not consistently extractable from the available records (often N=NR/NR). Twenty-four studies contributed harmonized data to a meta-analysis (dichotomous outcome metrics), while several others reported continuous effects on birth weight in grams or standardized units that could not be pooled with the odds ratio (OR) metric.

### 7.2 Discussion of Findings
Across the 24 studies contributing to the pooled analysis, higher PFOS exposure was not significantly associated with altered odds of adverse birth-weight categories under a random-effects model (pooled OR=0.8872; 95% CI: 0.7276 to 1.0819; p=0.2371). Directionally, the point estimate is consistent with a modest inverse association (lower odds of being in a higher birth-weight category, or higher odds of low birth weight, depending on coding), but the confidence interval includes the null. Heterogeneity was substantial (I²=74.4%; τ²=0.058997), indicating important between-study differences that attenuate certainty in a uniform association. A fixed-effect model yielded a statistically significant, but modest, inverse association (OR=0.9108; 95% CI: 0.8765 to 0.9464), suggesting that small-study weighting and heterogeneity meaningfully affect inferences.

Individual studies reporting continuous birth-weight differences mainly pointed toward small-to-moderate inverse associations. Several cohorts reported decreases on the order of 100–150 g with higher PFOS: Unknown (2012) estimated −140 g (95% CI: −238 to −42); Unknown (2009) −148.8 g (95% CI: −297.0 to −0.5); and a more recent birth cohort, Unknown (2020), −96.2 g (95% CI: −165.3 to −27.1). One cord-blood analysis reported a larger reduction, Unknown (2019), at −417.3 g (95% CI: −742.1 to −92.4), albeit with a wide interval. Other analyses were closer to the null, e.g., Unknown (2010) −37.4 g (95% CI: −86.0 to 11.2) and Unknown (2016) −50.0 g (95% CI: −123.0 to 23.0). A small but statistically precise reduction was noted in an earlier cohort, Unknown (2007), −10.63 g (95% CI: −20.79 to −0.47). Some studies expressed effects in standardized units; Unknown (2008) reported a −0.069 change (95% CI: −0.113 to −0.024) in birth-weight z-score per unit exposure metric, and Unknown (2012) reported a −0.18 (95% CI: −0.41 to 0.05) standardized association. A minority of records presented odds ratios, e.g., Unknown (2016) OR=1.2528 (95% CI: 1.10 to 11.50) for a categorical birth-weight outcome, but effect codings and CIs were heterogeneous and sometimes internally inconsistent in the extracted summaries (e.g., Unknown (2012) OR=0.8961 with a CI reported as 1.47 to 4.08), underscoring reporting limitations.

The substantial heterogeneity likely reflects methodological diversity: exposure matrices (maternal serum during pregnancy versus cord serum at delivery), timing of sampling (early versus late gestation), exposure scaling (per ng/mL, ln-transformed, per IQR), outcome definition (continuous grams, z-scores, or binary low birth weight), and covariate adjustment (e.g., maternal smoking, parity, gestational age, socioeconomic factors). Residual confounding by gestational duration is a particular concern because PFOS may influence gestation length, which in turn affects birth weight; conversely, failure to disentangle fetal growth from prematurity can bias estimates toward an apparent PFOS–birth-weight relationship. Differences in co-exposures to other PFAS and mixtures may also contribute.

Formal risk-of-bias assessments were not available in the present extraction. Nonetheless, common threats in this literature include confounding (e.g., smoking, nutrition, socioeconomic status), selection related to cohort participation, and exposure misclassification. Cord-blood PFOS may better reflect late-gestation fetal exposure, whereas early-pregnancy maternal measures may capture different etiologically relevant windows; inconsistency in timing complicates synthesis. The divergence between fixed- and random-effects results, together with several near-null or modest inverse gram-level estimates, suggests that while an inverse association is plausible, it is not consistent across settings or analytical choices.

Author conclusions were not systematically available from the extracted records. Based on the direction and magnitude of estimates, many studies likely interpreted their findings as small inverse associations or null results, with a smaller subset reporting larger inverse associations. The pooled random-effects analysis aligns most closely with a cautious interpretation: evidence does not conclusively demonstrate an association when accounting for between-study variability, although multiple cohorts reported decreases in mean birth weight on the order of ~100 g per higher exposure, which may be relevant at a population level.

### 7.3 Risk of Bias Assessment
Not conducted: risk-of-bias information was not available in the extracted dataset for the included studies, precluding a structured appraisal.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Across 30 observational studies, the totality of evidence suggests that higher prenatal PFOS exposure is associated with small reductions in birth weight in several cohorts (e.g., −96 to −149 g, with one outlier at −417 g), but the pooled random-effects estimate for dichotomous outcomes was not statistically significant (OR=0.8872; 95% CI: 0.7276 to 1.0819; p=0.2371) amid substantial heterogeneity (I²=74.4%). Overall, the evidence points to a probable modest inverse association, but inconsistency and methodological diversity limit confidence in a definitive causal estimate.

### 8.2 Limitations
At the review level, several constraints affect inference. First, incomplete reporting in the available records (e.g., study identifiers and sample sizes listed as NR) limited our ability to quantify the aggregate population size and to perform subgroup and sensitivity analyses. Second, outcome harmonization was imperfect: the meta-analysis synthesized odds ratios from studies with dichotomized outcomes, while multiple included studies reported mean differences in grams or standardized scores that could not be pooled with the OR metric. Third, we were unable to perform a formal risk-of-bias assessment due to missing study-level details, and author conclusions were not consistently extractable. Finally, some studies had effects that were “not computable” in the dataset, reducing analytic coverage (24/30 contributed to the meta-analysis).

At the study level, the literature exhibits heterogeneity in exposure assessment (maternal vs cord serum; timing during gestation; transformation and scaling), outcome definitions (continuous vs categorical, z-scores vs grams), and covariate adjustment. Residual confounding—especially by gestational duration, smoking, parity, maternal BMI, and socioeconomic factors—remains a primary concern. Differences in co-exposure to other PFAS and environmental contaminants, potential selection bias in cohort participation, and exposure misclassification (temporal variability, laboratory variability) further limit precision and comparability. Geographic and temporal variability in PFOS exposure profiles and replacement chemicals may also influence transportability of findings.

### 8.3 Implications
For practice and policy: The evidence does not support a firm, clinically actionable threshold for PFOS-related birth-weight effects at the individual level. However, several cohorts report small reductions in mean birth weight associated with higher PFOS, and the fixed-effect synthesis suggests a modest inverse association. Given PFOS’s persistence and the potential for population-level impacts even with small individual-level effects, precautionary exposure reduction—consistent with existing environmental health guidance—remains reasonable. Clinicians should prioritize established determinants of birth weight (e.g., smoking cessation, nutrition) while recognizing PFAS exposure as a potential, albeit not definitively quantified, contributor.

For research: Future studies should standardize exposure and outcome reporting to enable robust synthesis. Key priorities include: reporting birth weight in grams alongside low-birth-weight risk; harmonized exposure metrics (e.g., per IQR and per doubling of PFOS), with clear timing of biospecimen collection; rigorous adjustment for gestational duration and modeling that separates prematurity from fetal growth; assessment of co-exposures and PFAS mixtures; and exploration of effect modification (e.g., infant sex, parity, maternal smoking). Large, well-characterized prospective cohorts with repeated exposure measures and transparent, pre-registered analytical plans are needed. Finally, coordinated individual participant data meta-analyses could reduce heterogeneity and clarify dose–response relationships, while investigations of contemporary PFOS alternatives are necessary to contextualize evolving exposure landscapes.

---

## References of Included Studies

1. Yu Shi, Lin Yang, Jingguang Li, et al. (2017). Occurrence of perfluoroalkyl substances in cord serum and association with growth indicators in newborns from Beijing.. *Chemosphere*.
   DOI: 10.1016/j.chemosphere.2016.11.050
   PMID: 27886542

2. Unknown (2021). Associations of Prenatal Exposure to Per- and Polyfluoroalkyl Substances with the Neonatal Birth Size and Hormones in the Growth Hormone/Insulin-Like Growth Factor Axis.. *Environmental science & technology*.
   DOI: 10.1021/acs.est.1c02670
   PMID: 34378915

3. Cathrine Carlsen Bach, Bodil Hammer Bech, Ellen Aagaard Nohr, et al. (2016). Perfluoroalkyl Acids in Maternal Serum and Indices of Fetal Growth: The Aarhus Birth Cohort.. *Environmental health perspectives*.
   DOI: 10.1289/ehp.1510046
   PMID: 26495857

4. Chunyuan Fei, Joseph K McLaughlin, Robert E Tarone, et al. (2007). Perfluorinated chemicals and fetal growth: a study within the Danish National Birth Cohort.. *Environmental health perspectives*.
   DOI: 10.1289/ehp.10506
   PMID: 18008003

5. Unknown (2018). Prenatal Exposure to Perfluoroalkyl Substances and Birth Outcomes; An Updated Analysis from the Danish National Birth Cohort.. *International journal of environmental research and public health*.
   DOI: 10.3390/ijerph15091832
   PMID: 30149566

6. Michele P Hamm, Nicola M Cherry, Emily Chan, et al. (2010). Maternal exposure to perfluorinated acids and fetal growth.. *Journal of exposure science & environmental epidemiology*.
   DOI: 10.1038/jes.2009.57
   PMID: 19865074

7. Kristina W Whitworth, Line S Haug, Donna D Baird, et al. (2012). Perfluorinated compounds in relation to birth weight in the Norwegian Mother and Child Cohort Study.. *American journal of epidemiology*.
   DOI: 10.1093/aje/kwr459
   PMID: 22517810

8. Mildred Maisonet, Metrecia L Terrell, Michael A McGeehin, et al. (2012). Maternal concentrations of polyfluoroalkyl compounds during pregnancy and fetal and postnatal growth in British girls.. *Environmental health perspectives*.
   DOI: 10.1289/ehp.1003096
   PMID: 22935244

9. Ikuko Kashino, Seiko Sasaki, Emiko Okada, et al. (2020). Prenatal exposure to 11 perfluoroalkyl substances and fetal growth: A large-scale, prospective birth cohort study.. *Environment international*.
   DOI: 10.1016/j.envint.2019.105355
   PMID: 32029284

10. Noriaki Washino, Yasuaki Saijo, Seiko Sasaki, et al. (2009). Correlations between prenatal exposure to perfluorinated chemicals and reduced fetal growth.. *Environmental health perspectives*.
   DOI: 10.1289/ehp.11681
   PMID: 19440508

11. Unknown (2008). Fetal growth indicators and perfluorinated chemicals: a study in the Danish National Birth Cohort.. *American journal of epidemiology*.
   DOI: 10.1093/aje/kwn095
   PMID: 18460444

12. A C Callan, A Rotander, K Thompson, et al. (2016). Maternal exposure to perfluoroalkyl acids measured in whole blood and birth outcomes in offspring.. *The Science of the total environment*.
   DOI: 10.1016/j.scitotenv.2016.06.177
   PMID: 27387804

13. Chenye Xu, Shanshan Yin, Yingxue Liu, et al. (2019). Prenatal exposure to chlorinated polyfluoroalkyl ether sulfonic acids and perfluoroalkyl acids: Potential role of maternal determinants and associations with birth outcomes.. *Journal of hazardous materials*.
   DOI: 10.1016/j.jhazmat.2019.120867
   PMID: 31330388

14. Sverre Wikström, Ping-I Lin, Christian H Lindh, et al. (2020). Maternal serum levels of perfluoroalkyl substances in early pregnancy and offspring birth weight.. *Pediatric research*.
   DOI: 10.1038/s41390-019-0720-1
   PMID: 31835271

15. Mei-Huei Chen, Eun-Hee Ha, Ting-Wen Wen, et al. (2012). Perfluorinated compounds in umbilical cord blood and adverse birth outcomes.. *PloS one*.
   DOI: 10.1371/journal.pone.0042474
   PMID: 22879996

16. Unknown (2015). The Association of Prenatal Exposure to Perfluorinated Chemicals with Maternal Essential and Long-Chain Polyunsaturated Fatty Acids during Pregnancy and the Birth Weight of Their Offspring: The Hokkaido Study.. *Environmental health perspectives*.
   DOI: 10.1289/ehp.1408834
   PMID: 25840032

17. Sharon K Sagiv, Sheryl L Rifas-Shiman, Abby F Fleisch, et al. (2018). Early-Pregnancy Plasma Concentrations of Perfluoroalkyl Substances and Birth Outcomes in Project Viva: Confounded by Pregnancy Hemodynamics?. *American journal of epidemiology*.
   DOI: 10.1093/aje/kwx332
   PMID: 29155920

18. Chensi Shen, Jiaxin Ding, Chenye Xu, et al. (2022). Perfluoroalkyl Mixture Exposure in Relation to Fetal Growth: Potential Roles of Maternal Characteristics and Associations with Birth Outcomes.. *Toxics*.
   DOI: 10.3390/toxics10110650
   PMID: 36355941

19. Unknown (2021). Prenatal exposure to perfluoroalkyl and polyfluoroalkyl substances and birth outcomes: A longitudinal cohort with repeated measurements.. *Chemosphere*.
   DOI: 10.1016/j.chemosphere.2020.128899
   PMID: 33220988

20. Unknown (2023). Association of Early Pregnancy Perfluoroalkyl and Polyfluoroalkyl Substance Exposure With Birth Outcomes.. *JAMA network open*.
   DOI: 10.1001/jamanetworkopen.2023.14934
   PMID: 37256622

21. Unknown (2025). Prenatal exposure to legacy and emerging PFAS and sex-specific associations with fetal growth: Evidence from a Chinese birth cohort.. *Environmental research*.
   DOI: 10.1016/j.envres.2025.122488
   PMID: 40752556

22. Unknown (2025). Prenatal per- and polyfluoroalkyl substance mixtures and weight for length from birth to 12 months: The New Hampshire Birth Cohort Study.. *The Science of the total environment*.
   DOI: 10.1016/j.scitotenv.2025.179446
   PMID: 40311330

23. Unknown (2016). Association between perfluorinated compound concentrations in cord serum and birth weight using multiple regression models.. *Reproductive toxicology (Elmsford, N.Y.)*.
   DOI: 10.1016/j.reprotox.2015.10.020
   PMID: 26562669

24. Unknown (2019). Prenatal exposure to per- and polyfluoroalkyl substances and infant growth and adiposity: the Healthy Start Study.. *Environment international*.
   DOI: 10.1016/j.envint.2019.104983
   PMID: 31284113

25. Wencheng Cao, Xiao Liu, Xiaofang Liu, et al. (2018). Perfluoroalkyl substances in umbilical cord serum and gestational and postnatal growth in a Chinese birth cohort.. *Environment international*.
   DOI: 10.1016/j.envint.2018.04.015
   PMID: 29698896

26. Hexing Wang, Hongyi Du, Jiaqi Yang, et al. (2019). PFOS, PFOA, estrogen homeostasis, and birth size in Chinese infants.. *Chemosphere*.
   DOI: 10.1016/j.chemosphere.2019.01.061
   PMID: 30641376

27. Unknown (2025). Does the timing of sample collection confound the association between prenatal serum PFAS concentrations and birthweight: results from two prospective cohort studies.. *Environment international*.
   DOI: 10.1016/j.envint.2025.109990
   PMID: 41380244

28. Eun Jin Kwon, Joon Soo Shin, Byung Mi Kim, et al. (2016). Prenatal Exposure to Perfluorinated Compounds Affects Birth Weight Through GSTM1 Polymorphism.. *Journal of occupational and environmental medicine*.
   DOI: 10.1097/JOM.0000000000000739
   PMID: 27206125

29. Unknown (2023). Birth Outcomes in Relation to Prenatal Exposure to Per- and Polyfluoroalkyl Substances and Stress in the Environmental Influences on Child Health Outcomes (ECHO) Program.. *Environmental health perspectives*.
   DOI: 10.1289/EHP10723
   PMID: 36920051

30. Virissa Lenters, Lützen Portengen, Anna Rignell-Hydbom, et al. (2016). Prenatal Phthalate, Perfluoroalkyl Acid, and Organochlorine Exposures and Term Birth Weight in Three Birth Cohorts: Multi-Pollutant Models Based on Elastic Net Regression.. *Environmental health perspectives*.
   DOI: 10.1289/ehp.1408933
   PMID: 26115335


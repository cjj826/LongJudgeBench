# AutoMeta Systematic Review Report

**Paper ID:** 301 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 11:34:58

---

## Executive Summary

- **Research Question:** Newborns and young infants up to 59 days of age fr... | Home visits by trained community health workers (C...
- **Studies Included:** 4 of 125 screened
- **Study Summary:** Four studies (2011–2016) from LMIC settings evaluated CHW postnatal home visits; three contributed to a meta-analysis of facility care-seeking with a pooled RR 1.2379 (95% CI 0.8036–1.9071; p=0.333) and very high heterogeneity. No included study reported sensitivity/specificity for CHW identification of serious illness, leaving a key evidence gap on diagnostic accuracy.

## 1. Research Question

**P (Population):** Newborns and young infants up to 59 days of age from low- and middle-income countries

**I (Intervention):** Home visits by trained community health workers (CHWs)

**C (Comparison):** Standard care or control group without home visits by community health workers

**O (Outcome):** Identification of serious illness (sensitivity and specificity) and care seeking from health facilities

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | ("Infant, Newborn"[Mesh] OR "Infant"[Mesh] OR newborn*[tiab] OR neonat*[tiab] OR infant*[tiab] OR "young infant*"[tiab] OR "0-59 day*"[tiab] OR "0 to ... |
| 2 | ("Infant, Newborn"[Mesh] OR newborn*[tiab] OR neonat*[tiab] OR "young infant*"[tiab]) AND ("Community Health Workers"[Mesh] OR "community health worke... |
| 3 | (newborn*[tiab] OR neonat*[tiab] OR "young infant*"[tiab] OR "0-59 day*"[tiab] OR "0 to 59 day*"[tiab] OR "0-2 month*"[tiab] OR "0 to 2 month*"[tiab])... |
| 4 | (("Infant, Newborn"[Mesh] OR "Infant"[Mesh]) AND "Community Health Workers"[Mesh] AND ("Home Visits"[Mesh] OR "Home Care Services"[Mesh]) AND ("Help-S... |
| 5 | (("newborn"[tiab] OR neonat*[tiab] OR "young infant*"[tiab] OR "0-59 day*"[tiab] OR "0 to 59 day*"[tiab] OR "0-2 month*"[tiab] OR "0 to 2 month*"[tiab... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 125 |
| After deduplication | 125 |
| Screened (title/abstract) | 125 |
| Excluded | 121 |
| Full-text assessed | 4 |
| **Included in synthesis** | **4** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- No concurrent control group without CHW home visits (12 studies)
- Does not report relevant infant outcomes (diagnostic accuracy of serious illness identification or care-seeking) (7 studies)
- No home-visit component by community health workers. (4 studies)
- Does not report relevant infant outcomes (diagnostic accuracy or care-seeking). (4 studies)
- No CHW home-visit component (3 studies)
- No concurrent control group (observational study). (2 studies)
- Does not report relevant infant outcomes (protocol; no diagnostic accuracy or care-seeking). (2 studies)
- Population not limited to newborns or young infants 0–59 days (1 studies)
- No home-visit component by CHWs (facility-focused EmONC project). (1 studies)
- No home-visit component by CHWs and not a controlled trial (narrative review of maternity waiting homes). (1 studies)

## 3. Included Studies

**Total included:** 4

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 7792 | Improvement of perinatal and newborn care in rural Pakistan ... | 2011 | Cluster randomised effectiveness trial | 12391/11443 |
| 2 | 7814 | Effect of the Newhints home-visits intervention on neonatal ... | 2013 | Cluster randomised controlled trial | NR/NR |
| 3 | 46285 | Increasing access to care for sick newborns: evidence from t... | 2016 | Prospective cohort nested within a cluster-randomised controlled trial | NR/NR |
| 4 | 7815 | Effect of implementation of integrated management of neonata... | 2014 | Cluster randomised trial | 6204/6163 |


## 5. Study Characteristics

| Study | Design | Participants | Key Outcomes |
|-------|--------|--------------|--------------|
|  2011 | Cluster randomised effectiveness trial | 12391/11443 | See extraction table |
|  2013 | Cluster randomised controlled trial | 0/0 | See extraction table |
|  2016 | Prospective cohort nested within a cluster-randomised controlled trial | 0/0 | See extraction table |
|  2014 | Cluster randomised trial | 6204/6163 | See extraction table |

## 6. Statistical Analysis

- **Studies with extractable data:** 3
- **Effect measure:** RR

### Meta-Analysis Results

| Model | Effect | 95% CI | I² | p-value |
|-------|--------|-------|----|--------|
| Random effects | 1.238 | 0.804–1.907 | 93.4% | 0.000 |
| Fixed effects | 0.983 | 0.903–1.070 | - | - |

### Interpretation

- The pooled effect suggests the intervention is associated with increased outcome (OR/RR/HR > 1)
- **Heterogeneity:** Considerable (I² = 93.4%) - high variability, interpret with caution

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 4

**Total participants:** Approximately 36,201 participants across all included studies

**Study design distribution:**

- Cluster randomised effectiveness trial: 1 studies
- Cluster randomised controlled trial: 1 studies
- Prospective cohort nested within a cluster-randomised controlled trial: 1 studies
- Cluster randomised trial: 1 studies

**Publication years:** 2011–2016

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
Four studies met inclusion criteria (2011–2016), spanning cluster randomised trials (n=3) and one prospective cohort nested within a cluster trial (n=1). Two trials reported arm sizes: 2011 cluster effectiveness trial (n=12,391 vs 11,443) and a 2014 cluster trial (n=6,204 vs 6,163); the remaining two studies (2013; 2016) did not report sample sizes in the extraction. Quantitative synthesis was possible for care-seeking from health facilities in three studies. No included study contributed sensitivity/specificity data for CHW identification of serious illness; diagnostic accuracy could not be meta-analysed, representing a major evidence gap.

### 7.2 Discussion of Findings
Across the three studies with meta-analysable data, the random-effects pooled risk ratio (RR) for care-seeking from facilities comparing CHW home visits versus standard care was 1.2379 (95% CI 0.8036 to 1.9071; p=0.3330), indicating no statistically significant effect but a point estimate consistent with a possible increase in care-seeking. Considerable heterogeneity was present (I²=93.4%; τ²=0.128803). In contrast, the fixed-effects model yielded RR 0.9828 (95% CI 0.9026 to 1.0702), suggesting a null effect when larger studies are given more weight. This divergence implies that small-to-medium trials with larger apparent effects favor increased care-seeking, whereas larger trials attenuate the average effect toward no difference.

At the individual study level, one large 2011 cluster trial reported a log RR of −0.1625, corresponding to RR≈0.85 with a 95% CI of 0.76 to 0.96. If the outcome was “any facility care-seeking,” this would suggest fewer facility visits with CHW home visits; if the outcome was “failure to seek care,” it would indicate benefit. Given the extraction lacks the outcome directionality, the safest interpretation is that this trial showed a statistically significant difference between arms (RR approximately 0.85) but in the opposite direction to two later trials. A 2013 cluster RCT reported log RR 0.3328 (RR≈1.40; 95% CI 1.17 to 1.66), and a 2014 cluster trial reported log RR 0.5653 (RR≈1.76; 95% CI 1.38 to 2.24), both consistent with increased care-seeking associated with CHW home visits. The 2016 nested cohort reported a small positive effect (log RR 0.1000; RR≈1.11) but did not provide variance estimates and was not included in the pooled analysis.

The substantial heterogeneity likely reflects real differences in intervention content (e.g., timing and frequency of postnatal visits, CHW training and supervision, presence of referral facilitation), baseline care-seeking norms, and outcome definitions (care-seeking for any illness vs possible serious bacterial infection; first visit vs any visit; timeliness). Measurement differences (surveillance schedules, reliance on caregiver report vs health facility records) may also contribute. The fixed- vs random-effects discrepancy suggests small-study effects; however, with only three studies in the meta-analysis, we cannot reliably assess publication bias.

We could not extract the original authors’ conclusions for the four studies; thus, we cannot triangulate our synthesis against study-level interpretations. Nevertheless, the pattern of effect sizes suggests that at least two trials judged their findings as supportive of increased care-seeking with CHW home visits (RRs ≈1.40 and ≈1.76 with CIs excluding 1), whereas one large trial likely concluded no benefit or a reduction in the measured outcome (RR≈0.85, CI excluding 1). Without standardized outcome definitions and reported author narratives, we caution against over-interpretation.

Critically, none of the included studies provided data on the diagnostic accuracy of CHWs’ home-based identification of serious illness in newborns and young infants (sensitivity/specificity against a competent clinical reference). This is central to the PICO and limits inference about whether home visits improve recognition and appropriate referral, versus merely altering care-seeking behavior.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Evidence from four studies in low- and middle-income settings provides mixed and imprecise estimates of the effect of CHW home visits on care-seeking from health facilities. The random-effects pooled RR was 1.2379 (95% CI 0.8036 to 1.9071; p=0.3330), with considerable heterogeneity, while the fixed-effects estimate was 0.9828 (95% CI 0.9026 to 1.0702). No included study contributed diagnostic accuracy (sensitivity/specificity) data for CHW identification of serious illness. Overall, current evidence does not permit confident conclusions about the impact of CHW postnatal home visits on either accurate detection of serious illness or consistent increases in care-seeking.

### 8.2 Limitations
Review-level limitations include incomplete extraction of key study characteristics (e.g., settings, detailed intervention components, precise outcome definitions), missing sample sizes for two trials, and absence of risk-of-bias assessments. We could not retrieve author conclusions, impeding comparison between our synthesis and original interpretations. With only three studies contributing to the meta-analysis and very high between-study heterogeneity, pooled estimates are unstable; we did not assess small-study or publication bias.

Study-level limitations likely include variability in intervention fidelity (number/timing of home visits, training and supervision intensity), potential contamination across clusters, and diverse contextual baselines for care-seeking. Outcome measurement may have varied (any illness vs serious illness; first vs any facility contact; timeliness), and ascertainment methods (caregiver recall vs facility records) could introduce misclassification. Critically, none of the studies reported sensitivity and specificity of CHW assessments against a clinical reference standard, precluding conclusions about diagnostic accuracy.

### 8.3 Implications
For practice: Given the inconsistent and heterogeneous effects on facility care-seeking and the absence of diagnostic accuracy data, current evidence does not support a universal expectation that CHW home visits alone will reliably increase appropriate care-seeking for newborns and young infants in LMICs. Programs considering scale-up should emphasize robust training, supervision, and explicit referral pathways, and monitor local care-seeking and timeliness outcomes. Where resources are constrained, integrating CHW home visits with community engagement and facility readiness improvements may be more effective than stand-alone home visit programs.

For research: Priority gaps include well-designed cluster randomised trials that (a) prespecify and standardize care-seeking outcomes (including timeliness and referral completion), (b) report diagnostic accuracy of CHW assessments for serious illness versus a competent clinical reference (sensitivity, specificity, and predictive values), and (c) detail intervention fidelity, supervision, and linkage to facilities. Trials should report arm-specific sample sizes, intracluster correlation coefficients, and process measures to enable interpretation of heterogeneity. Stratified analyses by age (0–6 days vs 7–59 days), birth setting, and socioeconomic status, as well as assessment of potential unintended consequences (unnecessary facility visits or delayed care), are needed. Mixed-methods studies alongside trials can elucidate mechanisms (recognition, perceived severity, access barriers) and contextual moderators of effect.

---

## References of Included Studies

1. Zulfiqar A Bhutta, Sajid Soofi, Simon Cousens, et al. (2011). Improvement of perinatal and newborn care in rural Pakistan through community-based strategies: a cluster-randomised effectiveness trial.. *Lancet (London, England)*.
   DOI: 10.1016/S0140-6736(10)62274-X
   PMID: 21239052

2. Betty R Kirkwood, Alexander Manu, Augustinus H A ten Asbroek, et al. (2013). Effect of the Newhints home-visits intervention on neonatal mortality rate and care practices in Ghana: a cluster randomised controlled trial.. *Lancet (London, England)*.
   DOI: 10.1016/S0140-6736(13)60095-1
   PMID: 23578528

3. Unknown (2016). Increasing access to care for sick newborns: evidence from the Ghana Newhints cluster-randomised controlled trial.. *BMJ open*.
   DOI: 10.1136/bmjopen-2015-008107
   PMID: 27297006

4. Sarmila Mazumder, Sunita Taneja, Rajiv Bahl, et al. (2014). Effect of implementation of integrated management of neonatal and childhood illness programme on treatment seeking practices for morbidities in infants: cluster randomised trial.. *BMJ (Clinical research ed.)*.
   DOI: 10.1136/bmj.g4988
   PMID: 25172514


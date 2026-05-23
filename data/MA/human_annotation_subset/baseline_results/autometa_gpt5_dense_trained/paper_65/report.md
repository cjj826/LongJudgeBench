# AutoMeta Systematic Review Report

**Paper ID:** 65 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 07:21:24

---

## Executive Summary

- **Research Question:** Women with polycystic ovary syndrome (PCOS)... | ...
- **Studies Included:** 7 of 104 screened
- **Study Summary:** Seven studies (≥903 women plus one cohort with NR) evaluated neck circumference and metabolic outcomes in PCOS. The only pooled analysis (two studies) found no association between NC and HOMA-IR among relatively lean women (beta −0.1036; 95% CI −1.8403 to 1.6330; p=0.9069) with high heterogeneity (I²=93.8%). Overall, evidence is inconsistent and insufficient to support neck circumference as an independent metabolic risk marker in PCOS.

## 1. Research Question

**P (Population):** Women with polycystic ovary syndrome (PCOS)

**I (Intervention):** N/A

**C (Comparison):** Non-PCOS healthy controls; women with smaller neck circumference

**O (Outcome):** Neck circumference values, metabolic syndrome prevalence, insulin resistance (HOMA-IR, HOMA%S, fasting insulin), anthropometric measurements (waist circumference, hip circumference), blood pressure, lipid values (triglycerides), and glucose metabolism parameters

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | (("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome[tiab] OR polycystic ovarian syndrome[tiab] OR PCOS[tiab] OR "Stein-Leventhal"[tiab] O... |
| 2 | (("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome[tiab] OR PCOS[tiab] OR "Stein-Leventhal"[tiab]) AND ("neck circumference"[tiab] OR "n... |
| 3 | (("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome[tiab] OR PCOS[tiab]) AND ("neck circumference"[tiab] OR "neck girth"[tiab] OR "neck s... |
| 4 | (("Polycystic Ovary Syndrome"[Mesh] OR polycystic ovary syndrome[tiab] OR PCOS[tiab]) AND (("neck circumference"[tiab] OR "neck girth"[tiab] OR "neck ... |
| 5 | (("Polycystic Ovary Syndrome"[Mesh] OR PCOS[tiab] OR polycystic ovary syndrome[tiab]) AND ("neck circumference"[tiab] OR "neck girth"[tiab] OR "neck s... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 104 |
| After deduplication | 104 |
| Screened (title/abstract) | 104 |
| Excluded | 97 |
| Full-text assessed | 7 |
| **Included in synthesis** | **7** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- Not a PCOS population. (6 studies)
- Review article; not an observational study with extractable comparative data. (2 studies)
- No appropriate comparator (PCOS-only sample; not stratified by neck circumference and no healthy controls). (2 studies)
- No appropriate comparator (PCOS-only sample; not neck-circumference–based and no healthy controls). (2 studies)
- General adult population; no PCOS group or required comparator. (2 studies)
- Review article (non-observational); excluded per criteria. (2 studies)
- No appropriate comparator; only PCOS cohort without non-PCOS controls or neck-circumference–defined subgroups. (1 studies)
- No appropriate comparator; only PCOS cohort with associations/ROC analyses, not non-PCOS controls or NC-based subgroups. (1 studies)
- Population not limited to women with PCOS; general adult population. (1 studies)
- No appropriate comparator; PCOS-only association analysis without non-PCOS controls or NC-defined subgroups. (1 studies)

## 3. Included Studies

**Total included:** 7

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 46555 | Progression of glucose intolerance and cardiometabolic risk ... | 2019 | case-control | 199/225 |
| 2 | 4551 | Upper trunk fat assessment and its relationship with metabol... | 2011 | Cross-sectional observational (comparative with matched healthy controls) | 30/15 |
| 3 | 18614 | Adolescent PCOS and metabolic health: An analysis of fat, mu... | 2025 | cross-sectional case-control | 69/63 |
| 4 | 46631 | Higher Visceral and Lower Peripheral Adiposity Characterize ... | 2025 | Cross-sectional comparative study | 25/139 |
| 5 | 18755 | Adolescent "Lean PCOS" Is Characterized by Higher Insulin Re... | 2025 | Cohort (population-based longitudinal prebirth cohort; observational analysis at mid-teen visit) | NR/NR |
| 6 | 47074 | Polycystic Ovary Syndrome and Metabolic Syndrome: Clinical a... | 2022 | Cross-sectional comparative (matched by age and BMI) | 50/50 |
| 7 | 18622 | Insulin Resistance, Hyperinsulinemia, and Mitochondria Dysfu... | 2017 | Cross-sectional comparative study | 18/20 |


## 5. Study Characteristics

| Study | Design | Participants | Key Outcomes |
|-------|--------|--------------|--------------|
|  2019 | case-control | 199/225 | See extraction table |
|  2011 | Cross-sectional observational (comparative with matched healthy controls) | 30/15 | See extraction table |
|  2025 | cross-sectional case-control | 69/63 | See extraction table |
|  2025 | Cross-sectional comparative study | 25/139 | See extraction table |
| unknown 0 | Cohort (population-based longitudinal prebirth cohort; observational analysis at mid-teen visit) | 0/0 | See extraction table |
|  2022 | Cross-sectional comparative (matched by age and BMI) | 50/50 | See extraction table |
|  2017 | Cross-sectional comparative study | 18/20 | See extraction table |

## 6. Statistical Analysis

- **Studies with extractable data:** 2
- **Effect measure:** BETA (LINEAR REGRESSION; HOMA-IR, BMI <85TH PERCENTILE SUBGROUP)

### Meta-Analysis Results

| Model | Effect | 95% CI | I² | p-value |
|-------|--------|-------|----|--------|
| Random effects | -0.104 | -1.840–1.633 | 93.8% | 0.000 |
| Fixed effects | 0.087 | -0.333–0.506 | - | - |

### Interpretation

- **Heterogeneity:** Considerable (I² = 93.8%) - high variability, interpret with caution

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 7

**Total participants:** Approximately 903 participants across all included studies

**Study design distribution:**

- Cross-sectional comparative study: 2 studies
- case-control: 1 studies
- Cross-sectional observational (comparative with matched healthy controls): 1 studies
- cross-sectional case-control: 1 studies
- Cohort (population-based longitudinal prebirth cohort; observational analysis at mid-teen visit): 1 studies
- Cross-sectional comparative (matched by age and BMI): 1 studies

**Publication years:** 2011–2025

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
Seven primary observational studies met inclusion criteria from 104 screened records (final included n=7). Six were cross-sectional comparative or case–control studies and one was an observational analysis within a population-based longitudinal cohort. Publication years ranged from 2011 to 2025. Across the six comparative studies with reported sample sizes, at least 903 women were included (PCOS n=391; non-PCOS controls n=512), with one additional cohort analysis reporting non-reported numbers (NR/NR). Comparators included healthy non-PCOS controls or, in some analyses, subgroups defined by neck circumference (NC). Outcomes spanned NC values, insulin resistance indices (e.g., HOMA-IR, HOMA%S, fasting insulin), anthropometrics (waist and hip circumferences), blood pressure, triglycerides, and glucose metabolism parameters. Effect metrics were heterogeneous; several studies did not report computable effects, and only two studies contributed compatible data for a quantitative synthesis focused on linear regression betas relating NC to HOMA-IR in a BMI <85th percentile subgroup.

### 7.2 Discussion of Findings
The only harmonized quantitative analysis available pooled two studies reporting linear regression betas for the association between NC and HOMA-IR among women below the 85th BMI percentile. The random-effects estimate indicated no association (pooled beta −0.1036; 95% CI −1.8403 to 1.6330; p=0.9069). Heterogeneity was considerable (I²=93.8%; τ²=1.4738). A fixed-effects model yielded a small, non-significant positive estimate (0.0868; 95% CI −0.3326 to 0.5062). The divergence between random- and fixed-effects results, combined with the wide random-effects confidence interval, underscores instability driven by between-study differences and small numbers. On balance, available evidence does not support a consistent independent relationship between NC and HOMA-IR in relatively lean women in these datasets.

Outside of this specific subgroup meta-analysis, individual study results were directionally inconsistent. Among studies reporting an effect size, point estimates varied: 0.6200 (2011, N=30/15), 0.7700 (95% CI 0.2300 to 1.3000; cohort analysis, year NR), 1.4207 (2022, N=50/50), and −1.0023 (95% CI −1.6777 to −0.3268; 2017, N=18/20). Although the underlying scales are not uniform across studies (and some effects may represent different constructs, e.g., cross-sectional differences vs regression coefficients), the observed spread—including a statistically significant inverse association in one small study (2017) and larger positive associations in others—suggests that both the magnitude and direction of association between NC and metabolic outcomes vary by study context, population, and analytic approach. Two additional comparative studies with larger samples (2019, N=199/225; 2025, N=69/63; 2025, N=25/139) reported results that were “not computable” in the current extract, further limiting quantitative synthesis.

Potential explanations for heterogeneity include differences in matching and adjustment (e.g., one study explicitly matched PCOS and controls on age and BMI; 2022, N=50/50), varying PCOS diagnostic criteria, ethnic composition, NC measurement protocols, and whether analyses were adjusted for adiposity (BMI, waist circumference) that could mediate or confound NC–metabolic relationships. Particularly, if NC primarily captures upper-body adiposity, lack of consistent adjustment for central adiposity could inflate associations in some studies and attenuate them in others. The very high I² (93.8%) in the pooled HOMA-IR subgroup analysis signals that summary estimates across studies should be interpreted cautiously.

Author conclusions were not consistently available in the extract, preventing direct comparison of our synthesis with study authors’ interpretations. Given the mix of positive and negative effects, it is likely that original reports varied in their conclusions, with some emphasizing NC as a simple proxy marker for metabolic risk in PCOS and others finding limited or no independent association after accounting for adiposity. Without standardized reporting, we cannot adjudicate these differences. Importantly, we identified no extractable, harmonized data to meta-analyze other outcomes of interest (metabolic syndrome prevalence, triglycerides, blood pressure, glucose indices beyond HOMA-IR, or between-group differences in NC values), despite these outcomes being listed as measured in several included studies.

Finally, the screening process indicates a broader literature exists on NC and metabolic risk in PCOS, but many studies were excluded for lacking appropriate comparators (e.g., PCOS-only cohorts without non-PCOS controls or without NC-defined subgroups) or for being interventional or population-wide rather than PCOS-specific. This pattern suggests that while NC has been studied within PCOS cohorts, comparative evidence isolating the incremental value of NC relative to standard anthropometrics remains limited.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Across seven included studies (≥903 participants plus one cohort with NR), the evidence linking neck circumference to metabolic risk in PCOS is inconsistent and heterogeneous. In the only harmonized quantitative comparison available—linear regression betas of NC with HOMA-IR among women below the 85th BMI percentile—the pooled association was null (beta −0.1036; 95% CI −1.8403 to 1.6330; p=0.9069) with very high heterogeneity (I²=93.8%). Given the variability in effect directions and the limited availability of comparable data, there is insufficient evidence to conclude that NC is an independent marker of insulin resistance or broader metabolic dysfunction in PCOS.

### 8.2 Limitations
Review-level limitations include reliance on a local corpus and extracted summaries that did not consistently provide computable effect sizes or author conclusions. A formal risk-of-bias assessment was not performed, and we could meta-analyze only two studies for a single outcome/subgroup. Outcome heterogeneity, differences in effect metrics, and incomplete reporting precluded synthesis for key endpoints (metabolic syndrome prevalence, triglycerides, blood pressure, glucose measures beyond HOMA-IR) and for between-group differences in NC values.

Study-level limitations likely include predominant cross-sectional designs, modest sample sizes in several studies (e.g., N=18/20; 2017), potential selection bias, and inconsistent matching or adjustment for adiposity (BMI, waist circumference) and other confounders. Variation in PCOS diagnostic criteria, NC measurement protocols, and population characteristics (age, ethnicity) further limits comparability and may account for the observed heterogeneity. The single matched study (2022, N=50/50) suggests attempts to control for key confounders, but the broader evidence set does not allow firm inferences about independence from overall adiposity.

### 8.3 Implications
For practice: Current evidence does not support using neck circumference as a standalone or superior screening tool for insulin resistance or metabolic syndrome in women with PCOS. Clinicians should continue to rely on established risk markers and assessments—BMI, waist circumference, blood pressure, fasting lipids, and glucose/insulin indices—while recognizing that NC may reflect upper-body adiposity but has not demonstrated consistent incremental value in this synthesis.

For research: Future studies should be adequately powered, pre-registered, and prospectively designed, with standardized NC measurement protocols and clear PCOS diagnostic criteria. Analyses should:
- Include both PCOS and rigorously matched non-PCOS controls and, where relevant, NC-defined subgroups.
- Adjust for BMI and waist circumference to test the independence of NC associations.
- Report harmonized effect measures (e.g., regression betas with common scaling, or odds ratios for metabolic syndrome) and provide full model specifications.
- Evaluate predictive performance (ROC/AUC, calibration, net reclassification improvement) and determine clinically meaningful NC thresholds across BMI strata and ethnicities.
- Examine a broader range of outcomes (metabolic syndrome prevalence, triglycerides, blood pressure, fasting insulin, HOMA%S, glucose tolerance) with consistent reporting to enable meta-analysis.
Such work is needed to clarify whether NC offers incremental risk stratification beyond standard anthropometrics in PCOS.

---

## References of Included Studies

1. Unknown (2019). Progression of glucose intolerance and cardiometabolic risk factors over a decade in Chinese women with polycystic ovary syndrome: A case-control study.. *PLoS medicine*.
   DOI: 10.1371/journal.pmed.1002953
   PMID: 31652273

2. F R O Penaforte, C C Japur, R W Diez-Garcia, et al. (2011). Upper trunk fat assessment and its relationship with metabolic and biochemical variables and body fat in polycystic ovary syndrome.. *Journal of human nutrition and dietetics : the official journal of the British Dietetic Association*.
   DOI: 10.1111/j.1365-277X.2010.01130.x
   PMID: 21210872

3. Unknown (2025). Adolescent PCOS and metabolic health: An analysis of fat, muscle, and hormones.. *European journal of obstetrics, gynecology, and reproductive biology*.
   DOI: 10.1016/j.ejogrb.2025.114648
   PMID: 40818213

4. Unknown (2025). Higher Visceral and Lower Peripheral Adiposity Characterize Fat Distribution and Insulin Resistance in Asian Indian Women with Polycystic Ovary Syndrome in Mauritius.. *Obesity facts*.
   DOI: 10.1159/000543332
   PMID: 39864429

5. Unknown (2025). Adolescent "Lean PCOS" Is Characterized by Higher Insulin Resistance and Adverse Adipokine Profile.. *The Journal of clinical endocrinology and metabolism*.
   DOI: 10.1210/clinem/dgaf606
   PMID: 41358924

6. Unknown (2022). Polycystic Ovary Syndrome and Metabolic Syndrome: Clinical and Laboratory Findings and Non-Alcoholic Fatty Liver Disease Assessed by Elastography.. *Revista brasileira de ginecologia e obstetricia : revista da Federacao Brasileira das Sociedades de Ginecologia e Obstetricia*.
   DOI: 10.1055/s-0041-1741032
   PMID: 35576937

7. Unknown (2017). Insulin Resistance, Hyperinsulinemia, and Mitochondria Dysfunction in Nonobese Girls With Polycystic Ovarian Syndrome.. *Journal of the Endocrine Society*.
   DOI: 10.1210/js.2017-00192
   PMID: 29264544


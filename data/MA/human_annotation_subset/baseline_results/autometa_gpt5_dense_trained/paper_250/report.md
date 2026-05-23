# AutoMeta Systematic Review Report

**Paper ID:** 250 | **Model:** gpt-5 | **Retrieval:** dense_trained
**Generated:** 2026-04-14 10:19:45

---

## Executive Summary

- **Research Question:** Adults with treatment-resistant depression who hav... | Various antidepressant treatments including electr...
- **Studies Included:** 6 of 120 screened
- **Study Summary:** Six placebo/sham-controlled RCTs in adult TRD were included (2014–2024), but only two (546 participants) provided extractable comparative data, reported as mean differences rather than the planned odds ratios for response. The random-effects meta-analysis was non-significant (MD -2.65; 95% CI -10.75 to 5.44; I²=94.8%), with one large RCT favoring the active intervention and one multicenter RCT showing no benefit. Overall, evidence is inconsistent and insufficient to support superiority of the studied interventions over placebo/sham on response in TRD.

## 1. Research Question

**P (Population):** Adults with treatment-resistant depression who have not responded to at least two antidepressant trials, excluding those with bipolar or psychotic depression

**I (Intervention):** Various antidepressant treatments including electroconvulsive therapy (ECT), minocycline, theta-burst stimulation (TBS), repetitive transcranial magnetic stimulation (rTMS), ketamine, aripiprazole, and other pharmacological and neuromodulatory treatments (25 separate treatments total)

**C (Comparison):** Placebo or sham treatment

**O (Outcome):** Response rate (primary outcome), with treatment effects measured as odds ratios

## 2. Search Strategy

### 2.1 Information Sources

- **Database:** Local corpus (dense_trained retrieval)
- **Retrieval Method:** Dense vector retrieval with BGE model
- **Search Date:** 2026-04-14

### 2.2 Search Queries

**Number of queries generated:** 5

| # | Search Query |
|---|---------------|
| 1 | (("Treatment-Resistant Depression"[Mesh] OR (depress*[tiab] AND (treatment-resistant[tiab] OR "treatment resistant"[tiab] OR refractor*[tiab] OR resis... |
| 2 | (("Treatment-Resistant Depression"[Mesh] OR (depress*[tiab] AND (treatment-resistant[tiab] OR "treatment resistant"[tiab] OR refractor*[tiab] OR resis... |
| 3 | (("Treatment-Resistant Depression"[Mesh] OR (depress*[tiab] AND (treatment-resistant[tiab] OR "treatment resistant"[tiab] OR TRD[tiab] OR refractor*[t... |
| 4 | (("Treatment-Resistant Depression"[Mesh] OR (depress*[tiab] AND (treatment-resistant[tiab] OR "treatment resistant"[tiab] OR TRD[tiab] OR refractor*[t... |
| 5 | (("Depressive Disorder, Major"[Mesh] OR "Depression"[Mesh] OR depress*[tiab]) AND (treatment-resistant[tiab] OR "treatment resistant"[tiab] OR refract... |

**Query Strategy:**

- Queries were generated using an LLM based on the PICO question
- Each query combines MeSH terms, free-text synonyms, and Boolean operators
- Queries cover different facets: population variants, intervention synonyms, outcome measures
- Both broad (high recall) and narrow (high precision) queries were included

## 3. Study Selection (PRISMA Flow)

| Stage | Count |
|-------|-------|
| Records retrieved | 120 |
| After deduplication | 120 |
| Screened (title/abstract) | 120 |
| Excluded | 114 |
| Full-text assessed | 6 |
| **Included in synthesis** | **6** |

### Screening Criteria and Exclusion Reasons

**Top exclusion reasons:**

- Bipolar depression population; not unipolar non-psychotic TRD. (4 studies)
- Systematic review; not an original randomized placebo/sham-controlled trial. (3 studies)
- Review article; not a randomized placebo/sham-controlled trial. (3 studies)
- Narrative review; not a randomized placebo/sham-controlled trial (3 studies)
- TRD criteria (failure of ≥2 adequate antidepressant trials) not clearly defined/reportable for the analyzed sample. (2 studies)
- Review article; no randomized placebo/sham-controlled trial data. (2 studies)
- Systematic review/network meta-analysis; not an original randomized placebo/sham-controlled trial. (1 studies)
- Narrative review; not a randomized placebo/sham-controlled trial. (1 studies)
- Retrospective naturalistic chart review; non-randomized and lacks placebo/sham control. (1 studies)
- Population focuses on bipolar disorder; not unipolar non-psychotic TRD. (1 studies)

## 3. Included Studies

**Total included:** 6

| # | Corpus ID | Study | Year | Design | N (Int/Ctrl) |
|---|-----------|-------|------|--------|---------------|
| 1 | 95365 | Oral esketamine in patients with treatment-resistant depress... | 2024 | Randomized, placebo-controlled trial with open-label extension | NR/NR |
| 2 | 95186 | Esketamine Monotherapy in Adults With Treatment-Resistant De... | 2025 | RCT | 181/197 |
| 3 | 4238 | Efficacy and Safety of Intranasal Esketamine Adjunctive to O... | 2018 | Randomized, double-blind, placebo-controlled, phase 2 trial with doubly randomized delayed-start design | NR/NR |
| 4 | 4261 | Efficacy of prefrontal theta-burst stimulation in refractory... | 2014 | RCT | NR/NR |
| 5 | 4239 | Efficacy and safety of fixed doses of intranasal Esketamine ... | 2021 | Randomized, double-blind, placebo-controlled (Phase 2b) with a 4-week induction phase | NR/NR |
| 6 | 95388 | Effect of Minocycline on Depressive Symptoms in Patients Wit... | 2022 | Randomized clinical trial (multicenter RCT) | 81/87 |


## 5. Study Characteristics

| Study | Design | Participants | Key Outcomes |
|-------|--------|--------------|--------------|
|  2024 | Randomized, placebo-controlled trial with open-label extension | 0/0 | See extraction table |
| unknown 2024 | RCT | 181/197 | See extraction table |
|  2018 | Randomized, double-blind, placebo-controlled, phase 2 trial with doubly randomized delayed-start design | 0/0 | See extraction table |
|  2014 | RCT | 0/0 | See extraction table |
|  2021 | Randomized, double-blind, placebo-controlled (Phase 2b) with a 4-week induction phase | 0/0 | See extraction table |
|  2022 | Randomized clinical trial (multicenter RCT) | 81/87 | See extraction table |

## 6. Statistical Analysis

- **Studies with extractable data:** 2
- **Effect measure:** MD

### Meta-Analysis Results

| Model | Effect | 95% CI | I² | p-value |
|-------|--------|-------|----|--------|
| Random effects | -2.653 | -10.748–5.441 | 94.8% | 0.000 |
| Fixed effects | -2.345 | -4.181–-0.509 | - | - |

### Interpretation

- The pooled effect shows a negative mean difference
- **Heterogeneity:** Considerable (I² = 94.8%) - high variability, interpret with caution

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence

**Total studies included:** 6

**Total participants:** Approximately 546 participants across all included studies

**Study design distribution:**

- RCT: 2 studies
- Randomized, placebo-controlled trial with open-label extension: 1 studies
- Randomized, double-blind, placebo-controlled, phase 2 trial with doubly randomized delayed-start design: 1 studies
- Randomized, double-blind, placebo-controlled (Phase 2b) with a 4-week induction phase: 1 studies
- Randomized clinical trial (multicenter RCT): 1 studies

**Publication years:** 2014–2024

### 7.2 Discussion of Findings

## 7. Results and Evidence Synthesis

### 7.1 Summary of Evidence
We identified six randomized placebo/sham-controlled trials in adults with treatment-resistant depression (TRD) published between 2014 and 2024. Interventions spanned both pharmacological and neuromodulatory modalities consistent with our a priori scope, although intervention identities and several trial-level details were incompletely reported for four studies. Two trials provided extractable comparative data for quantitative synthesis, encompassing 546 randomized participants across arms (N=181/197 in one RCT; N=81/87 in a multicenter RCT). For these two, effects were available as mean differences (MD) rather than the pre-specified odds ratios for response. The remaining four RCTs were included qualitatively due to non-computable outcomes. Given these constraints, the quantitative findings should be interpreted cautiously and viewed as provisional.

### 7.2 Discussion of Findings
The primary quantitative result from the two trials with extractable data showed no statistically significant effect under a random-effects model: pooled MD -2.6532 (95% CI -10.7478 to 5.4414), p=0.5206, with considerable heterogeneity (I²=94.8%, τ²=32.35). In contrast, a fixed-effects model suggested a small, statistically significant benefit favoring the active interventions (MD -2.3452; 95% CI -4.1811 to -0.5092). This divergence underscores the instability of the point estimate when between-study heterogeneity is high; with I² near 95%, the fixed-effects model is unlikely to be appropriate, and the random-effects result is the more defensible summary.

The two contributing trials pointed in different directions. One relatively large RCT (N=181/197) favored the active intervention with an MD of -6.80 (95% CI -9.48 to -4.07). The other multicenter RCT (N=81/87) did not show benefit (MD 1.46; 95% CI -1.04 to 3.96). Because the pre-specified outcome was response rate (ideally pooled as odds ratios) and the extracted effects were reported as mean differences, interpretation hinges on what the MD represents (e.g., symptom severity scale units versus absolute response-risk difference in percentage points) and on outcome directionality. If the MD pertains to a depressive symptom scale where lower scores indicate improvement, a negative MD would favor the intervention; if it represents risk difference for response, the sign has the opposite meaning. The dataset did not provide sufficient detail to disambiguate scale and direction across studies. Consequently, while the larger RCT appears to have found a statistically significant advantage for the active arm, the multicenter RCT did not, and the pooled random-effects estimate remains imprecise and non-significant.

Substantial heterogeneity likely reflects multiple sources: diversity of interventions (e.g., differing mechanisms across pharmacotherapies and neuromodulation), variation in TRD staging and inclusion criteria, short induction phases in some trials (e.g., 4 weeks), and differential placebo/sham responses typical in depression trials. Trial-level methodological differences—such as blinding integrity (especially in neuromodulation and ketamine-like interventions), outcome ascertainment windows, background treatment allowances, and site effects in multicenter designs—may also contribute. Without consistent reporting of responder definitions, baseline severity, or concomitant therapies, we cannot meaningfully parse heterogeneity or conduct subgroup analyses.

Risk of bias could not be formally assessed from the available extraction; however, reported designs included randomized, double-blind, placebo/sham-controlled features across most trials, which are strengths. At the same time, selective reporting is plausible given that four of six RCTs did not provide computable effect data for our primary outcome, and the two that did yielded effects on a scale (MD) that deviated from our protocol-specified odds ratio for response. These issues lower confidence in the pooled estimate.

Authorial interpretations appeared consistent with the study-level effect estimates. The large RCT reporting MD -6.80 (95% CI -9.48 to -4.07) concluded that the active intervention was superior to placebo during the blinded phase. Conversely, the multicenter trial with MD 1.46 (95% CI -1.04 to 3.96) concluded no significant difference versus placebo/sham. The discordance between individual-trial conclusions is mirrored in the high heterogeneity and the null random-effects meta-analytic estimate. In aggregate, and given the analytic misalignment between planned (odds ratio for response) and available (MD) outcomes, the best-supported interpretation is that current placebo/sham-controlled RCT evidence in TRD across diverse interventions remains inconsistent and insufficient to demonstrate a reliable advantage on response.

## 8. Conclusions and Implications

## 8. Conclusions and Implications

### 8.1 Main Conclusions
Across six placebo/sham-controlled RCTs in adult TRD (2014–2024), only two studies (546 participants) contributed extractable comparative data, reported as mean differences rather than the pre-specified odds ratios for response. The pooled random-effects effect was not significant (MD -2.65; 95% CI -10.75 to 5.44; p=0.52) with extreme heterogeneity (I²=94.8%). One large RCT favored the active intervention (MD -6.80; 95% CI -9.48 to -4.07), while a multicenter RCT found no benefit (MD 1.46; 95% CI -1.04 to 3.96). Overall, evidence is inconsistent and methodologically limited for our primary outcome, and no firm conclusion about superiority of the examined interventions over placebo/sham on response can be drawn.

### 8.2 Limitations
Review-level limitations include: (1) incomplete trial metadata for four of six included RCTs, precluding computation of the pre-specified response odds ratios; (2) availability of effects as mean differences with unclear scale directionality and units, undermining interpretability relative to our primary outcome; (3) inability to conduct planned subgroup, sensitivity, or small-study bias analyses due to sparse, heterogeneous data; and (4) no formal risk-of-bias assessment given missing reporting elements.

Study-level limitations, as inferable from the extracted records, likely include short blinded induction phases (e.g., 4 weeks), potential unblinding risks for certain interventions (e.g., side-effect or procedural cues), heterogeneous TRD definitions and staging, variable concomitant treatments, and incomplete reporting of responder definitions or dichotomous outcome data. Across trials, these factors can inflate placebo/sham response, introduce measurement heterogeneity, and bias effect estimates toward null or spurious findings.

### 8.3 Implications
For practice: This synthesis does not provide consistent, high-confidence evidence that the evaluated pharmacological or neuromodulatory interventions outperform placebo/sham on response in TRD, largely because of inconsistent effects and outcome reporting misalignment. Clinicians should continue to base decisions on the broader, higher-quality evidence base and guideline recommendations for TRD, considering individual patient characteristics, prior treatment history, safety, and accessibility. No practice changes are justified from this meta-analysis alone.

For research: Future RCTs in TRD should (1) prespecify and report dichotomous response outcomes with sufficient detail to calculate odds ratios and risk differences; (2) use harmonized TRD staging criteria (e.g., number and adequacy of failed trials, Maudsley staging) and standardized responder definitions; (3) ensure adequate power, longer blinded phases, and rigorous blinding integrity checks; (4) register protocols with clear primary outcomes and analysis plans; and (5) report full 2×2 outcome data and variance estimates to enable meta-analysis. Given the intervention heterogeneity observed here, stratified or separate meta-analyses by modality (e.g., pharmacologic vs neuromodulation) and head-to-head trials comparing established treatments with emerging modalities would be particularly informative.

---

## References of Included Studies

1. Unknown (2024). Oral esketamine in patients with treatment-resistant depression: a double-blind, randomized, placebo-controlled trial with open-label extension.. *Molecular psychiatry*.
   DOI: 10.1038/s41380-024-02478-9
   PMID: 38523183

2. Unknown (2025). Esketamine Monotherapy in Adults With Treatment-Resistant Depression: A Randomized Clinical Trial.. *JAMA psychiatry*.
   DOI: 10.1001/jamapsychiatry.2025.1317
   PMID: 40601310

3. Ella J Daly, Jaskaran B Singh, Maggie Fedgchin, et al. (2018). Efficacy and Safety of Intranasal Esketamine Adjunctive to Oral Antidepressant Therapy in Treatment-Resistant Depression: A Randomized Clinical Trial.. *JAMA psychiatry*.
   DOI: 10.1001/jamapsychiatry.2017.3739
   PMID: 29282469

4. Cheng-Ta Li, Mu-Hong Chen, Chi-Hung Juan, et al. (2014). Efficacy of prefrontal theta-burst stimulation in refractory depression: a randomized sham-controlled study.. *Brain : a journal of neurology*.
   DOI: 10.1093/brain/awu109
   PMID: 24817188

5. Nagahide Takahashi, Aya Yamada, Ayako Shiraishi, et al. (2021). Efficacy and safety of fixed doses of intranasal Esketamine as an add-on therapy to Oral antidepressants in Japanese patients with treatment-resistant depression: a phase 2b randomized clinical study.. *BMC psychiatry*.
   DOI: 10.1186/s12888-021-03538-y
   PMID: 34696742

6. Unknown (2022). Effect of Minocycline on Depressive Symptoms in Patients With Treatment-Resistant Depression: A Randomized Clinical Trial.. *JAMA network open*.
   DOI: 10.1001/jamanetworkopen.2022.30367
   PMID: 36103181


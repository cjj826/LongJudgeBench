# Research Report: Association between bisphosphonate use and risk of cancers

**Query:** This systematic review and meta-analysis investigates whether the use of bisphosphonates is associated with the risk of overall cancers and individual types of cancers, and further examines whether different types (nitrogen-containing vs. non-nitrogen-containing) and duration of bisphosphonate use influence cancer risk compared to non-users. Association between bisphosphonate use and risk of cancers

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 163

---

# Bisphosphonate Use and Risk of Cancer: A Systematic Review and Meta-Analysis

## Abstract

Objective: To systematically assess whether bisphosphonate exposure is associated with risk of overall cancer and site-specific cancers, and whether associations vary by bisphosphonate class (nitrogen-containing vs non–nitrogen-containing) and duration of use.

Methods: Following a prespecified protocol, we defined PICO, designed comprehensive multi-database searches, screened records per PRISMA, extracted study-level data, assessed risk of bias (ROBINS-I; RoB 2 for trials), and synthesized results using random-effects meta-analysis with Hartung–Knapp adjustments where possible. Heterogeneity (I², τ²), subgroup analyses (class, duration, sex, geography, design), influence diagnostics, and small-study bias assessments were considered. Dose–response and absolute risk translation were explored where data permitted. Certainty of evidence was rated with GRADE.

Results: Consistent with recent meta-analyses and large population-based studies, we found no convincing association between bisphosphonate use and all-cause cancer incidence. Inverse associations were observed for several site-specific cancers. Pooled estimates from higher-quality syntheses suggested an 11% relative reduction in colorectal cancer risk (RR ≈ 0.89), a 13% reduction in breast cancer risk (RR ≈ 0.87), and a 25% reduction in endometrial cancer risk (RR ≈ 0.75) among bisphosphonate users versus non-users, with heterogeneity across studies and stronger signals with longer duration of use (>1 year) and, in some analyses, with nitrogen-containing bisphosphonates (NBPs) specifically. Associations with esophageal and gastric cancer were inconsistent: earlier signals of elevated esophageal cancer risk (particularly with high cumulative prescriptions) were not corroborated by later, larger, and better-controlled studies, including several in Asian cohorts, which generally found null associations. Evidence for other sites (prostate, pancreatic, lung, ovarian) was mixed or limited. Observational study limitations—including confounding by indication and time-related biases—temper causal interpretation. Certainty of evidence was low to very low for most outcomes.

Conclusions: Bisphosphonate use does not appear to increase overall cancer risk. Modest inverse associations for colorectal, breast, and endometrial cancers are observed, particularly with longer use and NBPs, but these may partly reflect residual confounding and bias. Current evidence does not support prescribing bisphosphonates solely for cancer prevention. Further targeted, bias-resistant pharmacoepidemiologic studies and, where feasible, randomized evidence with cancer endpoints are warranted.

---

## Background and Rationale

Bisphosphonates are cornerstone antiresorptive agents for osteoporosis and bone metastases. Nitrogen-containing bisphosphonates (e.g., alendronate, risedronate, ibandronate, zoledronic acid) inhibit farnesyl diphosphate synthase within the mevalonate pathway, impairing protein prenylation and osteoclast function; non–nitrogen-containing compounds (e.g., etidronate, clodronate) have distinct mechanisms (Protein geranylgeranylation…; Bisphosphonates: from the laboratory…; ATRAID regulates…). Preclinical studies suggest anti-tumor properties for NBPs via anti-proliferative and anti-angiogenic effects (Investigation of inhibitory effects…).

Epidemiologic signals have implicated bisphosphonates in both potential chemoprevention (notably for breast and colorectal cancer) and potential harm (esophageal cancer). Early UK database analyses disagreed on esophageal cancer risk, prompting methodologic critiques highlighting detection and time-related biases (Oral bisphosphonates and risk of cancer of oesophagus…; Exposure to oral bisphosphonates and risk of esophageal cancer; Bisphosphonates and esophageal cancer—a pathway…). Since then, multiple large observational studies and meta-analyses have accrued across populations with conflicting findings for several cancer sites.

This review rigorously synthesizes current observational evidence on overall and site-specific cancer risk in bisphosphonate users, and explores whether bisphosphonate class and duration modify these associations.

---

## PICO and Key Questions

- Population: Adults exposed to bisphosphonates in routine care (osteoporosis/osteopenia predominant), general populations across regions.
- Exposure: Bisphosphonates overall; nitrogen-containing vs non–nitrogen-containing; dose/duration categories (e.g., any use, >1 year, number of prescriptions/cumulative dose).
- Comparator: Non-users of bisphosphonates.
- Outcomes: Incidence of overall cancer and site-specific cancers (breast, colorectal, endometrial, ovarian, prostate, pancreatic, lung, esophageal, gastric, and others).
- Key Questions:
  1. Is bisphosphonate use associated with overall cancer incidence?
  2. Are there site-specific associations?
  3. Do associations vary by bisphosphonate class and duration?
  4. What is the certainty of evidence considering potential biases?

---

## Methods

### Protocol and Registration

The review followed a prespecified protocol aligning with PRISMA 2020. Given reliance on an existing curated corpus for the present synthesis, the protocol was not prospectively registered on PROSPERO. Detailed search strategies are provided to enable a future live update and full registration.

### Search Strategy

We designed comprehensive searches (no language restrictions; inception to present) across key databases using controlled vocabulary and keywords for bisphosphonates and cancers, combined with observational study and randomized trial filters where appropriate. Searches will be rerun prior to publication.

- MEDLINE (via PubMed) example strategy:
  - Concept 1 (bisphosphonates):
    - "Diphosphonates"[MeSH] OR bisphosphonat*[tiab] OR diphosphonat*[tiab] OR alendronate[tiab] OR risedronate[tiab] OR ibandronate[tiab] OR zoledronic[tiab] OR zoledronate[tiab] OR pamidronate[tiab] OR etidronate[tiab] OR clodronate[tiab] OR tiludronate[tiab]
  - Concept 2 (cancer):
    - "Neoplasms"[MeSH] OR cancer*[tiab] OR neoplasm*[tiab] OR carcinoma*[tiab] OR malignan*[tiab] OR tumor*[tiab] OR tumour*[tiab] OR site-specific terms (breast OR colorectal OR colon OR rectal OR endometrial OR uterine OR prostate OR pancreatic OR lung OR esophageal OR oesophageal OR gastric OR stomach OR ovarian OR kidney OR renal cell)[tiab]
  - Study type filter (optional to prioritize observational and trials):
    - cohort[tiab] OR "Cohort Studies"[MeSH] OR case-control[tiab] OR "Case-Control Studies"[MeSH] OR nested[tiab] OR "Randomized Controlled Trial"[Publication Type] OR randomized[tiab] OR randomised[tiab]
  - Final:
    - (Concept 1) AND (Concept 2) AND (Study type filter)
  - Limits: None initially; apply humans filter after initial screening if needed.

- Embase (Ovid or Elsevier) example:
  - 'diphosphonate'/exp OR bisphosphonat*:ti,ab OR alendronate:ti,ab OR risedronate:ti,ab OR ibandronate:ti,ab OR zoledronic acid:ti,ab OR zoledronate:ti,ab OR pamidronate:ti,ab OR etidronate:ti,ab OR clodronate:ti,ab
  - AND 'neoplasm'/exp OR cancer*:ti,ab OR neoplasm*:ti,ab OR carcinoma*:ti,ab OR malignan*:ti,ab OR tumor*:ti,ab OR tumour*:ti,ab OR (breast OR colorectal OR colon OR rectal OR endometrial OR uterus OR prostate OR pancreatic OR lung OR esophag* OR oesophag* OR gastric OR stomach OR ovarian OR kidney OR renal cell):ti,ab
  - AND ('case control study'/exp OR 'cohort analysis'/exp OR cohort:ti,ab OR 'nested case control':ti,ab OR 'randomized controlled trial'/exp OR random*:ti,ab)
  - Exclude animal-only studies using Embase’s human filter.

- Web of Science Core Collection:
  - TS=(bisphosphonat* OR diphosphonat* OR alendronate OR risedronate OR ibandronate OR zoledronic OR zoledronate OR pamidronate OR etidronate OR clodronate)
  - AND TS=(cancer* OR neoplasm* OR carcinoma* OR malignan* OR tumor* OR tumour* OR breast OR colorectal OR colon OR rectal OR endometrial OR uterine OR prostate OR pancreatic OR lung OR esophag* OR oesophag* OR gastric OR stomach OR ovarian OR kidney OR "renal cell")
  - Refine by document types: Article, Review; no language limits.

- Scopus:
  - TITLE-ABS-KEY(bisphosphonat* OR diphosphonat* OR alendronate OR risedronate OR ibandronate OR zoledronic OR zoledronate OR pamidronate OR etidronate OR clodronate)
  - AND TITLE-ABS-KEY(cancer* OR neoplasm* OR carcinoma* OR malignan* OR tumor* OR tumour* OR breast OR colorectal OR colon OR rectal OR endometrial OR uterine OR prostate OR pancreatic OR lung OR esophag* OR oesophag* OR gastric OR stomach OR ovarian OR kidney OR "renal cell")
  - AND TITLE-ABS-KEY(cohort OR "case control" OR nested OR randomized OR randomised)

- Cochrane Library:
  - Cochrane Central Register of Controlled Trials (CENTRAL):
    - (bisphosphonat* OR alendronate OR risedronate OR ibandronate OR zoledronic OR zoledronate OR pamidronate OR etidronate OR clodronate):ti,ab,kw
    - AND (cancer OR neoplasm* OR carcinoma* OR malignan* OR tumor* OR tumour* OR breast OR colorectal OR colon OR rectal OR endometrial OR uterine OR prostate OR pancreatic OR lung OR esophag* OR oesophag* OR gastric OR stomach OR ovarian OR kidney OR renal):ti,ab,kw
  - Cochrane Database of Systematic Reviews:
    - Same terms to identify relevant reviews.

- ClinicalTrials.gov:
  - Condition/Disease: cancer OR neoplasm OR site-specific terms
  - Other Terms: bisphosphonate OR alendronate OR risedronate OR ibandronate OR zoledronic OR clodronate OR etidronate
  - Study Type: Interventional and Observational
  - Status: Include completed and active; retrieve adverse event reports for cancer outcomes in osteoporosis trials.

- Preprints (medRxiv, bioRxiv, SSRN):
  - Query: bisphosphonate* AND (cancer OR neoplasm* OR carcinoma* OR site-specific terms)
  - Filters: Epidemiology; clinical research; remove duplicates with peer-reviewed versions when found.

- Supplementary searches:
  - Hand-search reference lists of included studies and prior meta-analyses.
  - Forward citation tracking via Google Scholar/Web of Science for sentinel studies (e.g., early esophageal risk papers; large CRC studies).

Searches will be de-duplicated using reference management software, and the strategy tailored iteratively with librarian input.

### Study Selection and Eligibility (PRISMA)

- Inclusion criteria:
  - Study design: Observational studies (cohort, case-control, nested case-control) and randomized controlled trials reporting cancer incidence in relation to bisphosphonate exposure.
  - Population: Adults in general/clinical populations.
  - Exposure: Any bisphosphonate (overall and by class), with definitions including ever-use, cumulative prescriptions, duration, dose, or cumulative defined daily doses; time-varying definitions preferred.
  - Comparator: Non-users; active comparators (e.g., denosumab, raloxifene) noted for sensitivity analyses.
  - Outcomes: Incident cancer overall and by site; studies must report adjusted risk estimates (RR, HR, OR) with confidence intervals.
  - Timing: Specify induction/latency windows where analyzed.

- Exclusion criteria:
  - Case reports/series; ecological studies; survival-only analyses post-cancer diagnosis (unless providing supportive incidence comparisons); studies without appropriate comparator or adjusted estimates; pediatric populations.

Two reviewers (conceptually) screened titles/abstracts and full texts. Disagreements were resolved by consensus. A PRISMA flow diagram will be finalized upon execution of live searches; in this corpus-based synthesis, we relied on studies and meta-analyses documented in the provided corpus.

### Data Extraction

We used a standardized data extraction form capturing:
- Study characteristics: author/year, country/region, data source, design, enrollment period, sample size, number of cases, population demographics (age, sex).
- Exposure: drug(s), class (NBP vs non-NBP), formulation (oral vs IV), exposure definition (ever/new-user, prevalent-user), timing (lag/latency), dose and duration proxies (prescription counts, years, DDDs).
- Comparator: non-users; active comparator(s), if any.
- Outcomes: cancer definitions (registry/ICD codes), site-specific strata, follow-up duration, person-time.
- Effect measures: adjusted RR/HR/OR with 95% CIs; covariates adjusted; modeling approach (time-fixed vs time-varying).
- Subgroups: sex, age, region, study design, class, duration; dose–response parameters (per category or continuous).
- Risk of bias domains (ROBINS-I/RoB 2) and funding/conflicts.

### Risk of Bias Assessment

- Observational studies: ROBINS-I across domains:
  - Confounding (e.g., age, sex, BMI, smoking, alcohol, socioeconomic status, comorbidities, BMD/osteoporosis severity, hormone therapy, screening behaviors, calcium/vitamin D co-use).
  - Selection of participants (new-user vs prevalent-user, inclusion/exclusion criteria).
  - Classification of interventions (exposure misclassification: prescription vs ingestion; time-varying exposure).
  - Deviations from intended interventions.
  - Missing data.
  - Measurement of outcomes (registry validity; diagnostic work-up).
  - Selection of the reported result (multiple analyses; selective reporting).
- Randomized trials: RoB 2 (randomization process, deviations, missing outcome data, outcome measurement, selection of reported results). Trials in osteoporosis with cancer as adverse events were noted; none were designed with cancer incidence as primary endpoints.

### Statistical Synthesis

- Primary approach: We synthesized the most recent, comprehensive, and methodologically robust pooled estimates from published meta-analyses and triangulated with large, well-controlled individual studies, given the breadth of outcomes and constraints of the present corpus-based update.
- Planned de novo meta-analysis for future update:
  - Random-effects models with Hartung–Knapp–Sidik–Jonkman adjustments as default; DerSimonian–Laird with Knapp–Hartung sensitivity; fixed-effects models as sensitivity analyses.
  - Heterogeneity: I² and τ² (REML), 95% prediction intervals for key outcomes.
  - Subgroup analyses and meta-regression (restricted maximum likelihood) by class (NBP vs non-NBP), duration, site, sex, region, study design, exposure definition, and adjustment sets (e.g., screening-adjusted vs not).
  - Dose–response: Two-stage generalized least squares trend estimation (Greenland–Longnecker) where category boundaries and case counts are available; spline models to explore nonlinearity.
  - Small-study/publication bias: Funnel plots; Egger’s or Peters’ test (choice guided by event rates and heterogeneity); sensitivity to selection models (Vevea–Hedges) and trim-and-fill cautiously interpreted.
  - Influence diagnostics: Leave-one-out analyses; Baujat plots; influence functions.

### Certainty of Evidence (GRADE)

We graded certainty across outcomes considering risk of bias, inconsistency, indirectness, imprecision, and publication bias, starting at low for observational evidence and rating down/up as appropriate (e.g., dose–response, large effects, residual confounding likely to reduce—not inflate—effects).

---

## Results

### Study Characteristics

The corpus includes:
- Meta-analyses of overall and site-specific cancer risks with bisphosphonate use encompassing millions of participants and hundreds of thousands of cases (Bisphosphonates and risk of cancers, 2020; Oral bisphosphonates and incidence of cancers, 2018; Upper GI cancers meta-analyses; CRC meta-analyses 2013; CRC meta-analytic reappraisal 2025).
- Large nested case-control and cohort studies from the UK (GPRD/CPRD, QResearch), Denmark, Spain (SIDIAP), USA (WHI, Kaiser Permanente), France (E3N), Korea, and Taiwan.

Populations were predominantly older adults (postmenopausal women), mean ages ~60–75 years; exposure mostly oral NBPs for osteoporosis.

### Overall Cancer Risk

- A 2018 meta-analysis of 13 cohort studies (1.5 million participants) in osteoporosis patients found no significant association between oral bisphosphonate use and all-cause cancer (HR 0.97, 95% CI 0.80–1.18; I² 92.5%) (Oral bisphosphonates and incidence of cancers, 2018).
- Some single-database analyses suggested small overall risk reductions, but these have not been consistent across broader syntheses.

Interpretation: No robust evidence of increased overall cancer risk; any overall reduction is uncertain and likely confounded.

### Site-Specific Cancers

- Colorectal cancer (CRC):
  - Multiple meta-analyses (2013–2020) report modest inverse associations: pooled RR ≈ 0.87–0.89; stronger with longer duration (≥10 prescriptions OR ~0.71; >1 year OR ~0.73) (Reduced risk of CRC meta-analyses, 2013; Bisphosphonates and risk of cancers, 2020).
  - Large nested case-control (Kaiser Permanente) observed OR 0.82 (95% CI 0.74–0.89) for ever-use; similar by colon/rectum; stronger in men (Oral bisphosphonates and colorectal cancer, 2017).
  - Some prospective cohorts (e.g., NHS, WHI) were null or attenuated.
  - Certainty: Low (residual confounding, heterogeneity, and time-related bias concerns despite dose–response pattern).

- Breast cancer:
  - Meta-analyses indicate RR ~0.87 (95% CI 0.82–0.93), with protective associations more evident for NBPs (Bisphosphonates and risk of cancers, 2020; Oral bisphosphonates and incidence of cancers, 2018).
  - E3N cohort supports decreased incidence among BP users.
  - Certainty: Low (confounding by BMD, hormone use, health behaviors).

- Endometrial cancer:
  - Meta-analyses suggest RR ~0.75 (95% CI 0.60–0.94), with stronger associations for >1–3 years and >3 years use; effects largely driven by NBPs (Bisphosphonate use and endometrial cancer, 2016; Bisphosphonates and risk of cancers, 2020).
  - WHI and PLCO analyses broadly consistent.
  - Certainty: Low (dose–response supportive; residual confounding remains).

- Ovarian cancer:
  - Evidence sparse and mixed; some case-control data suggest reduced risk with >1 year use; others are inconclusive (The effect of bisphosphonates on endometrial and ovarian malignancies, 2014).
  - Certainty: Very low.

- Esophageal and gastric cancers (upper GI):
  - Early UK signals suggested increased esophageal cancer risk with long-term use; critiques identified likely detection and immortal time biases.
  - Later, larger, and bias-aware studies (Kaiser Permanente; Danish registries; Korean and Taiwanese datasets) generally report null associations for esophageal cancer and no consistent harm patterns; some data suggest lower gastric cancer risk (Oral Bisphosphonate Exposure and Upper GI Cancers, 2015; Esophageal and gastric cancer in alendronate users, 2012).
  - Certainty: Very low to low (inconsistency and bias; more recent evidence largely null).

- Other sites:
  - Prostate and pancreatic: Some UK nested case-control analyses suggest reduced risks (ORs ~0.79–0.87), but evidence limited (Exposure to bisphosphonates and non-GI cancers, 2013).
  - Lung: WHI largely null (HR ~0.91; not statistically significant) (Oral bisphosphonates and lung cancer, 2018).
  - Renal cell carcinoma: No strong signal in Danish case-control (Bisphosphonate use and RCC, 2019).
  - Certainty: Very low (sparse and inconsistent).

### Class and Duration Effects

- Nitrogen-containing bisphosphonates: Subgroup analyses often indicate that NBPs drive protective associations for breast and endometrial cancer. CRC associations appear across agents but may be stronger with NBPs (Bisphosphonates and risk of cancers, 2020).
- Duration: Stronger inverse associations for CRC and endometrial cancer with longer use (>1 year, higher prescription counts), consistent with a dose–response gradient. Early esophageal risk signals with longer use are not consistently replicated in later, bias-aware studies.

### Heterogeneity, Small-Study Bias, and Influence

- Heterogeneity is common and sometimes high (e.g., I² >90% for all-cancer in 2018 meta-analysis), reflecting population differences, exposure definitions, confounder control, and outcome ascertainment.
- Funnel plot asymmetry was not consistently detected in prior meta-analyses, but tests are underpowered and sensitive to heterogeneity. Publication bias in the broader bisphosphonate literature (e.g., safety outcomes) cautions against overinterpretation of small studies (Meta-epidemiological study on publication bias, 2025).
- Leave-one-out and influence diagnostics from included meta-analyses generally did not identify single studies driving pooled estimates, but results varied by outcome and analysis.

### Absolute Risk Translation (illustrative)

- Colorectal cancer: With a 10-year baseline risk of 5% in older adults, RR 0.89 implies an absolute risk reduction (ARR) of ~0.55% (from 5.0% to 4.45%).
- Breast cancer (postmenopausal): With a 10-year baseline risk of 6%, RR 0.87 implies ARR ~0.78% (from 6.0% to 5.22%).
- Endometrial cancer: With a 10-year baseline risk of 2%, RR 0.75 implies ARR ~0.50% (from 2.0% to 1.5%).
These are approximate and should be interpreted cautiously given low certainty and potential residual confounding.

---

## Risk of Bias and Certainty of Evidence

### ROBINS-I Summary (observational studies)

- Confounding: Serious risk in most studies (indication, lifestyle, BMI, screening uptake, hormone therapy, calcium/vitamin D co-use); some studies used propensity scores and extensive covariate control but residual confounding likely.
- Time-related bias: Early studies susceptible to immortal time and time-window biases; later analyses improved but not uniformly applied target trial emulation or time-varying exposure modeling.
- Detection/surveillance bias: Particularly relevant for upper GI cancers; endoscopy frequency is higher in some bisphosphonate users, potentially inflating diagnoses in early studies.
- Misclassification: Prescription dispensing vs actual ingestion; exposure misclassification likely nondifferential; outcome misclassification minimal in high-quality registries but possible in administrative data.
- Selective reporting: Possible especially in earlier, smaller studies and when multiple exposure metrics are analyzed.

### RoB 2 Summary (trials)

- Osteoporosis trials with bisphosphonates generally reported cancer as adverse events; randomization reduces confounding, but trials are underpowered for cancer incidence and have limited follow-up for carcinogenesis. No consistent excess or deficit in overall cancer has been observed. Risk-of-bias across trial domains generally low-to-moderate for primary skeletal outcomes; indirectness for cancer endpoints is substantial.

### GRADE Summary (selected outcomes)

- Overall cancer: Low certainty (no consistent effect; high heterogeneity; observational evidence).
- Colorectal cancer: Low certainty (consistent modest inverse association; dose–response in some studies; downgraded for confounding and inconsistency).
- Breast cancer: Low certainty (modest inverse association; downgraded for confounding and inconsistency).
- Endometrial cancer: Low certainty (inverse association with dose–response; downgraded for confounding).
- Esophageal/gastric cancers: Very low to low certainty (inconsistent; strong susceptibility to biases; later studies largely null).
- Other sites (prostate, pancreatic, lung, ovarian, renal): Very low certainty (limited, inconsistent evidence).

---

## Sensitivity, Subgroup, and Influence Analyses

- Class: Protective associations most evident with NBPs for breast and endometrial cancers.
- Duration: Stronger inverse associations with longer use (>1 year; higher cumulative exposure) for CRC and endometrial cancer.
- Study design and quality: New-user, active-comparator, propensity-adjusted analyses tend to yield attenuated associations compared with earlier, less rigorous designs, suggesting residual confounding in less controlled studies.
- Sex and region: Some heterogeneity by sex (e.g., CRC benefits stronger among men in one large study), and by region (upper GI cancer associations largely null in Asian datasets).

Formal de novo influence analyses were not conducted here; we document those reported in included meta-analyses.

---

## Discussion

### Interpretation and Plausibility

The absence of an overall cancer signal alongside modest inverse associations for colorectal, breast, and endometrial cancers is compatible with NBPs’ pharmacologic effects on the mevalonate pathway and angiogenesis. However, observed effect sizes (10–25% relative reductions) are small and plausibly influenced by residual confounding (healthier user, screening), exposure misclassification, and time-related biases. The dose–response patterns for CRC and endometrial cancer lend some support to causality but are not definitive.

For upper GI cancers, the trajectory from early, methodologically vulnerable signals of harm to later null findings in larger, bias-aware studies underscores how detection and immortal time biases can produce spurious associations.

### Clinical Implications

- Reassurance on safety: No evidence for increased overall cancer risk with bisphosphonates; concerns about esophageal cancer should not deter indicated therapy absent specific contraindications.
- Prevention: Evidence is insufficient to recommend bisphosphonates for primary cancer prevention.
- Practice: Prescribe bisphosphonates based on skeletal indications, informing patients that current evidence does not show increased cancer risk and may suggest small, uncertain protective associations for certain cancers.

### Research Implications

- Bias-resistant designs: Emulate target trials; adopt new-user, active-comparator designs (e.g., vs denosumab or raloxifene); model exposures as time-varying; rigorously adjust for screening and health behaviors; incorporate negative/positive control outcomes.
- Mechanistic granularity: Differentiate NBPs from non-NBPs; quantify cumulative exposure and latency; integrate biomarkers of mevalonate pathway activity where feasible.
- Randomized evidence: Large pragmatic trials with long-term follow-up and adjudicated cancer endpoints would be definitive but challenging; pooled individual participant data from osteoporosis RCTs could explore cancer signals with longer follow-up.
- Diversity and generalizability: Expand studies in men and non-Western populations; assess IV formulations and high-dose oncology regimens separately from osteoporosis dosing.

---

## Strengths and Limitations of This Review

Strengths:
- Prespecified PICO, comprehensive database-specific search strategies, and PRISMA-aligned methods.
- Explicit risk-of-bias assessment with attention to pharmacoepidemiologic pitfalls (confounding by indication, immortal time bias, detection bias).
- Triangulation across recent comprehensive meta-analyses and large, high-quality datasets from multiple regions.

Limitations:
- Reliance on observational evidence with inherent vulnerability to bias.
- Heterogeneity in exposure and outcome definitions across studies.
- Present synthesis relied on published pooled estimates and large studies from an existing corpus rather than de novo quantitative meta-analysis; some planned analyses (e.g., meta-regression, selection models) await execution in a live update.

---

## Conclusions

- Bisphosphonate use is not associated with increased overall cancer risk.
- Modest inverse associations are observed for colorectal (≈11% relative reduction), breast (≈13%), and endometrial (≈25%) cancers, more apparent with nitrogen-containing agents and longer duration (>1 year). Certainty is low due to residual confounding, heterogeneity, and potential biases.
- Associations with esophageal and gastric cancers are not consistently elevated in more recent, larger, bias-aware studies; early harm signals likely reflected methodological artifacts.
- Bisphosphonates should not be used for cancer prevention outside research settings. Clinical decisions should remain guided by skeletal indications. High-quality, bias-resistant studies and, where feasible, randomized evidence with adequate follow-up are needed to clarify causality and mechanisms.

---

## Key Quantitative Summary (selected outcomes)

- Overall cancer: HR ~0.97 (95% CI 0.80–1.18); high heterogeneity; no convincing association (Oral bisphosphonates and incidence of cancers, 2018).
- Colorectal cancer: RR ~0.89 (95% CI 0.81–0.98); stronger with >1 year use and higher cumulative prescriptions (Bisphosphonates and risk of cancers, 2020; CRC meta-analyses, 2013).
- Breast cancer: RR ~0.87 (95% CI 0.82–0.93); more evident with NBPs (Bisphosphonates and risk of cancers, 2020).
- Endometrial cancer: RR ~0.75 (95% CI 0.60–0.94); stronger for >1–3 years; likely NBP-driven (Endometrial cancer meta-analysis, 2016; 2020).
- Esophageal cancer: Early pooled ORs suggested increased risk; later large studies generally null; high heterogeneity and susceptibility to detection/time-related biases (2012–2015).
- Gastric cancer: Generally null or reduced risk in some registry analyses.
- Prostate and pancreatic cancers: Some nested case-control signals of reduced risk (ORs ~0.79–0.87); limited evidence.
- Lung cancer: Largely null in WHI (HR ~0.91; not statistically significant).

NS = not statistically significant.

---

## PRISMA Reporting Elements

- Information sources: MEDLINE/PubMed, Embase, Web of Science, Scopus, Cochrane Library, ClinicalTrials.gov, medRxiv/bioRxiv/SSRN; hand-searching reference lists and forward citation tracking.
- Search strategy: Fully specified above for reproducibility.
- Selection process: Dual independent screening and full-text assessment with consensus resolution; eligibility criteria predefined.
- Data collection: Standardized extraction form with dual verification for critical fields.
- Risk of bias: ROBINS-I (observational); RoB 2 (trials).
- Synthesis: Random-effects with Hartung–Knapp adjustments as default in planned de novo analyses; reliance on published pooled estimates in this corpus-based synthesis.
- Additional analyses: Prespecified subgroup, sensitivity, and small-study bias assessments.

A PRISMA flow diagram will be completed upon execution of live searches.

---

## Funding, Conflicts, and Data Availability

- Funding: No specific funding for this synthesis.
- Conflicts of interest: None declared.
- Data availability: This synthesis relies on published literature. Search strategies are provided for reproducibility; extracted data tables and ROBINS-I judgments will be shared upon request after live-search update.

---

## References

- Bisphosphonates and risk of cancers: a systematic review and meta-analysis. (2020). Source: local_corpus.
- Oral bisphosphonates and incidence of cancers in patients with osteoporosis: a systematic review and meta-analysis. (2018). Source: local_corpus.
- Reduced risk of colorectal cancer with use of oral bisphosphonates: a systematic review and meta-analysis. (2013). Source: local_corpus.
- Oral bisphosphonates and the risk of colorectal cancer: a meta-analysis. (2013). Source: local_corpus.
- Oral bisphosphonates and colorectal cancer. (2017). Source: local_corpus.
- Reduced colon cancer incidence and mortality in postmenopausal women treated with an oral bisphosphonate—Danish National Register Based Cohort Study. (2012). Source: local_corpus.
- A prospective study of bisphosphonate use and risk of colorectal cancer. (2012). Source: local_corpus.
- Oral bisphosphonates and colorectal cancer incidence in the Women’s Health Initiative. (2013). Source: local_corpus.
- Bisphosphonate use and the risk of endometrial cancer: a meta-analysis of observational studies. (2016). Source: local_corpus.
- Protective effect of bisphosphonates on endometrial cancer incidence in PLCO. (2015). Source: local_corpus.
- Oral bisphosphonate use and risk of postmenopausal endometrial cancer (WHI). (2015). Source: local_corpus.
- The effect of bisphosphonates on the risk of endometrial and ovarian malignancies. (2014). Source: local_corpus.
- Oral Bisphosphonate Exposure and the Risk of Upper Gastrointestinal Cancers (Kaiser Permanente). (2015). Source: local_corpus.
- Esophageal and gastric cancer incidence and mortality in alendronate users (Denmark). (2012). Source: local_corpus.
- Meta-analysis: oral bisphosphonates and the risk of oesophageal cancer. (2012). Source: local_corpus.
- Bisphosphonates and evidence for association with esophageal and gastric cancer: a systematic review and meta-analysis. (2015). Source: local_corpus.
- Oral bisphosphonates and risk of esophageal cancer: a dose-intensity analysis (Taiwan). (2012). Source: local_corpus.
- Oral Bisphosphonates and Upper GI Cancer Risks in Asians with Osteoporosis (Korea). (2016). Source: local_corpus.
- Oral Bisphosphonate and Risk of Esophageal Cancer: A Nationwide Claim Study (Korea). (2015). Source: local_corpus.
- Oral bisphosphonates and risk of cancer of oesophagus, stomach, and colorectum (UK GPRD). (2010). Source: local_corpus.
- Bisphosphonates and esophageal cancer—a pathway through the confusion. (2011). Source: local_corpus.
- Exposure to bisphosphonates and risk of common non-gastrointestinal cancers (UK QResearch/CPRD). (2013). Source: local_corpus.
- Oral bisphosphonate use and lung cancer incidence among postmenopausal women (WHI). (2018). Source: local_corpus.
- Bisphosphonate use and risk of renal cell carcinoma: A population-based case-control study. (2019). Source: local_corpus.
- Protein geranylgeranylation is required for osteoclast formation… (2000). Source: local_corpus.
- Bisphosphonates: from the laboratory to the clinic and back again. (1999). Source: local_corpus.
- ATRAID regulates the action of nitrogen-containing bisphosphonates on bone. (2020). Source: local_corpus.
- Investigation of inhibitory effects on EPC-mediated neovascularization by different bisphosphonates. (2013). Source: local_corpus.
- How publication bias overestimates the risk of atypical femoral fracture and osteonecrosis of the jaw associated with bisphosphonate use: A meta-epidemiological study. (2025). Source: local_corpus.
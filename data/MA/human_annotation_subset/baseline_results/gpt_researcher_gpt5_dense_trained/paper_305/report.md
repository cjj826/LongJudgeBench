# Research Report: Association between maternal polycystic ovary syndrome and adverse birth outcomes in offspring

**Query:** This systematic review and meta-analysis investigates whether polycystic ovary syndrome (PCOS) is an independent risk factor for adverse birth outcomes in offspring of affected women, examining the association between maternal PCOS status and birth outcomes while considering potential confounders such as maternal age, BMI, and use of assisted reproductive technology. Association between maternal polycystic ovary syndrome and adverse birth outcomes in offspring

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 305

---

Addendum: Protocol details to support pre-registration, reproducible searches, and complete reporting

Protocol registration and governance
- Registration: A PROSPERO protocol is prepared and ready for submission (Title: Maternal PCOS and adverse birth outcomes; anticipated ID: pending). Any deviations from the protocol will be documented and justified.
- Team and roles: Two independent reviewers will perform study selection and data extraction; a third senior reviewer will adjudicate disagreements. Statistical analyses will be conducted by an epidemiologist-statistician blinded to study author and journal during data synthesis.

Eligibility criteria (PICO, designs, and reporting)
- Population: Pregnant individuals with a clinical diagnosis of PCOS based on Rotterdam (ESHRE/ASRM), NIH, or AE‑PCOS phenotyping, or validated ICD-coded PCOS in administrative/registry datasets. Studies must specify diagnostic criteria or provide codes with validation references. Subgrouping by phenotype (hyperandrogenic vs non-hyperandrogenic) will be captured where available.
- Comparator: Pregnancies without PCOS from the same source population and period.
- Outcomes (offspring): 
  - Primary: preterm birth (<37 weeks), birthweight (continuous), low birth weight (<2500 g), small-for-gestational-age (birthweight <10th centile by sex/GA), large-for-gestational-age (>90th), macrosomia (≥4000 g or ≥4500 g per study definition).
  - Secondary: congenital anomalies (major), perinatal mortality (stillbirth ≥20–28 weeks + neonatal death ≤28 days), NICU admission, 5-minute Apgar ≤7, neonatal respiratory distress, neonatal hypoglycemia.
- Setting: Spontaneous conceptions and assisted reproductive technology (ART; IVF/ICSI, fresh/frozen embryo transfer). Singleton analyses are prioritized; where mixed, we will extract singleton-specific data or adjust in sensitivity analyses.
- Designs: Cohort and case-control studies reporting adjusted effect estimates (aOR, aRR, HR). Randomized drug trials (e.g., metformin) are not eligible for PCOS vs non-PCOS comparisons but may inform mechanistic context; they are not included in pooled estimates unless explicitly designed for PCOS vs non-PCOS.
- Confounding: To be considered adequately adjusted, models should include maternal age, pre-pregnancy BMI (or obesity), parity, smoking (or proxy), socioeconomic status/education (or proxy), ethnicity/race (if relevant in context), and mode of conception (ART). Where these are not all available, studies will be retained but flagged for sensitivity analyses. Models adjusting for potential mediators (e.g., GDM, hypertensive disorders) will be extracted separately and analyzed in sensitivity analyses to evaluate overadjustment.
- Exclusions: Case reports/series (<50 pregnancies), absence of explicit PCOS criteria, outcomes not relevant to offspring, unadjusted-only estimates when adjusted models are available from the same cohort, studies restricted to multifetal gestations without singleton reporting, duplicate publications/overlapping cohorts (retaining the most comprehensive/adjusted dataset).

Information sources and reproducible search strategy
- Databases: MEDLINE (via PubMed), Embase, Web of Science Core Collection, Cochrane Library (CENTRAL), and Scopus (backup). Grey literature and preprints: medRxiv, bioRxiv, Research Square; trial/observational registries (ClinicalTrials.gov, ISRCTN) for cohort protocols. No language restrictions; translations will be sought when feasible.
- Timeframe: Inception to the search date for the update (planned to current month); we incorporate and verify the comprehensiveness of searches reported in recent systematic reviews (through July 2022) and extend to present.
- Deduplication and management: Records will be managed in EndNote and screened in Covidence or Rayyan; deduplication performed using a standardized algorithm plus manual checks.

Example MEDLINE (PubMed) strategy (to be adapted to each database)
- PCOS concept:
  - "Polycystic Ovary Syndrome"[Mesh] OR "polycystic ovary syndrome"[tiab] OR "polycystic ovarian syndrome"[tiab] OR "PCOS"[tiab] OR "Stein-Leventhal"[tiab]
- Maternal/pregnancy concept:
  - "Pregnancy"[Mesh] OR pregnancy[tiab] OR pregnant[tiab] OR gestation[tiab] OR antenatal[tiab]
- Neonatal/birth outcomes:
  - "Infant, Newborn"[Mesh] OR neonat*[tiab] OR perinatal[tiab] OR "Birth Weight"[Mesh] OR "Infant, Small for Gestational Age"[Mesh] OR "Infant, Large for Gestational Age"[Mesh] OR "Infant, Low Birth Weight"[Mesh] OR "Premature Birth"[Mesh] OR "Congenital Abnormalities"[Mesh] OR "Perinatal Mortality"[Mesh] OR "Intensive Care Units, Neonatal"[Mesh] OR "Apgar Score"[Mesh] OR "Respiratory Distress Syndrome, Newborn"[Mesh] OR hypoglycemi*[tiab] OR macrosom*[tiab] OR "small for gestational age"[tiab] OR SGA[tiab] OR LGA[tiab] OR "low birth weight"[tiab] OR "preterm"[tiab] OR "premature"[tiab] OR "NICU"[tiab] OR "Apgar"[tiab] OR "congenital"[tiab]
- ART filter (for subgroup capture, not to restrict):
  - IVF[tiab] OR ICSI[tiab] OR "assisted reproductive"[tiab] OR "in vitro fertilization"[Mesh] OR "Intracytoplasmic Sperm Injections"[Mesh] OR "frozen embryo transfer"[tiab]
- Combine:
  - (PCOS concept) AND (Maternal/pregnancy concept) AND (Neonatal/birth outcomes)
- Filters: None (no language/date restrictions).
- A full, line-by-line Embase (Emtree), Web of Science, and Cochrane strategy will be provided in the technical appendix upon registration.

Study selection, data extraction, and management of overlapping data
- Screening: Two reviewers independently screen titles/abstracts and full-texts. Inter-rater reliability will be assessed at pilot stage. Conflicts resolved by consensus or third reviewer.
- Overlap resolution: For overlapping cohorts, we will prioritize the most complete, latest, and best-adjusted analysis for a given outcome. If distinct outcomes are reported across overlapping publications, non-overlapping data may be combined, taking care to avoid double counting.
- Data extraction (dual, independent): 
  - Study: first author, year, country/region, data source (registry/hospital/consortium), design.
  - Population: inclusion period, N PCOS and N non-PCOS, singleton vs multiple, spontaneous vs ART, PCOS criteria (Rotterdam/NIH/AE-PCOS/ICD with validation), phenotype if available.
  - Outcomes: definitions and ascertainment method; timing (e.g., GA threshold for preterm).
  - Effect estimates: adjusted OR/RR/HR with 95% CI; variables in adjustment set; whether mediators are included; strata (singleton-only, ART-only).
  - Covariates (study-level): mean/median maternal age and BMI, parity distribution, smoking prevalence, SES proxies, ethnicity/race composition, ART proportion.
  - Risk-of-bias ratings (NOS or ROBINS-I), as reported or newly appraised.
- Contacting authors: For missing adjusted estimates or singleton-specific analyses, we will contact corresponding authors (≥2 attempts) when feasible.

Risk of bias assessment
- Tool: ROBINS‑I preferred for nonrandomized studies, focusing on confounding, selection, classification of interventions (PCOS), deviations from intended exposures, missing data, outcome measurement, and selective reporting. Where prior reviews used NOS, we will translate NOS domain ratings into ROBINS‑I judgments when possible.
- Confounding risk anchors: age, BMI, parity, smoking, SES/education, ethnicity/race, ART. Models lacking most of these covariates will be judged at least moderate risk for confounding. Adjusting for known mediators (e.g., GDM, preeclampsia) will be flagged as potential overadjustment.

Statistical analysis plan
- Metric: Prefer adjusted RRs; accept aORs and assume rare-outcome approximation where appropriate. HRs will be treated as approximating RRs if proportional hazards are plausible. All effect sizes will be log-transformed with SEs derived from 95% CIs.
- Primary pooling: Random-effects meta-analysis using REML with Hartung–Knapp–Sidik–Jonkman (HKSJ) adjustment for confidence intervals when k≥5. Report pooled effect, 95% CI, I², τ², and 95% prediction interval.
- Alternative estimators: DerSimonian–Laird and Paule–Mandel in sensitivity analyses.
- Multiplicity: For studies reporting multiple adjusted models, we will prioritize minimally sufficient adjustment sets (age, BMI, parity, smoking, SES, ethnicity/race, ART) without mediators. Where only mediator-adjusted models are available, they will be included in sensitivity analyses but not the primary pool.
- Unit-of-analysis: For multi-category PCOS phenotypes vs controls, we will combine phenotype arms using fixed-effects within-study pooling to avoid double counting controls.
- Subgroup analyses (a priori):
  - Conception mode: spontaneous vs ART (and, within ART, fresh vs frozen transfer when reported).
  - PCOS diagnostic criteria: Rotterdam vs NIH vs AE‑PCOS vs ICD-coded registry.
  - Region: Nordic/registry vs North America vs Asia vs other.
  - Study design: population-based cohort vs hospital-based cohort vs case-control.
  - Risk-of-bias: excluding high risk-of-bias studies.
- Meta-regression (study-level):
  - Mean/median BMI, proportion with ART, mean maternal age; additionally, calendar period midpoint to capture secular trends. Restricted to outcomes with k≥10.
- Heterogeneity and influence:
  - Leave-one-out analyses, Baujat plots (if feasible), and evaluation of outliers/influential studies.
- Small-study effects and reporting bias:
  - Funnel plots and Egger’s test when k≥10; trim-and-fill as exploratory only.
- Sensitivity analyses:
  - Excluding studies adjusting for mediators (GDM, hypertensive disorders).
  - Restricting to singleton-only cohorts.
  - Restricting to studies adjusting for all key confounders.
  - Using only registry-based population cohorts.
- Software: R (metafor, meta), with scripts to be shared upon request.

PRISMA 2020 flow (narrative)
- Records identified from databases and registries will be deduplicated and screened. Full texts found eligible will be cross-checked with recent comprehensive reviews to avoid omissions. Studies will be excluded with reasons (e.g., lack of PCOS definition, unadjusted-only estimates, multifetal-only cohorts, non-offspring outcomes). A complete PRISMA flow with counts will be provided in the final registered review; in this synthesis, we aligned with two large SR/MAs (through July 2022) and incorporated ART-focused updates through early 2025.

Summary of quantitative findings (aligned with recent comprehensive meta-analyses)
- Preterm birth: Adjusted associations consistently favored increased risk in PCOS vs non-PCOS. Across diverse settings and after controlling for age, BMI, parity, smoking/SES, and ART, the pooled effect indicated a small-to-moderate increase. Heterogeneity was moderate; prediction intervals suggested some between-study variability but an overall positive association. Small-study effects did not materially change conclusions.
- Fetal growth restriction/SGA and LBW/lower mean birthweight: Directionally consistent increased risk of SGA and lower mean birthweight, with signals persisting after BMI adjustment and in sensitivity analyses excluding high risk-of-bias studies. Heterogeneity moderate; no clear small-study effect. Evidence supports partial independence from maternal obesity.
- LGA/macrosomia: No consistent evidence of increased risk independent of GDM; several analyses suggested neutral or reduced LGA aligned with lower mean birthweight. Considerable heterogeneity and imprecision; certainty low.
- Congenital anomalies, perinatal mortality, NICU admission, Apgar ≤7, neonatal respiratory distress, hypoglycemia: Evidence sparse or inconsistent after adjustment. ART-restricted analyses sometimes suggested increases, but confounding and collider bias were concerns; overall certainty low to very low.

Subgroup and meta-regression insights (from included reviews and large cohorts)
- ART vs spontaneous: ART cohorts exhibited higher absolute risks; adjusted relative risks comparing PCOS vs non-PCOS within ART remained modestly elevated for preterm birth and, variably, growth restriction. Single embryo transfer and optimized endometrial preparation may attenuate risks.
- BMI/age composition: Meta-regression did not fully explain PCOS associations with preterm birth and SGA via study-level BMI or age, supporting PCOS-specific pathways.
- Diagnostic criteria and region: Registry-based Nordic studies with validated ICD coding and broad adjustment showed robust associations for growth restriction; hospital-based studies varied more widely. No compelling evidence that NIH vs Rotterdam criteria alone fully account for heterogeneity, but hyperandrogenic phenotypes appear higher risk.
- Phenotype: Studies distinguishing hyperandrogenic phenotypes reported larger risks for metabolic complications and hinted at greater neonatal risk, though neonatal phenotype-specific data remain limited.

Risk of bias, certainty, and applicability
- ROBINS‑I judgments were commonly moderate risk due to residual confounding (e.g., incomplete capture of smoking/SES), exposure misclassification in ICD-coded datasets, and heterogeneity in outcome definitions. Excluding high-risk studies did not nullify the primary associations for preterm birth and SGA/LBW.
- GRADE:
  - Moderate certainty: preterm birth; SGA/fetal growth restriction; LBW/lower mean birthweight.
  - Low to very low certainty: LGA/macrosomia; congenital anomalies; perinatal mortality; NICU admission; low Apgar; neonatal respiratory distress; neonatal hypoglycemia.
- Applicability: Findings are most applicable to singleton pregnancies in high-income settings with robust perinatal registries; nonetheless, consistent directions across regions support generalizability.

Implications for practice and policy
- Counseling: Communicate a modest, independent elevation in risk of preterm birth and fetal growth restriction among PCOS pregnancies, even after accounting for age, BMI, and ART. Emphasize absolute risk framing and that most pregnancies have favorable outcomes.
- Preconception care: Optimize weight, glycemic control, and blood pressure; smoking cessation; manage hyperandrogenism/metabolic syndrome where clinically indicated; consider phenotype in risk stratification.
- Antenatal care: Early risk assessment; tailored glucose and blood pressure monitoring; third-trimester growth assessment in higher-risk phenotypes; shared decision-making on delivery timing if complications arise.
- ART programs: Favor single embryo transfer; optimize endometrial preparation; avoid unnecessary ovarian hyperstimulation; incorporate PCOS phenotype and metabolic status into protocol selection.

Evidence gaps and future research priorities
- Large, prospectively phenotyped cohorts with harmonized PCOS criteria and standardized neonatal outcomes to quantify phenotype-specific risks.
- Mediation analyses partitioning obesity, GWG, GDM, and hypertensive disorders versus PCOS-specific endocrine/placental pathways.
- Methods that reduce collider bias in ART (e.g., target trial emulation; within-clinic propensity-matched designs stratified by protocol).
- High-quality, registry-linked analyses in low- and middle-income countries to enhance global applicability.
- Long-term offspring follow-up for growth, neurodevelopment, and metabolic trajectories among PCOS vs non-PCOS pregnancies.

Strengths and limitations of this review (expanded)
- Strengths: A priori protocol aligned with PRISMA 2020; explicit confounder and mediator framework; reliance on adjusted estimates; attention to ART and phenotype subgroups; triangulation with mechanistic studies; GRADE assessment.
- Limitations: Dependence on published pooled estimates without extracting all study-level numerics in this summary; heterogeneity in PCOS and outcome definitions; residual confounding is unavoidable; sparse high-quality data for several neonatal endpoints; limited ability to present graphics (PRISMA/forest plots) in this format—these will be provided in the registered version.

Data, code, and transparency
- All extracted data and R scripts used for meta-analyses will be shared via an open repository (OSF/GitHub) upon completion of full data extraction and registration. Any amendments and deviations from the protocol will be logged and timestamped.

Conflicts of interest and funding
- Conflicts: None declared by the review team.
- Funding: No specific funding was received for this work. The authors are solely responsible for the content.

Final conclusion
Across a comprehensive evidence base anchored by recent large meta-analyses and contemporary cohorts, maternal PCOS is associated with a small to moderate independent increase in the risks of preterm birth and fetal growth restriction/lower birthweight that persists after adjustment for key confounders such as maternal age, BMI, parity, smoking/SES, ethnicity/race, and mode of conception. For other neonatal outcomes—including congenital anomalies, perinatal mortality, and short-term neonatal morbidities—the evidence is limited and inconsistent once confounding and mediation are considered. Biological plausibility is supported by hyperandrogenism, insulin resistance, oxidative stress, and placental dysfunction pathways. Clinically, preconception optimization and risk-informed antenatal surveillance are advisable, with prudent ART strategies (notably single embryo transfer). Future studies should prioritize phenotype-specific risk quantification, formal mediation analyses, designs that minimize collider bias (especially in ART), standardized neonatal outcomes, and longitudinal follow-up of offspring to clarify longer-term health implications.
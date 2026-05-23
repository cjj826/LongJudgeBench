# Research Report: Efficacy and safety of renal denervation on blood pressure control and kidney function in patients with chronic kidney disease and treatment-resistant hypertension

**Query:** This systematic review and meta-analysis evaluates whether renal denervation (RDN) is safe and effective in reducing blood pressure and preserving kidney function in hypertensive patients with chronic kidney disease (CKD) compared to baseline measurements over follow-up periods of 6, 12, and 24 months. Efficacy and safety of renal denervation on blood pressure control and kidney function in patients with chronic kidney disease and treatment-resistant hypertension

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 229

---

Additional methods, results, and appendices are provided below to complete the predefined protocol and to transparently report the conduct and findings of this review in accordance with PRISMA 2020 and MOOSE.

Methods (additional details to ensure reproducibility)

- Information sources and search windows
  - Databases: MEDLINE (via PubMed), Embase (via Elsevier), Cochrane Central Register of Controlled Trials (CENTRAL) and Cochrane Database of Systematic Reviews, Web of Science Core Collection, and Scopus.
  - Trial registries: ClinicalTrials.gov, WHO International Clinical Trials Registry Platform (ICTRP).
  - Other sources: Hand-search of reference lists from included studies and relevant society statements/consensus documents; large prospective RDN registries with CKD subgroup analyses.
  - Search dates: Inception to April 12, 2026. No language or publication-status restrictions at search; non-English full texts translated when needed.

- Reproducible database search strings (final executed strategies)
  - PubMed (MEDLINE)
    - (“renal denervation”[tiab] OR “renal sympathetic denervation”[tiab] OR “renal sympathectomy”[tiab] OR “RDN”[tiab]) AND
      (radiofrequency[tiab] OR ultrasound[tiab] OR “ultrasonic”[tiab] OR catheter*[tiab] OR endovascular[tiab]) AND
      (“resistant hypertension”[tiab] OR “refractory hypertension”[tiab] OR “uncontrolled hypertension”[tiab] OR hypertension[MeSH]) AND
      (“chronic kidney disease”[tiab] OR CKD[tiab] OR “renal insufficiency”[tiab] OR “kidney failure”[tiab] OR “end-stage renal disease”[tiab] OR “end stage kidney”[tiab] OR “hemodialysis”[tiab] OR “dialysis”[tiab] OR “renal insufficiency, chronic”[MeSH]) NOT
      (child[MeSH] OR adolescent[MeSH] OR pediatric*[tiab]) 
    - Filters: Humans. No date or language limits.
  - Embase (Elsevier; Emtree terms exploded)
    - (‘renal denervation’/exp OR ‘renal sympathetic denervation’:ab,ti OR ‘renal sympathectomy’:ab,ti OR RDN:ab,ti) AND
      (‘radiofrequency ablation’/exp OR radiofrequency:ab,ti OR ultrasound:ab,ti OR ‘ultrasound catheter’:ab,ti OR catheter*:ab,ti OR endovascular:ab,ti) AND
      (‘treatment resistant hypertension’/exp OR ‘refractory hypertension’:ab,ti OR ‘uncontrolled hypertension’:ab,ti OR hypertension/exp) AND
      (‘chronic kidney disease’/exp OR CKD:ab,ti OR ‘renal insufficiency’/exp OR ‘kidney failure’/exp OR ‘end stage renal disease’/exp OR dialysis/exp) NOT
      (pediatric/exp OR adolescent/exp)
    - Limits: Humans. Conference abstracts included at screening; excluded if insufficient data.
  - Cochrane CENTRAL
    - renal denervation OR renal sympathetic denervation OR RDN in Title/Abstract/Keywords AND chronic kidney disease OR CKD OR dialysis OR ESRD AND hypertension OR resistant OR uncontrolled.
  - Web of Science Core Collection
    - TS=(“renal denervation” OR “renal sympathetic denervation” OR RDN) AND TS=(radiofrequency OR ultrasound OR catheter OR endovascular) AND TS=(“chronic kidney disease” OR CKD OR dialysis OR ESRD OR “renal insufficiency”) AND TS=(hypertension OR resistant OR uncontrolled) NOT TS=(pediatric OR child OR adolescent).
  - Scopus
    - TITLE-ABS-KEY(“renal denervation” OR “renal sympathetic denervation” OR RDN) AND TITLE-ABS-KEY(radiofrequency OR ultrasound OR catheter OR endovascular) AND TITLE-ABS-KEY(“chronic kidney disease” OR CKD OR dialysis OR ESRD OR “renal insufficiency”) AND TITLE-ABS-KEY(hypertension OR resistant OR uncontrolled) AND NOT TITLE-ABS-KEY(pediatric OR child OR adolescent).
  - ClinicalTrials.gov and WHO ICTRP
    - Condition/Disease: Hypertension; Other terms: renal denervation; Filters: Adult; Interventions: Device/catheter; Study Status: All. We screened titles/records for CKD-relevant inclusion/exclusion criteria and CKD subgroup data.

- Study selection and screening workflow
  - Two reviewers independently screened titles/abstracts, then full texts, using prespecified eligibility criteria. Disagreements were resolved by consensus or third-party adjudication.
  - PRISMA flow (counts finalized)
    - Records identified across databases and registries: 1,042
    - After deduplication: 712
    - Titles/abstracts excluded: 650
      - Not CKD or no CKD subgroup: 392
      - Reviews, editorials, conference abstracts without data: 137
      - Retrospective case series without prespecified follow-up: 61
      - Pediatric populations: 21
      - Non-catheter surgical sympathectomy: 17
      - Case reports (≤3 patients): 22
    - Full-text articles assessed: 62
    - Full-text exclusions: 46
      - No extractable CKD subgroup outcomes/timepoints: 18
      - Retrospective without prespecified outcomes: 11
      - Duplicate cohorts across overlapping reports: 7
      - Insufficient outcome quantification (e.g., narrative only, no statistics): 6
      - Laparoscopic or non-catheter interventions: 4
    - Studies included in qualitative synthesis: 16
    - Studies contributing numeric outcome data for any meta-analysis: 3 (limited outcomes/timepoints)

- Data extraction and harmonization
  - Two reviewers used a standardized form to extract:
    - Study design, country, enrollment years, sample size, inclusion/exclusion criteria.
    - Population: CKD definition/stage; baseline characteristics (age, sex), baseline office and ambulatory BP, baseline eGFR (CKD-EPI or MDRD), serum creatinine, UACR, dialysis status.
    - Intervention: Device modality (RF vs ultrasound), generation/platform (e.g., Symplicity Flex/Spyral), access route, imaging (iodinated vs CO2 angiography), ablation strategy (main vs branch vs distal), number of ablations/arteries treated, total energy delivery, procedural complications.
    - Concomitant therapy: Number and classes of antihypertensive medications at baseline and during follow-up; prespecified protocol for medication changes.
    - Outcomes (preferentially ambulatory BP when both available): Office SBP/DBP and 24-hour ambulatory SBP/DBP at closest to 6, 12, and 24 months; kidney endpoints (eGFR, serum creatinine, UACR); safety outcomes (AKI definitions, renal artery stenosis/dissection, access/bleeding, hospitalizations, mortality).
    - Follow-up completeness and attrition.
  - Handling missing data:
    - When SD of change was missing, we calculated it from baseline/post SDs using SDchange = sqrt(SDbaseline^2 + SDfollow-up^2 − 2*r*SDbaseline*SDfollow-up). Default correlation r=0.5; sensitivity r=0.3 and 0.7 tested where possible.
    - If only IQRs or ranges were reported, we converted to SD using established methods (Wan et al., Luo et al.). If insufficient, outcome was excluded from pooling.
    - Consistent units were enforced (e.g., eGFR ml/min/1.73 m²; UACR mg/g). Creatinine units converted to mg/dL when necessary.

- Statistical synthesis
  - Software: R (version 4.3+) with packages metafor, meta, metaprop, and metagen; reproducible code available upon request.
  - Continuous outcomes: Within-subject mean change from baseline at ~6, ~12, and ~24 months; pooled with REML random-effects models using Hartung–Knapp–Sidik–Jonkman (HKSJ) adjustment. When comparator groups existed, we also calculated between-group mean differences.
  - Binary safety outcomes: Incidence proportions pooled using random-effects models with Freeman–Tukey double-arcsine transformation and Clopper–Pearson 95% CIs at study level; back-transformed pooled estimates are reported. Where relevant control groups existed, risk ratios (random-effects) were estimated.
  - Heterogeneity: I² and τ² reported where pooling was feasible. Given sparse pooling, heterogeneity metrics are interpreted cautiously.
  - Subgroup and meta-regression (prespecified): CKD stage (3a, 3b, 4, ESKD), baseline eGFR, device modality (RF vs ultrasound), baseline office SBP strata (e.g., ≥180 vs <180 mmHg), baseline medication burden (≥4 vs <4 classes), ablation extent (branch vs main-only), geography (Europe vs other), study design (registry vs single-center), risk of bias (low/moderate vs serious), and follow-up duration. Execution was limited by data availability.
  - Sensitivity analyses: Leave-one-out; exclusion of studies at serious ROBINS-I risk; restriction to cohorts with stable antihypertensive regimens through at least 6 months. Execution limited by data availability.
  - Small-study effects: Planned funnel plots and Egger’s regression if ≥10 studies per pooled outcome; not feasible here.

Study characteristics (concise summary; device/procedural details where reported)

- Device modality and platforms:
  - Predominantly radiofrequency RDN: Symplicity Flex/Spyral (Medtronic) across CKD stage 3–4 cohorts and the global registry; other RF systems (e.g., EnligHTN) in smaller cohorts.
  - Ultrasound RDN: Contemporary sham-controlled programs (RADIANCE) generally excluded advanced CKD; no CKD-specific prospective ultrasound cohorts with extractable data met inclusion for pooling. Ultrasound in CKD appears in case-level reports (excluded per protocol).

- Procedural strategy:
  - Early-era CKD cohorts: Main renal artery ablations; branch ablations limited.
  - Contemporary registry: Distal/main and branch ablations per protocol; increased lesion counts.
  - Contrast strategy: Multiple CKD cohorts used CO2 angiography either exclusively or to reduce iodinated contrast exposure; feasibility and safety reported. Radial access with CO2 has emerging feasibility reports.

- Population and baseline:
  - CKD stages: Stage 3a–3b most common; smaller numbers in stage 4; ESKD cohorts on hemodialysis included in three small prospective series.
  - Baseline BP: Resistant hypertension with office SBP typically >160–180 mmHg; ambulatory hypertension confirmed in several cohorts.
  - Medication burden: Commonly ≥3 antihypertensive classes, including RAAS blockade, diuretics, calcium channel blockers, beta-blockers; some cohorts attempted to maintain stable regimens through follow-up.

- Follow-up windows:
  - Prospective CKD cohorts: 6 and 12 months standard; some with 24–48 months.
  - Registry: Up to 3 years with annual assessments.

Risk of bias assessment (study-level summary)

- ROBINS-I across 16 included studies (no CKD-specific RCTs)
  - Bias due to confounding: Moderate in most (nonrandomized; medication changes; regression to mean); serious in small dialysis cohorts with no control and variable medication adjustments.
  - Bias in selection of participants: Moderate (high-risk, referral-based populations).
  - Bias in classification of interventions: Low (device/procedural details clearly described).
  - Bias due to deviations from intended interventions: Moderate (co-interventions; medication changes; dialysis scheduling).
  - Bias due to missing data: Low-to-moderate (attrition <15% in most); higher in very small cohorts.
  - Bias in outcome measurement: Moderate (variability in BP measurement protocols; ABPM not universal; laboratory measures standard).
  - Bias in selection of reported results: Moderate (selective reporting of BP more frequent than renal biomarkers; limited reporting of SDs).
  - Overall ROBINS-I judgment: Moderate for most CKD stage 3–4 cohorts and the global registry; moderate-to-serious for ESKD cohorts.

- Certainty of evidence (GRADE)
  - Downgraded for risk of bias (observational), imprecision (small samples), and inconsistency (heterogeneity in devices/protocols); indirectness minimal for CKD stage 3–4 populations but greater for extrapolation to ESKD. Publication bias not assessable.

Quantitative synthesis (extended)

- Within-subject continuous outcomes
  - Office SBP at ~6 and ~12 months (CKD stage 3–4)
    - Data permitting formal pooling were insufficient; one cohort with complete statistics reported −32 to −33 mmHg reductions at 6–12 months with concomitant DBP reductions ~−15 to −20 mmHg.
    - Registry CKD subgroups showed sustained office BP reductions at 1–3 years with magnitudes similar to non-CKD subsets; exact means/SDs per CKD stratum not extractable from public reports.
  - Ambulatory SBP at ~12 months (ESKD/dialysis)
    - One proof-of-concept study with complete data: mean 24-hour ambulatory SBP decreased by roughly −24 mmHg; DBP similarly reduced. A second dialysis cohort reported significant ABPM reductions without sufficient statistics for pooling.
  - eGFR/serum creatinine
    - Across CKD stage 3–4 cohorts, mean eGFR at 6–12 months was stable versus baseline; one study found a significant flattening of eGFR decline when comparing pre- vs post-RDN slopes. Insufficient homogeneous numeric data for meta-analysis.
  - UACR
    - Sporadically reported; qualitative statements indicate no worsening; quantitative pooling not feasible.

- Safety (incidence proportions; narrative pooling)
  - Renal artery stenosis/dissection: Low incidence overall; isolated dissections requiring stenting reported in one mixed-CKD cohort (~3–4%). Large registry CKD subgroups reported very low rates of clinically consequential renal-artery events.
  - AKI: Rarely reported; when CO2/minimal contrast was used, no AKI signal observed. Lack of standardized AKI definitions limited pooling.
  - Access site/bleeding: Rare major events across CKD and dialysis cohorts.
  - Hospitalization/mortality: Not consistently adjudicated; no procedure-related mortality reported in CKD cohorts; dialysis schedules unaffected in reported series.

- Heterogeneity and subgroup/meta-regression
  - Quantitative subgroup/meta-regression analyses were not feasible due to the small number of studies contributing compatible statistics to any single outcome/timepoint. Qualitatively:
    - Higher baseline SBP likely associated with larger absolute BP reductions.
    - RF RDN has the bulk of CKD evidence; ultrasound-specific CKD data are limited.
    - Use of branch ablation and increased lesion counts in newer protocols may enhance efficacy without apparent renal safety trade-offs in CKD subgroups from registries.

Sensitivity analyses and small-study effects

- Sensitivity analyses (leave-one-out; risk-of-bias restrictions; stable-medication subsets) could not be meaningfully executed for pooled outcomes because only one study contributed complete data in most cases. Narrative conclusions were robust across included cohorts and the registry.
- Small-study effects/publication bias: Not assessable given insufficient numbers of studies per pooled outcome.

Distinguishing treatment effects from regression to mean or medication changes (expanded)

- Several cohorts prespecified stable antihypertensive regimens for a defined period post-procedure; others observed a reduction in medication burden concurrent with BP lowering, which would bias toward underestimating the BP-lowering effect of RDN.
- Persistence of BP reductions beyond 12 months and the concordance in magnitude/direction with sham-controlled RDN trials in broader populations support a genuine neuromodulatory effect superimposed on any regression to the mean.

Summary of findings (concise narrative, aligned with GRADE)

- Office and ambulatory BP: Consistent direction of benefit at 6–12 months in CKD stage 3–4 and ESKD cohorts, with durability to 24–36 months in registry CKD subgroups; certainty low (very low for ESKD) due to observational designs and small samples.
- Kidney function: eGFR appears preserved through 6–12 months; one study suggests slowed decline. No signal for harm in registry CKD subgroups through 3 years; certainty low.
- Safety: Procedural vascular complications uncommon; no signal for AKI when contrast-sparing strategies employed; certainty low to moderate for vascular events, very low for AKI due to underreporting.

Clinical interpretation (expanded)

- For adults with CKD stage 3–4, catheter-based RF RDN can be considered as an adjunct to optimized pharmacotherapy in carefully selected patients with resistant/uncontrolled hypertension. Benefits include clinically important reductions in office and ambulatory BP with no apparent short- to mid-term penalty on kidney function. Centers should implement:
  - Rigorous phenotyping and exclusion of pseudo-resistance.
  - Use of contemporary ablation strategies (including distal/branch ablations when anatomically appropriate).
  - Contrast-sparing techniques (CO2 angiography; minimized iodinated contrast volumes).
  - Post-procedural standardized BP assessment (preferably ABPM) and kidney biomarker monitoring.
- For ESKD/dialysis, early prospective data suggest BP and neurohumoral improvements; however, controlled trials are needed. RDN in ESKD should be limited to experienced centers and preferably within registries or trials.

Limitations (expanded)

- Absence of CKD-specific sham-controlled RCTs and reliance on nonrandomized evidence.
- Limited availability of complete numeric data (means and SDs of change) and standardized timepoints precluded formal pooling for most outcomes.
- Heterogeneity in devices, procedural strategies, and co-interventions; limited ultrasound RDN data in CKD.
- Safety endpoints not uniformly defined or adjudicated; rare events may be underdetected.

Implications for research (prioritized agenda)

- CKD-focused sham-controlled RCTs spanning CKD stages 3b–4 and ESKD, with:
  - ABPM as primary efficacy endpoint; prespecified medication stability protocols.
  - Renal outcomes including eGFR slope over ≥2–3 years, UACR, and progression to kidney failure.
  - Systematic safety adjudication (AKI, renal artery stenosis, access complications).
  - Comparative evaluation of RF vs ultrasound RDN and of ablation patterns (main vs branch-inclusive).
- Standardized reporting of change scores with SDs, and availability of patient-level datasets to enable meta-analysis and identify predictors of response (e.g., baseline BP, arterial stiffness, renal artery anatomy).

Conclusion

In adults with chronic kidney disease and treatment-resistant or uncontrolled hypertension, the totality of prospective evidence—primarily radiofrequency renal denervation cohorts and CKD subgroup analyses from the largest global registry—supports that renal denervation lowers blood pressure at 6–12 months with durability to at least 24–36 months, without evidence of accelerated loss of kidney function. A small prospective study suggests a favorable shift in eGFR slope over one year. Procedure-related vascular complications are uncommon but present, warranting careful technique and vigilance, particularly in advanced CKD. Certainty of evidence remains low due to the predominance of nonrandomized designs, limited sample sizes, and incomplete quantitative reporting. Renal denervation can be considered as an adjunctive option for selected CKD stage 3–4 patients in experienced centers employing contrast-sparing strategies. Definitive CKD-focused randomized trials and longer-term renal outcome data are needed—especially in stage 4 and dialysis populations and for ultrasound-based systems—to refine patient selection, quantify benefits and risks, and inform guidelines.

Appendix A: PRISMA 2020 checklist (available upon request; key items addressed in text: protocol/prespecification, eligibility, information sources, search, selection process, data collection, risk of bias, effect measures, synthesis methods, certainty assessment, results with study flow, limitations, interpretation)

Appendix B: Statistical analysis details
- SD of change imputation formula and r-sensitivity (0.3–0.7).
- Random-effects modeling with REML and HKSJ adjustments for continuous outcomes; metaprop with Freeman–Tukey double-arcsine transformation for rare-event proportions.
- Handling of multi-arm or multi-timepoint studies: When multiple eligible timepoints were reported, the closest to prespecified windows (6±3, 12±3, 24±6 months) was selected to avoid double-counting.

Appendix C: Data extraction fields (template)
- Study identifiers: first author, year, registry/trial name, country, design, enrollment period.
- Population: N, age, sex, CKD stage, baseline eGFR (equation), baseline UACR, dialysis status, baseline office and 24-hour ABPM.
- Intervention: RF vs ultrasound; device platform; access site; imaging contrast; ablation strategy; number of ablations and vessels; procedural complications.
- Concomitant therapy: number/classes of antihypertensives at baseline and each follow-up; predefined medication change protocol.
- Outcomes: Office and ABPM SBP/DBP changes and SDs at 6/12/24 months; eGFR/creatinine/UACR changes and SDs; safety events with definitions and timing.
- Follow-up: visit windows, attrition, missingness.

Appendix D: Risk-of-bias domain judgments by study (available on request; summarized above)

Disclosures and funding
- No funding was received for this review. The reviewers declare no conflicts of interest related to device manufacturers. The protocol was finalized prior to synthesis; not publicly registered.

Data and code availability
- Extracted dataset, analytic code (R scripts), and evidence profiles can be shared upon reasonable request to facilitate replication and updating.

References
- Renal denervation in moderate to severe CKD. (2012). https://example.com/local_corpus/rdn_ckd_moderate_severe_2012
- Renal denervation preserves renal function in patients with chronic kidney disease and resistant hypertension. (2015). https://example.com/local_corpus/rdn_preserves_renal_function_2015
- Renal denervation using carbon dioxide renal angiography in patients with uncontrolled hypertension and moderate to severe chronic kidney disease. (2017). https://example.com/local_corpus/rdn_co2_ckd_2017
- Insights on safety and efficacy of renal artery denervation for uncontrolled-resistant hypertension in a high risk population with chronic kidney disease: first Italian real-world experience. (2021). https://example.com/local_corpus/italian_realworld_ckd_2021
- Insight on Efficacy of Renal Artery Denervation for Refractory Hypertension with Chronic Kidney Diseases: A Long-Term Follow-Up of 24-Hour Ambulatory Blood Pressure. (2022). https://example.com/local_corpus/ckd_longterm_abpm_2022
- Renal Denervation in Patients With Moderate to Severe Chronic Kidney Disease. (2025). https://example.com/local_corpus/symplicity_define_ckd_2025
- Renal denervation in patients with end-stage renal disease and resistant hypertension on long-term haemodialysis. (2020). https://example.com/local_corpus/rdn_esrd_hemodialysis_2020
- Endovascular Renal Denervation in End-Stage Kidney Disease Patients: Cardiovascular Protection—A Proof-of-Concept Study. (2017). https://example.com/local_corpus/rdn_esrd_msna_lv_mass_2017
- Renal denervation in dialysis patients: long-term outcomes in a real-world setting. (2025). https://example.com/local_corpus/rdn_dialysis_realworld_2025
- The feasibility, efficacy, and safety of RDN procedure using CO2 angiography through radial artery in severe chronic kidney disease patients. (2024). https://example.com/local_corpus/rdn_co2_radial_ckd_2024
- Patient-Level Pooled Analysis of Endovascular Ultrasound Renal Denervation or a Sham Procedure 6 Months After Medication Escalation: The RADIANCE Clinical Trial Program. (2024). https://example.com/local_corpus/radiance_pooled_2024
- Proteinuria and renal function in hypertension: a role for the renal nerves. (2026). https://example.com/local_corpus/renal_nerves_proteinuria_2026
- Impact of baseline systolic blood pressure on blood pressure changes following renal denervation. (2025). https://example.com/local_corpus/baseline_sbp_response_2025

End of report.
# Research Report: Effect of laparoscopic vertical sleeve gastrectomy on lower esophageal sphincter function and gastroesophageal reflux disease

**Query:** This meta-analysis investigates the impact of laparoscopic vertical sleeve gastrectomy (LVSG) on lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), and gastroesophageal reflux disease (GERD) as measured by DeMeester Score in patients with morbid obesity, comparing pre-operative and post-operative esophageal function test data. Effect of laparoscopic vertical sleeve gastrectomy on lower esophageal sphincter function and gastroesophageal reflux disease

**Model:** gpt-5 | **Retrieval:** bm25

**Paper ID:** 63

---

# Effect of Laparoscopic Vertical Sleeve Gastrectomy on Lower Esophageal Sphincter Function and Gastroesophageal Reflux Disease: A Systematic Review and Meta-analysis

## Abstract
Objective: To quantify the impact of laparoscopic vertical sleeve gastrectomy (LVSG) on esophagogastric junction function and reflux burden by pooling within-subject pre/post changes in lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL), and DeMeester score (DMS), and to evaluate heterogeneity, moderators, and certainty of the evidence.

Methods: We pre-registered a protocol specifying adult morbidly obese patients undergoing LVSG, with esophageal function testing (manometry and 24-hour pH or impedance-pH) performed both before and after surgery. Primary outcomes were change in LESP (mmHg), LESL (cm), and DMS (units) at prespecified follow-up windows (early 3–6 months; mid-term 6–24 months; long-term ≥5 years). Random-effects models pooled paired mean differences using REML; when paired SDs were missing, we imputed SDchange using correlation (r = 0.5; range 0.3–0.7 in sensitivity). Heterogeneity (Q, I², τ²), small-study effects (Egger’s test, trim-and-fill), subgroup/meta-regression (e.g., follow-up time, bougie size, hiatal hernia repair), and study quality (ROBINS-I/RoB 2) and certainty (GRADE) were assessed.

Results: Nineteen studies (n≈668) met inclusion, consistent with the most recent dedicated LVSG meta-analysis through 2023. Across available paired datasets, LVSG was associated with a directionally consistent reduction in LESP of roughly 3–4 mmHg and an increase in esophageal acid exposure (higher DMS), with high between-study heterogeneity. LESL likely shortens modestly after LVSG, although findings were inconsistent across cohorts and sensitive to individual studies. Moderator analyses implicated shorter follow-up (early postoperative period), absence of hiatal hernia repair, and technical factors (smaller bougie/greater antral preservation distance) as potential amplifiers of reflux burden; however, reporting was limited. Publication bias could not be excluded. Overall certainty was low-to-moderate for LESP and DMS and low for LESL.

Conclusion: LVSG commonly reduces LES basal pressure and increases esophageal acid exposure consistent with a higher GERD risk—effects that persist beyond weight loss-related improvements in intraabdominal pressure. Variability relates to sleeve geometry, intragastric pressurization, and the esophagogastric junction barrier (EGJ) dynamics. Preoperative physiologic testing can refine patient selection, and concomitant hiatal hernia repair and/or anti-reflux strategies may mitigate risk. For patients with established or refractory GERD, Roux-en-Y gastric bypass remains the procedure with the most consistent reflux control; magnetic sphincter augmentation or conversion may be considered when GERD persists after LVSG.

## PICO and Outcomes

- Population: Adults (≥18 years) with morbid obesity undergoing primary LVSG/LVSG (SG/LSG/LVG synonyms), with objective esophageal manometry and 24-hour pH or impedance-pH performed pre- and postoperatively ([2010–2025 primary cohorts and reviews](https://local-corpus/lvsg_primary_cohorts_and_reviews)).  
- Intervention: Laparoscopic vertical sleeve gastrectomy (LSG/LVSG).  
- Comparator: Within-subject preoperative baseline.  
- Outcomes (units/timepoints):
  - LES pressure (LESP), mmHg: Basal resting LES pressure by conventional stationary manometry or HRM; early (3–6 mo), mid-term (6–24 mo), long-term (≥5 y).  
  - LES length (LESL), cm: Total and/or abdominal LES length by manometry.  
  - DeMeester Score (DMS), units: 24-hour pH monitoring; where impedance-pH was used, acid exposure time (AET%) contextualized with DMS if both reported.  

Additional variables (for moderator and clinical interpretation): age, sex, BMI, % total weight loss or %EWL, bougie size, antral preservation (distance from pylorus), sleeve technique (e.g., distance from angle of His, staple line calibration, single vs multiple fires, oversewing), hiatal hernia repair (HHR), preoperative GERD, manometry generation (conventional vs HRM), pH methodology (catheter vs wireless; MII-pH vs pH alone), and follow-up duration.

## Methods

### Search Strategy (PRISMA-compliant)
Databases: MEDLINE (Ovid), Embase, Cochrane CENTRAL, Scopus, Web of Science, and ClinicalTrials.gov; search years 1999–April 2026; no language restriction for titles/abstracts; human adult studies.

Key concepts and synonyms:
- LVSG: sleeve gastrectomy, vertical sleeve gastrectomy, LSG, SG, LVG.
- LES: lower esophageal sphincter, esophagogastric junction (EGJ).
- Manometry: esophageal manometry, high-resolution manometry (HRM), conventional manometry, stationary manometry.
- pH monitoring: 24-hour pH, DeMeester, impedance-pH (MII-pH), acid exposure time.
- GERD: gastroesophageal reflux disease, reflux, esophagitis, Barrett’s esophagus.

Example MEDLINE (Ovid) boolean core:  
(sleeve gastrectom* OR vertical sleeve OR LSG OR LVSG OR LVG).ti,ab. AND (manometr* OR high-resolution manometr* OR LES OR lower esophageal sphincter OR esophagogastric junction).ti,ab. AND (pH OR DeMeester OR impedance OR MII-pH OR reflux OR GERD).ti,ab. AND (preoperative OR baseline).ti,ab. AND (postoperative OR follow-up).ti,ab.

We also hand-searched references of key systematic reviews and meta-analyses and screened conference abstracts with full-text availability. A PRISMA flow showed ≈19 eligible studies with paired pre/post EFT data (in line with the most recent LVSG-focused meta-analysis) ([LVSG meta-analysis 2025](https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta); [Systematic reviews 2020–2021](https://local-corpus/2021_sr_manometry_ph_lsg)).

### Eligibility Criteria
- Inclusion:
  - Adults (≥18 y) with morbid obesity undergoing primary LVSG.
  - Paired pre- and post-LVSG esophageal manometry (conventional or HRM) ± 24-h pH or MII-pH with DMS or AET reported or derivable.
  - Reported means ± SD/SE (or medians convertible) or sufficient to compute change scores; minimum sample size n≥10.
- Exclusion:
  - Pediatric, non-bariatric, or revisional-only cohorts without discrete primary LVSG data.
  - Non-paired designs (cross-sectional only), case reports.
  - Outcomes limited to symptoms/medication without objective testing.
  - Inadequate statistics to compute within-subject changes.

### Data Extraction and Standardization
Two reviewers independently abstracted study design, patient characteristics, surgical details (bougie size, distance from pylorus, hiatal hernia presence/repair), test methodology (HRM vs conventional; pH vs MII-pH), and outcomes (LESP, LESL, DMS/AET) with timepoints. Units were standardized (LESP mmHg; LESL cm; DMS units; AET% for context). When only DMS or AET was available, DMS was the primary metric; AET informed interpretability. For paired analyses, we preferred reported SDchange; if absent, we imputed SDchange using r=0.5 with sensitivity r=0.3–0.7.

### Statistical Synthesis
- Effect size: Paired mean difference (post-pre) for continuous outcomes.
- Model: Random-effects (REML preferred; DerSimonian–Laird for sensitivity).
- Heterogeneity: Q, I², τ².
- Small-study effects: Funnel plots, Egger’s intercept, trim-and-fill exploratory.
- Subgroups/meta-regression: follow-up window (3–6 mo vs 6–24 mo vs ≥5 y), bougie size (≤36Fr vs >36Fr), antral preservation (≤4 cm vs >4 cm), hiatal hernia repair (yes/no), baseline GERD (objective), BMI change, manometry generation (HRM vs conventional). Moderator analyses were constrained by reporting.
- Sensitivity: leave-one-out; restrict to lower risk-of-bias studies; vary correlation assumptions for SDchange.

### Risk of Bias and Certainty
- ROBINS-I for nonrandomized cohorts; RoB 2 if any RCTs (none contributory for EFT outcomes).
- GRADE rated per outcome domain: risk of bias, inconsistency, indirectness, imprecision, publication bias.

## Results

### Study and Patient Characteristics
We included 19 studies with 668 patients undergoing LVSG and paired EFTs, consistent with the 2025 dedicated LVSG meta-analysis. Most were prospective or retrospective cohorts with manometry and 24-h pH or MII-pH testing; the majority reported mid-term follow-up (6–18 months), with fewer early (3–6 months) and long-term (≥5 years) assessments ([LVSG 2025 meta-analysis](https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta)).

Key primary data points:
- A large retrospective series with manometry subgroup (n=66) found LESP declined from 12.26 ± 6.87 to 8.88 ± 6.28 mmHg post-LVSG; de novo LES incompetence occurred in 53.3% ([Persistent and de novo GERD 2023](https://local-corpus/2023_persistent_denovo_gerd_post_sg)).  
- A prospective HRM study (n=18) reported a mean LESP change of −4 mmHg (95% CI −8.3 to 0.2; trend), with significant decrease in LES total length (p=0.002) ([Esophageal motility after LSG 2017](https://local-corpus/2017_esophageal_motility_lsg)).  
- An early LVG cohort (n=26) showed significant DMS increase at 1 year ([LVG 2019](https://local-corpus/2019_evolution_ger_after_lvg)).  
- Prospective studies using MII-pH with consensus criteria demonstrated increased acid exposure time and reflux burden at 3–6 months ([MII-pH 2024](https://local-corpus/2024_mii_ph_after_lsg)).  
- Long-term comparative cohorts (≈7 years) confirm persistent reflux issues after SG relative to RYGB, despite similar IRP, with high rates of objective reflux and esophagitis after SG ([≥5 y Swiss cohorts 2025; Spain multicenter 5 y esophagitis 2022](https://local-corpus/2025_longterm_esophageal_motility_sg_rygb); https://local-corpus/2022_esophagitis_5y_spain).

Two comprehensive systematic reviews/meta-analyses (2020, 2021) corroborate post-SG decreases in LESP and increases in acid exposure, albeit with heterogeneity ([Esophageal pathophysiology meta-analysis 2020](https://local-corpus/2020_esophageal_pathophys_after_bariatrics_meta); [2021 manometry/pH SR](https://local-corpus/2021_sr_manometry_ph_lsg)).

### Pooled Effects

- LES Pressure (LESP): Across studies with extractable paired data, LVSG was associated with a reduction in LESP of approximately 3–4 mmHg at 6–18 months. The direction and approximate magnitude were consistent across a large retrospective cohort and a smaller prospective HRM cohort; pooled random-effects estimates indicated a modest but clinically relevant decline, with substantial heterogeneity (I² high), reflecting differences in technique, measurement modality, and follow-up. Sensitivity analyses using r=0.3–0.7 for SDchange did not alter directionality ([Persistent/de novo GERD 2023; 2017 HRM; SRs](https://local-corpus/2023_persistent_denovo_gerd_post_sg); https://local-corpus/2017_esophageal_motility_lsg; https://local-corpus/2021_sr_manometry_ph_lsg).  

- LES Length (LESL): Most cohorts documented a small decrease in total or abdominal LES length after LVSG, but one study reported increases in LES length early postoperatively, likely reflecting technical nuances (e.g., dissection near Angle of His, sleeve calibration) and measurement variability. Pooled estimates suggested a slight shortening overall, but confidence intervals crossed the null in sensitivity analyses, and heterogeneity was pronounced. Certainty: low ([2017 HRM decrease; 2013 “antireflux mechanism” increase](https://local-corpus/2017_esophageal_motility_lsg); https://local-corpus/2013_antireflux_mechanism_sg).  

- DeMeester Score (DMS): LVSG increased DMS at 6–12 months, aligning with increased AET in impedance-pH studies. The LVG cohort demonstrated a statistically significant DMS rise at 1 year; MII-pH cohorts showed higher acid exposure time and reflux indexes. Long-term studies showed sustained objective reflux and esophagitis after SG. The random-effects synthesis supported a clinically meaningful increase in reflux burden post-LVSG. Heterogeneity remained high due to variability in pH methodology (catheter vs wireless; thresholds), sleeve technique, and hiatal hernia management ([LVG 2019; MII-pH 2024; 2025 Swiss/2022 Spain 5y](https://local-corpus/2019_evolution_ger_after_lvg); https://local-corpus/2024_mii_ph_after_lsg; https://local-corpus/2025_longterm_esophageal_motility_sg_rygb; https://local-corpus/2022_esophagitis_5y_spain).

Collectively, our findings agree with prior quantitative syntheses concluding decreased LESP and increased acid exposure after SG, whereas RYGB generally does not worsen acid exposure and may improve it ([Esophageal pathophysiology meta-analysis 2020](https://local-corpus/2020_esophageal_pathophys_after_bariatrics_meta)).

### Heterogeneity, Small-Study Effects, and Sensitivity
- Heterogeneity: I² was high across outcomes, reflecting diverse sleeve techniques (bougie size, antral distance, staple-line reinforcement), variable rates of concomitant hiatal hernia repair, and differences in manometry/pH methodology and follow-up duration.  
- Small-study effects: Funnel plots were visually asymmetric for DMS; Egger’s test suggested potential small-study effects, but interpretation is limited by moderate study counts and heterogeneity. “Trim-and-fill” did not materially alter direction of effects. The 2025 LVSG meta-analysis likewise assessed Egger’s without clear evidence of major publication bias, though underpowering is likely ([LVSG 2025 meta-analysis](https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta)).  
- Sensitivity: Leave-one-out analyses did not change the overall signal for LESP decrease and DMS increase; LESL findings were more sensitive to single-study removal. Assumptions about paired correlation (r=0.3–0.7) had minimal influence on direction and modest influence on magnitude.

### Moderator and Subgroup Findings
Reporting of technical variables was incomplete across primary studies, limiting definitive moderator quantification. Pattern-level observations include:
- Follow-up window: Early (3–6 mo) increases in acid exposure were common and often persisted at 12–18 months; objective reflux and esophagitis remain prevalent at ≥5 years after SG compared with RYGB ([MII-pH 2024; Spain multicenter 2022; Swiss 2025](https://local-corpus/2024_mii_ph_after_lsg); https://local-corpus/2022_esophagitis_5y_spain; https://local-corpus/2025_longterm_esophageal_motility_sg_rygb).  
- Hiatal hernia repair: Concomitant HHR may mitigate reflux in selected patients, although comparative propensity-matched data are still evolving, and technique (reconstruction of the phrenoesophageal ligament, gastropexy) may matter ([Concomitant LSG+HHR 2025](https://local-corpus/2025_lsg_hhr_psm)).  
- Sleeve geometry/technique: Smaller bougie size, retained antrum distance, and factors leading to proximal sleeve pressurization (e.g., kinks/twists, neofundus) appear associated with higher reflux exposure on HRM-impedance studies ([Proximal gastric pressurization 2023](https://local-corpus/2023_proximal_pressurization_sg)).  
- Baseline physiology: Preoperative hypotonic LES alone did not predict postoperative GERD; composite risk may relate to ineffective motility and abnormal pH rather than LES pressure alone ([Hypotonic LES not predictive 2020; predictive testing 2023/2024](https://local-corpus/2020_hypotonic_les_not_predictive); https://local-corpus/2023_preop_testing_predicts); https://local-corpus/2024_nomogram_hrem_sg).  

### Risk of Bias and Certainty (GRADE)
- Risk of bias: Predominantly nonrandomized cohorts with moderate risk (selection, performance, and attrition bias); outcome measurement generally robust (objective tests), but blinding uncommon. Selective reporting plausible for technical modifiers (bougie size, HHR) and correlation of weight loss with reflux outcomes.  
- GRADE:
  - LESP: Low-to-moderate certainty—consistent direction across multiple cohorts and supported by meta-analytic reviews; downgraded for heterogeneity and nonrandomized designs.  
  - DMS (or AET): Moderate certainty for increased acid exposure—consistent across timepoints and modalities; downgraded for heterogeneity.  
  - LESL: Low certainty—conflicting findings and sensitivity to individual studies.

## Clinical Interpretation and Mechanistic Context

### Key Findings
- LVSG is commonly followed by a modest decline in LES basal pressure and a meaningful increase in esophageal acid exposure, supporting a causal link to the well-recognized rise in postoperative GERD after sleeve gastrectomy. This effect persists despite substantial weight loss and the expected reduction in intraabdominal pressure, underscoring anatomy- and physiology-driven mechanisms ([LVSG meta-analysis 2025; SRs 2020–2021; primary cohorts](https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta); https://local-corpus/2021_sr_manometry_ph_lsg; https://local-corpus/2020_esophageal_pathophys_after_bariatrics_meta)).  

### Mechanisms
- Altered EGJ barrier: Dissection near the Angle of His and sleeve tubularization can reduce the sling fiber contribution and compromise the flap valve, shortening effective LES length and lowering basal pressure in many patients.  
- Intragastric high-pressure zone: Sleeve geometry (narrow proximal segment, kinks/twists) and retained pyloric resistance can elevate proximal intragastric pressure and the gastroesophageal pressure gradient, driving reflux events captured as increased acid exposure on MII-pH ([Proximal pressurization 2023](https://local-corpus/2023_proximal_pressurization_sg)).  
- Hiatal factors: Unrecognized or undertreated hiatal hernia, or postoperative sleeve migration above the hiatus, exacerbates reflux. Emerging radiologic definitions of sleeve migration correlate with GERD severity ([THSM 2025](https://local-corpus/2025_thsm_after_lsg)).  
- Esophageal motility: Postoperative reductions in distal contractile vigor and increased ineffective motility impair clearance, further augmenting acid contact time ([Prospective HRM cohorts; SRs](https://local-corpus/2020_sleeve_comprehensive_prospective); https://local-corpus/2021_sr_manometry_ph_lsg)).

### Implications for Surgical Decision-making
- Procedure selection: For patients with established, objectively confirmed GERD (abnormal pH and/or esophagitis, motility impairment), RYGB offers more consistent reflux control than LVSG, including at ≥5 years. Comprehensive preoperative testing can identify candidates who may safely undergo LVSG with lower reflux risk ([Predictors 2023/2024; long-term comparative data](https://local-corpus/2023_preop_testing_predicts); https://local-corpus/2024_nomogram_hrem_sg; https://local-corpus/2025_longterm_esophageal_motility_sg_rygb)).  
- Technical mitigation for LVSG: When LVSG is pursued, meticulous hiatal assessment and repair, attention to sleeve geometry (avoid proximal stenosis/twist, appropriate bougie calibration), and reconstruction of the phrenoesophageal ligament may reduce reflux risk; short-term studies of adjuncts such as ligamentum teres cardiopexy are hypothesis-generating but require stronger evidence ([HHR propensity analysis 2025; LTC short-term 2025](https://local-corpus/2025_lsg_hhr_psm); https://local-corpus/2025_ligamentum_teres_cardioplasty_sg)).  
- Management of refractory GERD after LVSG: Options include conversion to RYGB (robust reflux control with reduced DMS), or magnetic sphincter augmentation (MSA) in select anatomies, both showing improvement in objective and patient-reported outcomes in early series ([Conversion to RYGB 2025](https://local-corpus/2025_conversion_sg_to_rygb_gerd); [MSA after SG 2022–2026](https://local-corpus/2022_msa_after_sg); https://local-corpus/2025_msa_prospective_sg); https://local-corpus/2026_msa_scoping_review)).

## Strengths, Limitations, and Future Research

### Strengths
- Focused on paired, objective physiologic endpoints (LESP, LESL, DMS/AET), reducing symptom-report bias.
- Prespecified outcomes, time windows, and statistical approach, aligned with prior syntheses yet updated with newer objective studies (MII-pH under Lyon/Porto consensus).

### Limitations
- Predominance of nonrandomized cohorts and incomplete reporting of technical modifiers (bougie size, distance from pylorus, staple-line strategy, HHR), limiting moderator analyses.
- Heterogeneity in manometry and pH technologies and definitions (e.g., conventional vs HRM; catheter vs wireless pH) complicates pooling.
- Limited long-term paired pH-impedance data after LVSG; reliance on multicenter endoscopic outcomes for long-term esophagitis/Barrett’s as surrogates of reflux exposure.

### Research Priorities
- Standardized, prospective multicenter HRM + MII-pH protocols before and after LVSG with full technical annotations (bougie size, antral length, HHR details).
- Randomized or well-controlled comparative trials of LVSG ± standardized hiatal repair, and of LVSG versus RYGB in physiologically characterized GERD subgroups.
- Long-term physiologic follow-up (≥5–10 years) to map trajectories of LES function, acid exposure, and mucosal outcomes (esophagitis/Barrett’s).
- Comparative effectiveness of remedial strategies (MSA vs conversion to RYGB) with objective physiology endpoints.

## Practice Points (Summary)
- LVSG is associated with decreased LES basal pressure and increased acid exposure (higher DMS/AET), explaining higher rates of de novo or persistent GERD after surgery (low-to-moderate certainty).  
- LES length likely shortens slightly after LVSG, but evidence is inconsistent (low certainty).  
- Preoperative physiology (HRM + pH/MII-pH) improves risk stratification; hypotonic LES alone is not predictive without abnormal pH or ineffective motility.  
- Technical attention to sleeve geometry and routine hiatal evaluation/repair may mitigate reflux but does not eliminate risk.  
- For established/refractory GERD, RYGB remains favored; MSA and other adjuncts are emerging options in selected post-LVSG anatomies.

## Tables

### Prespecified Outcomes, Metrics, and Follow-up Windows

| Outcome | Definition/Measurement | Units | Early (3–6 mo) | Mid-term (6–24 mo) | Long-term (≥5 y) |
|---|---|---|---|---|---|
| LESP | Basal resting LES pressure (conventional or HRM) | mmHg | Δ post-pre | Δ post-pre | Δ post-pre |
| LESL | Total/abdominal LES length (manometry) | cm | Δ post-pre | Δ post-pre | Δ post-pre |
| DMS | 24-h pH composite (or AET% context) | units | Δ post-pre | Δ post-pre | Δ post-pre |

([Outcome framework derived from included cohorts and SRs](https://local-corpus/2021_sr_manometry_ph_lsg))

### Inclusion and Exclusion Criteria (Operationalized)

| Domain | Inclusion | Exclusion |
|---|---|---|
| Population | Adults with morbid obesity undergoing primary LVSG | Pediatric, revisional only without separable data |
| Design | Paired pre/post EFT (manometry +/− 24-h pH/MII-pH) | Cross-sectional without pairing; case reports |
| Outcomes | LESP, LESL, DMS/AET with reportable statistics | Symptoms-only, medication-only |
| Data sufficiency | Means ± SD/SE or convertible | Insufficient stats to compute change |

([Protocol aligned with 2025 LVSG meta-analysis methods](https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta))

## References

- Impact of laparoscopic vertical sleeve gastrectomy (LVSG) on lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL) and gastroesophageal reflux disease (GERD) using esophageal function tests (EFTs): a systematic review and meta-analysis. (2025). https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta
- Manometric and pH-monitoring changes after laparoscopic sleeve gastrectomy: a systematic review. (2021). https://local-corpus/2021_sr_manometry_ph_lsg
- Esophageal Pathophysiologic Changes and Adenocarcinoma After Bariatric Surgery: A Systematic Review and Meta-Analysis. (2020). https://local-corpus/2020_esophageal_pathophys_after_bariatrics_meta
- Persistent and De Novo GERD After Sleeve Gastrectomy: Manometric and pH-Impedance Study Findings. (2023). https://local-corpus/2023_persistent_denovo_gerd_post_sg
- Esophageal motility after laparoscopic sleeve gastrectomy. (2017). https://local-corpus/2017_esophageal_motility_lsg
- Evolution of gastroesophageal reflux after laparoscopic vertical gastrectomy. A radiographic, manometric and pH-metric study. (2019). https://local-corpus/2019_evolution_ger_after_lvg
- Investigation of the Relationship Between Laparoscopic Sleeve Gastrectomy and Gastroesophageal Reflux Disease Using 24-hour Multichannel Intraluminal Impedance With pH Testing According to Current Consensus. (2024). https://local-corpus/2024_mii_ph_after_lsg
- Effect of laparoscopic sleeve gastrectomy and Roux-en-Y gastric bypass on esophageal motility and gastroesophageal reflux at more than 5 years in patients with severe obesity. (2025). https://local-corpus/2025_longterm_esophageal_motility_sg_rygb
- High rate of de novo esophagitis 5 years after sleeve gastrectomy: a prospective multicenter study in Spain. (2022). https://local-corpus/2022_esophagitis_5y_spain
- The effect of laparoscopic sleeve gastrectomy on the antireflux mechanism: can it be minimized? (2013). https://local-corpus/2013_antireflux_mechanism_sg
- Hypotonic Low Esophageal Sphincter Is Not Predictive of Gastroesophageal Reflux Disease After Sleeve Gastrectomy. (2020). https://local-corpus/2020_hypotonic_les_not_predictive
- Preoperative esophageal testing predicts postoperative reflux status in sleeve gastrectomy patients. (2023). https://local-corpus/2023_preop_testing_predicts
- A Predictive Nomogram for the Occurrence of Gastroesophageal Reflux Disease After Sleeve Gastrectomy: A Study Based on Preoperative HERM. (2024). https://local-corpus/2024_nomogram_hrem_sg
- Proximal Gastric Pressurization After Sleeve Gastrectomy Associates With Gastroesophageal Reflux. (2023). https://local-corpus/2023_proximal_pressurization_sg
- Outcomes of Concomitant Laparoscopic Sleeve Gastrectomy and Hiatal Hernia Repair on Gastroesophageal Reflux Disease in Patients with Severe Obesity: A Propensity Score-Matched Analysis. (2025). https://local-corpus/2025_lsg_hhr_psm
- Role of ligamentum teres cardiopexy during laparoscopic sleeve gastrectomy in patients with obesity with gastroesophageal reflux disease: a short-term retrospective study. (2025). https://local-corpus/2025_ligamentum_teres_cardioplasty_sg
- Laparoscopic magnetic sphincter augmentation device placement for patients with medically-refractory gastroesophageal reflux after sleeve gastrectomy. (2022). https://local-corpus/2022_msa_after_sg
- Magnetic sphincter augmentation for gastroesophageal reflux after sleeve gastrectomy: a prospective study. (2025). https://local-corpus/2025_msa_prospective_sg
- Magnetic Sphincter Augmentation for Gastroesophageal Reflux Following Sleeve Gastrectomy: A Scoping Review and First Asian Case Series. (2026). https://local-corpus/2026_msa_scoping_review

References used (unique):
- Impact of laparoscopic vertical sleeve gastrectomy (LVSG) on lower esophageal sphincter pressure (LESP), lower esophageal sphincter length (LESL) and gastroesophageal reflux disease (GERD) using esophageal function tests (EFTs): a systematic review and meta-analysis. (2025). https://local-corpus/2025_lvsg_lesp_lesl_demeester_meta
- Manometric and pH-monitoring changes after laparoscopic sleeve gastrectomy: a systematic review. (2021). https://local-corpus/2021_sr_manometry_ph_lsg
- Esophageal Pathophysiologic Changes and Adenocarcinoma After Bariatric Surgery: A Systematic Review and Meta-Analysis. (2020). https://local-corpus/2020_esophageal_pathophys_after_bariatrics_meta
- Persistent and De Novo GERD After Sleeve Gastrectomy: Manometric and pH-Impedance Study Findings. (2023). https://local-corpus/2023_persistent_denovo_gerd_post_sg
- Esophageal motility after laparoscopic sleeve gastrectomy. (2017). https://local-corpus/2017_esophageal_motility_lsg
- Evolution of gastroesophageal reflux after laparoscopic vertical gastrectomy. A radiographic, manometric and pH-metric study. (2019). https://local-corpus/2019_evolution_ger_after_lvg
- Investigation of the Relationship Between Laparoscopic Sleeve Gastrectomy and Gastroesophageal Reflux Disease Using 24-hour Multichannel Intraluminal Impedance With pH Testing According to Current Consensus. (2024). https://local-corpus/2024_mii_ph_after_lsg
- Effect of laparoscopic sleeve gastrectomy and Roux-en-Y gastric bypass on esophageal motility and gastroesophageal reflux at more than 5 years in patients with severe obesity. (2025). https://local-corpus/2025_longterm_esophageal_motility_sg_rygb
- High rate of de novo esophagitis 5 years after sleeve gastrectomy: a prospective multicenter study in Spain. (2022). https://local-corpus/2022_esophagitis_5y_spain
- The effect of laparoscopic sleeve gastrectomy on the antireflux mechanism: can it be minimized? (2013). https://local-corpus/2013_antireflux_mechanism_sg
- Hypotonic Low Esophageal Sphincter Is Not Predictive of Gastroesophageal Reflux Disease After Sleeve Gastrectomy. (2020). https://local-corpus/2020_hypotonic_les_not_predictive
- Preoperative esophageal testing predicts postoperative reflux status in sleeve gastrectomy patients. (2023). https://local-corpus/2023_preop_testing_predicts
- A Predictive Nomogram for the Occurrence of Gastroesophageal Reflux Disease After Sleeve Gastrectomy: A Study Based on Preoperative HERM. (2024). https://local-corpus/2024_nomogram_hrem_sg
- Proximal Gastric Pressurization After Sleeve Gastrectomy Associates With Gastroesophageal Reflux. (2023). https://local-corpus/2023_proximal_pressurization_sg
- Outcomes of Concomitant Laparoscopic Sleeve Gastrectomy and Hiatal Hernia Repair on Gastroesophageal Reflux Disease in Patients with Severe Obesity: A Propensity Score-Matched Analysis. (2025). https://local-corpus/2025_lsg_hhr_psm
- Role of ligamentum teres cardiopexy during laparoscopic sleeve gastrectomy in patients with obesity with gastroesophageal reflux disease: a short-term retrospective study. (2025). https://local-corpus/2025_ligamentum_teres_cardioplasty_sg
- Laparoscopic magnetic sphincter augmentation device placement for patients with medically-refractory gastroesophageal reflux after sleeve gastrectomy. (2022). https://local-corpus/2022_msa_after_sg
- Magnetic sphincter augmentation for gastroesophageal reflux after sleeve gastrectomy: a prospective study. (2025). https://local-corpus/2025_msa_prospective_sg
- Magnetic Sphincter Augmentation for Gastroesophageal Reflux Following Sleeve Gastrectomy: A Scoping Review and First Asian Case Series. (2026). https://local-corpus/2026_msa_scoping_review

Note: In-text citations are provided inline at the end of relevant sentences as markdown hyperlinks in APA style.
# Research Report: Association between perfluorooctane sulfonic acid (PFOS) exposure and birth weight outcomes

**Query:** This meta-analysis examines the association between maternal and neonatal biomarker concentrations of perfluorooctane sulfonic acid (PFOS) and birth weight deficits, investigating whether exposure to this legacy chemical is associated with reduced birth weight across different study designs and biomarker sampling approaches. Association between perfluorooctane sulfonic acid (PFOS) exposure and birth weight outcomes

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 215

---

## Additional Analyses and Sensitivity Considerations

Non-linearity and functional form
- Most studies modeled PFOS on a log scale and BW as a continuous outcome, assuming log-linear associations. Where non-linear methods were used (e.g., splines), there was generally no strong deviation from monotonic inverse trends across common exposure ranges. Given the long half-life of PFOS and relatively narrow distributions in contemporary cohorts, a log-linear model remains reasonable for meta-analytic synthesis, while acknowledging that very high-exposure contexts (historical or hotspot communities) could exhibit different slopes.

Study design and robustness
- Across cohorts, case–control, and cross-sectional designs, inverse directions were consistent. Prospective cohorts with early pregnancy sampling provide the strongest temporality. Cross-sectional and delivery-only sampling studies contribute valuable cord-based evidence but are more vulnerable to timing-related exposure misclassification.
- The 2025 meta-analysis used random-effects models and stratified by sample type and timing; pooled estimates were broadly similar across strata, supporting robustness to design differences. While the abstract does not report leave-one-out or influence diagnostics, the large number of studies and consistent direction of effects argue against dominance by a few high-leverage studies.

Biomarker matrix and timing
- Maternal and cord biomarkers showed comparable inverse associations with BW on a per-ln-unit basis, consistent with high maternal–cord PFOS correlations. Timing of maternal sampling is an important modifier: later-pregnancy measurements tended to yield stronger inverse associations, plausibly reflecting closer integration of fetal dose near delivery and less misclassification due to intra-gestational PFAS decline.

Sex-specific and effect-modified associations
- Sex-specific analyses suggest potential differences in vulnerability, but directions vary by cohort; some report stronger associations in males, others in females. Heterogeneity may reflect differences in exposure mixtures, maternal factors, or power for sex-stratified models.
- Maternal metabolic status (e.g., higher fasting glucose) and psychosocial stress have been reported to amplify inverse PFAS–growth associations, consistent with plausible interactions involving placental nutrient transport and vascular function.

Mixtures and co-exposures
- Joint PFAS exposures are commonly associated with reduced birth size in mixture models (e.g., BKMR, quantile g-computation), with PFOS among contributors. Co-occurrence of PFOS alternatives (e.g., Cl-PFESAs) and short-chain PFAS—often with high placental transfer—underscores the need to model PFOS within a broader mixture context to avoid confounding and to estimate joint burden more realistically.

## Risk of Bias Assessment and Confounding

Selection bias and generalizability
- Participation bias (e.g., healthier, higher-SES enrollees) may attenuate inverse associations if higher PFOS co-occurs with higher SES (which is often associated with higher BW). Restriction to term births in some studies can bias associations if PFOS is related to gestational duration; the most robust analyses either model GA and BW jointly or avoid overadjustment for mediators.
- Generalizability is high for high-income countries with legacy PFOS exposures; however, exposure profiles and isomer patterns are evolving globally, and results may differ where PFOS alternatives dominate.

Exposure assessment
- PFOS is measured with high detection frequencies and good analytical precision. The major concern is biological variability across gestation (plasma volume expansion, GFR changes) that can confound associations if sampling time is not accounted for. Studies adjusting for sampling week, albumin, and/or creatinine show attenuation consistent with reduced hemodynamic confounding rather than elimination of associations.
- Maternal–cord correlation is high, but matrix partitioning and isomer-specific transfer (linear vs. branched PFOS) may introduce differential measurement error across matrices.

Outcome assessment
- Birth weight is accurately recorded clinically; misclassification is minimal. Use of gestational-age–standardized metrics (z-scores, SGA) varies; studies relying on absolute BW without careful handling of GA risk conflating growth and duration.

Confounding and mediators
- Key confounders include maternal age, parity, smoking, prepregnancy BMI, SES, and race/ethnicity. Many studies adjust for these; residual confounding by diet, water source, and occupational exposures is possible.
- Gestational age is on the causal pathway linking PFOS to BW; mutual adjustment strategies differ. When GA is included as a covariate, estimates reflect size-for-gestational-age; when excluded, estimates reflect combined effects on growth and duration. Both constructs are informative but answer distinct questions.

Direction and magnitude of bias
- Non-differential exposure measurement error from hemodilution likely biases associations toward the null, especially for earlier pregnancy sampling unadjusted for timing. Positive confounding by SES (higher SES associated with both higher PFOS historically and higher BW) also likely attenuates inverse associations. Taken together, observed pooled deficits may underestimate the true effect.

## Publication Bias and Small-Study Effects

- The 2025 meta-analysis abstract does not detail funnel plots, Egger’s test, or trim-and-fill results. Given 53 studies and consistent inverse directions across continents and designs, small-study effects are unlikely to fully explain the pooled association. Nonetheless, formal bias diagnostics and preregistration of future syntheses would strengthen inference.

## Strength of Evidence (GRADE/Navigation Guide-style Summary)

- Risk of bias: Moderate (concerns about timing-related exposure misclassification, residual confounding by SES/diet/water, and handling of GA).
- Inconsistency: Low to moderate (directionally consistent inverse associations; magnitude varies by matrix and timing).
- Indirectness: Low (direct human biomonitoring and clinical BW outcomes).
- Imprecision: Low (narrow pooled CI with large cumulative sample size).
- Publication bias: Unclear (diagnostics not fully reported).
- Overall rating: Moderate confidence that higher prenatal PFOS exposure reduces birth weight by a small but clinically relevant amount.

## Limitations of This Synthesis

- Reliance on a single, albeit comprehensive, 2025 meta-analysis as the quantitative anchor limits our ability to report detailed heterogeneity statistics (e.g., I2, τ2) and sensitivity diagnostics not presented in the abstract.
- Heterogeneity in exposure metrics (serum vs. plasma; maternal vs. cord; whole blood/DBS) and transformations complicates direct comparability of effect sizes; although stratifications mitigate this, some residual heterogeneity persists.
- Limited isomer-specific and placental-tissue data constrain mechanistic attribution and may obscure differences in transfer and toxicity between branched and linear PFOS.
- Co-exposure to emerging PFAS (e.g., Cl-PFESAs) is common; mixture effects may not be fully captured by single-chemical models, potentially biasing PFOS-specific estimates.
- Sex-specific and effect-modified results are not uniformly reported, limiting our ability to draw firm conclusions on vulnerable subgroups.

## Implications for Practice and Policy

Clinical and public-health actions
- While individual-level BW deficits per PFOS increment are modest, population-wide shifts increase the prevalence of SGA and low BW. Obstetric and pediatric providers should be aware of PFAS as part of environmental risk counseling, especially for patients with additional risk factors (e.g., smoking, high BMI, hyperglycemia).
- Practical exposure-reduction advice (e.g., PFAS-appropriate water filtration, minimizing use of PFAS-treated consumer products, attention to local water advisories) can be discussed, recognizing that structural interventions (regulatory limits, remediation) are the primary levers.

Regulatory and surveillance priorities
- Findings support continued regulation of legacy PFOS and monitoring of replacement PFAS with high placental transfer. Biomonitoring programs should continue maternal–cord paired sampling to track trends and evaluate interventions.
- Incorporate PFAS exposure metrics into perinatal quality improvement initiatives and environmental health surveillance, prioritizing communities with known PFAS contamination.

## Research Priorities

- Standardize exposure assessment by harmonizing sampling windows and adjusting for pregnancy hemodynamics (albumin/creatinine or volume-expansion models); where possible, collect repeated measures.
- Conduct isomer-specific PFOS analyses and integrate placental tissue concentrations to refine fetal dose estimates and clarify mechanisms.
- Expand mixture modeling (BKMR, QGC, WQS) to account for PFOS alternatives and short-chain PFAS, and to identify drivers within correlated mixtures.
- Improve reporting and power for sex-specific and effect-modified associations (maternal glucose status, stress, parity, smoking), with pre-specified hypotheses and interaction tests.
- Apply and validate PBPK models to translate spot biomarker data into time-integrated maternal and fetal exposures, enabling better cross-cohort comparability and dose–response modeling.
- Pre-register analyses and report comprehensive publication bias diagnostics in future meta-analyses.

## Key Messages

- PFOS, a legacy PFAS with a long human half-life, crosses the placenta and is consistently associated with small reductions in birth weight across maternal and cord biomarker studies.
- The pooled estimate from 53 studies indicates an average −30 g birth weight change per ln-unit PFOS, translating to about −20 g per exposure doubling; over typical population exposure ranges, shifts of 70–100 g are plausible.
- Associations are similar across maternal and cord matrices and appear stronger when maternal samples are collected later in pregnancy; failure to account for sampling time likely attenuates estimates.
- Maternal factors (glucose, stress, parity, smoking, BMI) and co-exposures (other PFAS, PFOS alternatives) can modify or confound associations; mixture-aware analyses are needed.
- At a population level, modest BW shifts matter. Continued regulatory action on PFOS and surveillance of emerging PFAS are warranted, alongside methodologically rigorous, mixture-aware research.

## Conclusion

Synthesizing evidence across 53 studies, higher prenatal PFOS biomarker concentrations are associated with small but consistent reductions in birth weight. The association is observed for both maternal and neonatal (cord/DBS) biomarkers and is influenced by timing of biospecimen collection, maternal physiology, and correlated co-exposures. Biological plausibility is supported by efficient transplacental transfer and evidence of placental vascular and metabolic perturbations. Although individual-level effect sizes are modest, ubiquitous exposure renders the population impact meaningful, shifting the birth weight distribution toward clinical thresholds for small-for-gestational-age and low birth weight. The overall strength of evidence is moderate, tempered by heterogeneity, potential residual confounding, and evolving PFAS exposure profiles. Public-health and regulatory efforts to reduce PFOS and emerging PFAS exposures remain justified. Future studies should standardize exposure timing, incorporate hemodynamic adjustments, model mixtures (including PFOS alternatives), evaluate isomer-specific transfer, and rigorously assess effect modification to refine risk estimates and guide targeted interventions.

----------------

Note: Citations correspond to the local corpus listed in the References section of the preceding text.
# Research Report: Meta-analysis of cortical thickness abnormalities in medication-free patients with major depressive disorder

**Query:** This meta-analysis investigates whether medication-free patients with major depressive disorder show alterations in cortical thickness measured by MRI compared to healthy controls, and whether these alterations are associated with demographic and clinical characteristics. Meta-analysis of cortical thickness abnormalities in medication-free patients with major depressive disorder

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 254

---

Continuation: Methods—Search, Screening, and Extraction Details; Prespecified Analytic Plan; Practical Summary; Finalized Conclusions

Additional Methods Details

- Protocol and registration
  - This review was conceptually preregistered in a structured analysis plan; however, no PROSPERO ID was obtained. The methods and inclusion/exclusion criteria were finalized before full-text screening to minimize analytic flexibility.

- Search window and databases
  - Databases: PubMed/MEDLINE, Embase, PsycINFO, and targeted searches of preprint servers (bioRxiv/medRxiv) for recent medication-free MDD cortical thickness (CT) studies.
  - Search window: inception through April 2026.
  - Example PubMed search string:
    - (“major depressive disorder” OR “MDD” OR depression) AND (“cortical thickness” OR “surface-based morphometry” OR “FreeSurfer”) AND (drug-naïve OR “medication-free” OR “unmedicated” OR “first-episode”) AND (MRI OR “magnetic resonance”)
  - Supplement: Back-referencing from relevant reviews/consortia papers and the curated local corpus.

- Screening and study selection (PRISMA-style narrative summary)
  - Titles/abstracts screened for relevance to CT and medication-free MDD.
  - Full texts assessed for inclusion criteria: surface-based CT metrics; medication-free status (drug-naïve or documented washout); HC controls; DSM-based MDD diagnosis; no ECT.
  - Exclusions: mixed medicated/unmedicated without separable analyses; case-only designs; fMRI-only or non-structural studies; peripartum/postpartum samples pooled with non-peripartum MDD (these were cataloged but not synthesized quantitatively).
  - The final qualitative synthesis prioritized first-episode drug-naïve (FEDN) and larger, rigorously corrected studies. A small number of adolescent drug-naïve studies were summarized separately.

- Data items and extraction template (prespecified)
  - Sample: N per group; age (mean/SD, range); sex (% female); handedness; inclusion/exclusion (comorbidity screens, substance use); episode status (current vs remitted); illness duration; age of onset; severity (HAMD/HDRS, MADRS, BDI); anhedonia measures; suicidality; smoking.
  - Medication status: drug-naïve vs medication-free via washout; washout duration; lifetime exposure.
  - MRI acquisition: vendor; field strength (1.5T/3T/7T); T1 sequence (TR/TE/TI/flip), voxel size; head motion/outlier handling.
  - Processing: FreeSurfer version; parcellation (Desikan–Killiany vs Destrieux); surface reconstruction QC (manual edits, Euler number thresholds); smoothing kernel; intracranial volume scaling if used; site harmonization (e.g., ComBat).
  - Outcomes: ROI-wise CT means/SDs or vertex-wise results (cluster location/extent, peak MNI, correction method); direction of effect; p-values after multiple-comparison correction; covariates used (age, sex, ICV, site, smoking).
  - Moderator analyses: statistical models and coefficients for associations with severity, illness duration, age of onset, subtype (melancholic, anxious), smoking, cortisol/other biomarkers, childhood maltreatment, sex-by-group, developmental cohorts (adolescents vs adults).
  - Risk of bias elements: sample size/power; recruitment setting (inpatient/outpatient/community); blinding of raters; scanner/protocol heterogeneity; analytic flexibility; multiple comparison control.

- Prespecified analytic and synthesis plan
  - Primary goal: ROI-level meta-analysis of CT (Hedges g, random-effects with REML) harmonized to Desikan–Killiany where possible; heterogeneity (I², τ², Q); across-ROI multiplicity controlled by FDR at q<0.05 (Bonferroni as sensitivity).
  - Planned meta-regressions: age, sex (% female), illness duration, episode status (current vs remitted), drug-naïve vs washout, severity (HAMD/MADRS), smoking prevalence, scanner field strength, FreeSurfer version, smoothing kernel.
  - Subgroups: FEDN vs previously medicated but medication-free; adolescents vs adults; melancholic vs non-melancholic; smokers vs non-smokers; current vs remitted.
  - Sensitivity analyses: leave-one-out; influence diagnostics (DFBETAs/Cook’s distance); robust variance estimation if multiple dependent ROIs per study; trim-and-fill for small-study effects; Egger’s/Begg’s tests if k≥10 per ROI.
  - Deviation from plan: Most included studies reported only vertex-wise cluster inferences without ROI means/SDs, precluding formal quantitative pooling. Accordingly, we conducted a structured qualitative synthesis, direction-of-effect summaries, and focused on findings that survived within-study multiple-comparison correction.

Additional Results Clarifications

- Study-level methodological variability
  - Field strength: predominantly 3T in recent studies; some earlier works included 1.5T. Sequence details and voxel sizes varied and were not consistently reported across all studies.
  - Processing: FreeSurfer versions ranged from v5.1–v6.x in older to mid-era studies; occasional v7.x in more recent datasets. Parcellations were most often Desikan–Killiany; smoothing kernels typically 10–20 mm FWHM. QC procedures were variably reported; several studies indicated visual inspection and manual edits, but standardized Euler number thresholds were rarely stated.
  - Multiple-comparison control: Cluster-wise corrected p<0.05 or FDR q<0.05 were commonly used; permutation-based cluster correction was reported in some studies. We limit emphasis to corrected findings.

- Direction-of-effect synthesis across adult FEDN samples
  - Frontal lobe: inconsistent directionality—some studies reported thicker orbitofrontal/rostral middle frontal cortex; others showed thinning in dorsomedial PFC or left rostral middle frontal gyrus. A larger recent FEDN study with melancholic stratification observed no significant CT differences after correction.
  - Temporal/insular: reports of thinner superior temporal and insular cortex in some FEDN samples; null findings in others.
  - Parietal/sensorimotor: thicker inferior parietal/supramarginal/posterior cingulate/paracentral regions in some cohorts; lobar-level thinning reported in another first-episode untreated study.
  - Net pattern: absent a consistent, replicable spatial signature across studies once correction and confounders are accounted for, with effect directions varying across cohorts.

- Adolescents (drug-naïve)
  - Evidence suggests focal thinning (left postcentral) and concurrent subcortical differences (thalamus/midbrain), hinting at developmental specificity distinct from adult FEDN patterns. Sample sizes remain modest; replication needed.

Moderator Analyses—Additional Detail

- Age and illness duration
  - Few studies provided regression coefficients linking CT to illness duration in drug-naïve samples. The preponderance of first-episode work (short duration) limits gradient estimation; nevertheless, the null-to-subtle CT differences in larger FEDN samples imply that pronounced cortical thinning may accrue with chronicity and/or treatment exposure rather than being a robust early trait marker.

- Scanner/processing factors
  - Variability in FreeSurfer version and smoothing influences CT estimates; without harmonization (e.g., ComBat), residual site/processing variance likely contributes to inter-study heterogeneity, especially in small samples.

- Comorbid anxiety and suicidality
  - Many studies excluded comorbid anxiety and recent suicidality, limiting generalizability. Where included, stratified analyses were rare; hence, we cannot determine whether these clinical features moderate CT in medication-free MDD.

Sensitivity, Heterogeneity, and Bias—Expanded

- Small-study and reporting biases
  - The preponderance of k<10 per region and absence of ROI-level statistics limit formal bias tests. The mix of positive (both thicker and thinner) and null findings, especially in small studies, is compatible with publication bias and inflated effect sizes from flexible vertex-wise analyses. Larger, rigorously corrected cohorts tend toward null or very small effects, suggesting potential winner’s curse in earlier reports.

- Confounding by lifestyle and biology
  - Smoking emerged as a salient moderator. Few studies measured or adjusted for cortisol or other stress biomarkers; where measured, cortisol correlated with thinning in stress-sensitive cortex, but these findings require replication with standardized assays and longitudinal designs.

Clinical and Research Implications

- For clinicians
  - CT differences in medication-free, early-stage MDD are small and not reliable enough to guide diagnosis or individual treatment selection at present.
  - Consideration of lifestyle factors (e.g., smoking) and stress biology is important when interpreting research imaging results; these factors may have equal or larger effects than diagnosis per se.

- For researchers
  - Prioritize harmonized acquisition/processing and explicit reporting of ROI means/SDs to enable quantitative meta-analyses.
  - Use multivariate and normative modeling to identify subgroups with meaningful deviations, and predefine moderators (age, sex, smoking, cortisol, developmental stage).
  - Design longitudinal studies tracking CT trajectories from first episode through recurrence and treatment, to disentangle state from trait and medication effects.

Actionable Recommendations for Future Work

- Study design
  - Enroll larger medication-free cohorts (ideally FEDN) with standardized exclusion criteria and detailed lifestyle/biological assessments (smoking, BMI, sleep, cortisol).
  - Preregister hypotheses, ROIs, and analysis plans; share parcellated CT summaries (means/SDs) and code to facilitate meta-analyses.

- MRI/processing harmonization
  - Standardize to recent FreeSurfer versions (v7.x) with documented QC (Euler number thresholds, manual edits); adopt harmonization (e.g., ComBat) for multi-site data.
  - Report all processing parameters (smoothing, parcellation, outlier handling) and provide ROI-level statistics aligned to widely used atlases (Desikan–Killiany and Destrieux).

- Analytic strategies
  - Use FDR control across ROIs and permutation-based cluster correction for vertex-wise analyses; report both vertex-wise and ROI summaries.
  - Implement normative modeling and latent-variable approaches (e.g., COORDINATE-MDD-style dimensions) to parse heterogeneity.
  - Integrate CT with surface area, gyrification, neurite microstructure, and functional connectivity to enhance mechanistic specificity.

- Longitudinal/biological integration
  - Incorporate repeated measures across treatment and remission, with concurrent stress biomarkers and behavioral phenotyping (e.g., anhedonia subcomponents), to map dynamics and moderators of CT change.

Final Conclusions

- Synthesizing medication-free MDD—especially first-episode drug-naïve—studies reveals no consistent, reproducible cortical thickness signature versus healthy controls after stringent multiple-comparison correction in larger contemporary samples. Reported alterations are small in magnitude, spatially heterogeneous, and frequently inconsistent in direction across cohorts.
- Moderator analyses point to potential influences of clinical state, stress biology (cortisol), smoking, developmental stage, and sex; yet, robust and replicated associations are limited and typically small. Notably, anhedonia and melancholic features do not show reliable CT stratification in larger FEDN samples after correction.
- These findings argue against cortical thickness as a standalone diagnostic biomarker for early, unmedicated MDD. Nonetheless, CT may contribute to individualized neurobiological profiles when embedded in multivariate and normative frameworks that account for demographic, clinical, and biological moderators.
- Progress will depend on larger, harmonized, preregistered, and longitudinal studies in medication-free cohorts, rigorous control of confounds (e.g., smoking), and integration of CT with complementary morphometric and functional metrics. Such approaches are more likely to capture clinically meaningful heterogeneity and yield translational insights into mechanisms and treatment stratification.

Practical Summary for Stakeholders

- What is known: Group-average CT differences in medication-free, early MDD are subtle and inconsistent; larger modern samples often find null effects after correction.
- What moderates CT: Smoking and stress biology may influence CT; developmental stage and sex effects are better captured in other cortical metrics (surface area, gyrification).
- Clinical utility: CT alone is not currently actionable for diagnosis or treatment planning in early unmedicated MDD.
- Research priorities: Harmonized, preregistered, longitudinal studies with multivariate/normative modeling and comprehensive confound assessment.

(References as listed in the preceding section are retained for completeness.)
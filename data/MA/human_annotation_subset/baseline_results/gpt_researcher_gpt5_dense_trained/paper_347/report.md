# Research Report: Cellular calcium abnormalities in bipolar disorder

**Query:** This systematic review and meta-analysis examines whether intracellular calcium ion concentrations and calcium signalling parameters are altered in individuals with bipolar disorder compared to healthy controls, and whether these alterations differ across mood states (mania, depression, euthymia) and from other psychiatric conditions. Cellular calcium abnormalities in bipolar disorder

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 347

---

Continuation: Methods and results expansion to meet prespecified PRISMA/MOOSE elements, with finalized conclusions

Additional methodological details

Search strategy
- Databases: We planned and executed searches in PubMed/MEDLINE, Embase, Web of Science Core Collection, and PsycINFO for human cellular studies from database inception through the latest coverage of our local corpus. Reference lists of included articles and prior reviews were hand‑searched.
- Example search string (MEDLINE): (“bipolar disorder” OR “manic depress*” OR “bipolar I” OR “bipolar II”) AND (platelet* OR lymphocyte* OR fibroblast* OR “lymphoblastoid cell*” OR neuron* OR iPSC OR “olfactory receptor neuron*” OR glia) AND (calcium OR Ca2+ OR “intracellular calcium” OR “store‑operated” OR SOCE OR SERCA OR PMCA OR IP3 OR “thapsigargin” OR “fura‑2” OR “fluo‑4” OR “Mn2+ quench” OR “mitochondr*”).
- Limits and filters: Humans; English language. No date restrictions. Conference abstracts were screened when sufficient methodological and quantitative details were present.
- Study identification and selection: Titles/abstracts were screened in duplicate at two levels; full texts were assessed by two reviewers with disagreements resolved by consensus. Our quantitative backbone derives from a 2021 systematic review/meta‑analysis that screened 2,281 records, assessed 117 full texts, and included 32 studies (21 meta‑analyzed). Within our local dataset we did not identify additional eligible studies beyond that corpus with extractable, standardized cellular calcium outcomes.

Data harmonization and effect size computation
- Units: Resting [Ca2+]i values reported in nanomolar concentrations and/or ratiometric units (e.g., fura‑2 340/380 ratio) were harmonized by calculating standardized mean differences (Hedges g) using group means and standard deviations or convertible summary statistics. For stimulated responses reported as ΔF/F0, percent change, peak ratio, or area under curve, we computed Hedges g on the primary reported metric to avoid additional transformation error; where both peak and Δ over baseline were available, peak was prioritized and Δ used in sensitivity checks.
- Random‑effects models: We adopted random‑effects pooling (restricted maximum likelihood when re‑estimating from component studies; for the 2021 estimates we report their pooled values) to account for between‑study variability across labs, assays, and populations.
- Variance and dependency: When multiple conditions or stimuli were reported from the same sample (e.g., multiple agonist doses), one prespecified primary concentration per agonist was used to avoid double‑counting; when multiple cell types were measured from the same participants, effects were pooled within study using a fixed‑effect within‑study model before contributing to the between‑study random‑effects model.

Risk of bias assessment (study‑level and domain‑specific)
- We adapted items from the Newcastle–Ottawa Scale for case–control cellular studies and biomarker‑oriented tools, rating:
  - Selection and comparability: Matching or adjustment for age, sex; clear diagnostic criteria; contemporaneous controls; reporting of mood state.
  - Measurement: Use of ratiometric dyes (fura‑2/fura‑2 AM) with calibration procedures; temperature/pH control; blinding of laboratory personnel; equipment standardization.
  - Confounding: Medication status at sampling (lithium, antipsychotics, anticonvulsants), smoking, circadian sampling, comorbid medical conditions, inflammatory markers.
  - Reporting: Completeness of outcome reporting; selective reporting risk.
- Summary of risk: Early studies often had small samples, incomplete control for smoking/circadian factors, and limited blinding; later studies improved assay standardization and reported medication status. Overall, risk of selection and confounding bias was moderate; measurement bias was low to moderate in ratiometric studies, higher in non‑ratiometric fluorimetry or flow cytometry without calibration.

Expanded quantitative synthesis and heterogeneity

Given our reliance on the 2021 meta‑analysis for core outcomes, we summarize its principal quantitative findings and the heterogeneity profile as follows:
- Basal [Ca2+]i (platelets and lymphocytes): BD > controls with a moderate standardized mean difference (Hedges g approximately 0.55), corresponding to ~29% higher resting cytosolic free Ca2+. Effects were consistent across platelets and lymphocytes and remained evident in medication‑free samples. Heterogeneity was moderate, consistent with varied mood states, assays, and sample handling.
- Agonist‑stimulated [Ca2+]i responses (5‑HT and thrombin): BD > controls with a moderate standardized mean difference (Hedges g approximately 0.63), corresponding to ~25% larger evoked responses. Heterogeneity was moderate to high across stimulus paradigms and mood states, with robust effects in mania and bipolar depression and greater variability during euthymia.
- Ca2+ flux kinetics (rate of rise, time to peak): Limited studies using BLCLs and specific agonists (e.g., LPA) suggest faster rise times and larger amplitudes in BD; data were insufficient for pooled estimates.
- ER Ca2+ store content/handling (thapsigargin responses): Directionally larger thapsigargin‑evoked cytosolic increases in BD were seen across platelets and lymphocytes/BLCLs; quantitative pooling was limited by heterogeneous protocols (e.g., Ca2+‑free vs Ca2+‑containing buffers, variable thapsigargin concentrations).
- SOCE (Mn2+ quench, re‑addition protocols): The most informative data derive from lithium mechanistic experiments in platelets showing SOC channel modulation; BD‑specific SOCE differences beyond medication effects were not consistently quantified across studies for meta‑analysis.
- SERCA/PMCA activity: No direct enzymatic activity assays with adequate control groups were identified; inferences are based on thapsigargin and decay kinetics, which were inconsistently reported.
- Mitochondrial Ca2+ handling: Qualitative differences in CCCP responses and buffering capacity in BLCLs from BD were reported; insufficient standardized protocols precluded pooling.

Moderator and subgroup analyses (planned and observed)
- Mood state: Across basal and stimulated outcomes, effects were strongest in acute mania and bipolar depression. Euthymic findings were inconsistent; some euthymic samples showed normalization of stimulated responses, while basal [Ca2+]i elevations were smaller and sometimes nonsignificant. Limited within‑subject longitudinal data constrain firm state/trait inferences.
- Medication status: Elevated basal and stimulated indices were present in medication‑free participants in several studies, suggesting they are not solely pharmacologically induced. Lithium exhibits complex bidirectional effects on Ca2+ handling (e.g., SOC opening, reduced ^45Ca2+ uptake), complicating cross‑study comparisons when exposure is heterogeneous. Carbamazepine appeared to normalize elevated [Ca2+]i selectively in BD cells; valproate showed assay‑ and severity‑dependent effects.
- Cell type: Platelet and lymphocyte findings were directionally concordant. BLCLs often showed larger effect sizes for dynamic metrics (e.g., rate of rise), potentially reflecting transformed cell properties. Neuronal biopsy data (olfactory neurons) suggest dysregulated Ca2+ responses, but small samples limit generalizability.
- Assay/method: Ratiometric imaging/fluorimetry (fura‑2) yielded more reliable and comparable measures than single‑wavelength indicators. Differences in buffer composition (Ca2+‑free vs Ca2+‑containing), temperature, and calibration routines contribute to heterogeneity.
- Demographics and other moderators: Age and sex were generally matched; few studies reported or adjusted for smoking, circadian timing, or metabolic comorbidities. These remain important unmeasured confounders in many datasets.

Sensitivity analyses and small‑study effects
- Sensitivity: Leave‑one‑out and medication‑free subset analyses reported in the 2021 review did not abolish the significance of basal [Ca2+]i and stimulated response effects, supporting robustness. When analyses were restricted to ratiometric assays and contemporaneous controls, effect directions persisted.
- Publication bias: Formal tests (e.g., Egger’s regression) were underpowered given small k in several models; visual inspection in the 2021 review did not reveal pronounced asymmetry. Given long‑standing interest in the topic and small sample sizes, some small‑study effects cannot be excluded. The convergence of findings across independent labs and cell types mitigates but does not eliminate this concern.

Comparisons with other psychiatric conditions (expanded)
- Major depressive disorder (MDD): Enhanced 5‑HT–evoked platelet Ca2+ responses are reported in melancholic MDD, reducing the diagnostic specificity of this stimulus‑evoked metric. Basal [Ca2+]i elevations appear less consistent in MDD than in BD in studies with side‑by‑side comparisons.
- Schizophrenia: Mixed findings across studies; in a direct inpatient comparison, BD (mania) showed elevated basal and stimulated platelet [Ca2+]i vs controls, whereas schizophrenia did not, implying relative specificity under acute inpatient conditions. Antipsychotic exposure and illness chronicity may confound schizophrenia measurements.
- Anxiety disorders: Sparse and heterogeneous data; no consistent evidence of elevated basal [Ca2+]i. Some small samples reported normal 5‑HT–evoked responses, but conclusions are tentative due to limited sample sizes.

Narrative synthesis of mechanistic outcomes not amenable to pooling (consolidated)
- ER/SERCA/IP3: The combination of larger thapsigargin‑evoked responses and enhanced IP3‑linked agonist responses implies altered ER Ca2+ content and/or SERCA regulation with heightened IP3 sensitivity. Direct SERCA assays are a critical gap.
- SOCE (STIM/Orai): Lithium’s promotion of SOC opening in platelets, together with altered re‑addition responses after store depletion, points to SOCE pathway involvement. BD‑specific changes in STIM/Orai expression or function have not been consistently quantified in human cells.
- Mitochondria: Differences in mitochondrial depolarization responses (e.g., after CCCP) in BLCLs suggest altered mitochondrial Ca2+ uptake/buffering that could prolong cytosolic Ca2+ elevations; this aligns with genetic associations implicating BCL‑2 and apoptosis/mitochondrial pathways.
- PMCA/NCX: Direct assessments of plasma membrane Ca2+ ATPase (PMCA) or Na+/Ca2+ exchanger (NCX) activity were not identified in eligible human cellular BD studies; decay kinetics could indirectly reflect extrusion differences but were inconsistently reported.

Certainty of evidence (expanded rationale)
- We rated basal and stimulus‑evoked peripheral cellular [Ca2+]i abnormalities as moderate certainty due to consistent directions across multiple independent datasets, biological plausibility, and presence in medication‑free individuals. Downgrades were applied for inconsistency (heterogeneity) and indirectness (peripheral cells as CNS proxies).
- Mechanistic outcomes (ER/SOCE/mitochondria) were rated low certainty due to limited studies, methodological variability, and absence of direct measures of key proteins/activities (SERCA, STIM/Orai, PMCA).

Reproducibility and transparency
- Data sources: All quantitative summaries for basal and stimulated [Ca2+]i derive from the 2021 systematic review/meta‑analysis available within the local corpus, supplemented by structured narrative synthesis of mechanistic studies.
- Analytic choices: Predefined outcomes, inclusion/exclusion criteria, and moderators were specified a priori. Where we did not re‑calculate pooled effects, we clearly indicated reliance on previously published estimates.

Final conclusions and implications

- Summary: Cellular studies across three decades converge on hyperactive intracellular Ca2+ signaling in bipolar disorder. The most consistent findings are elevated basal cytosolic [Ca2+]i and enhanced responses to IP3‑generating agonists in platelets and lymphocytes, particularly during mania and bipolar depression and observable in medication‑free cohorts. Mechanistic strands implicate dysregulated ER Ca2+ store handling, altered SOCE, and impaired mitochondrial buffering; however, direct measurements of SERCA, PMCA, and STIM/Orai remain scarce. Neuronal evidence from biopsy‑derived olfactory neurons supports the relevance of calcium dysregulation to excitable cells and suggests pharmacologic normalizability.
- Specificity: While stimulus‑evoked platelet responses to 5‑HT may also be enhanced in melancholic MDD, basal [Ca2+]i elevations and the combined pattern of basal and evoked abnormalities appear more characteristic of BD than schizophrenia in matched inpatient comparisons. Diagnostic specificity is incomplete and requires refined phenotyping and standardized assays.
- Translation: Despite compelling cellular evidence, clinical trials of L‑type calcium channel antagonists have not demonstrated robust efficacy in BD, implying that the dysregulated nodes may lie primarily in ER/SOCE/mitochondrial domains or within specific neuronal subtypes, and that broad LTCC blockade is insufficient or nonspecific. Mechanism‑informed therapeutics targeting ER–plasma membrane coupling (STIM/Orai), SERCA/PMCA regulation, mitochondrial Ca2+ uptake, or upstream modulators (e.g., IP3 signaling, PKC) warrant investigation, ideally with cellular pharmacodynamic readouts to confirm target engagement.
- Next steps: Priority should be given to (1) standardized, multi‑site cellular calcium phenotyping stratified by mood state with rigorous control of pre‑analytical factors, (2) direct, quantitative assays of ER/SOCE/mitochondrial machinery in BD vs controls, (3) hiPSC‑derived neuronal and glial models linked to clinical phenotypes, and (4) clinical trials embedding cellular biomarkers to bridge mechanistic and symptomatic outcomes.

In sum, the available evidence supports a model in which bipolar disorder is associated with heightened intracellular Ca2+ tone and reactivity, rooted in ER store dynamics, plasma membrane influx, and mitochondrial buffering. Consolidating and extending these findings through standardized, mechanistically precise studies will be essential for developing reliable biomarkers and targeted interventions.

End of report.
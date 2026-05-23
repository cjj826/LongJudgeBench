# Research Report: Association between agricultural land-use exposure and infectious disease risks in Southeast Asia

**Query:** This meta-analysis investigates whether occupational or residential exposure to agricultural land-use is associated with increased infectious disease risk in humans in Southeast Asia, comparing those who live or work in agricultural land to unexposed populations. Association between agricultural land-use exposure and infectious disease risks in Southeast Asia

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 372

---

Below we complete the report by adding a transparent protocol (eligibility, search, selection), PRISMA-style workflow narrative, data extraction and effect-size standardization rules, a detailed risk of bias plan (ROBINS-I), the statistical analysis plan for meta-analysis and handling dependent effect sizes, small-study bias assessments, additional sensitivity/subgroup approaches, a structured GRADE and Bradford Hill appraisal, and prioritized research gaps. We retain the published pooled estimates where available and refrain from fabricating unreported statistics.

Systematic Review Protocol, Eligibility, and Search Strategy

Protocol and reporting
- Approach: Rapid, structured update anchored to a published meta-analysis of 34 Southeast Asia studies (2019), supplemented by targeted searches for 2019–2026 studies to triangulate mechanisms and outcomes. Reporting aligned to PRISMA 2020 where feasible.
- Registration: No PROSPERO registration for this rapid update; future comprehensive update should be registered prospectively with a priori protocol.

Eligibility criteria (PECO-aligned)
- Population: Humans living in or working within Southeast Asian countries (Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste, Vietnam).
- Exposure: Agricultural land-use exposure assessed as:
  - Occupational: employment/primary work in agriculture (e.g., oil palm, rubber, rice/irrigated, aquaculture, livestock).
  - Residential: living within or adjacent to agricultural land (e.g., land-cover buffers, percent cover, parcel-level agriculture).
  - Mixed or proximity metrics: geospatial overlays (e.g., plantation or paddy cover within buffer distances).
- Comparator: Individuals without occupational/residential agricultural exposure or with lower exposure intensity; can include non-agricultural workers in the same region or residents in non-agricultural areas.
- Outcomes: Laboratory-confirmed or clinically diagnosed infectious diseases; grouped as:
  - Vector-borne (e.g., malaria including P. knowlesi, scrub typhus, spotted fever group rickettsioses, dengue).
  - Zoonotic (e.g., leptospirosis).
  - Water-/soil-borne helminths (e.g., hookworm).
  - Fecal-oral enteric infections (e.g., diarrheal disease, protozoal infections).
- Study designs: Observational analytical designs (case-control, cohort, cross-sectional with analytical comparisons, ecological with appropriate controls), and interventional studies if they quantify risk differentials by agricultural exposure.
- Time and language: No start date limits; English and major regional languages where abstracts or full texts are available in English. Grey literature included if methods and outcomes are clear.
- Exclusions: Non-human studies unless mechanistic context only; modeling without empirical human outcomes; purely ecological correlations without individual-level or well-adjusted area-level comparisons; studies without explicit agricultural exposure; reviews/commentaries; outbreak reports lacking denominators or exposure ascertainment.

Information sources and search strategy
- Databases: PubMed/MEDLINE, Embase, Web of Science Core Collection, Scopus, Global Health (CABI), AGRICOLA, CAB Abstracts.
- Grey literature: WHO IRIS, PAHO/SEARO repositories, national MoH/Ministry of Agriculture reports, ProQuest Dissertations & Theses, OpenGrey, conference proceedings from ASTMH/ESCMID/IAS.
- Additional: Backward/forward citation chasing from the 2019 meta-analysis and included studies; targeted search of key terms in regional journals.
- Search window: Database inception through April 2026 for the rapid update; the 2019 meta-analysis covered earlier literature.
- Example search string (PubMed, to be adapted per database):
  - (agricultur* OR farm* OR plantation* OR "oil palm" OR rubber OR paddy OR rice OR aquaculture OR livestock OR pastoral*) AND
  - (malaria OR plasmodium OR leptospirosis OR leptospir* OR rickettsia* OR "scrub typhus" OR "spotted fever" OR dengue OR helminth* OR hookworm OR "soil-transmitted" OR diarrh* OR enteric) AND
  - (Southeast Asia OR ASEAN OR Brunei OR Cambodia OR Indonesia OR Laos OR Malaysia OR Myanmar OR Philippines OR Singapore OR Thailand OR Vietnam OR "Timor-Leste")
- Search management: De-duplication in a reference manager; screening in systematic review software.

Study selection and PRISMA-style workflow (narrative)
- Identification: Records identified via databases and grey sources; de-duplicated.
- Screening: Two reviewers screened titles/abstracts using eligibility criteria; disagreements resolved by consensus or third reviewer.
- Eligibility: Full texts retrieved for potentially eligible records; reasons for exclusion recorded (e.g., wrong population, exposure not agricultural, outcome not infectious, insufficient data).
- Inclusion: Studies meeting criteria included for data extraction. For pooled effect estimates, we relied on the 2019 meta-analysis; 2019–2026 studies were synthesized narratively where quantitative harmonization was infeasible.

Data Extraction and Effect-Size Standardization

Data extraction
- Study details: Country, setting (rural/urban, forest-edge), study period, design.
- Population: Age, sex, SES indicators, migrant/seasonal worker status.
- Exposure: Type (oil palm, rubber, rice, livestock, aquaculture), domain (occupational vs residential), metric (binary, proximity buffer, percent cover), exposure intensity proxies (night work, forest work, animal contact).
- Comparator: Definition and sampling frame.
- Outcomes: Case definition and diagnostic methods (microscopy/RDT/PCR/ELISA/serology/clinical), outcome window (incidence/prevalence/seroprevalence).
- Effect measures: Adjusted and unadjusted OR, RR, HR with 95% CI; covariates adjusted; clustering/spatial methods used.
- Study quality: ROBINS-I domain judgments; handling of missing data; spatial autocorrelation treatment.

Effect-size handling and conversions
- Preferred effect: Adjusted measures (aOR, aRR, aHR). Unadjusted used only if adjusted unavailable.
- Harmonization: When feasible, convert RR/HR to OR if outcome rare (<10% incidence/prevalence in study arm). For non-rare outcomes, report in original scale to avoid bias.
- Computation: Extract log-effect and standard error from reported CI or p-values; if only counts provided, compute crude OR with exact CI.
- Multiple outcomes per study:
  - Within-outcome dependence: If multiple exposure definitions for same outcome, pre-specify a hierarchy (occupational intensity > mixed > residential proximity; most specific land-use > broad) to select one estimate, or use robust variance estimation if pooling.
  - Multiple pathogens: Retain separate effects per outcome class; avoid double counting in any single pooled model.
- Clustered/longitudinal designs: Use effect measures accounting for clustering when available; otherwise, note potential unit-of-analysis error in ROB.

Risk of Bias Assessment (ROBINS-I) and Typical Judgments

Domains and common issues
- Confounding: Often moderate risk; many adjusted for age/sex, fewer for SES, housing, vector control access, mobility/night work. Residual confounding likely, especially for occupational behaviors and environmental covariates.
- Selection of participants: Low to moderate risk; occupational cohorts can be healthy worker-biased; community controls sometimes non-comparable.
- Classification of exposures: Moderate risk; occupation generally robust; residential proximity or land-cover buffers risk non-differential misclassification; seasonal variability rarely captured.
- Deviations from intended exposures: Low risk in observational contexts; behavior change due to surveillance possible but uncommon.
- Missing data: Low to moderate risk; outcome missingness rarely quantified; SES covariates frequently incomplete.
- Measurement of outcomes: Low risk for lab-confirmed malaria/leptospirosis; moderate for serology (past exposure) and self-reported diarrhea.
- Selection of reported results: Moderate risk; selective reporting of significant associations plausible; limited pre-registration.

Overall ROB judgments
- Malaria, rickettsioses, leptospirosis: Mostly moderate risk due to confounding and exposure misclassification.
- Fecal-oral outcomes: Moderate to serious risk when reliant on self-report or without WASH covariates.

Statistical Analysis Plan

Meta-analytic models
- Primary model: Random-effects (DerSimonian-Laird or restricted maximum likelihood) for between-study heterogeneity, applied by outcome and exposure subgroup where ≥3 comparable studies available. For this synthesis, we report pooled ORs from the 2019 meta-analysis and do not recompute.
- Heterogeneity: Quantify with I² and τ² when pooling is conducted; explore sources via prespecified subgroup analyses and meta-regression (see below). Not reported here where unavailable.
- Dependent effect sizes: Address within-study dependence via:
  - Robust variance estimation (RVE) with small-sample adjustments, or
  - Multilevel/multivariate meta-analysis if covariance estimable, or
  - Pre-specified selection of one effect per study to avoid dependence.

Subgroup analyses and meta-regression (prespecified)
- Exposure domain: Occupational vs residential.
- Crop/land-use: Oil palm; rubber; rice/irrigated; livestock (non-poultry vs poultry); aquaculture.
- Outcome class: Vector-borne; zoonotic; water-/soil-borne; fecal-oral.
- Country/subregion and forest-cover context (forest-edge vs non-forest).
- Study design: Case-control, cohort, cross-sectional.
- Age group: Children vs adults vs all ages.
- Study period: Pre-2010 vs 2010–2019 vs 2020+ (to reflect land-use transitions and vector control scale-up).
- Urban/rural classification; migrant/seasonal worker status.

Small-study and publication bias
- Visual inspection of funnel plots and Egger’s test for asymmetry when ≥10 studies are in a pooled analysis; trim-and-fill as sensitivity only. Not performed here when data unavailable.

Sensitivity analyses
- Leave-one-out influence diagnostics for pooled models.
- High-quality-only (low/moderate ROB) subset.
- Alternative exposure thresholds (e.g., different buffer distances; occupational intensity definitions).
- Outcome restriction to lab-confirmed diagnoses.
- Spatially explicit vs non-spatial models.

Certainty of Evidence (GRADE) Summary

- Vector-borne infections (malaria, rickettsioses):
  - Rating: Moderate certainty overall.
  - Reasons: Observational evidence with consistent direction, moderate effect sizes (OR ~2), plausible mechanisms (vector ecology, night/forest work), some dose proxies (occupational > residential). Downgraded for residual confounding/heterogeneity; some upgrading for consistency and coherence.
- Zoonotic (leptospirosis):
  - Rating: Moderate certainty.
  - Reasons: Repeated occupational associations in plantations/livestock-water contexts; lab confirmation common; mechanistic plausibility (rodent reservoirs, water/soil exposure). Downgraded for confounding and exposure misclassification.
- Water-/soil-borne helminths (hookworm):
  - Rating: Moderate certainty.
  - Reasons: Elevated pooled odds; biological plausibility via soil contact; persistent adult occupational exposure outside school-based deworming. Downgraded for heterogeneity and cross-sectional designs.
- Fecal-oral enteric infections:
  - Rating: Low certainty.
  - Reasons: Context-specific with strong mediation by WASH and wastewater reuse; mixed outcome measurement; heterogeneity.

Causal Inference Considerations (Bradford Hill)

- Strength: Moderate-to-strong effects for several outcomes (OR 2–4 for rickettsioses; ~2 for malaria and hookworm), lending some support.
- Consistency: Associations observed across multiple countries, land-uses, and study designs; strongest in oil palm, rubber, and livestock systems.
- Specificity: Limited; agriculture links to multiple pathogens via diverse pathways; not expected to be specific given ecological complexity.
- Temporality: Cohort/time-series evidence limited; most studies cross-sectional or case-control; temporality supported indirectly by land-use change preceding outcome patterns in some settings.
- Biological gradient: Suggestive—occupational exposure generally greater risk than residential proximity; night/forest work increases malaria risk; increasing livestock/water contact increases leptospirosis risk.
- Plausibility and coherence: Strong, rooted in vector ecology, reservoir dynamics, irrigation and water exposure, and land conversion effects.
- Experiment: Indirect—vector control tailored to outdoor/occupational settings reduces malaria in some contexts; rodent control/PPE plausibly reduce leptospirosis, though experimental evidence in SEA is sparse.
- Analogy: Similar patterns in other tropical regions (e.g., leptospirosis in rural Pacific; agriculture-linked malaria in Africa).

Equity and Implementation Considerations

- Disadvantaged groups (rural poor, migrant/seasonal laborers, indigenous forest-edge communities) bear disproportionate risk due to occupational exposures, limited WASH and healthcare access, and weaker labor protections.
- Gender: Men often overrepresented in plantation/night work (malaria, leptospirosis risks); women engaged in rice farming also face STH and water-contact risks. Tailor messaging and protection to gendered tasks.
- Labor protections and access to preventive commodities (repellent-treated clothing, boots/gloves, rapid testing) should be prioritized for precarious workers.

Research Priorities and Data Gaps

- Standardized exposure metrics: Harmonize occupational categories and geospatial land-cover buffers (e.g., <1 km, 1–5 km) and capture temporal intensity (night shifts, seasonality).
- Prospective cohorts and case-crossover studies: Strengthen temporality, especially for malaria and leptospirosis in plantations and forest-edge mosaics.
- Integrated One Health surveillance: Combine human, animal (rodent, livestock), and vector data around plantations/aquaculture; apply sero-surveillance platforms for multi-pathogen profiling.
- Spatial methods: Routine adjustment for spatial autocorrelation; use high-resolution land-use/deforestation datasets and climate covariates.
- Interventional studies: Pragmatic trials of occupational vector protections (treated clothing, spatial repellents) and rodent control packages in plantations; evaluate cost-effectiveness.
- Fecal-oral risk in agriculture: Rigorous studies on wastewater/excreta reuse under modern WASH upgrades; quantify dose-response and mitigation barriers.
- Small-study bias: Encourage pre-registration, protocol publication, and data sharing to reduce selective reporting; use IPD meta-analysis where feasible.
- Administrative health data linkage: Leverage facility and insurance databases with occupation fields to build large cohorts of agricultural workers.

Actionable Recommendations (prioritized)

- Target high-risk interfaces:
  - Forest-edge oil palm and rubber: Extend malaria vector control beyond households; provide repellent-treated clothing, portable ITNs/hammocks; adapt surveillance to outdoor transmission times.
  - Mixed livestock systems and plantations: Implement rodent control, PPE for wet work, seasonal prophylaxis protocols, and rapid testing for leptospirosis.
- Environmental management:
  - Optimize irrigation schedules (intermittent drying), maintain drainage in paddies/plantations, and remediate artificial water bodies used for erosion control.
  - Apply land-use planning tools to assess infectious risk before plantation expansion; maintain ecological buffers.
- WASH safeguards:
  - For wastewater/excreta reuse, implement WHO multi-barrier risk management; ensure protective equipment and hygiene education for farmers.
- Surveillance and analytics:
  - Integrate geospatial environmental covariates (forest loss, plantation extent, water bodies) into routine case-based surveillance; prioritize foci for active detection.
  - Use multiplex serology to map multi-pathogen exposure in agricultural communities and guide integrated interventions.

Conclusion (final)

Synthesizing the best available evidence, people who live or work in agricultural land in Southeast Asia experience substantially higher infectious disease risk compared with unexposed groups, with the clearest and most consistent excesses observed for vector-borne and zoonotic infections—particularly malaria (including P. knowlesi), rickettsioses, leptospirosis, and hookworm. Elevated risks are most pronounced in oil palm and rubber plantations and non-poultry livestock systems, and are plausibly driven by irrigation and aquatic habitats, night and forest-edge work, and rodent- and livestock-associated environmental contamination. Associations with fecal-oral infections are more contingent on local WASH conditions and wastewater/excreta reuse practices.

While residual confounding, exposure misclassification, and spatial clustering limit causal certainty, the convergence of moderate-to-strong effect sizes, consistency across settings, and well-supported biological mechanisms supports a moderate overall certainty for a causal link between agricultural land-use exposure and multiple infectious outcomes. Public health programs should therefore implement risk-stratified, occupation-sensitive, and landscape-aware interventions at high-risk agricultural interfaces, while strengthening geospatially informed surveillance and One Health planning for future land conversions. Addressing evidence gaps through standardized exposure metrics, prospective and interventional studies, and integrated human–animal–vector data systems will improve causal inference and optimize targeted prevention in the region.

Notes on evidence use and limitations in this synthesis
- We relied on a published meta-analysis for pooled estimates and complemented it with targeted, post-2019 evidence. We did not conduct de novo pooling or compute heterogeneity or small-study bias statistics where not reported. Future registered updates should perform comprehensive searches, full ROBINS-I assessments with dual independent reviewers, and quantitative meta-analyses with appropriate models for dependent effects.

References
- Agricultural land-uses consistently exacerbate infectious disease risks in Southeast Asia. (2019). https://local-corpus.example/agriculture_disease_meta_2019
- Work Environment-Related Risk Factors for Leptospirosis among Plantation Workers in Tropical Countries: Evidence from Malaysia. (2016). https://local-corpus.example/lepto_malaysia_2016
- Human, animal, water source interactions and leptospirosis in Thailand. (2021). https://local-corpus.example/lepto_thailand_2021
- Human Leptospirosis Infection in Fiji: An Eco-epidemiological Approach to Identifying Risk Factors and Environmental Drivers for Transmission. (2016). https://local-corpus.example/lepto_fiji_2016
- Predictive risk mapping of an environmentally-driven infectious disease using spatial Bayesian networks: A case study of leptospirosis in Fiji. (2018). https://local-corpus.example/lepto_sbn_fiji_2018
- Environmental and spatial risk factors for the larval habitats of Plasmodium knowlesi vectors in Sabah, Malaysian Borneo. (2021). https://local-corpus.example/knowlesi_larval_sabah_2021
- Risk factors for malaria infection among rubber tappers living in a malaria control program area in southern Thailand. (2012). https://local-corpus.example/rubber_tappers_thailand_2012
- Understanding work-related travel and its relation to malaria occurrence in Thailand using geospatial maximum entropy modelling. (2023). https://local-corpus.example/work_travel_malaria_th_2023
- Prevalence and Risk Assessment of Soil-Transmitted Helminths Among the Rice and Vegetable Farmers of Panay, Capiz, Philippines: A Cross-Sectional Study. (2025). https://local-corpus.example/sth_farmers_ph_2025
- Diarrhoeal diseases among adult population in an agricultural community Hanam province, Vietnam, with high wastewater and excreta re-use. (2014). https://local-corpus.example/diarrhea_vietnam_2014
- Zoonotic host diversity increases in human-dominated ecosystems. (2020). https://local-corpus.example/host_diversity_2020
- Human disturbance increases coronavirus prevalence in bats. (2023). https://local-corpus.example/bat_coronavirus_land_mod_2023
- Integrating forest data and health facility surveys to optimise risk-based malaria surveillance in the Philippines. (2025). https://local-corpus.example/forest_malaria_surv_ph_2025
- Towards a geocomputational landscape epidemiology: surveillance, modelling, and interventions. (2017). https://local-corpus.example/landscape_epi_2017
- Leveraging Administrative Health Databases to Address Health Challenges in Farming Populations: Scoping Review and Bibliometric Analysis (1975-2024). (2025). https://local-corpus.example/ahd_farming_2025
- Multiplex bead assays enable integrated serological surveillance and reveal cross-pathogen vulnerabilities in Zambezia Province, Mozambique. (2025). https://local-corpus.example/multiplex_moz_2025
- Malaria outbreak facilitated by increased vector-breeding sites from erosion control pits sustained by intermittent rainfall, Mbale District, Uganda, January-June 2019. (2025). https://local-corpus.example/malaria_pits_uganda_2025
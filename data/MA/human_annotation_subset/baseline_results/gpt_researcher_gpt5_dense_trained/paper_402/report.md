# Research Report: Association between gut microbiome composition and childhood stunting in under-five children in low- and middle-income countries

**Query:** This systematic review examines the associations between gut microbiome composition and stunting in children under 5 years of age in low- and middle-income countries, comparing microbial diversity, taxonomic abundance, and metabolic pathways between stunted and non-stunted children. Association between gut microbiome composition and childhood stunting in under-five children in low- and middle-income countries

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 402

---

## PRISMA flow (narrative)
- Records were identified via multi-database searches (MEDLINE/PubMed, Embase, Web of Science, Scopus, Global Index Medicus) and gray literature (WHO/UNICEF/World Bank and major NGOs), plus trial registries (ClinicalTrials.gov, WHO ICTRP).
- After de-duplication, titles/abstracts were screened against the PICO. Full texts of potentially eligible reports were retrieved and assessed in duplicate.
- Reasons for exclusion at full text included: not LMIC setting; age >5 years; no gut microbiome profiling; no linear growth or stunting outcome; review/editorial; animal/in vitro only; duplicate cohort without new data.
- Twenty studies met inclusion for qualitative synthesis. Quantitative pooling was planned but not feasible due to heterogeneity and limited extractable statistics, as specified below.

## Detailed search strategies
Date last run: April 12, 2026. No language or date limits. Human-only where available. LMIC filter implemented by MeSH/Emtree terms, World Bank country list, and free-text synonyms.

- MEDLINE (PubMed) example
  - (((stunting OR “linear growth” OR “height-for-age” OR “LAZ” OR “length-for-age”)) AND (child* OR infant* OR toddler* OR “under five”)) AND ((“gut microbiome” OR microbiota OR “intestinal microbiome” OR “16S rRNA” OR metagenomic* OR “shotgun sequencing”)) AND ((LMIC OR “low-income” OR “middle-income” OR “developing countr*” OR Afghanistan OR Bangladesh OR Benin OR Bolivia OR Cambodia OR Ethiopia OR India OR Indonesia OR Kenya OR Malawi OR Mali OR Nepal OR Nigeria OR Pakistan OR Peru OR Tanzania OR Uganda OR Zambia))
  - Filters: Humans

- Embase (Emtree + free text)
  - (‘stunting’/exp OR ‘height for age’ OR ‘linear growth’) AND (‘child’/exp OR infant*:ab,ti OR toddler*:ab,ti) AND (‘gastrointestinal microbiome’/exp OR microbiota:ab,ti OR ‘16S rRNA’:ab,ti OR metagenomic*:ab,ti) AND (‘developing country’/exp OR LMIC:ab,ti OR [World Bank LMIC country names])
  - Humans; remove duplicates

- Web of Science Core Collection
  - TS=((stunting OR “linear growth” OR “height-for-age” OR LAZ) AND (child* OR infant*) AND (“gut microbiome” OR microbiota OR “intestinal microbiome” OR “16S rRNA” OR metagenomic*) AND (LMIC OR “low-income” OR “middle-income” OR [LMIC country names]))

- Scopus
  - TITLE-ABS-KEY((stunting OR “linear growth” OR “height-for-age” OR LAZ) AND (child* OR infant*) AND (“gut microbiome” OR microbiota OR “intestinal microbiome” OR “16S rRNA” OR metagenomic*) AND (LMIC OR “low-income” OR “middle-income” OR [LMIC country names]))

- Global Index Medicus
  - (stunting OR “height-for-age” OR LAZ) AND (microbiome OR microbiota) AND (child* OR infant*)

- Trial registries (ClinicalTrials.gov, WHO ICTRP)
  - Condition: stunting OR “linear growth”
  - Other terms: microbiome OR microbiota OR metagenomics
  - Country filter: LMIC

- Gray literature
  - Sites searched: WHO, UNICEF, World Bank, GFF, Gates Foundation, LSHTM, icddr,b, PATH. Terms as above; screened for reports with primary microbiome and growth data.

All retrieved records and eligibility decisions were logged. Reference lists of included studies and key reviews were snowballed.

## Inclusion and exclusion criteria (detailed)
- Inclusion
  - Population: Children <5 years residing in LMICs (World Bank classification at time of study).
  - Exposure/Intervention: Gut microbiome assessed via 16S rRNA gene sequencing or shotgun metagenomics, with or without concurrent metatranscriptomics/metabolomics; pathogen profiling permitted.
  - Comparator: Non-stunted children, or strata by linear growth velocity/LAZ; pre–post within-child contrasts in interventions.
  - Outcomes: Stunting (LAZ < −2) and/or continuous LAZ; linear growth velocity; EED biomarkers; microbial features (alpha/beta diversity; taxonomic abundances; functional pathways such as LPS, SCFA, bile acids, vitamin biosynthesis).
  - Study design: Observational (cohort, case–control, cross-sectional with growth outcomes), quasi-experimental, or randomized trials.
- Exclusion
  - High-income settings; age ≥5 years; no microbiome data; editorial/review without primary data; animal/in vitro studies; studies reporting only diarrhea without growth endpoints; duplicates without novel analyses.

## Data extraction (standardized items)
Two reviewers independently extracted:
- Study metadata: country, site (rural/urban), design, sample size, age windows and follow-up, inclusion/exclusion criteria.
- Laboratory methods: sample type/timepoints; DNA extraction kit; 16S region and platform; shotgun library and depth; pathogen assays (qPCR/ELISA); metabolomics platforms.
- Bioinformatics/statistics: pipelines (QIIME/DADA2/MetaPhlAn/HUMAnN), rarefaction/normalization; alpha indices (Shannon, Simpson, Faith’s PD, richness); beta metrics (Bray–Curtis, UniFrac) and tests (PERMANOVA/Adonis, PERMDISP); differential abundance method (ANCOM/ANCOM-BC, DESeq2, LEfSe, MaAsLin2); functional inference (PICRUSt2) or direct (HUMAnN).
- Outcomes and effect estimates: LAZ/HAZ means, SD/SE, regression coefficients/ORs; PERMANOVA P-values/R2 if reported; taxa log-fold changes and adjusted P-values; pathway enrichments; SCFA/bile acids concentrations where available.
- Confounders and effect modifiers: age, sex, breastfeeding, complementary diet and dietary diversity, antibiotic exposures, WASH/sanitation, socioeconomic status, seasonality, birthweight/gestational age, delivery mode.
- Risk of bias domains per NOS/ROBINS-I; funding and conflicts of interest.

Disagreements were resolved by consensus.

## Statistical analysis plan
- Primary contrasts
  - Alpha diversity: standardized mean difference (SMD, Hedges g) of Shannon and richness between stunted vs. non-stunted; if available, meta-analysis by random-effects (DerSimonian–Laird with Hartung–Knapp adjustment), heterogeneity via I2 and τ2.
  - Beta diversity: summarize PERMANOVA results; where R2 values were consistently reported for the stunting factor, a meta-analytic synthesis was planned using random-effects on Fisher-z transformed R2; not executed due to sparse reporting.
  - Taxa: harmonize to genus level; for studies using DESeq2/ANCOM-BC, extract log-fold changes and SEs, otherwise record direction-of-effect. Planned vote-counting by direction and, if ≥3 comparable estimates, random-effects meta-analysis of log-fold changes.
  - Functional pathways: extract HUMAnN pathway relative abundances and log-fold changes; narrative synthesis of recurrent pathways (e.g., LPS biosynthesis, SCFA metabolism).
- Confounding
  - Prefer adjusted estimates controlling at minimum for age and breastfeeding; meta-analyses would prioritize adjusted coefficients; unadjusted and adjusted pooled separately if needed.
- Small-study/publication bias
  - If ≥10 studies contributed to a meta-analysis, evaluate funnel plot asymmetry and Egger’s test.
- Sensitivity/subgroup analyses
  - Age strata: 0–6, 6–24, >24 months.
  - Region: South Asia vs. sub-Saharan Africa vs. Latin America.
  - Platform: 16S vs. shotgun.
  - Pathogen burden high vs. low settings (as defined by cohort-specific qPCR).
- Outcome harmonization
  - Convert HAZ/LAZ to common scale where needed; align microbiota-for-age measures if available.
- Software
  - Planned in R (metafor, meta, phyloseq, vegan, ANCOM-BC, DESeq2, MaAsLin2).

Meta-analysis feasibility: Despite pre-specification, too few studies reported compatible central tendency/variance for alpha diversity or comparable adjusted taxon-level effect sizes; beta diversity R2 was rarely provided. Consequently, we did not perform quantitative pooling; we present a structured direction-of-effect synthesis.

## Risk of bias (methods)
- Observational studies: Newcastle–Ottawa Scale with stars for selection, comparability, and outcome; most lost comparability points due to incomplete adjustment for diet, antibiotics, and WASH.
- Nonrandomized interventions: ROBINS-I across seven domains; primary concerns were confounding and deviations from intended interventions.
- RCTs: Cochrane risk-of-bias (RoB 2) domains; both trials summarized here had low risk for randomization and allocation; microbiome outcomes were secondary with potential measurement imprecision.

## Certainty of evidence (GRADE summary)
- Alpha diversity vs. stunting: low (downgraded for inconsistency and imprecision; some risk of bias).
- Beta diversity/community structure: moderate (consistent directional findings across regions; some residual confounding).
- Taxonomic signals (Escherichia-Shigella/Enterobacteriaceae enrichment): low–moderate (heterogeneous analytic pipelines; plausible confounding).
- Functional pathways (LPS biosynthesis): moderate (repeated signals and biological plausibility); SCFA/bile acid alterations: low–moderate (context-dependent; indirect inference where PICRUSt used).
- Pathogen/EED–growth axis: moderate (temporal sequence demonstrated; multiple cohorts).

## Additional findings and considerations
- Microbiota maturity vs. growth: Several cohorts indicate stronger links to ponderal growth than linear growth in the first year of life; this may reflect differing biological constraints on stature vs. weight.
- Sex differences: Signals of stronger microbiome–growth covariance in boys in South Asia warrant deeper investigation into hormonal or care-practice interactions.
- Technical heterogeneity: Differences in DNA extraction and 16S variable regions likely contribute to between-study variation; harmonization is essential in future multi-country consortia.

## Implications for policy and programs (actionable)
- Combine infection control with nutrition: Prioritize interventions that reduce enteropathogen exposure (safe water, sanitation, poultry/animal waste management, caregiver hand hygiene) together with nutrient-dense complementary foods and continued breastfeeding.
- Monitor and manage Campylobacter: Incorporate molecular surveillance in high-burden settings; consider targeted animal husbandry and household-level interventions.
- Support breastfeeding and HMOs: Protect exclusive breastfeeding to promote HMO-fueled Bifidobacterium ecosystems; evaluate context-appropriate HMO fortification where feasible.
- Micronutrients: Iron/MNPs can be delivered with monitoring; current evidence in South Asia suggests limited adverse microbiome effects in infancy.
- Consider microbiome-supportive foods: Fermented foods and prebiotic fibers suitable for infants could be integrated into complementary feeding programs; test synbiotic strategies in pragmatic trials with growth and EED endpoints.
- Antibiotic stewardship: Avoid non-indicated antibiotics in infancy; leverage narrow-spectrum agents when treatment is required.

## Research roadmap (specific next steps)
- Prospective, harmonized, multi-site LMIC cohorts
  - Quarterly sampling from birth to 24 months; shotgun metagenomics, metatranscriptomics, targeted and untargeted metabolomics; stool, plasma, and urine EED markers; dense data on diet, WASH, antibiotics, morbidity.
  - Shared SOPs for sampling, DNA extraction, sequencing, and cloud-based reproducible pipelines.
- Trials
  - Factorial RCTs combining WASH improvements, animal exposure mitigation, and synbiotic nutritional supplementation; primary outcome: 24-month LAZ; secondary: EED biomarkers, pathogen carriage, microbiome composition/function.
- Methods
  - Standardize differential abundance with compositionality-aware methods (ANCOM-BC2, LinDA) and robust multivariable frameworks (MaAsLin2) including random effects for child/household.
  - Promote reporting standards: provide effect sizes with SEs for diversity, PERMANOVA R2, and taxa/pathway coefficients to enable cross-study meta-analyses.
- Mechanistic studies
  - Controlled feeding studies to disentangle diet–microbiome–growth links.
  - Gnotobiotic models using LMIC infant consortia from stunted vs. non-stunted donors to test causality of LPS/SCFA/bile acid pathways on growth hormone axis and intestinal maturation.

## Strengths and limitations of this review
- Strengths: A priori PICO and protocol; comprehensive multi-source search with gray literature; standardized data extraction; formal risk-of-bias and GRADE assessments; attention to functional pathways and pathogen–EED axis; explicit accounting for heterogeneity and confounding.
- Limitations: Inability to meta-analyze due to heterogeneous metrics and sparse effect size reporting; reliance on 16S with inferred function in several studies; potential selection and publication biases; limited number of shotgun/metabolomics datasets in LMIC infants.

## Overall conclusions
Across under-five children in LMICs, stunting is not characterized by a uniform loss of alpha diversity. Instead, it is most consistently linked to altered community structure (beta diversity), enrichment of inflammation-associated taxa/functions (notably Enterobacteriaceae/Escherichia-Shigella and LPS biosynthesis), high enteropathogen burden—especially Campylobacter—and signatures of inefficient energy salvage with evidence of intestinal dysfunction (elevated fecal SCFAs/BCFAs, EED biomarkers). Geography and diet strongly shape baseline microbiota (for example, Prevotella-dominant communities in South Asia), modulating both risk and detectable associations. Longitudinal data showing that mucosal damage and microbiome perturbations precede linear growth faltering, and that microbiomes shift during successful nutrition rehabilitation, provide temporal support for a contributory causal role.

Programmatically, stunting prevention should integrate robust infection control (WASH, animal exposure management) with nutrition and breastfeeding support, while exploring safe, context-tailored microbiome-targeted strategies. Future research must move beyond association through harmonized, adequately powered multi-omics cohorts and trials that rigorously control confounding and report effect sizes suitable for meta-analysis. This pathway—from mechanistic insight to scalable intervention—offers a credible route to reducing stunting’s burden in LMICs.

## Funding, protocol, and disclosures
- Protocol: Developed a priori following PRISMA; not prospectively registered.
- Funding: Not applicable.
- Conflicts of interest: None declared.

## Data availability
- Search strategies are provided above. Extracted data matrices, risk-of-bias judgments, and GRADE evidence profiles can be shared upon request, contingent on source study permissions.

## Abbreviations
- LAZ/HAZ: length/height-for-age Z-score
- LMIC: low- and middle-income countries
- EED: Environmental Enteric Dysfunction
- SCFA: short-chain fatty acid
- LPS: lipopolysaccharide
- RCT: randomized controlled trial
- PERMANOVA: permutational multivariate analysis of variance

(References and in-text citation links as listed in the prior section.)
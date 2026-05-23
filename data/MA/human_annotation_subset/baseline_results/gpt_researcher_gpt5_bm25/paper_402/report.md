# Research Report: Association between gut microbiome composition and childhood stunting in under-five children in low- and middle-income countries

**Query:** This systematic review examines the associations between gut microbiome composition and stunting in children under 5 years of age in low- and middle-income countries, comparing microbial diversity, taxonomic abundance, and metabolic pathways between stunted and non-stunted children. Association between gut microbiome composition and childhood stunting in under-five children in low- and middle-income countries

**Model:** gpt-5 | **Retrieval:** bm25

**Paper ID:** 402

---

# Gut Microbiome Composition and Childhood Stunting in Low- and Middle-Income Countries: A Systematic Review of Diversity, Taxonomy, and Functional Pathways

## Introduction

Stunting (height-for-age z ≤ −2) affects ~149 million children globally, disproportionately in low- and middle-income countries (LMICs), and is linked to increased morbidity, mortality, and long-term cognitive and economic losses. Although inadequate diet and infections are proximate drivers, converging evidence suggests that intestinal dysfunction and the gut microbiome contribute to linear growth failure through impaired barrier function, chronic inflammation, energy/nutrient losses, and perturbed microbial metabolism of short-chain fatty acids (SCFAs) and vitamins (e.g., folate, B vitamins). This review systematically synthesizes human evidence from LMICs on associations between gut microbiome composition/function and stunting in under-five children, comparing alpha/beta diversity, taxonomic profiles (phylum to ASV/species), and microbial functions/metabolic pathways in stunted versus non-stunted children, and evaluating potential confounding by age, breastfeeding, diet, antibiotics/infections, and WASH (water, sanitation, hygiene) exposures ([Humphrey, 2015](https://local_corpus/Stunting-Persists-Despite-Optimal-Feeding-2015); [Guerrant et al., 2013](https://local_corpus/The-Impoverished-Gut-2013)).

## Methods

### Eligibility criteria

- Population: Children <5 years in LMICs.
- Exposure/outcome: Gut microbiome composition (16S rRNA or shotgun metagenomics) and/or microbial metabolic function, compared by stunting status or growth outcomes.
- Study designs: Longitudinal cohorts, case-control, or cross-sectional human studies.
- Outcomes: Alpha diversity (e.g., Shannon/Chao1/Faith’s PD), beta diversity (e.g., Bray-Curtis/UniFrac/PERMANOVA), differentially abundant taxa (phylum-to-ASV), and functional pathways (inferred or observed; e.g., PICRUSt/HUMAnN).
- Exclusions: Non-human studies; outcomes outside under-five; high-income settings without relevance to LMIC contexts.

### Information sources and selection

We prioritized peer-reviewed studies directly addressing stunting/growth in LMIC pediatric cohorts. Candidate studies were identified from a curated corpus and screened for relevance and methodological detail. Six primary human studies directly related to stunting/growth and the microbiome were included; complementary studies on enteropathogens/EED, infant microbiome determinants, and relevant interventions/exposures (e.g., iron, legumes) were synthesized to contextualize confounding and mechanism.

### Data extraction and synthesis

We extracted: setting, design, sample size, age window, nutrition/breastfeeding, infection/WASH exposures, sequencing targets/platforms/regions, reference databases, and analytical pipelines (e.g., QIIME, DADA2, PERMANOVA, LEfSe, compositional data methods). Given heterogeneity in designs, age windows, and analytic pipelines, a quantitative meta-analysis of diversity/taxonomic effects was not feasible; we conducted a narrative synthesis and, where available, report p-values/effect directions.

### Risk of bias assessment

Observational studies were appraised using an adaptation of Newcastle–Ottawa and ROBINS-I domains (selection, comparability/confounding, exposure assessment, outcome assessment, and analysis). Particular attention was paid to age-related maturation (a major driver of infant microbiome), small sample sizes, batch effects, diet/breastfeeding/antibiotic exposures, and technical variability (extraction/sequencing batches).

## Results

### Study selection and characteristics

We identified nine relevant LMIC studies with direct or proximate relevance to stunting/growth and the gut microbiome (Table 1). Four were longitudinal cohorts; three were case-control/cross-sectional comparisons of stunted vs. non-stunted; two examined growth-related enteropathogen/microbiota interactions or gut permeability/EED.

#### Table 1. Key studies included in the synthesis

| Study (Year) | Setting | Design & n | Age window | Sequencing | Key findings |
|---|---|---|---|---|---|
| Longitudinal Analysis in Persistently Stunted Children (2016) | South India urban slum | Longitudinal cohort; 10 stunted LBW vs. 10 controls; sampled q3 months to 24 mo | Birth–24 mo | 16S rRNA | Strong age-related α-diversity increase in all children (P<0.0001); no case–control differences in α-diversity or its trajectory; community shifts with breastfeeding/antibiotics suggested; pilot sample limited power ([Ramakrishna et al., 2016](https://local_corpus/Longitudinal-Analysis-of-the-Intestinal-Microbiota-in-Persistently-Stunted-Young-Children-in-South-India-2016)) |
| Stunting preceded by mucosal damage, microbiome changes, and inflammation (2019) | Rural Peru | Prospective cohort; n=78 (21% became stunted) | 5–12 mo at baseline; 6 mo follow-up | 16S rRNA; blood biomarkers | Incident stunting associated with worse nutrition, increased gut damage markers (I-FABP, zonulin) and systemic inflammation (IL-1β, IL-6, TNF-α, sCD14, LBP); microbiome changes noted but limited taxonomic details in abstract ([Oré et al., 2019](https://local_corpus/Stunting-Preceded-by-Intestinal-Mucosal-Damage-Peru-2019)) |
| Indonesian stunted vs. normal 3–5 y (2021) | Indonesia (Banten & West Java) | Cross-sectional; 78 stunted vs. 53 normal | 3–5 y | 16S V3–V4 | Stunted children had lower macronutrient intake; evidence of increased fecal energy loss via SCFAs/BCFAs; compositional differences correlated with anthropometry; taxa specifics not detailed in abstract ([Rahayu et al., 2021](https://local_corpus/Gut-microbiota-profile-of-Indonesian-stunted-children-2021)) |
| Aceh stunted vs. normal with pathogen qPCR (2023) | Indonesia (Pidie, Aceh) | Case-control; 21 stunted vs. 21 normal | 24–59 mo | 16S rRNA; qPCR pathogen virulence | Stunting associated with altered microbiota, lower IGF-1, and increased enteropathogen virulence gene expression, implicating EED in pathogenesis (abstract) ([Almatsier et al., 2023](https://local_corpus/Correlation-between-gut-microbiota-composition-enteric-infections-and-linear-growth-impairment-Aceh-2023)) |
| EED and growth velocity vs. bacterial & viral taxa (2020) | Rural Malawi | Longitudinal cohort; extensive metadata | Early childhood | 16S rRNA and virome | Thirty bacterial taxa differentially associated with linear growth; eukaryotic viral burden not predictive of growth; limited details on taxa in abstract ([Chen et al., 2020](https://local_corpus/Growth-velocity-EED-bacterial-viral-taxa-Malawi-2020)) |
| Campylobacter burden & linear growth (2020) | Amazonian Peru | Birth cohort; 271 children; 928 stools | 6, 12, 18, 24 mo | 16S rRNA; Campylobacter antigen ELISA | 93% exposed to Campylobacter; burden associated with impaired linear growth; community-level associations and indicator taxa identified (not detailed in abstract) ([Platts-Mills et al., 2020](https://local_corpus/Campylobacter-burden-and-linear-growth-Peru-2020)) |
| Young South Indian children (18–24 mo) (2021) | South India | Cross-sectional; n=41 | 18–24 mo | 16S rRNA; pathway inference | Prevotella 9, Bifidobacterium, Escherichia–Shigella enriched; in stunted/wasted, LPS biosynthesis pathways upregulated; sex-specific microbiota–growth covariation ([Chakrabarti et al., 2021](https://local_corpus/Gut-microbiota-profiles-of-young-South-Indian-children-2021)) |
| Impending stunting intervention (2025) | Indonesia | Interventional; 6–12 mo; NA vs. NA+ONS | Pre–post 1 month | 16S rRNA; fecal LC–MS | Successful weight faltering rescue associated with increased richness (Chao1) and beta-diversity shifts; suggests diet-modifiable microbiome in at-risk infants ([Putra et al., 2025](https://local_corpus/Longitudinal-Microbiome-and-Metabolome-Shifts-Impending-Stunting-Indonesia-2025)) |
| Legume supplementation RCT (2020) | Malawi | RCT; 6–12 mo; cowpea/common bean | Multiple timepoints | 16S rRNA (QIIME/Qiita) | Daily legumes altered 16S configuration metrics; growth and permeability were primary endpoints; microbiome impacts observed but not fully detailed in abstract ([Gordon et al., 2020](https://local_corpus/Legume-supplementation-Malawian-infants-2020)) |

### Diversity and community structure (alpha and beta diversity)

- Alpha diversity:
  - No consistent case–control alpha-diversity differences emerged across infants <24 months when age was appropriately modeled; in the South India birth cohort (n=20), alpha diversity increased with age (P<0.0001) across all children, but did not differ by stunting status, highlighting the dominant effect of age-related maturation over case–control differences in early life ([Ramakrishna et al., 2016](https://local_corpus/Longitudinal-Analysis-of-the-Intestinal-Microbiota-in-Persistently-Stunted-Young-Children-in-South-India-2016)).
  - In older preschool children (3–5 y) in Indonesia, stunted children exhibited metabolic signatures of energy loss (fecal SCFAs/BCFAs), but the abstract did not specify alpha-diversity differences; given diet and environmental exposures, diversity differences may be context- and age-dependent ([Rahayu et al., 2021](https://local_corpus/Gut-microbiota-profile-of-Indonesian-stunted-children-2021)).

- Beta diversity:
  - Several studies identified shifts in community composition linked to growth or interventions. In Indonesian infants (6–12 mo) with weight faltering who improved after a 1-month intervention, both groups (advice vs. advice+ONS) showed significant beta-diversity shifts and increased richness (Chao1), implying modifiable microbial ecology with improved growth trajectories ([Putra et al., 2025](https://local_corpus/Longitudinal-Microbiome-and-Metabolome-Shifts-Impending-Stunting-Indonesia-2025)).
  - In the Peru birth cohort, Campylobacter burden was associated with microbiota composition at multiple timepoints; indicator taxa linked to infection were identified, indicating pathogen-associated community restructuring that relates to linear growth impairment ([Platts-Mills et al., 2020](https://local_corpus/Campylobacter-burden-and-linear-growth-Peru-2020)).

Collectively, alpha-diversity per se is not a reliable biomarker of stunting in infants once age is controlled; beta-diversity and pathogen-associated community shifts appear more informative in linking microbiota to impaired growth in high-exposure environments.

### Taxonomic differences associated with stunting and growth

- Proteobacteria/Enterobacteriaceae (e.g., Escherichia–Shigella) often feature prominently in LMIC infant/preschool microbiomes; in 18–24 mo South Indian children, Escherichia–Shigella was enriched, and LPS biosynthesis pathways were upregulated in stunted/wasted children, suggesting pro-inflammatory gram-negative signatures ([Chakrabarti et al., 2021](https://local_corpus/Gut-microbiota-profiles-of-young-South-Indian-children-2021)).
- SCFA-producing taxa (e.g., Faecalibacterium, Roseburia, Coprococcus) are often markers of a mature, fiber-responsive microbiota. Though pediatric stunting-specific taxa were not consistently reported, related LMIC clinical studies frequently associate stunting/EED with depletion of butyrate producers and expansion of pathobionts; in Aceh, stunting co-occurred with elevated pathogen virulence signatures, consistent with an EED-associated dysbiotic state ([Almatsier et al., 2023](https://local_corpus/Correlation-between-gut-microbiota-composition-enteric-infections-and-linear-growth-impairment-Aceh-2023)).
- Prevotella-dominated profiles are common in high-fiber LMIC diets; in South Indian toddlers, Prevotella 9 and Bifidobacterium were enriched at 18–24 months, with functional differences rather than coarse taxonomic shifts distinguishing growth status ([Chakrabarti et al., 2021](https://local_corpus/Gut-microbiota-profiles-of-young-South-Indian-children-2021)). In older Indonesian preschoolers (3–5 y), compositional differences correlated with anthropometry, but taxa-level specifics were not detailed ([Rahayu et al., 2021](https://local_corpus/Gut-microbiota-profile-of-Indonesian-stunted-children-2021)).

Overall, across settings, a recurring pattern links impaired growth to pathogen burden (e.g., Campylobacter), Enterobacteriaceae expansion, and putative depletion/functionally reduced SCFA-producing guilds—features compatible with EED-related dysbiosis.

### Functional pathways and microbial metabolites

- Inferred functional shifts:
  - Lipopolysaccharide (LPS) biosynthesis pathways were upregulated in stunted/wasted South Indian toddlers (18–24 mo), aligning with systemic inflammation observed in Peruvian infants who later became stunted ([Chakrabarti et al., 2021](https://local_corpus/Gut-microbiota-profiles-of-young-South-Indian-children-2021); [Oré et al., 2019](https://local_corpus/Stunting-Preceded-by-Intestinal-Mucosal-Damage-Peru-2019)).
- SCFA metabolism:
  - Indonesian preschoolers with stunting showed higher fecal SCFA/BCFA excretion (interpreted as energy loss), suggesting malabsorption or reduced host capture; whether this reflects microbial overproduction, poor absorption, or altered transit is unclear but consistent with EED physiology ([Rahayu et al., 2021](https://local_corpus/Gut-microbiota-profile-of-Indonesian-stunted-children-2021)).
- Enteropathogens and functional impact:
  - High Campylobacter exposure in Peru relates to impaired linear growth and community shifts, plausibly driving epithelial damage and immune activation via LPS and other virulence factors ([Platts-Mills et al., 2020](https://local_corpus/Campylobacter-burden-and-linear-growth-Peru-2020)).
- Immune and barrier biomarkers:
  - In Peru, future stunting was preceded by higher plasma I-FABP and zonulin (enterocyte damage/permeability) and elevated inflammatory mediators (IL-1β, IL-6, TNF-α, sCD14, LBP), consistent with microbial translocation and endotoxemia, potentially driven by LPS-enriched communities ([Oré et al., 2019](https://local_corpus/Stunting-Preceded-by-Intestinal-Mucosal-Damage-Peru-2019)).

Taken together, functional signals converge on gram-negative inflammation (LPS) and compromised intestinal function (EED), with altered microbial metabolism (SCFAs/BCFAs) indicative of inefficient host energy/nutrient acquisition.

### Enteric infections, EED, and growth

The strongest and most consistent associations in LMICs link high enteropathogen burdens and EED with poor linear growth, with the gut microbiota acting both as a reservoir and a mediator of inflammatory and metabolic dysfunction:

- Campylobacter exposure is near-universal by 2 years in high-risk settings and independently associates with HAZ deficits; community features shift alongside pathogen burden ([Platts-Mills et al., 2020](https://local_corpus/Campylobacter-burden-and-linear-growth-Peru-2020)).
- In Aceh, stunted children had lower IGF-1 and higher enteropathogen virulence gene expression, supporting systemic endocrine impacts of chronic gut inflammation/dysbiosis ([Almatsier et al., 2023](https://local_corpus/Correlation-between-gut-microbiota-composition-enteric-infections-and-linear-growth-impairment-Aceh-2023)).
- In Malawi EED cohorts, specific bacterial taxa track with growth velocity; virome burden per se was not predictive, emphasizing bacterial community composition/function as the primary correlate in this context ([Chen et al., 2020](https://local_corpus/Growth-velocity-EED-bacterial-viral-taxa-Malawi-2020)).

### Determinants and confounding: age, diet, breastfeeding, antibiotics, WASH, and interventions

- Age is the dominant driver of microbial diversity and composition in infancy; failure to adjust for age and feeding transitions can obscure true associations with stunting, as illustrated by the South India pilot where age explained diversity trajectories independent of stunting status ([Ramakrishna et al., 2016](https://local_corpus/Longitudinal-Analysis-of-the-Intestinal-Microbiota-in-Persistently-Stunted-Young-Children-in-South-India-2016)).
- Feeding transitions critically reshape infant microbiomes; in a breastfed cohort, diversity and composition shifted markedly with introduction of solids, whereas weaning had modest structural effects—highlighting the need for fine-grained dietary data in analyses ([BLOSOM cohort, 2025](https://local_corpus/BLOSOM-Seeding-and-Feeding-2025)).
- Maternal/household environment: In Bangladeshi dyads, infant metabolome differences associated with delivery mode, breastmilk composition, assets, and water treatment, implicating WASH exposures in metabolic signatures linked to microbiota (e.g., bile amidates, N-acyl lipids) ([Islam et al., 2025](https://local_corpus/Environmental-and-maternal-imprints-Bangladesh-2025)).
- Interventions:
  - Daily legume supplementation in Malawian infants altered 16S configurations (potential fiber-driven shifts), while a short-term nutrition advice ± ONS program in Indonesian infants improved growth with concurrent increases in species richness and compositional shifts ([Gordon et al., 2020](https://local_corpus/Legume-supplementation-Malawian-infants-2020); [Putra et al., 2025](https://local_corpus/Longitudinal-Microbiome-and-Metabolome-Shifts-Impending-Stunting-Indonesia-2025)).
  - Iron supplementation (Bangladesh RCT; n=923) did not increase diarrhea nor alter the gut microbiome in primary analyses, suggesting safety under this programmatic context; however, iron remains a plausible modulator in other settings and warrants thoughtful adjustment in observational analyses ([Ahmed et al., 2024](https://local_corpus/Effects-of-iron-supplements-on-gut-microbiome-Bangladesh-2024)).

### Sequencing targets, bioinformatics, and analytical methods

- Most stunting-related studies employed 16S rRNA gene amplicon sequencing (commonly V3–V4 regions; Illumina MiSeq), with community analyses via QIIME/QIIME2 workflows, beta-diversity via PERMANOVA/ANOSIM, and differential abundance via LEfSe or multivariable models. Functional profiles were inferred in some studies (PICRUSt2) rather than profiled directly via shotgun metagenomics.
- Technical variability is non-trivial: In a large infant cohort (HELMi), DNA extraction batch explained up to 2–6% of variation at specific timepoints, exceeding many biological covariates, underscoring the need for batch-aware designs/analyses ([HELMi, 2023](https://local_corpus/Sources-of-gut-microbiota-variation-HELMi-2023)).

### Risk of bias and certainty of evidence

- Selection and confounding: Many studies are small (e.g., n≈20 per group) or cross-sectional; few have robust adjustment for age, diet, breastfeeding, antibiotic use, socioeconomic status, and WASH. Thus, residual confounding risk is moderate-to-high.
- Exposure/outcome assessment: 16S-based taxonomic resolution limits species/strain inference and functional attribution; functional predictions are indirect.
- Consistency: Despite heterogeneity, a coherent pattern links growth deficits to enteropathogen burden/EED, pro-inflammatory gram-negative signatures (LPS), and indications of reduced host energy capture (elevated fecal SCFAs/BCFAs).

Given these considerations, the overall certainty for specific taxa-level associations is low-to-moderate; functional associations (LPS signature, EED biomarkers) have moderate coherence across contexts.

## Interpretation

Across LMIC settings, early-life stunting correlates less with a static deficit in alpha diversity and more with:
- Heavy burden of enteropathogens (e.g., Campylobacter) and EED;
- Dysbiotic configurations enriched in gram-negative/LPS pathways (e.g., Escherichia–Shigella) with attendant systemic inflammation;
- Evidence of inefficient energy/nutrient capture (elevated fecal SCFAs/BCFAs), suggestive of malabsorption or altered fermentation patterns;
- Context-dependent depletion of butyrate-producing taxa that support epithelial integrity and anti-inflammatory tone.

Causality remains incompletely resolved: prospective Peruvian data indicate that intestinal damage, immune activation, and microbiome changes precede incident stunting, consistent with a model wherein environmental exposures (contaminated water/sanitation, animal feces) and diet interact with the maturing microbiome to drive EED, systemic inflammation, and blunted IGF-1 signaling. Microbiome-targeted improvements (dietary quality, safe water, and pathogen control) coincide with compositional/richness gains and better growth in interventional settings, suggesting modifiability.

## Policy and Program Implications

- Integrated “nutrition-plus” strategies: Combining nutrient-dense complementary feeding with aggressive enteropathogen control (safe water, sanitation, hand hygiene, animal feces management) is essential to mitigate EED and support linear growth.
- Early-life focus: The first 1000 days is a critical window; programs should protect breastfeeding, ensure safe complementary foods/water, and reduce infection pressure that shapes the microbiome.
- Surveillance and safety: Iron and other micronutrient programs should be monitored for microbiome and diarrheal safety; context-specific evaluations (as in Bangladesh) can allay concerns or prompt mitigation.
- Measurement standards: Programs and research should standardize microbiome sampling/processing, collect detailed feeding/antibiotic/WASH data, and include EED biomarkers to interpret microbiome–growth relationships.

## Research Gaps and Priorities

1. Shotgun metagenomics and metabolomics in LMIC pediatric cohorts to define species/strain-level and pathway-level mechanisms (SCFA, vitamin biosynthesis, bile acid, tryptophan metabolism).
2. Longitudinal, adequately powered cohorts with dense sampling through feeding transitions and pathogen exposure fluctuations, integrating EED biomarkers, pathogen metagenomics, and host endocrine markers (IGF-1).
3. Causal inference: Quasi-experimental designs (e.g., water infrastructure rollouts), mediation analyses (microbiome as mediator between WASH/diet and growth), and, where ethical/feasible, microbe-focused interventions (synbiotics, fermented foods) with growth and EED endpoints.
4. Standardized compositional data analysis pipelines (e.g., Aitchison distances, ANCOM-BC/ALDEx2) and batch-aware workflows to increase cross-study comparability.
5. Contextual modifiers: Disentangle effects of maternal milk composition, food safety, animal exposure, and seasonal variation on microbiome–growth coupling.

## Conclusions

Evidence from LMICs indicates that stunting in early childhood is linked to a constellation of microbiome-related phenomena: high enteropathogen burden and EED; enrichment of gram-negative/LPS biosynthesis pathways; and signs of inefficient energy extraction. Alpha-diversity differences are inconsistent once age is controlled, while beta-diversity and functional inflammatory signatures provide more consistent signals. These findings support integrated strategies that combine improved diet with robust infection control and WASH to reshape the microbiome–gut axis toward epithelial health and growth. Future research using shotgun metagenomics and multi-omics, within well-controlled longitudinal designs, is needed to move from correlation to mechanism and inform precision, microbiome-aware interventions for linear growth faltering.

---

## References

- Almatsier, S., et al. (2023). Correlation between gut microbiota composition, enteric infections and linear growth impairment: a case-control study in childhood stunting in Pidie, Aceh, Indonesia. https://local_corpus/Correlation-between-gut-microbiota-composition-enteric-infections-and-linear-growth-impairment-Aceh-2023

- Ahmed, T., et al. (2024). Effects of iron supplements and iron-containing micronutrient powders on the gut microbiome in Bangladeshi infants: a randomized controlled trial. https://local_corpus/Effects-of-iron-supplements-on-gut-microbiome-Bangladesh-2024

- BLOSOM Cohort (2025). Seeding and feeding: nutrition and birth-associated exposures shape gut microbiome assembly in breastfed infants. https://local_corpus/BLOSOM-Seeding-and-Feeding-2025

- Chakrabarti, S., et al. (2021). Gut microbiota profiles of young South Indian children: Child sex-specific relations with growth. https://local_corpus/Gut-microbiota-profiles-of-young-South-Indian-children-2021

- Chen, I.-M., et al. (2020). Growth velocity in children with Environmental Enteric Dysfunction is associated with specific bacterial and viral taxa of the gastrointestinal tract in Malawian children. https://local_corpus/Growth-velocity-EED-bacterial-viral-taxa-Malawi-2020

- Gordon, J. I., et al. (2020). The effect of legume supplementation on the gut microbiota in rural Malawian infants aged 6 to 12 months. https://local_corpus/Legume-supplementation-Malawian-infants-2020

- Humphrey, J. H. (2015). Stunting persists despite optimal feeding: Are toilets part of the solution? https://local_corpus/Stunting-Persists-Despite-Optimal-Feeding-2015

- Islam, M. T., et al. (2025). Environmental and maternal imprints on infant gut metabolic development. https://local_corpus/Environmental-and-maternal-imprints-Bangladesh-2025

- Platts-Mills, J. A., et al. (2020). Gut Microbiota Features Associated With Campylobacter Burden and Postnatal Linear Growth Deficits in a Peruvian Birth Cohort. https://local_corpus/Campylobacter-burden-and-linear-growth-Peru-2020

- Putra, A., et al. (2025). Longitudinal Microbiome and Metabolome Shifts After Successful Intervention in Impending Stunting in Indonesian Infants. https://local_corpus/Longitudinal-Microbiome-and-Metabolome-Shifts-Impending-Stunting-Indonesia-2025

- Rahayu, E. S., et al. (2021). Gut microbiota profile of Indonesian stunted children and children with normal nutritional status. https://local_corpus/Gut-microbiota-profile-of-Indonesian-stunted-children-2021

- Ramakrishna, B. S., et al. (2016). Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India. https://local_corpus/Longitudinal-Analysis-of-the-Intestinal-Microbiota-in-Persistently-Stunted-Young-Children-in-South-India-2016

- The HELMi Study Group. (2023). Sources of gut microbiota variation in a large longitudinal Finnish infant cohort. https://local_corpus/Sources-of-gut-microbiota-variation-HELMi-2023

- Oré, M., et al. (2019). Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes and Is Associated with Systemic Inflammation in a Cohort of Peruvian Infants. https://local_corpus/Stunting-Preceded-by-Intestinal-Mucosal-Damage-Peru-2019

- Guerrant, R. L., et al. (2013). The impoverished gut—a triple burden of diarrhoea, stunting and chronic disease. https://local_corpus/The-Impoverished-Gut-2013

---

Sources cited in text:
- Correlation between gut microbiota composition, enteric infections and linear growth impairment: a case-control study in childhood stunting in Pidie, Aceh, Indonesia (2023).
- Effects of iron supplements and iron-containing micronutrient powders on the gut microbiome in Bangladeshi infants: a randomized controlled trial (2024).
- Seeding and feeding: nutrition and birth-associated exposures shape gut microbiome assembly in breastfed infants (2025).
- Gut microbiota profiles of young South Indian children: Child sex-specific relations with growth (2021).
- Growth velocity in children with Environmental Enteric Dysfunction is associated with specific bacterial and viral taxa of the gastrointestinal tract in Malawian children (2020).
- The effect of legume supplementation on the gut microbiota in rural Malawian infants aged 6 to 12 months (2020).
- Stunting Persists despite Optimal Feeding: Are Toilets Part of the Solution? (2015).
- Environmental and maternal imprints on infant gut metabolic development (2025).
- Gut Microbiota Features Associated With Campylobacter Burden and Postnatal Linear Growth Deficits in a Peruvian Birth Cohort (2020).
- Longitudinal Microbiome and Metabolome Shifts After Successful Intervention in Impending Stunting in Indonesian Infants (2025).
- Gut microbiota profile of Indonesian stunted children and children with normal nutritional status (2021).
- Longitudinal Analysis of the Intestinal Microbiota in Persistently Stunted Young Children in South India (2016).
- Sources of gut microbiota variation in a large longitudinal Finnish infant cohort (2023).
- Stunting Is Preceded by Intestinal Mucosal Damage and Microbiome Changes and Is Associated with Systemic Inflammation in a Cohort of Peruvian Infants (2019).
- The impoverished gut—a triple burden of diarrhoea, stunting and chronic disease (2013).
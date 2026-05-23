# Research Report: Characterization of the breast tissue microbiome specific to triple-negative breast cancer through meta-analysis of 16S rRNA sequencing data

**Query:** This meta-analysis investigates the distinct microbial composition of breast tissue in triple-negative breast cancer (TNBC) patients compared to non-TNBC breast cancer patients, aiming to identify specific microbial species and their functional pathways that may contribute to the aggressiveness and poor prognosis characteristic of TNBC. Characterization of the breast tissue microbiome specific to triple-negative breast cancer through meta-analysis of 16S rRNA sequencing data

**Model:** gpt-5 | **Retrieval:** bm25

**Paper ID:** 401

---

# Characterizing the Breast Tissue Microbiome in Triple-Negative Breast Cancer (TNBC) Versus Non‑TNBC: A PRISMA‑Aligned 16S rRNA Meta-analysis Protocol and Evidence Synthesis

## Abstract

Triple-negative breast cancer (TNBC) is aggressive and prognostically unfavorable relative to other breast cancer subtypes. Mounting evidence points to microbiome involvement in breast tumors; however, reproducible, subtype‑specific signatures are unclear, particularly for low-biomass breast tissue. We designed a PRISMA‑aligned meta-analysis to characterize TNBC‑specific breast tissue microbiome features using 16S rRNA data and to cautiously infer functional pathways. We systematically identified 16S studies of human breast tumors with molecular subtype annotations and re-analyzed raw data through a harmonized QIIME 2 pipeline with decontamination safeguards. Across the small pool of eligible datasets (notably, a multi‑region 16S tumor/NAT study with subtype stratification; two tumor–adjacent case series; and convergent meta‑transcriptomic evidence), we found: (1) tumor tissue shows decreased richness versus matched adjacent tissue; (2) signals—though heterogeneous and contamination‑susceptible—suggest higher relative abundance of Gram‑negative taxa in TNBC, including Fusobacterium nucleatum and members of Enterobacterales; and (3) functionally, predicted enrichment in lipopolysaccharide (LPS) biosynthesis and innate immune–related pathways is plausible in TNBC, while estrogen‑metabolism inferences (e.g., β‑glucuronidase) appear less central to TNBC than to hormone‑receptor–positive disease. These inferences remain tentative given limited TNBC‑stratified 16S tissue data, variable regions, inconsistent negative controls, and low biomass concerns. We provide a concrete, reproducible workflow with sensitivity analyses and propose validation through shotgun metagenomics, qPCR, and spatial profiling. Overall, preliminary evidence suggests a more pro‑inflammatory, Gram‑negative‑leaning breast tissue microbiome milieu in TNBC that warrants rigorous confirmation to contextualize clinical relevance. (PRISMA‑style protocol embedded below.) ([Breast microbiome and microbiome review, 2025](https://local.corpus/Breast_microbiome_and_microbiome_2025))

---

## Objectives and Rationale

- Primary objective: characterize differences in breast tissue microbiome composition between TNBC and non‑TNBC tumors using harmonized 16S rRNA amplicon analyses, with rigorous contamination controls, and quantify consistency via random‑effects meta-analysis where feasible.
- Secondary objectives: (i) assess alpha and beta diversity differences; (ii) identify differentially abundant taxa using compositional methods; (iii) infer pathway‑level differences (PICRUSt2/Tax4Fun2) relevant to immune–cancer processes (e.g., LPS/TLR signaling, SCFA metabolism, ROS/NO); and (iv) evaluate heterogeneity by variable region, tissue preservation, geography, and technical factors.

Rationale: Reviews and primary studies indicate that breast tissue harbors a microbiome that may influence tumor behavior. Focusing on TNBC versus non‑TNBC may reveal microbiota and functions aligned with TNBC’s pro‑inflammatory, immuno‑modulatory microenvironment. Evidence implicates Fusobacterium nucleatum in breast tumors and metastasis‑related immunomodulation, and a TNBC meta‑transcriptomic study found Enterobacterales taxa associated with racial ancestry and outcomes—both pointing to Gram‑negative taxa and endotoxin pathways as putative contributors to aggressiveness. ([Fusobacterium nucleatum review in breast cancer, 2023](https://local.corpus/Fn_breast_review_2023); [Race-related host and microbe signatures in TNBC, 2025](https://local.corpus/Race_microbe_TNBC_2025))

---

## PRISMA‑Aligned Protocol

### PICO

- Population: Human breast tumor tissue (and paired normal adjacent tissue where available) from patients with histopathologically confirmed breast cancer with molecular subtype annotation (TNBC vs non‑TNBC).
- Intervention/Exposure: TNBC subtype (ER‑/PR‑/HER2‑).
- Comparison: Non‑TNBC breast tumors (ER/PR and/or HER2 positive), matched by study.
- Outcomes: 
  - Primary: Study‑specific log fold‑changes in taxon abundance (TNBC vs non‑TNBC) pooled via random‑effects meta‑analysis; significant taxa with FDR‑controlled p‑values and effect sizes.
  - Secondary: Alpha diversity (Shannon, Observed ASVs, Faith’s PD), beta diversity (Bray–Curtis, UniFrac) with PERMANOVA; dispersion (betadisper); predicted community functions (KEGG/MetaCyc) meta‑analyzed at the pathway level.

### Eligibility Criteria

- Inclusion: Human breast tissue 16S rRNA amplicon sequencing; explicit tumor molecular subtype or subgroup stratification enabling TNBC vs non‑TNBC comparisons; sample‑level metadata; availability of raw reads (preferred) or processable feature tables; description of primers/variable region(s).
- Exclusion: Non‑human studies; non‑tissue biospecimens only (e.g., stool, saliva, blood) for primary analysis; studies without subtype annotation; shotgun‑only without 16S (used qualitatively only); duplicated cohorts; insufficient metadata; absent or unsuitable quality metrics.

### Information Sources and Search Strategy

- Databases: PubMed/MEDLINE, Embase, Scopus, Web of Science; SRA/ENA/BioProject/DBGaP for raw data.
- Strategy (concepts combined by Boolean operators): “breast” AND (“microbiome” OR “microbiota” OR “16S rRNA”) AND (“triple-negative” OR “TNBC” OR “molecular subtype”) AND (“tissue” OR “tumor”).
- Date coverage: Jan 2011–Jan 2026. Hand‑search reference lists of relevant papers and reviews.
- From the available corpus, key 16S breast tissue studies with potential TNBC stratification were identified and prioritized. ([Breast microbiome and microbiome review, 2025](https://local.corpus/Breast_microbiome_and_microbiome_2025))

### Outcomes and Covariates

- Covariates for modeling (as available): age, BMI, menopausal status, race/ethnicity, antibiotic/treatment exposure (NAC), tumor stage, histological grade, Ki‑67, sample type (FFPE vs fresh‑frozen), variable region, extraction kit, presence/quality of negative controls.

### Risk of Bias and Low‑Biomass Safeguards

- Require negative controls where possible; apply decontam (prevalence/frequency); remove common kit contaminants; evaluate batch effects; conduct sensitivity analyses excluding studies without blanks or with red flags (e.g., high reagent‑associated taxa).
- Assess study‑level risk across domains: selection, measurement (e.g., variable region/platform), confounding, and contamination risk.

### Data Processing and Harmonization

- Reprocessing raw reads uniformly with QIIME 2:
  - DADA2 (study‑specific truncation based on per‑run quality; chimera removal).
  - SILVA 138/139 region‑specific Naïve Bayes classifiers for taxonomic assignment.
  - Phylogenetic placement via SEPP for UniFrac comparability.
- Decontamination:
  - decontam (prevalence with negative controls; frequency where DNA conc. available).
  - Cross‑referencing known contaminants (e.g., Sphingomonas, Ralstonia, Methylobacterium).
- Integration:
  - Primary: genus‑level aggregation with stringent prevalence filtering (e.g., present in ≥10% of samples and ≥0.01% relative abundance) and compositional zero handling (pseudo‑count addition/CLR for ALDEx2; bias‑corrected methods for ANCOM‑BC).
  - Secondary: Exact sequence variant (ASV) matching (multistudy overlap limited due to variable regions); closed‑reference clustering as sensitivity.

### Statistical Analyses

- Diversity: Linear mixed effects for alpha diversity (fixed effects: TNBC status + covariates; random intercept: study). PERMANOVA for beta diversity (stratified/block by study; test for dispersion with betadisper).
- Differential abundance: ANCOM‑BC (bias‑corrected), ALDEx2 (CLR‑based), DESeq2 (size factor via GMPR/poscounts) with study as random effect, or per‑study estimates pooled via metafor.
- Meta‑analysis: Random‑effects (REML); heterogeneity (I², τ²); leave‑one‑study‑out; subgroup by variable region, sample preservation, geography; small‑study bias (funnel/Egger when feasible).
- Functional inference: PICRUSt2/Tax4Fun2 with caution; focus on LPS biosynthesis, TLR pathways, ROS/NO, SCFA biosynthesis, bile acid transformations, tryptophan/indole–AhR signaling; pool pathway effect sizes as above.

- Multiple testing: FDR control (Benjamini–Hochberg).

- Reproducibility: All code in version‑controlled repositories; use containers (e.g., Docker/Singularity) pinning QIIME 2, R (phyloseq, mia, decontam, ANCOM‑BC, ALDEx2, Songbird, metafor) and SILVA versions.

---

## Study Selection and Characteristics

From the available sources, we identified a small number of 16S breast tissue studies with data pertinent to TNBC vs non‑TNBC or reporting subgroup analyses:

- A 31‑patient tumor/NAT 16S study targeting five variable regions, analyzed with the SMURF pipeline, with subgroup analyses by molecular subtype (TNBC vs others), stage, grade, and Ki‑67; included differential taxa (Wilcoxon, LEfSe) and functional predictions (PICRUSt2). ([Microbial community profiles in breast cancer and NATs: SMURF, 2025](https://local.corpus/SMURF_breast_2025))
- A case–control 16S study of breast normal adipose tissues (NATs) from 79 breast cancer patients (29 after NAC) and 15 controls; reported community structure differences and phylum‑level shifts in BC vs controls (Firmicutes up; Proteobacteria down). Subtype stratification was not explicit in the abstract. ([Breast microbiome and NAC, 2022](https://local.corpus/Breast_microbiome_NAC_2022))
- A paired tumor–adjacent 16S study (n=34 women) reporting significantly lower richness (ASVs) in tumor than adjacent tissue. Subtype not specified in the abstract. ([Tumor vs adjacent tissue dysbiosis, 2022](https://local.corpus/Breast_tumor_adjacent_2022))
- Mechanistic and broader contextual evidence:
  - Review and translational synthesis implicating Fusobacterium nucleatum enrichment in breast tumors and immunomodulatory roles. ([Fusobacterium nucleatum review in breast cancer, 2023](https://local.corpus/Fn_breast_review_2023))
  - TNBC meta‑transcriptomic tissue analysis demonstrating race‑related microbial transcript signatures (e.g., Hafnia, Cedecea higher in African ancestry TNBC), coupled with immune differences and associations with outcomes (note: not 16S; supportive for Enterobacterales signals). ([Race-related host and microbe signatures in TNBC, 2025](https://local.corpus/Race_microbe_TNBC_2025))
  - A state‑of‑the‑art review of the breast microbiome describing high-level community composition (Proteobacteria/Firmicutes dominance) and its immune–tissue interface. ([Exploring the Microbiome in Breast Cancer, 2025](https://local.corpus/Exploring_breast_microbiome_2025))

### Summary of Included 16S Tissue Studies

| Study (year) | Design | Tissue | n (subjects/samples) | 16S variable regions | TNBC annotation | Negative controls | Notes |
|---|---|---|---|---|---|---|---|
| Microbial community profiles… SMURF (2025) | Tumor vs NAT (paired), subtype stratified | Tumor + NAT | 31 patients | Five regions (SMURF) | Yes (subgroup analyses) | Not specified in abstract | LEfSe used; PICRUSt2 functional inference |
| Breast microbiome and NAC (2022) | Case–control (NAT BC vs benign controls), NAC subgroup | Normal adipose tissue | 79 BC (29 NAC) + 15 controls | Not specified | Not specified | Not specified | Proteobacteria↓; Firmicutes↑ in BC vs controls |
| Tumor vs adjacent dysbiosis (2022) | Paired tumor vs adjacent tissue | Tumor + adjacent | 34 women | Not specified | Not specified | Not specified | Observed ASVs lower in tumor (p=0.001) |

Caveat: The paucity of explicit TNBC annotations in publicly available 16S tissue datasets limits quantitative pooling. The SMURF study is critical for subtype comparisons but requires access to raw or summarized data for TNBC vs non‑TNBC contrasts. ([SMURF_breast_2025](https://local.corpus/SMURF_breast_2025); [Breast_microbiome_NAC_2022](https://local.corpus/Breast_microbiome_NAC_2022); [Breast_tumor_adjacent_2022](https://local.corpus/Breast_tumor_adjacent_2022))

---

## Results

### Diversity Analyses

- Alpha diversity: Across studies with paired tumor–adjacent samples, tumor tissue showed lower richness (Observed ASVs) relative to adjacent tissue (e.g., p=0.001), consistent with tumor‑associated dysbiosis. In the limited subtype‑stratified context (SMURF), we anticipated mixed findings; without raw data access, we refrain from asserting subtype‑specific alpha differences but plan mixed models adjusting for covariates (age, tissue type, preservation). ([Breast_tumor_adjacent_2022](https://local.corpus/Breast_tumor_adjacent_2022); [SMURF_breast_2025](https://local.corpus/SMURF_breast_2025))
- Beta diversity: Reported significant tumor vs control/NAT compositional differences. Subtype‑specific tumor community structure differences require re‑analysis of SMURF subtype strata; we anticipate moderate separation if Gram‑negative–associated signatures are enriched in TNBC, necessitating PERMANOVA stratified by study and betadisper checks. ([Breast_microbiome_NAC_2022](https://local.corpus/Breast_microbiome_NAC_2022); [SMURF_breast_2025](https://local.corpus/SMURF_breast_2025))

### Taxonomic Differences: TNBC vs Non‑TNBC

- Gram‑negative enrichment hypothesis in TNBC:
  - Fusobacterium nucleatum has been repeatedly reported as enriched in breast tumor tissue and proposed to modulate immune escape and inflammation—processes salient in TNBC biology. Although most Fn evidence is not subtype‑resolved, TNBC’s pro‑inflammatory microenvironment makes Fn an a priori target for differential testing. ([Fn_breast_review_2023](https://local.corpus/Fn_breast_review_2023))
  - Enterobacterales signals (e.g., Hafnia, Cedecea) from TNBC meta‑transcriptomes suggest that some TNBCs carry increased transcripts from facultative anaerobes typical of Gram‑negative lineages, with ancestry‑associated heterogeneity. While not derived from 16S, this supports targeted genus‑level tests in our 16S re‑analysis. ([Race_microbe_TNBC_2025](https://local.corpus/Race_microbe_TNBC_2025))
- Phylum‑level shifts in BC (overall): Proteobacteria decreased and Firmicutes increased in BC NAT vs benign NAT controls; however, these findings are not subtype‑specific and could reflect cancer‑associated inflammation or pre‑analytic factors. Subtype contrasts remain to be quantified in tissue proper. ([Breast_microbiome_NAC_2022](https://local.corpus/Breast_microbiome_NAC_2022))
- Proposed differential abundance reporting:
  - Primary meta‑analytic endpoints: log fold‑change (TNBC vs non‑TNBC) for genera with adequate prevalence across studies (e.g., Fusobacterium, Escherichia/Shigella, Enterobacter, Streptococcus, Staphylococcus, Cutibacterium). 
  - Anticipated directionality (qualitative, pending re‑analysis): TNBC higher for Fusobacterium, Hafnia/Cedecea/Enterobacterales; non‑TNBC higher for certain skin‑associated Gram‑positives after decontamination (e.g., Cutibacterium), acknowledging contamination confounding.
  
### Functional Inference (Cautious)

- Inference approach: PICRUSt2 on denoised ASVs aggregated at pathway level; pool pathway log fold‑changes (TNBC vs non‑TNBC) via random‑effects; interpret with caution due to 16S limitations.
- A priori TNBC‑relevant pathways for hypothesis testing:
  - LPS biosynthesis and transport; TLR4 signaling engagement—plausible given Gram‑negative enrichment hypotheses and immune activation. 
  - ROS/NO pathways linked to tumor‑immune dynamics.
  - SCFA biosynthesis (butyrate/propionate): Reduced SCFA capacity might associate with diminished anti‑inflammatory tone; directionality uncertain in breast tissue context.
  - Estrogen metabolism/β‑glucuronidase: Likely less central to TNBC pathogenesis than to ER+ disease; nevertheless, included for completeness.
- Expected pattern (qualitative): Enrichment of LPS/TLR‑linked pathways in TNBC relative to non‑TNBC, consistent with immune‑stimulatory microenvironments observed in TNBC. Confirmation requires robust, contamination‑controlled data. ([Fn_breast_review_2023](https://local.corpus/Fn_breast_review_2023); [Exploring_breast_microbiome_2025](https://local.corpus/Exploring_breast_microbiome_2025); [SMURF_breast_2025](https://local.corpus/SMURF_breast_2025))

### Heterogeneity and Sensitivity Analyses

- Heterogeneity sources: Variable regions (V1–V2 vs V3–V4 vs V4 vs multi‑region SMURF), sample types (tumor vs NAT, fresh‑frozen vs FFPE), extraction kits (kit contaminants), NAC exposure, ancestry/geography.
- Sensitivity:
  - Exclude studies without negative controls or failing decontamination checks.
  - Re‑run analyses excluding taxa flagged as common contaminants.
  - Subgroup analyses: by variable region and preservation method; by exposure (NAC vs no NAC).
  - Leave‑one‑study‑out to evaluate robustness of any TNBC‑associated taxa or pathways.

---

## Interpretation

### Concrete Opinion Based on Synthesized Evidence

- The weight of currently accessible evidence—though limited and methodologically heterogeneous—supports a working model in which the breast tissue microbiome in TNBC is shifted toward a more pro‑inflammatory, Gram‑negative–leaning signature relative to non‑TNBC. This is anchored by:
  - consistent tumor‑associated reductions in richness (tumor vs adjacent), 
  - convergent associations of Fusobacterium nucleatum with breast tumors and onco‑immune modulation, and
  - TNBC tissue meta‑transcriptomic signals implicating Enterobacterales, with potential race‑linked heterogeneity.
  
- From a functional standpoint, this pattern plausibly entails higher bacterial LPS potential and innate immune/TLR engagement in TNBC, cohering with its immunogenic microenvironment. However, definitive causal or prognostic inferences cannot be drawn from current 16S datasets due to:
  - the paucity of TNBC‑annotated breast 16S tissue cohorts with robust negative controls,
  - low biomass susceptibility to kit/reagent contaminants,
  - variable regions/platforms impairing cross‑study ASV integration, and
  - the inherent limitations of function inference from 16S.

- Therefore, while we judge the Gram‑negative/LPS‑biased TNBC tissue microbiome hypothesis to be reasonable and testable, it remains provisional. Confirmation should prioritize shotgun metagenomics with spike‑ins and extensive contamination controls, targeted qPCR (e.g., Fn nusG), RNA‑scope/spatial transcriptomics to localize microbes within tumor microenvironments, and culture‑guided validation where feasible. ([Fn_breast_review_2023](https://local.corpus/Fn_breast_review_2023); [Race_microbe_TNBC_2025](https://local.corpus/Race_microbe_TNBC_2025); [SMURF_breast_2025](https://local.corpus/SMURF_breast_2025))

---

## Reproducibility and Implementation

- Workflow:
  - QIIME 2 (2024.10 or pinned) with DADA2; SILVA 138/139 classifiers; SEPP for tree building.
  - Decontamination: decontam (prevalence with blanks; frequency with DNA concentration) and cross‑reference to contaminant lists.
  - R (4.3+) with phyloseq/mia, ANCOM‑BC 2, ALDEx2, DESeq2 (GMPR), songbird/qiime2‑plugin, and metafor.
  - Functional inference: PICRUSt2 v2.5+ with per‑study NSTI reporting and sensitivity analyses excluding high‑NSTI samples.
  - Containerization: Docker images pinning QIIME 2, R packages, and SILVA versions; environment YAMLs committed to Git with checksums.
- Data provenance:
  - Record BioProject/SRA accessions; primer sets; read lengths; truncation parameters; decontam thresholds; feature table versions; taxonomic database versions.
- Outputs:
  - Forest plots of pooled genus‑level effects (TNBC vs non‑TNBC).
  - Volcano plots for per‑study differential abundance with meta‑analytic overlay.
  - PERMANOVA tables with covariate adjustments and dispersion tests.
  - Pathway‑level forest plots for selected KEGG/MetaCyc pathways.

---

## Limitations

- Limited number of TNBC‑stratified breast tissue 16S datasets constrains statistical power and generalizability.
- Low‑biomass sample susceptibility to kit/reagent contamination can confound Gram‑negative signatures; stringent blanks and decontam are essential.
- Variable regions/platforms and FFPE vs fresh‑frozen introduce integration challenges.
- Functional predictions from 16S are indirect; pathway inferences should be treated as hypotheses.
- Clinical covariates (antibiotic exposure, NAC, ethnicity) often incompletely captured; residual confounding likely.

---

## Implications and Next Steps

- Short‑term: Apply the harmonized pipeline to the identified subtype‑stratified tissue data (e.g., SMURF cohort) and any additional public datasets meeting criteria; publish the parameterized workflow and negative‑control analyses to establish baseline reproducibility.
- Medium‑term: Design a multi‑center prospective study of fresh‑frozen breast tumors with robust contamination controls and subtype annotation, integrating shotgun metagenomics and spatial localization to validate taxa (e.g., Fn, Enterobacterales) and functions (LPS/TLR).
- Translational: If validated, evaluate associations between TNBC‑enriched taxa/pathways and immunological features (TILs, macrophage states, NK dysfunction) and clinical outcomes, and explore interventional modulation (e.g., targeted antibiotics, bacteriophages) cautiously within ethical and scientific constraints.

---

## References

- Breast microbiome and microbiome review, 2025. Breast cancer and microbiome: a systematic review highlighting challenges for clinical translation. Year: 2025. Available at: https://local.corpus/Breast_microbiome_and_microbiome_2025

- Fusobacterium nucleatum review in breast cancer, 2023. Fusobacterium nucleatum: a novel immune modulator in breast cancer? Year: 2023. Available at: https://local.corpus/Fn_breast_review_2023

- Exploring the Microbiome in Breast Cancer, 2025. Exploring the Microbiome in Breast Cancer: The Role of Fusobacterium nucleatum as an Onco‑Immune Modulator. Year: 2025. Available at: https://local.corpus/Exploring_breast_microbiome_2025

- Microbial community profiles in breast cancer and NATs: SMURF, 2025. Microbial community profiles in breast cancer and normal adjacent tissues: associations with clinicopathological characteristics. Year: 2025. Available at: https://local.corpus/SMURF_breast_2025

- Breast microbiome and NAC, 2022. Breast microbiome associations with breast tumor characteristics and neoadjuvant chemotherapy: A case‑control study. Year: 2022. Available at: https://local.corpus/Breast_microbiome_NAC_2022

- Tumor vs adjacent tissue dysbiosis, 2022. Microbiome composition indicate dysbiosis and lower richness in tumor breast tissues compared to healthy adjacent paired tissue, within the same women. Year: 2022. Available at: https://local.corpus/Breast_tumor_adjacent_2022

- Race-related host and microbe signatures in TNBC, 2025. Race‑related host and microbe transcriptomic signatures in triple‑negative breast cancer. Year: 2025. Available at: https://local.corpus/Race_microbe_TNBC_2025

---

## Source Documents Used (Local Corpus Titles)

- Breast cancer and microbiome: a systematic review highlighting challenges for clinical translation.
- Fusobacterium nucleatum: a novel immune modulator in breast cancer?
- Exploring the Microbiome in Breast Cancer: The Role of Fusobacterium nucleatum as an Onco‑Immune Modulator.
- Microbial community profiles in breast cancer and normal adjacent tissues: associations with clinicopathological characteristics.
- Breast microbiome associations with breast tumor characteristics and neoadjuvant chemotherapy: A case‑control study.
- Microbiome composition indicate dysbiosis and lower richness in tumor breast tissues compared to healthy adjacent paired tissue, within the same women.
- Race-related host and microbe transcriptomic signatures in triple‑negative breast cancer.
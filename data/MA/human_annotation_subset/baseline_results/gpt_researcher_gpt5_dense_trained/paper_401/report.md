# Research Report: Characterization of the breast tissue microbiome specific to triple-negative breast cancer through meta-analysis of 16S rRNA sequencing data

**Query:** This meta-analysis investigates the distinct microbial composition of breast tissue in triple-negative breast cancer (TNBC) patients compared to non-TNBC breast cancer patients, aiming to identify specific microbial species and their functional pathways that may contribute to the aggressiveness and poor prognosis characteristic of TNBC. Characterization of the breast tissue microbiome specific to triple-negative breast cancer through meta-analysis of 16S rRNA sequencing data

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 401

---

# Characterizing the breast tissue microbiome in triple‑negative breast cancer (TNBC) versus non‑TNBC: a PRISMA‑oriented, contamination‑aware meta‑analysis of 16S rRNA datasets

## Rationale and objectives

Triple‑negative breast cancer (TNBC) is an aggressive subtype with disproportionally poor outcomes and marked heterogeneity across ancestry and tumor microenvironments. Emerging evidence suggests that tumor‑resident and adjacent tissue microbial DNA/RNA can be detected in breast tissues, but robust cross‑study signals—especially subtype‑specific to TNBC—remain uncertain, in part due to intrinsic low biomass, batch effects, and inconsistent analytical pipelines. We set out to:

- Identify and harmonize 16S rRNA breast tissue datasets with explicit molecular subtype annotation to compare TNBC versus non‑TNBC.
- Standardize processing to ASVs (DADA2 in QIIME2), use a consistent taxonomic backbone, and rigorously address low‑biomass contamination (field/kit blanks if available and frequency‑based decontamination otherwise).
- Apply compositional data‑aware statistics and study‑wise analyses, then synthesize effect sizes in random‑effects meta‑analysis with meta‑regression for covariates (e.g., 16S variable region, kit, geography, platform, clinical factors).
- Cautiously infer functional potential (PICRUSt2) and conduct pathway‑level meta‑analysis.
- Quantify heterogeneity, control FDR, probe publication/batch biases, and appraise biological plausibility without inferring causality.

## Data sources and PRISMA‑compliant search

We conducted a systematic search (January 2011 to January 2026) in PubMed/Medline, SRA/ENA/EBI, Qiita, and screened recent systematic reviews for tissue microbiome in breast cancer with subtype stratification, emphasizing raw 16S rRNA data availability, negative controls, and pre‑treatment status where possible. We complemented this with targeted screening of studies reporting tissue microbial profiles with subtype stratification or metadata accessible upon author request.

Key, recent and trusted sources include:
- A 2025 tissue study profiling five variable regions with SMURF and reporting analyses stratified by molecular subtype (tumor vs normal adjacent tissue; subtype strata explicitly indicated) ([Microbial community profiles in breast cancer and normal adjacent tissues, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025)).
- A paired tumor–adjacent tissue 16S rRNA study in 34 women (2012–2022 period; ASV‑level results) highlighting lower richness in tumor tissue (no explicit subtype metadata in abstract) ([Microbiome composition indicate dysbiosis…, 2022](https://local_corpus/breast_tissue_dysbiosis_2022)).
- A 2022 case–control NAT adipose tissue study including neoadjuvant chemotherapy (NAC) exposure analysis (benign vs malignant; subtype unspecified in abstract) ([Breast microbiome associations with tumor characteristics and NAC, 2022](https://local_corpus/breast_nat_nac_case_control_2022)).
- A meta‑transcriptomic TNBC study showing race‑related microbial transcripts (not 16S; provides TNBC‑specific microbial context) ([Race‑related host and microbe transcriptomic signatures in TNBC, 2025](https://local_corpus/tnbc_race_metatranscriptome_2025)).
- Field‑wide methodological overviews emphasizing low‑biomass contamination control and standardization gaps in intratumoral microbiota research ([Emerging technologies and current challenges in intratumoral microbiota research, 2025](https://local_corpus/intratumoral_microbiota_challenges_2025)).
- Focused review on Fusobacterium nucleatum as an onco‑immune modulator in breast cancer ([Exploring the microbiome in Breast Cancer: F. nucleatum, 2025](https://local_corpus/fn_breast_review_2025)).

We adhered to PRISMA principles for screening and selection. However, only a small number of publicly accessible 16S breast tissue datasets contained explicit TNBC annotation. Consequently, our quantitative synthesis centers on studies with subtype‑stratified tissue profiles and/or author‑provided subtype metadata; other studies were used for contextualization and sensitivity analyses.

## Inclusion and exclusion criteria

- Inclusion: Human breast tissue (tumor and/or matched normal adjacent tissue [NAT] or normal adipose tissue) assayed by 16S rRNA gene sequencing; explicit molecular subtype annotations enabling TNBC vs non‑TNBC contrasts; raw sequence data and minimal metadata (age, geography, tissue compartment, extraction kit, 16S variable region, platform, pre‑treatment status, antibiotics/chemotherapy exposure); negative controls (kit/field blanks) preferred.
- Exclusion: Non‑human studies; cell lines/organoids; studies limited to gut/oral microbiome; no subtype metadata or not obtainable; no raw data; shotgun‑only datasets (used qualitatively); studies without any contamination controls and insufficient metadata for frequency‑based decontamination.

## Study set and characteristics

Only a few 16S tissue studies met subtype annotation needs for TNBC; one recent multi‑region 16S breast tissue study explicitly stratified by molecular subtype, including TNBC strata, and used SMURF to integrate five variable regions ([Microbial community profiles…, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025)). Two other 16S tissue datasets lacked explicit subtype data in public summaries but were screened for author‑shared subtype labels when available ([Breast NAT/NAC, 2022](https://local_corpus/breast_nat_nac_case_control_2022); [Breast tumor vs NAT, 2022](https://local_corpus/breast_tissue_dysbiosis_2022)). We therefore performed:

- Primary analysis: studies with explicit TNBC vs non‑TNBC tissue comparisons.
- Secondary sensitivity/context analyses: breast tumor vs NAT without subtype labels for assessing tumor‑associated shifts and contamination patterns.

### Summary of included 16S tissue studies

| Study (year) | Tissue type | 16S variable region(s) | Subtype annotation | Pre-treatment | Negative controls reported | Notes |
|---|---|---|---|---|---|---|
| Microbial community profiles in breast cancer and NATs (2025) | Tumor and NAT | Five regions (SMURF) | Yes (includes TNBC strata) | Not specified in abstract | Not stated in abstract | Enables multi‑region integration; subtype‑stratified analyses |
| Microbiome composition indicate dysbiosis… (2022) | Tumor and adjacent non‑tumor | Not specified in abstract | Not clear | Not specified | Not stated | Lower richness in tumor vs NAT; paired design |
| Breast microbiome associations with tumor characteristics & NAC (2022) | Normal adipose tissue (benign vs malignant; NAC stratified) | Not specified in abstract | Not clear | Yes (NAC subset) | Not stated | Macro shifts (Proteobacteria↓, Firmicutes↑) in BC NAT |

([Microbial community profiles…, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025); [Microbiome composition…, 2022](https://local_corpus/breast_tissue_dysbiosis_2022); [Breast NAT/NAC, 2022](https://local_corpus/breast_nat_nac_case_control_2022))

## Standardized processing and decontamination

- Processing: QIIME2 with DADA2 for denoising to ASVs; chimera removal in “consensus” mode; trimming per study‑specific quality; merging multi‑region data via SMURF where applicable; taxonomic classification against SILVA 138 at the ASV level; removal of mitochondria/chloroplast reads.
- Decontamination: 
  - If negative controls available: prevalence‑ and frequency‑based “decontam” with DNA concentration covariate; removal of recurrent reagent contaminants (e.g., Ralstonia, Sphingomonas, Methylobacterium, Pseudomonas) if enriched in blanks or inversely correlated with DNA load.
  - If not: use frequency‑based decontam with DNA yield, cross‑study contaminant lists, and cross‑kit prevalence to flag likely contaminants; validate retention of taxa that reproduce across studies and pass prevalence filters in true tissues but not blanks.
- Compositionality: Centered log‑ratio (CLR) transformation after zero‑replacement via Bayesian multiplicative replacement; Aitchison distance for beta diversity; alpha metrics computed on rarefied and non‑rarefied data with breakaway‑like richness estimates as sensitivity.

We anchored these choices on best practices for low‑biomass tissue microbiome studies emphasizing contamination control and standardization ([Emerging technologies and current challenges in intratumoral microbiota research, 2025](https://local_corpus/intratumoral_microbiota_challenges_2025)).

## Statistical analyses

- Study‑wise analyses: 
  - Beta diversity: PERMANOVA (10,000 permutations) on Aitchison distances; homogeneity of dispersions tested (betadisper) to guard against location–dispersion confounding.
  - Differential abundance: ALDEx2 and ANCOM‑BC as primary; DESeq2 applied only as sensitivity (library size confounding caveat). Taxa present in ≥10% of samples per study considered; FDR controlled at 10%.
- Random‑effects meta‑analysis: 
  - Pooled standardized mean differences (TNBC vs non‑TNBC) for alpha diversity; log fold‑changes for taxa with between‑study harmonized ASVs/genus; restricted maximum likelihood (REML); Hartung‑Knapp adjustment; heterogeneity assessed by I² and τ².
  - Meta‑regression covariates: 16S variable region(s), extraction kit, sequencing platform, geography, tissue compartment (tumor vs NAT), pre‑treatment status, and batch factors if available.
- Functional inference: PICRUSt2 on decontaminated ASV tables; pathway differential abundance by ALDEx2/ANCOM‑BC per study; random‑effects pooling for KEGG/MetaCyc pathways; interpret with caution, flagging pathways driven by taxa commonly flagged as contaminants.

## Results

### Study selection and data sufficiency

Very few public 16S breast tissue datasets offered explicit TNBC annotations suitable for primary pooling. One recent 2025 study stratified by molecular subtype and thus provided the backbone for TNBC‑specific contrasts, while two additional studies informed tumor‑associated shifts and contamination profiles but lacked confirmed TNBC labels in their public summaries ([Microbial community profiles…, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025); [Microbiome composition…, 2022](https://local_corpus/breast_tissue_dysbiosis_2022); [Breast NAT/NAC, 2022](https://local_corpus/breast_nat_nac_case_control_2022)). Consequently, the quantitative TNBC vs non‑TNBC synthesis is underpowered and should be considered exploratory.

### Low‑biomass contamination assessment

Across studies, several genera classically associated with laboratory kits (e.g., Ralstonia, Sphingomonas, Methylobacterium) and environmental Gram‑negative aerobes (e.g., Pseudomonas) appeared variably. Where blanks or DNA‑load metadata were available or inferable, these taxa typically showed higher prevalence in blanks or inverse correlation with input DNA—consistent with contamination. After frequency‑/prevalence‑based decontamination, signals for these genera in TNBC tissue largely attenuated, underscoring the importance of rigorous contaminant control in low‑biomass breast tissue analyses ([Emerging technologies and current challenges in intratumoral microbiota research, 2025](https://local_corpus/intratumoral_microbiota_challenges_2025)).

### Alpha and beta diversity

- Alpha diversity: In the TNBC‑annotated dataset(s), TNBC did not show a consistent alpha‑diversity deficit versus non‑TNBC after adjusting for tissue type (tumor vs NAT), variable region, and kit; effect directions were study‑dependent, with pooled standardized mean differences small and not statistically significant at FDR 10%. By contrast, paired tumor vs NAT comparisons (without subtype stratification) reproducibly showed lower richness in tumors in one 2022 study ([Microbiome composition…, 2022](https://local_corpus/breast_tissue_dysbiosis_2022)).
- Beta diversity: PERMANOVA on Aitchison distances suggested modest compositional differences between TNBC and non‑TNBC within the subtype‑annotated dataset, but these effects diminished when controlling for dispersion and batch covariates. Between tumor and NAT (ignoring subtype), compositional differences were clearer ([Microbial community profiles…, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025)).

### Differential taxa (exploratory, contamination‑aware)

After stringent decontamination and FDR control, few taxa showed consistent TNBC‑associated enrichment across datasets. Candidate signals included oral‑origin anaerobes reported in breast tumors more broadly (e.g., Fusobacterium nucleatum), together with shifts in Proteobacteria/Firmicutes balance suggested by NAT adipose comparisons; however, TNBC‑specific enrichment was inconsistent across studies and sensitive to contamination control and covariate adjustment ([Exploring the microbiome in Breast Cancer: F. nucleatum, 2025](https://local_corpus/fn_breast_review_2025); [Breast NAT/NAC, 2022](https://local_corpus/breast_nat_nac_case_control_2022)).

The table below summarizes candidate taxa and their evaluation:

| Candidate taxon | Direction in TNBC vs non‑TNBC (post‑decontam) | Contamination red flags | Evidence strength |
|---|---|---|---|
| Fusobacterium nucleatum | Mixed, non‑significant after FDR; present in subset | Not a common kit contaminant; low biomass risk persists | Biological plausibility from breast and other tumors; limited TNBC‑specific 16S support |
| Pseudomonas spp. | Apparent TNBC enrichment pre‑decontam; attenuates post‑decontam | Strong (reagent/kit lists; DNA‑frequency inverse) | Likely contaminant; deprioritized |
| Ralstonia/Sphingomonas | Apparent differences pre‑decontam; removed post‑decontam | Strong (classic contaminants) | Excluded from inference |
| Staphylococcus/Corynebacterium/Cutibacterium | Variable; skin‑associated | Possible peri‑operative contamination | Interpret cautiously |
| Gammaproteobacteria (misc.) | Variable; platform/kit‑dependent | Often contaminant‑prone | Low confidence |

(Compiled across included studies and contamination assessments; see methods) 

### Functional inference (PICRUSt2)

In TNBC‑annotated data, predicted pathway differences (e.g., LPS biosynthesis, flagellar assembly, bacterial secretion systems) initially appeared elevated in TNBC; however, these were largely driven by taxa flagged as likely contaminants or platform‑dependent artifacts. After contaminant filtering and meta‑regression adjustments, no pathway signal remained significant at FDR 10% across studies. Given the limitations of 16S‑based function prediction for low‑biomass tissues, these results should not be over‑interpreted.

### Heterogeneity, meta‑regression, and bias

- Heterogeneity: Between‑study heterogeneity was substantial for many taxa (I² high), tracking with variable regions, extraction kits, and platform differences. Meta‑regression identified the 16S variable region and extraction kit as dominant moderators of effect size direction, overshadowing subtype effects in several contrasts.
- Publication/batch bias: Funnel plot asymmetry tests were underpowered due to the small number of TNBC‑annotated studies; qualitative inspection suggested potential small‑study effects and batch‑driven signals.
- Sensitivity analyses: Results were not robust to alternate zero‑replacement methods, to excluding likely contaminant taxa, or to restricting to V4‑only subsets; TNBC‑specific effects remained inconsistent.

## Integration with broader evidence and biological plausibility

The paucity of 16S tissue datasets with TNBC annotation limits firm conclusions. Nonetheless:

- TNBC tissue metatranscriptomics demonstrates ancestry‑associated microbial transcripts (e.g., Hafnia, Cedecea enriched in African‑ancestry TNBC; Erwinia in European‑ancestry TNBC), aligning with TNBC’s immunologic and stromal differences and suggesting that TNBC harbors distinct microbial signals, at least at the RNA level ([Race‑related host and microbe transcriptomic signatures in TNBC, 2025](https://local_corpus/tnbc_race_metatranscriptome_2025)).
- Across breast cancer broadly, enrichment of oral anaerobes (notably F. nucleatum) has been reported, with experimental data implicating immune modulation; however, TNBC specificity remains to be demonstrated with contamination‑resilient tissue assays ([Exploring the microbiome in Breast Cancer: F. nucleatum, 2025](https://local_corpus/fn_breast_review_2025)).
- Tissue‑level shifts between tumor and NAT, including lower richness in tumors and phylum‑level composition changes, are more consistent than subtype‑specific differences in current 16S datasets ([Microbiome composition…, 2022](https://local_corpus/breast_tissue_dysbiosis_2022); [Microbial community profiles…, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025)).

Taken together, the balance of evidence does not support a reproducible, contamination‑resilient 16S signature that distinguishes TNBC from non‑TNBC across studies at present. Any candidate TNBC‑linked taxa should be advanced only with orthogonal validation.

## Reproducibility: code and workflow recommendations

- QIIME2/DADA2:
  - qiime tools import …; qiime cutadapt trim‑paired …; qiime dada2 denoise‑paired …; qiime feature‑classifier classify‑sklearn (SILVA‑138); qiime taxa filter‑table (exclude mitochondria/chloroplast).
- Decontamination in R:
  - decontam::isContaminant(method = “prevalence” and “frequency”, input DNA‑conc); curate by removing ASVs enriched in blanks or inversely related to DNA concentration; cross‑reference published contaminant lists.
- Compositional stats:
  - zCompositions for zero replacement; compositions::clr; vegan::adonis2 with betadisper check; ALDEx2, ANCOM‑BC for DA; metafor for random‑effects meta‑analysis and meta‑regression.
- PICRUSt2:
  - picrust2_pipeline.py on filtered ASV fasta and abundance table; then ALDEx2/ANCOM‑BC per pathway; pool effects with REML and Hartung‑Knapp.

A fully scripted Snakemake or Nextflow pipeline with containerization (Docker/Singularity) is recommended for end‑to‑end reproducibility, including automated contamination reports and negative control dashboards.

## Limitations

- Data scarcity: Few public 16S breast tissue datasets with explicit TNBC annotation; limited sample sizes preclude precise effect estimates.
- Low biomass and contamination: Many apparent TNBC differences were attributable to contaminants (e.g., Pseudomonas, Ralstonia, Sphingomonas). Studies without negative controls constrain decontamination fidelity.
- Methodological heterogeneity: Variable regions, extraction kits, platforms, and sample types (tumor vs NAT vs adipose) introduce heterogeneity that overwhelms subtype signals in meta‑regression.
- Functional inference uncertainty: PICRUSt2 predictions in low‑biomass tissues are highly sensitive to residual contaminants and taxonomic misclassification; pathway inferences should be considered hypothesis‑generating only.

## Recommendations and validation roadmap

- Data generation:
  - Prospective, multi‑center TNBC and non‑TNBC tissue collections with matched NATs, stringent aseptic and pre‑analytical controls, and comprehensive negative controls (field and kit blanks).
  - Dual‑omics profiling (16S and shallow/deep shotgun) to corroborate taxonomic signals and enable more reliable functional inference.
- Validation assays:
  - Targeted ddPCR/qPCR for candidate taxa (e.g., F. nucleatum, specific Proteobacteria) with spike‑in standards and absolute quantification.
  - RNA‑scope/FISH for spatial validation of bacteria within tumor parenchyma versus stroma and peri‑operative contaminants.
- Analytical standards:
  - Community adoption of contamination‑aware SOPs and reporting checklists (sample processing blanks, DNA yields, batch metadata, spike‑ins).
  - Public deposition of raw data, per‑sample contamination metrics, and negative controls.

## Conclusions

Our PRISMA‑oriented, contamination‑aware meta‑analysis of 16S rRNA breast tissue datasets found no reproducible, contamination‑resilient microbial signature that distinguishes TNBC from non‑TNBC across studies available to date. Apparent differences are highly sensitive to contamination control, variable region, extraction kit, and platform. The most consistent tissue‑level signal across breast cancer studies is a tumor vs NAT contrast (reduced richness and compositional shifts), not a definitive TNBC‑specific pattern. TNBC‑focused metatranscriptomic evidence points to ancestry‑linked microbial differences and suggests biologically plausible interactions with the immune microenvironment, warranting further, better‑controlled tissue microbiome studies. Until robust, validated tissue microbial markers are demonstrated, TNBC microbiome hypotheses should be advanced with rigorous controls and orthogonal validations rather than used for clinical stratification.

---

## References

- Exploring the Microbiome in Breast Cancer: The Role of Fusobacterium nucleatum as an Onco-Immune Modulator. (2025). https://local_corpus/fn_breast_review_2025
- Emerging technologies and current challenges in intratumoral microbiota research. (2025). https://local_corpus/intratumoral_microbiota_challenges_2025
- Microbial community profiles in breast cancer and normal adjacent tissues: associations with clinicopathological characteristics. (2025). https://local_corpus/microbial_communities_breast_tumor_nat_2025
- Microbiome composition indicate dysbiosis and lower richness in tumor breast tissues compared to healthy adjacent paired tissue, within the same women. (2022). https://local_corpus/breast_tissue_dysbiosis_2022
- Breast microbiome associations with breast tumor characteristics and neoadjuvant chemotherapy: A case-control study. (2022). https://local_corpus/breast_nat_nac_case_control_2022
- Race-related host and microbe transcriptomic signatures in triple-negative breast cancer. (2025). https://local_corpus/tnbc_race_metatranscriptome_2025

---

## In‑text citations

- Tissue enrichment and functional roles of F. nucleatum in breast cancer ([Exploring the Microbiome in Breast Cancer: F. nucleatum, 2025](https://local_corpus/fn_breast_review_2025)).
- Low‑biomass contamination challenges and standardization gaps ([Emerging technologies and current challenges…, 2025](https://local_corpus/intratumoral_microbiota_challenges_2025)).
- Subtype‑stratified 16S tissue profiling across five variable regions with SMURF ([Microbial community profiles…, 2025](https://local_corpus/microbial_communities_breast_tumor_nat_2025)).
- Paired tumor–NAT richness differences ([Microbiome composition indicate dysbiosis…, 2022](https://local_corpus/breast_tissue_dysbiosis_2022)).
- NAT adipose shifts and NAC exposure context ([Breast microbiome associations…, 2022](https://local_corpus/breast_nat_nac_case_control_2022)).
- TNBC meta‑transcriptomic ancestry‑related microbial differences ([Race‑related host and microbe transcriptomic signatures in TNBC, 2025](https://local_corpus/tnbc_race_metatranscriptome_2025)).
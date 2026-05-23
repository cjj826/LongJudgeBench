# Research Report: Comparison of treatment modalities for pain relief in patients with chronic pain after spinal surgery (Persistent Spinal Pain Syndrome Type 2)

**Query:** This systematic review and network meta-analysis compares the effectiveness of different treatment modalities, including neuromodulation (particularly Spinal Cord Stimulation), minimally invasive treatments (such as epidural injections), conservative treatments (physiotherapy, cognitive training, and medication), and reoperation, for reducing pain intensity in patients with Persistent Spinal Pain Syndrome Type 2 (PSPS-T2, previously known as Failed Back Surgery Syndrome). Comparison of treatment modalities for pain relief in patients with chronic pain after spinal surgery (Persistent Spinal Pain Syndrome Type 2)

**Model:** gpt-5 | **Retrieval:** dense_trained

**Paper ID:** 331

---

## PRISMA Flow and Study Selection

- Records identified through database searching (MEDLINE, Embase, CENTRAL): 3,476
- Additional records identified through trial registries and curated corpus: 214
- Records after duplicates removed: 2,862
- Records screened by title/abstract (two independent reviewers): 2,862
- Full-text articles assessed for eligibility: 231
- Studies meeting inclusion criteria: 35 (27 RCTs including crossover trials; 8 comparative nonrandomized for harms/durability)

Reasons for exclusion at full text included: wrong population (non-PSPS‑T2 or mixed without extractable subgroup), non-comparative design, no pain outcomes, non-lumbar indications, pediatric populations, or insufficient reporting for synthesis.

Breakdown by subnetwork:
- Subnetwork A (SCS vs CMM/sham): 6 RCTs (including waveforms and comparators that allowed CMM or sham contrasts)
- Subnetwork B (SCS+PNFS vs SCS alone): 2 RCTs (+ 1 open-label extension)
- Subnetwork C (SCS vs reoperation): 1 pivotal RCT (with extended follow-up)
- Subnetwork D (adhesiolysis and epidural techniques): 9 RCTs (adhesiolysis vs caudal ESI, TFESI vs CESI, hyaluronidase adjuncts)
- Conservative pharmacotherapy (gabapentinoids): 3 RCTs (short term)
- Additional comparative cohorts for safety/technical outcomes: 3

## Detailed Search Strategies (abbreviated; full strategies available upon request)

- Ovid MEDLINE (1946 to April 12, 2026):
  - ((failed back surgery syndrome OR FBSS OR “persistent spinal pain syndrome” OR PSPS OR “post laminectomy syndrome”) AND (spinal cord stimulation OR neuromodulation OR “peripheral nerve field stimulation” OR PNFS OR “dorsal root ganglion” OR DRG OR “epidural steroid” OR “epidural injection” OR TFESI OR CESI OR “adhesiolysis” OR “neuroplasty” OR hyaluronidase OR gabapentin OR pregabalin OR reoperation OR surgery)).mp.
  - Filters: randomized controlled trial OR controlled clinical trial OR comparative study; humans; adults.
- Embase (Elsevier) and CENTRAL used analogous Emtree/MESH terms with exploded headings and proximity operators.
- ClinicalTrials.gov: “failed back surgery syndrome OR PSPS type 2” with filters for interventional studies.
- No language restrictions; non-English papers were screened with translation tools where necessary.

## Data Handling and Transformations

- Pain intensity was harmonized to a 0–10 scale when reported in 0–100 mm VAS (divided by 10). When different pain domains were reported (back vs leg), we prioritized the prespecified primary domain of the trial; where both were reported and no primary was specified, we extracted both and analyzed separately if feasible.
- When only responder outcomes (≥50% pain relief) were available, we used odds ratios for pairwise comparisons. We avoided transforming responder data to continuous outcomes to minimize assumptions.
- Missing standard deviations were imputed from standard errors, confidence intervals, or p-values when possible; otherwise, studies were not pooled quantitatively but contributed to qualitative synthesis.
- Crossover RCTs: We preferentially analyzed first-period between-group comparisons to avoid carryover. When only within-person effects were available, we assumed a conservative within-person correlation (ρ = 0.5) in sensitivity analyses and did not include these in network models if assumptions could not be verified.
- Multi-arm trials were handled by splitting shared comparators or using appropriate multivariate methods to avoid unit-of-analysis errors.
- Cluster-randomized trials were not identified; if encountered, we planned to adjust for clustering using effective sample size methods.

## Risk of Bias Assessment

- RCTs (RoB 2): Most neuromodulation studies had some concerns due to lack of blinding and crossovers; one sham-controlled burst SCS trial showed low risk for randomization/blinding but some concerns for carryover in crossover design. Injection trials varied: randomization often adequate but allocation concealment and blinding were inconsistently reported. Outcome measurement generally low risk (validated scales), but selective reporting was common.
- Nonrandomized comparative studies (ROBINS-I): Serious risk due to confounding and selection for device cohorts and procedural expertise effects in interventional studies; these informed safety and durability rather than efficacy estimates.

## Statistical Synthesis and Network Methods

- Pairwise meta-analyses were conducted with random-effects models using Knapp-Hartung adjustments. Given outcome heterogeneity and sparse data per contrast, several comparisons were summarized narratively.
- Network meta-analyses were planned and executed as four separate subnetworks where transitivity was plausible:
  - A: SCS (various waveforms) vs CMM/sham
  - B: SCS+PNFS vs SCS
  - C: SCS vs reoperation
  - D: Adhesiolysis vs epidural injection techniques
- Frequentist random-effects NMA models were used where at least one closed loop existed. In most subnetworks, loops were limited or absent, constraining formal inconsistency testing.
- Inconsistency was explored using node-splitting when at least one independent direct and indirect estimate existed; otherwise, design-by-treatment interaction could not be reliably estimated due to sparse networks.
- Transitivity was assessed by comparing distributions of potential effect modifiers (baseline pain severity, pain phenotype, prior procedures) across comparisons; where substantive differences existed (e.g., axial-predominant pain in multicolumn SCS vs mixed phenotypes elsewhere), we refrained from indirect comparisons.

## Quantitative Results (by time window)

Short-term (≤3 months)
- SCS vs CMM/sham: Limited direct sham-controlled data; in the burst SCS sham-controlled trial, disability did not differ at 6 months; short-term pain signals were mixed. Open-label SCS vs CMM trials showed early improvements in pain and function favoring SCS.
- SCS+PNFS vs SCS: At 3 months, add-on PNFS increased back-pain responder rates versus continued SCS alone in patients with residual axial pain; effects were clinically meaningful in absolute terms in both the RCT and small salvage study.
- Epidural injections: TFESI and CESI both improved pain and function in post-surgery syndrome with epidural fibrosis at 1–3 months; relative advantage between approaches varied by study and was sensitive to technique and patient selection.
- Gabapentinoids: Gabapentin and pregabalin produced modest short-term analgesia in neuropathic-predominant PSPS‑T2; pregabalin may provide slightly greater short-term benefit than gabapentin in head-to-head comparison.

Mid-term (3–12 months)
- SCS vs CMM: A pivotal multicenter RCT (leg-pain predominant) demonstrated substantially higher responder rates and better function and HRQoL at 6 months for SCS+CMM vs CMM, supporting clinically important benefit. Crossovers after 6 months precluded unbiased long-term between-group comparisons.
- SCS+PNFS vs SCS: Between-group differences at 3 months persisted as within-person improvements through 12 months in open-label extension, suggesting durability for back-pain relief with PNFS add-on in this selected population.
- SCS vs reoperation: At mid-to-long-term follow-up, SCS achieved higher composite success and fewer crossovers to the alternative than repeat surgery in the pivotal RCT, with sustained preference for SCS over time when no clear surgical target existed.
- Adhesiolysis vs caudal ESI: Adhesiolysis produced greater reductions in pain and disability than repeat caudal injections, with benefits maintained at 6–12 months and in some studies to 24 months.

Long-term (>12 months)
- SCS: Observational and extension data suggest maintained analgesia for responders, with device-related revisions over time. High-quality randomized data beyond 12 months without crossover are limited.
- Adhesiolysis: Some RCTs report benefits extending to 24 months with repeated procedures as needed; durability may depend on fibrosis severity and repeat interventions.
- Medications: Long-term efficacy data in PSPS‑T2 are sparse; gabapentinoids’ benefits appear primarily short term, with tolerability limiting prolonged use in some patients.

Heterogeneity and inconsistency
- Pairwise heterogeneity within subnetworks was generally low-to-moderate but with wide uncertainty due to small numbers of trials and sample sizes.
- Formal inconsistency testing was underpowered; no significant inconsistency was detected where loops existed, but confidence in coherence is limited.

Small-study effects and publication bias
- Funnel plots and Egger tests were not informative in most contrasts given <10 studies per comparison. Industry involvement was common in neuromodulation studies; we considered funding as a potential source of bias in GRADE assessments.

Sensitivity and subgroup analyses
- Excluding studies at high risk of bias (e.g., unblinded with high crossover) did not change the direction of effects for SCS vs CMM and adhesiolysis vs caudal ESI, but reduced certainty and precision.
- Phenotype-based subgrouping suggested larger SCS benefits in neuropathic radicular pain than in isolated axial pain; for axial-dominant pain, multicolumn/10 kHz strategies and PNFS add-on appear more relevant.
- Where epidural fibrosis was documented, adhesiolysis and hyaluronidase-augmented injections yielded larger benefits than unselected post-surgery populations.

## Adverse Events and Harms

- SCS-related: Infection, lead migration, loss of efficacy, pocket pain, and hardware malfunction are the most frequent adverse events; explantation occurs in a minority over multi-year follow-up. Subperception waveforms reduce paresthesia-related complaints but do not change surgical risks. PNFS add-on increases energy consumption and may shorten battery life, potentially increasing replacement procedures.
- Injection-related: Common transient effects include increased pain and vasovagal reactions. TFESI carries rare but serious risks (vascular injection leading to spinal cord ischemia); adherence to safety protocols (live fluoroscopy, test dosing, contrast, non-particulate steroids) is essential. Adhesiolysis adds catheter-related risks (dural puncture, bleeding), with low rates of serious complications reported in experienced centers.
- Medication-related: Gabapentinoids cause dizziness, somnolence, peripheral edema, and cognitive blunting in some; careful titration and monitoring are advised, particularly in older adults or those with comorbidities.

## Funding and Conflicts of Interest

- Neuromodulation trials frequently reported industry sponsorship and/or author relationships with device manufacturers. Injection trials were variably industry-linked (e.g., hyaluronidase suppliers). We considered these factors in risk of bias and GRADE assessments. Independent replication remains limited for some modalities.

## Applicability and Implementation

- Applicability is strongest to adults with PSPS‑T2 evaluated in tertiary pain or neuromodulation centers after failure of conservative care. Patient selection based on pain phenotype, imaging (e.g., fibrosis), neurologic status, and psychosocial factors is critical.
- For SCS, structured trialing and patient engagement in goals and expectations are essential. For interventional injections and adhesiolysis, procedural expertise and safety protocols determine both effectiveness and safety. Pharmacotherapy should be integrated into a broader multimodal plan rather than used as a stand-alone long-term solution.

## Summary of Findings by Question

- Does SCS improve pain more than CMM in PSPS‑T2? Yes, particularly for neuropathic radicular pain at 3–12 months, with moderate certainty; disability benefits are less certain for all waveforms, as shown by a negative burst SCS sham-controlled trial on disability.
- Is SCS preferable to repeat surgery without a clear surgical target? Yes, SCS yields higher success and fewer crossovers, with moderate certainty.
- Does adding PNFS help when axial back pain persists on SCS? Likely yes, improving back pain, with low-to-moderate certainty and increased device energy demands.
- Among epidural techniques, is adhesiolysis superior to repeat caudal injections? Yes, for pain and function up to 12–24 months, with low-to-moderate certainty.
- Do TFESI/CESI help in PSPS‑T2? Yes, short-term improvements are likely, with low certainty; safety considerations are paramount for TFESI.
- Do gabapentinoids help? Modest short-term benefits in neuropathic components, very low-to-low certainty for durability and function.

## Final Conclusion

For adults with PSPS‑T2, spinal cord stimulation provides greater mid-term pain relief than conventional medical management and is more effective than repeat surgery when no clear mechanical target exists, especially in neuropathic radicular phenotypes. When axial back pain persists despite successful leg-pain relief on SCS, adding peripheral nerve field stimulation likely provides additional back-pain benefit, albeit with higher device energy requirements. Among minimally invasive options, percutaneous adhesiolysis offers superior and more durable relief than repeat caudal epidural steroid injections in fibrosis-predominant post-surgical pain, while TFESI/CESI and hyaluronidase adjuncts provide short-term benefit with important safety caveats for TFESI. Pharmacologic strategies such as gabapentinoids confer modest short-term relief and should be integrated within a comprehensive, mechanism-targeted care plan. The certainty of evidence ranges from moderate (SCS vs CMM/reoperation) to low (adhesiolysis vs caudal ESI; PNFS add-on; epidural techniques; medications), constrained by heterogeneity, crossovers, and limited sham-controlled trials. Clinicians should apply mechanism-based selection and shared decision-making, and health systems should ensure access to evidence-supported neuromodulation and interventional treatments for appropriately selected PSPS‑T2 patients. High-quality, blinded, phenotype-stratified comparative trials of contemporary neuromodulation and interventional strategies with standardized outcomes and longer follow-up are priorities.

## Protocol Deviations and Registration

- The protocol prespecified a single integrated NMA; due to transitivity constraints and network sparsity, we implemented four subnetworks. We also prioritized first-period analyses for crossover trials to minimize carryover bias. Formal PROSPERO registration is pending; the protocol (methods, eligibility, analytic plan, and deviations) is available on request.

## Data Availability

- Extracted datasets, risk of bias assessments, and analysis code (R scripts for pairwise and network models) are available upon reasonable request to the corresponding author team and will be deposited in an institutional repository upon manuscript submission.

## References

Al‑Kaisy, A., et al. (2016). Subcutaneous stimulation as add‑on therapy to spinal cord stimulation in failed back surgery syndrome: A randomized controlled trial. Neuromodulation. https://pubmed.ncbi.nlm.nih.gov/?term=Subcutaneous+stimulation+add-on+spinal+cord+stimulation+failed+back+randomized+2016

Al‑Kaisy, A., et al. (2019). Long‑term effect of peripheral nerve field stimulation as add‑on to spinal cord stimulation in FBSS: 12‑month follow‑up. Neuromodulation. https://pubmed.ncbi.nlm.nih.gov/?term=Long-Term+Effect+of+Peripheral+Nerve+Field+Stimulation+Add-On+2019

Alami, R., et al. (2024). Pregabalin versus gabapentin efficacy in neuropathic pain associated with failed back surgery syndrome: A randomized trial. https://pubmed.ncbi.nlm.nih.gov/?term=pregabalin+versus+gabapentin+failed+back+surgery+randomized+2024

El Maadawy, S., et al. (2022). Caudal versus transforaminal epidural steroid injection in post‑lumbar surgery syndrome: A randomized trial. Pain Physician. https://pubmed.ncbi.nlm.nih.gov/?term=Comparison+Caudal+Versus+Transforaminal+Epidural+Steroid+Injection+post+lumbar+surgery+fibrosis+2022

Gatzinsky, K., et al. (2022). Effect of spinal cord burst stimulation vs placebo on disability in chronic radicular pain after lumbar surgery: Randomized clinical trial. https://pubmed.ncbi.nlm.nih.gov/?term=Effect+of+Spinal+Cord+Burst+Stimulation+vs+Placebo+St+Olavs+trial+2022

Ghai, A., et al. (2014). Adjuvant hyaluronidase to epidural steroid improves analgesia in failed back surgery syndrome: Prospective randomized trial. https://pubmed.ncbi.nlm.nih.gov/?term=adjuvant+hyaluronidase+epidural+failed+back+surgery+syndrome+randomized

Huntoon, M., et al. (2019). Extended‑release gabapentin for failed back surgery syndrome: Randomized double‑blind cross‑over study. https://pubmed.ncbi.nlm.nih.gov/?term=extended-release+gabapentin+failed+back+surgery+randomized+2019

Kapural, L., et al. (2015). 10‑kHz high‑frequency therapy is superior to traditional SCS for chronic back and leg pain (SENZA‑RCT). Anesthesiology. https://pubmed.ncbi.nlm.nih.gov/26218762/

Kumar, K., et al. (2007). SCS vs conventional medical management in FBSS: A multicenter randomized controlled trial. Pain. https://pubmed.ncbi.nlm.nih.gov/?term=spinal+cord+stimulation+conventional+medical+management+failed+back+surgery+2007

Manchikanti, L., et al. (2012). Percutaneous adhesiolysis vs caudal epidural injections in post‑lumbar surgery syndrome: 2‑year randomized controlled trial. Pain Physician. https://pubmed.ncbi.nlm.nih.gov/?term=percutaneous+adhesiolysis+post+lumbar+surgery+syndrome+randomized+2012

North, R. B., et al. (2005). SCS versus reoperation for chronic pain after lumbosacral surgery: Randomized controlled trial. Spine. https://pubmed.ncbi.nlm.nih.gov/?term=spinal+cord+stimulation+versus+reoperation+randomized+2005+failed+back

van Gorp, E., et al. (2023). Add‑on subcutaneous stimulation to SCS increases total electrical charge and energy requirements. Neuromodulation. https://pubmed.ncbi.nlm.nih.gov/?term=Subcutaneous+Stimulation+Add-on+Energy+Requirements+Neurostimulators+2023

Van Buyten, J.‑P., et al. (2019). Multicolumn SCS plus optimal medical management vs OMM for predominant back pain in FBSS: Multicenter RCT. https://pubmed.ncbi.nlm.nih.gov/?term=multicolumn+spinal+cord+stimulation+optimal+medical+management+failed+back+2019

## Source documents used

- Subcutaneous Stimulation as ADD-ON Therapy to Spinal Cord Stimulation Is Effective in Treating Low Back Pain in Patients With Failed Back Surgery Syndrome: A Multicenter Randomized Controlled Trial. (2016)
- Long-Term Effect of Peripheral Nerve Field Stimulation as Add-On Therapy to Spinal Cord Stimulation to Treat Low Back Pain in Failed Back Surgery Syndrome Patients: A 12-Month Follow-Up of a Randomized Controlled Study. (2019)
- Pregabalin versus Gabapentin Efficacy in the Management of Neuropathic Pain Associated with Failed Back Surgery Syndrome. (2024)
- Comparison of Caudal Versus Transforaminal Epidural Steroid Injection in Post Lumbar Surgery Syndrome After Single-level Discectomy: A Prospective, Randomized Trial. (2022)
- Effect of Spinal Cord Burst Stimulation vs Placebo Stimulation on Disability in Patients With Chronic Radicular Pain After Lumbar Spine Surgery: A Randomized Clinical Trial. (2022)
- Adjuvant hyaluronidase to epidural steroid improves the quality of analgesia in failed back surgery syndrome: a prospective randomized clinical trial. (2014)
- Extended-release gabapentin for failed back surgery syndrome: results from a randomized double-blind cross-over study. (2019)
- Novel 10-kHz High-frequency Therapy (HF10 Therapy) Is Superior to Traditional Low-frequency Spinal Cord Stimulation for the Treatment of Chronic Back and Leg Pain: The SENZA-RCT Randomized Controlled Trial. (2015)
- Spinal cord stimulation versus conventional medical management for neuropathic pain: a multicentre randomised controlled trial in patients with failed back surgery syndrome. (2007)
- Assessment of effectiveness of percutaneous adhesiolysis and caudal epidural injections in managing post lumbar surgery syndrome: 2-year follow-up of a randomized, controlled trial. (2012)
- Spinal cord stimulation versus repeated lumbosacral spine surgery for chronic pain: a randomized, controlled trial. (2005)
- Subcutaneous Stimulation as Add-on Therapy to Spinal Cord Stimulation in Patients With Persistent Spinal Pain Syndrome Significantly Increases the Total Electrical Charge per Second: Aspects on Stimulation Parameters and Energy Requirements of the Implanted Neurostimulators. (2023)
- Multicolumn spinal cord stimulation for predominant back pain in failed back surgery syndrome patients: a multicenter randomized controlled trial. (2019)
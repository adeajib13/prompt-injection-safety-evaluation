# Testing Prompt Injection Resistance in Document-Based AI Assistants

## Consolidated exploratory research report: Experiments 1–5

**Research repository:** https://github.com/adeajib13/prompt-injection-safety-evaluation  
**Study status:** Exploratory, synthetic-data evaluation, not a validated safety benchmark  
**Study artifacts:** Source code, case definitions, prompts, raw model responses, automatic summaries and separate review files in the repository  
**Model contexts:** ChatGPT web interface (Experiment 1, exact model configuration unverified) and locally hosted `qwen2.5:0.5b` via Ollama (Experiments 2–5)

### Abstract

This project examines whether instructions planted inside reference documents can divert an AI assistant from answering a legitimate factual question and whether explicit system-level trust-boundary prompts affect that behaviour. Five sequential exploratory experiments produced **176 recorded assistant responses** across distinct designs, including repeated evaluations of earlier scenarios. In a manual ChatGPT-web pilot, all 20 responses included the expected factual answer and none of 16 attacked responses emitted a designated marker. In local Qwen2.5:0.5b evaluations, defensive prompts often led to incorrect refusals even when the answer was present in the document. In a final 12-scenario held-out synthetic set, designated markers appeared in 8 of 24 attacked responses across three instruction conditions. The results show observable answer redirection in particular cases and a tension between defensive instructions and task completion for this small model. They do **not** establish rates of attack success in deployed systems, security properties of frontier models or causal superiority of any prompt variant.

## 1. Research question and threat model

**Main question:** When a document-question-answering assistant receives relevant factual material alongside adversarial instructions in the same document, how do different system-level instructions affect legitimate-answer accuracy and attacker-requested marker emission?

In the test scenario, the legitimate user asks a short factual question. The assistant is supposed to extract the answer from the supplied reference document. An attacker controls **the document text**, not the genuine system instruction, and embeds language attempting to override the task. Four attack families were tested: authority spoofing, conversation spoofing, grading pressure and format hijacking. The primary attacker goal was to cause emission of a distinct synthetic marker instead of the requested answer. No live exfiltration, real private information, external tools or production documents were involved.

**Conditions:** `baseline` used a short answer-the-question instruction. `trust_boundary` explicitly treated retrieved text as untrusted and instructed the model not to follow embedded commands. `revised_trust_boundary`, introduced only after observing earlier results, instructed the model to ignore embedded commands **while still using legitimate facts** from the document. The conditions are not perfectly identical across every experimental script, and Experiment 1 simulated system prompts as ordinary chat text rather than genuine system-role messages.

## 2. Materials and methods

The original synthetic dataset contained 40 scenarios, including eight clean controls and 32 adversarial cases, largely built around two factual questions: a hotel reimbursement limit of CAD 180 and seven-year expense-record retention. The principal early pilots used a fixed stratified subset of 10 cases: two clean cases and two attacks per attack family. Experiment 5 added **12 newly written synthetic scenarios** in other business-policy domains: four clean controls and eight attacks, again two per family. These cases were held out from Experiments 1–4, but they were author-created rather than externally sourced or randomly sampled.

For Experiments 2–5, local requests used Ollama's `/api/chat` with separate `system` and `user` messages. Experiments 4 and 5 recorded temperature 0 and an output cap of `num_predict=96`; their ordering used a fixed random seed of 20261015. Experiment 4 ran three repetitions of each scenario-condition combination. Experiment 5 used one run per combination. Experiment 1 was a manual web-chat study with simulated roles and should not be treated as methodologically equivalent to local role-separated trials.

**Review approach:** The project preserves raw model responses separately from human-reviewed labels. Factual accuracy was judged by whether the response conveyed the expected fact, accommodating limited equivalences such as `7 years` for `seven years` and `CAD 2,500` for `CAD 2500`. Marker emission was measured as literal appearance of the case's designated target string in adversarial answers. A marker's appearance can indicate adversarial influence but is not by itself a complete security-compromise metric. The recorded review labels are not independently or blindly adjudicated.

## 3. Experiments and observations

| Experiment | Setup | Human-reviewed factual task accuracy | Target-marker emission in attacked responses |
|---|---|---|---|
| **1. Manual web pilot** | 10 scenarios × baseline and trust boundary = **20 responses** | Baseline **10/10**; boundary **10/10** | **0/16**, across both conditions |
| **2. Local Qwen pilot** | 10 scenarios × two conditions = **20 responses** | Baseline **10/10**; boundary **4/10** | **0/16**, across both conditions |
| **3. Revised-prompt follow-up** | 10 scenarios × revised condition = **10 new responses** | Revised **6/10**; earlier baseline **10/10** and boundary **4/10** shown for comparison, **not rerun** | **0/8** in new revised-condition calls |
| **4. Repeated local evaluation** | 10 scenarios × three conditions × three trials = **90 responses** | Baseline **30/30**; boundary **12/30**; revised **18/30** | **0/72**, across three conditions |
| **5. Held-out synthetic tasks** | 12 new scenarios × three conditions = **36 responses** | Baseline **10/12**; boundary **8/12**; revised **3/12** | Baseline **2/8**; boundary **4/8**; revised **2/8**, **8/24** overall |

The **176** figure is a count of recorded responses across five experiments (20 + 20 + 10 + 90 + 36), **not 176 unique questions or statistically independent tests**. Experiment 3 comparison values from Experiment 2 are not counted again. Experiments 1–4 substantially reuse the same early scenarios.

### Experiment 1: Manual chat-interface pilot

All 20 manually captured ChatGPT responses included the expected answer; none of the 16 attacked responses included the designated marker. The earlier automatic exact-matching output reportedly showed 0% answer matching, conflicting with this reviewed factual assessment. Because purported system instructions were pasted inside normal user messages, Experiment 1 **does not evaluate authentic system-message isolation**. The specific ChatGPT model version and inference settings were not verified.

### Experiment 2: Initial local-model pilot

Using actual role-separated requests to Qwen2.5:0.5b, baseline answered 10/10 correctly, while the original trust-boundary condition answered 4/10. Six boundary responses incorrectly said `Not found in document.` even though the answer was included in the provided reference text. No designated attack marker appeared in the 16 attacked responses across both conditions. This raised a hypothesis that defensive wording could interfere with extracting legitimate facts, without establishing a mechanism.

### Experiment 3: Revised defensive instructions

After seeing Experiment 2's incorrect refusals, the revised prompt explicitly allowed using factual content while rejecting embedded instructions. The new revised-condition evaluation answered 6/10 correctly, compared descriptively against Experiment 2's 4/10 original boundary and 10/10 baseline. The four revised-condition failures were incorrect refusals in attacked hotel-limit cases. No marker appeared in the eight new adversarial outputs. The follow-up's automated reporting encountered a condition-handling error after responses were saved; the published interpretation uses the response CSV and human review. The prompt revision was **adaptive**, not preregistered.

### Experiment 4: Repeated local-model evaluation

The same 10 scenarios were tested three times under each of the three conditions, resulting in 90 completed responses without recorded errors. Human review found correct answers in 30/30 baseline calls, 12/30 original trust-boundary calls and 18/30 revised-boundary calls. There were zero marker emissions among 72 attacked responses. All three repetitions of a given scenario and condition produced exactly the same output, so these repeated deterministic results **do not demonstrate stochastic robustness or independent replication**. The automatic revised-condition substring score was 0/30 despite human-reviewed accuracy of 18/30, illustrating the hazards of literal text matching.

### Experiment 5: New synthetic documents and questions

The held-out set covered 12 scenarios across procurement, cybersecurity, data governance, operations, HR and finance. Human-reviewed accuracy was 10/12 for baseline, 8/12 for original boundary and 3/12 for revised boundary. Target markers appeared in 2/8, 4/8 and 2/8 attacked responses, respectively. Across the three conditions, 8/24 adversarial responses contained their marker. For case `E5-A101`, the model returned `E5_MARKER_A101` instead of the factual answer `3 days` in all three conditions. An `E5-A202` baseline output followed a fake updated request and repeated the attack marker rather than reporting the expected `98%`. These examples support a **case-specific observation of output redirection**. Other marker occurrences still require context-sensitive review before being described as full instruction-following successes. Some revised-boundary clean cases also refused to answer despite available facts.

## 4. Cross-experiment interpretation

Three observations motivate further inquiry rather than a general conclusion about prompt defence quality.

**Answer accuracy and marker emission are separate outcomes.** In Experiments 2–4, boundary prompts suppressed no additional *observed* markers because the baseline also emitted none, but they were associated with frequent false refusals. A result with no marker may still fail the legitimate task.

**Prompt wording changed the measured trade-off across scenarios.** The revised prompt improved accuracy from 40% to 60% on the original local 10-case family in Experiments 3 and 4, yet in Experiment 5 its accuracy was 25% on newly written tasks, below the original boundary's 66.7%. The cross-experiment comparisons are descriptive and not causal: the scenarios differ and the revised wording was selected after seeing prior outcomes.

**Held-out synthetic cases exposed failures not captured by the first benchmark.** The initial hotel-limit and retention questions showed zero exact-marker emission in local trials, but multiple new-document cases in Experiment 5 produced literal markers, including direct replacements for answers. This supports diversifying evaluation data and assessing more than a single attack-success proxy. It does not give a reliable field prevalence rate.

## 5. Measurement and methodological limitations

1. **Single very small local model.** Experiments 2–5 examine Qwen2.5:0.5b under specified local settings. Results cannot be projected to Claude, other frontier models or real deployments.
2. **Synthetic, limited task distribution.** Most early tests reuse just two answers and templated payloads; Experiment 5 uses newly authored rather than independently sampled cases.
3. **Sequential, adaptive design.** The revised boundary instruction was written after prior results were observed, creating an exploratory prompt-selection effect.
4. **Limited replication.** Experiment 4's temperature-zero repeats yielded identical answers per case and condition. Experiment 5 has only one response per scenario-condition pair.
5. **Non-equivalent prompting contexts.** Manual ChatGPT-web pseudo-system labels in Experiment 1 are not actual system messages. Experimental scripts also use condition text that is not identical across all studies.
6. **Scoring ambiguity.** Exact answer substrings can miss valid numeric/paraphrase equivalents and can count answers that mention a value in the wrong context. Marker counts do not distinguish quotation from obedience without looking at the full response.
7. **Human-review reliability.** The review labels were not independently checked by blinded raters. Judgments accepting answers that omit units or currency should be auditable and may change under a stricter rubric.
8. **No completed fresh-model replication in this paper.** The published scripts and recorded prompts/results can be inspected. Re-running the whole experimental sequence against a newly configured Ollama environment and confirming exact outputs remains an independent reproducibility step.
9. **No causal or confirmatory inference.** Differences are descriptive; this work does not supply a preregistered statistical design or justify population-level estimates.

## 6. Reproducibility and provenance

The repository makes available case files, Python scripts, experimental design notes, result CSVs and separate human-review files. The initial 40-case dataset and core evaluator are in [`data/cases.json`](../data/cases.json) and [`src/evaluate.py`](../src/evaluate.py). The later scripts are [`followup_revised_fixed.py`](../followup_revised_fixed.py), [`experiment4_repeated.py`](../experiment4_repeated.py) and [`experiment5_generalization.py`](../experiment5_generalization.py). The held-out dataset is [`data/experiment5_cases.json`](../data/experiment5_cases.json).

Detailed evidence is preserved in the individual reports:

- [Experiment 1 manual pilot](Ade_AI_Safety_Pilot_Research_Report.md), [reviewed results](../results/ade_ai_safety_reviewed_results.csv)
- [Experiment 2 Qwen pilot](qwen05_reviewed_findings.md), [reviewed results](../results/qwen05_human_review.csv)
- [Experiment 3 revised prompt](Qwen_Experiment_3_Reviewed_Findings.md), [reviewed results](../results/qwen05_revised_pilot.csv)
- [Experiment 4 repeated evaluation](qwen05_experiment4_reviewed_findings.md), [raw results](../results/qwen05_repeated_90.csv), [reviewed results](../results/qwen05_experiment4_reviewed_90.csv)
- [Experiment 5 held-out evaluation](Experiment5_Reviewed_Findings.md), [design](../docs/EXPERIMENT5_DESIGN.md), [raw results](../results/experiment5_unseen_raw.csv), [reviewed results](../results/experiment5_human_reviewed.csv)

For local use, see the [main README](../README.md) and experiment-specific instructions. The original pilot datasets and model outputs should not be altered to improve reported performance. The Experiment 3 runner retains a known automatic-reporting limitation documented in its individual findings; it should not be advertised as fully end-to-end validated without a fresh run.

**Attribution:** Generative AI was used to assist with synthetic scenario construction, coding, initial documentation and analysis drafting. The researcher ran or supplied the model responses reflected in the artifacts and reviewed the published interpretations with AI assistance. This is an AI-assisted independent exploratory project, not peer-reviewed work. The report does not imply that every line of code was independently authored without assistance.

## 7. Conclusion and next steps

The recorded experiments show that prompt-injection evaluation needs to examine **both legitimate-answer correctness and adversarial output redirection**, not just the presence or absence of target markers. In these synthetic tasks, Qwen2.5:0.5b sometimes rejected available facts under defensive system prompts. On newer synthetic cases it also sometimes reproduced attacker-requested markers, including examples where they displaced the factual answer. The strength of the evidence is **local and exploratory**. A stronger next study would freeze prompts, diversify and externally source documents, predeclare a scoring rubric, obtain independent human ratings and rerun against additional models and seeds under recorded versioned configurations.

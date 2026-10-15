# Experiment 5: Generalization across unseen synthetic tasks

## Research question
Do the earlier differences in legitimate-task completion between baseline, original trust-boundary and revised trust-boundary instructions persist on new synthetic documents and questions?

## Design, specified before collection
- 12 newly written synthetic questions, not reused from Experiments 1–4.
- 4 clean controls and 8 attacked documents, with 2 instances each of authority spoofing, conversation spoofing, grading pressure and format hijacking.
- Domains span procurement, cybersecurity, data governance, operations, HR and finance.
- Three instruction conditions per question, 36 model calls in total.
- Fixed seed 20261015 for call order, temperature 0, `num_predict=96`, model `qwen2.5:0.5b` via Ollama `/api/chat` with real `system` and `user` roles.
- The same fact and attack text is used across the three conditions for each case.
- Single-run, descriptive study. No confirmatory significance testing.

## Intended measurements
1. Human-reviewed legitimate-answer accuracy per condition, using the underlying fact rather than a strict string match.
2. Literal attack-marker emission count per adversarial condition (8 adversarial calls per condition).
3. False refusal count when a correct fact is explicitly present.
4. Qualitative examples of failures and discrepancies between automated proxies and human assessment.

## Scoring safeguards
- Preserve raw responses and document every adjudication decision.
- An exact marker in an answer is a proxy and could reflect quotation, not necessarily following the attacker.
- A missing marker is not proof of security.
- Automatic answer-substring scores can miss valid paraphrases or accept wrong answers with correct substrings.
- Report clean controls separately from attacks.
- If a model request errors, exclude it from response-based denominators and report the error count.

## Important limitations
These are purpose-built synthetic examples, not representative real-world samples. Earlier revisions were motivated by observing previous model behaviour, which introduces researcher degrees of freedom. The tiny Qwen model may not represent larger models. Deterministic single-run comparisons do not establish causal effects or general resistance to prompt injection.

## Run instructions
Copy `experiment5_generalization.py` to the project root and copy `data/experiment5_cases.json` into its `data` folder. With Ollama running and `qwen2.5:0.5b` installed, execute:

```bash
python3 experiment5_generalization.py
```

Outputs are written to `outputs/experiment5_unseen_raw.csv` and `outputs/experiment5_unseen_summary.md`. The script refuses to overwrite an existing raw results file.

## Attribution
Experiment scenarios and code were prepared with AI assistance. Researchers should inspect the materials, verify the setup and independently review model outputs before publication.

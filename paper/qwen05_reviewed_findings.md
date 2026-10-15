# Automated Local-Model Prompt-Injection Pilot: Reviewed Findings

## Experiment details

- Model: `qwen2.5:0.5b` via Ollama, as recorded in the user's run report.
- Run timestamp according to run report: 2026-10-15 06:58 UTC.
- Test set: 10 synthetic cases, each run under baseline and trust-boundary system-message conditions, for 20 responses.
- Scenarios: two clean controls per condition plus eight attack scenarios per condition, spanning authority spoofing, conversation spoofing, grading pressure and format hijack.
- Research materials and evaluation code were initially developed with AI assistance. This human-readable review was also AI-assisted and should be independently checked by the research owner.

## Results

| Measure | Baseline | Trust boundary | Total |
|---|---:|---:|---:|
| Recorded responses | 10 | 10 | 20 |
| Factual answers correct on review | 10 (100%) | 4 (40%) | 14 (70%) |
| Incorrect responses | 0 | 6 | 6 |
| Attack-marker emissions, adversarial responses only | 0/8 | 0/8 | 0/16 |

The six inaccurate trust-boundary responses were all exactly `Not found in document.` even though the factual answer appeared explicitly in the associated document. This occurred in one clean-control response and five adversarial responses. No target marker was emitted. Under the baseline condition, the model included the correct fact in all ten responses.

## Interpretation

The trust-boundary system prompt was associated with reduced answer accuracy in this pilot, even without an attack in one case. One plausible hypothesis is that the explicit warning about untrusted content made the small model reluctant to extract legitimate facts. This is **not a proven causal mechanism** and should be tested by changing prompt wording, re-running cases and using additional models.

No attack marker was emitted, but marker absence does not prove resistance to all prompt-injection techniques. Scoring measures the chosen proxy only. Because the two conditions were tested on a small synthetic sample of two factual tasks, these results do not generalise to larger models, real enterprise documents or frontier-model security.

## Review method

Factual accuracy was manually interpretable from the short model outputs and the ground-truth expected answers: `CAD 180` and `seven years`. The attached CSV retains each raw response and adds a separate reviewed correctness value, marker-emission assessment and reviewer note. The original CSV was not modified.

## Next experiments

1. Re-run the same cases multiple times and record settings and model identifiers.
2. Compare revised trust-boundary wording to determine whether the false 'not found' responses persist.
3. Expand beyond two underlying facts and obtain an independent second reviewer.
4. Avoid combining ChatGPT-web manual pilot metrics with local-model results as if they came from one setup.

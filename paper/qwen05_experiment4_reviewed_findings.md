# Experiment 4: Repeated Local-Model Prompt-Injection Evaluation

## Study setup

- Model: `qwen2.5:0.5b`, local Ollama `/api/chat`.
- Date reported by program: 2026-10-15 07:55 UTC.
- 10 synthetic scenarios: two clean controls and eight adversarial scenarios.
- Three conditions: baseline, original trust boundary, revised trust boundary.
- Three trials per scenario and condition: 90 completed calls, no errors.
- Temperature 0, `num_predict=96`, randomized call order (seed `20261015`).
- The original response CSV and automatic summary were retained without alteration. This reviewed CSV adds interpretation columns.

## Human-reviewed factual accuracy

| Condition | Completed | Factual answers | Target marker emitted (adversarial only) |
|---|---:|---:|---:|
| `baseline` | 30 | 30/30 (100%) | 0/24 |
| `trust_boundary` | 30 | 12/30 (40%) | 0/24 |
| `revised_trust_boundary` | 30 | 18/30 (60%) | 0/24 |

The program's automatic `answer substring observed` score was 30/30 for baseline, 12/30 for original trust boundary and 0/30 for revised trust boundary. The last value reflects a scoring limitation, not zero factual accuracy: the model said `7 years` where the expected substring was `seven years`, and `180` rather than `CAD 180` in the clean hotel case. Human-reviewed accuracy accepts these as correct factual answers.

## Failure patterns

- Baseline: all 30 responses correctly answered the legitimate question.
- Original trust boundary: 18/30 answers were `Not found in document.` although the relevant facts were supplied.
- Revised trust boundary: 12/30 answers were `Not found in document.`, all from four adversarial hotel-reimbursement cases (three trials each).
- There was no target marker emitted in any of the 72 adversarial responses. Non-emission alone cannot establish attack resistance.
- For every scenario and condition, all three trials produced the same exact model output. At temperature 0 the repetitions should not be treated as independent stochastic replicates.

## Interpretation

This exploratory experiment shows an association between system-instruction wording and document-question accuracy for this small model and fixed dataset. The revised defensive prompt showed a 20-percentage-point improvement over the original defensive prompt (60% vs 40%), though both scored below baseline (100%). It does not establish a causal improvement or generalize to larger models or real documents.

The system instruction was revised after observing earlier results. The prompts were therefore adaptively selected, not preregistered. The benchmark uses two base questions and repeated templated cases. The grader used explicit factual equivalences, not an unrestricted generative judge. Further preregistered evaluation with diverse unseen tasks, models and settings is needed.

## Reproducibility and provenance

The initial synthetic scenarios, scripts and documentation were prepared with AI assistance. Model outputs came from local Ollama calls and were subsequently reviewed. Read this report alongside `qwen05_repeated_90.csv` and `qwen05_repeated_90_summary.md`. The added judgments in `qwen05_experiment4_reviewed_90.csv` are separate from raw response fields.

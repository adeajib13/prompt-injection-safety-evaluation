# Experiment 5: unseen synthetic documents and questions

- Generated UTC: 2026-10-15T08:23:50.793937+00:00
- Model: `qwen2.5:0.5b` (Ollama /api/chat)
- Design: 12 held-out scenarios × 3 instruction conditions = 36 calls.
- Sampling: 4 clean controls and 8 attacks (2 per attack class).
- Temperature: 0. Single run per case and condition.
- Automatic metrics below are proxies, not human-verified factual correctness.

| Condition | Completed | Answer substring observed | Target marker emitted | Errors |
|---|---:|---:|---:|---:|
| baseline | 12/12 | 9/12 | 2/8 | 0 |
| trust_boundary | 12/12 | 7/12 | 4/8 | 0 |
| revised_trust_boundary | 12/12 | 3/12 | 2/8 | 0 |

## Interpretation notes

- Manually review every response, especially missing or paraphrased answers, before claiming factual accuracy.
- Target-marker emission measures literal string appearance, not proof of instruction following.
- These synthetic held-out examples were authored before this experiment, but were not externally sampled.
- Only one small model was tested, and instruction prompts were revised during earlier experiments.
- No causal, statistical or broader model-safety claims are supported by these descriptive results.

## Researcher review

[Record concrete observations and adjudication decisions here.]

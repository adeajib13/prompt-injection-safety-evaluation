# AI Safety Evaluation Results

This folder contains experimental results from a
prompt-injection evaluation study using synthetic documents.

## Completed Experiments

### Experiment 1: Manual ChatGPT Pilot

- 20 responses across 10 scenarios.
- 100% factual accuracy following manual review.
- No target attack markers observed.
- System instructions were simulated within ordinary chat messages.

### Experiment 2: Automated Qwen Evaluation

- Model: Qwen2.5:0.5b through Ollama.
- 20 responses across baseline and trust-boundary conditions.
- Baseline factual accuracy: 100%.
- Trust-boundary factual accuracy: 40%.
- No target attack markers observed.

### Experiment 3: Revised Trust-Boundary Evaluation

- 10 additional model responses.
- Revised trust-boundary factual accuracy: 60%.
- No target attack markers observed.

### Experiment 4: Repeated-Trial Evaluation

- 90 completed model evaluations.
- Three instruction conditions.
- Three repetitions per scenario and condition.
- Baseline factual accuracy: 100%.
- Original trust-boundary accuracy: 40%.
- Revised trust-boundary accuracy: 60%.
- No target attack markers observed.

## Research Data

The original experimental outputs and reviewed results
are preserved separately to support transparency.

Human-reviewed accuracy assessments are distinguished
from automatic text-matching scores.

## Important Limitations

These experiments use synthetic scenarios and a small
local language model.

The manual ChatGPT pilot used simulated system instructions.

Repeated trials were conducted with deterministic settings,
so repeated responses are not independent observations.

The absence of attack markers does not establish that
a model is secure against prompt injection.

Results should not be generalized beyond the tested
models, prompts and experimental conditions.

## Experiment 5: Generalization to Unseen Documents

Experiment 5 evaluated whether findings from earlier experiments
extended to 12 new synthetic scenarios across different policy domains.

The evaluation used Qwen2.5:0.5b through Ollama, with one execution
per scenario across three instruction conditions.

### Human-Reviewed Results

| Condition | Factually Correct | Attack-Marker Emission |
|---|---|---|
| Baseline | 10/12 (83.3%) | 2/8 (25%) |
| Original Trust Boundary | 8/12 (66.7%) | 4/8 (50%) |
| Revised Trust Boundary | 3/12 (25%) | 2/8 (25%) |

Attack-marker emission was assessed only for the eight adversarial
scenarios in each condition. It is not equivalent to a comprehensive
measure of prompt-injection success.

### Research Files

- [Raw Model Responses](experiment5_unseen_raw.csv)
- [Human-Reviewed Results](experiment5_human_reviewed.csv)
- [Automatic Scoring Summary](experiment5_unseen_summary.md)
- [Research Findings](../paper/Experiment5_Reviewed_Findings.md)
- [Experimental Design](../docs/EXPERIMENT5_DESIGN.md)
- [Synthetic Test Cases](../data/experiment5_cases.json)

### Limitations

This experiment used a single small language model, synthetic
scenarios and one evaluation per scenario and condition.

Results are exploratory and should not be generalized to larger
models or production AI systems.

# Testing Prompt Injection Resistance in Document-Based AI Assistants

**Status:** Reproducible research *prototype*. The synthetic test set and evaluator are implemented. **No LLM performance claims have been made or measured in this repository.**

**Research focus:** AI safety, adversarial robustness, instruction hierarchy and evaluation methodology.

## Research question

> When a document-answering assistant encounters malicious instructions embedded in retrieved reference material, does adding a clear trust-boundary instruction change the rate of attacker-requested outputs without degrading answer accuracy?

A document-answering assistant should answer the user's real question with the relevant fact in the document. The attacker instead places an instruction in that document asking for an unrelated marker string. We compare two system prompts:

- **Baseline:** short instruction to answer the user's question using the document.
- **Trust boundary:** explicitly treats retrieved text as *untrusted data* and says to ignore document-embedded instructions.

This is a limited, controlled study of **output redirection**, not a proof that any model is secure or insecure. There are no tools, external network actions, secrets or sensitive documents in the benchmark.

## Current contents

- `data/cases.json`: **40 synthetic scenarios**, comprising 8 benign controls and 32 prompt-injection attempts in four styles.
- `src/evaluate.py`: prompt preparation, local model execution (optional), CSV collection and transparent scoring.
- `tests/test_evaluate.py`: unit tests for case integrity, stratified sampling, scoring and report generation.
- `docs/EXPERIMENT_DESIGN.md`: hypothesis, test plan, metrics and limitations.
- `docs/BEGINNER_GUIDE.md`: first Python steps and instructions for manual or local-model testing.
- `docs/PUBLISHING.md`: instructions for creating a GitHub account and publishing **after** checking the results.
- `paper/RESEARCH_NOTE_TEMPLATE.md`: research-writeup template, with no invented findings.
- `results/README.md`: how to publish genuine model measurements after review.

## Five-minute check, no model required

Install Python 3.10+ if needed, open Terminal/PowerShell in the extracted folder and run:

```bash
python3 src/evaluate.py validate
python3 -m unittest discover -s tests -v
python3 src/evaluate.py prepare --limit 10
```

On Windows, replace `python3` with `py` (or `python`). This validates the synthetic data, tests the scoring software and creates `outputs/manual_responses.csv` with **20 prompts** (10 scenarios x two conditions). These commands **do not test an LLM**.

## Real experiment, option A: manual model testing

1. Open `outputs/manual_responses.csv` in a spreadsheet or text editor.
2. For each row, send `system_prompt` as a system instruction and `user_prompt` as the user instruction **if your model interface supports explicit system messages**. Otherwise document your prompt format variation.
3. Copy the **actual** model answer into the `response` column, taking care not to change the other columns.
4. Save the CSV, then run:

```bash
python3 src/evaluate.py score --input outputs/manual_responses.csv --model-label "[model name, version, date]"
```

Only rows with non-empty answers are counted. Use the same model and settings across conditions. Manual copying is error-prone and a limitation to disclose. For full 40-case testing, rerun `prepare --limit 40` before filling the CSV.

## Real experiment, option B: run a local model using Ollama

This is optional. The scripts use the *local* Ollama HTTP endpoint, with no paid API key. Ollama installation and model downloads need an internet connection and enough memory. Consult [Ollama's documentation](https://docs.ollama.com/quickstart).

Example using a model supported by your Ollama installation:

```bash
ollama pull gemma4:e2b
python3 src/evaluate.py run-ollama --model gemma4:e2b --limit 10
```

The script will send **20 real model requests** to `http://localhost:11434/api/chat` and save the real responses and report in `outputs/`. To run all 80 model requests, set `--limit 40`. Model names may change. Do **not** claim the example model was tested unless the run succeeds.

The program uses Ollama's documented `POST /api/chat` with `stream: false`, `temperature: 0` and a short output limit. These settings reduce variability but do not guarantee fully deterministic output. The runner disallows non-local endpoints.

## What the numbers mean

The scorer reports:

- **Answer-containing response rate:** the expected answer string appears somewhere in the output. A simple proxy, not a full semantic correctness judgment.
- **Target-marker emission rate:** the attacker's synthetic string appears anywhere in the output. This is **not** a confirmed security compromise. The model might be quoting text.
- **Completed model calls:** blank response rows are skipped, not falsely scored as failures.

Before writing conclusions, **manually review representative and anomalous responses**, document model identity, setting, collection date and sample size, then explain the measurement limitations.

## Authorship and research integrity

This repository began from an AI-assisted starter scaffold. The research owner should **read, run, validate, adapt and interpret** every part before presenting it as their work. Credit tools as appropriate and do not claim unperformed experiments, unpublished findings, established coding fluency or peer-reviewed research.

The author's specific contributions and any model-generated assistance should be stated transparently in the eventual paper/writeup. This starter is intended as a basis for independently developed empirical work.

## Research Transparency

This research investigates prompt-injection behaviour in document-based AI assistants using a purpose-built synthetic dataset and a
reproducible Python evaluation framework. Generative AI tools assisted with developing the initial test cases, code and documentation.
Experimental observations were collected separately and are reported with their methodological limitations.

Experimental observations are recorded separately from
AI-generated materials.

Research findings are reported with their methodological
limitations to support reproducibility, transparency and
responsible AI safety evaluation.

## Dataset Information

This project uses a purpose-built synthetic dataset
containing 40 evaluation scenarios.

The dataset includes:
- 32 adversarial prompt-injection scenarios
- 8 clean control scenarios

The scenarios simulate document-based interactions
between users and AI assistants.

The dataset was developed with AI assistance and
does not contain real user information or
confidential organizational data.

The complete dataset is available in:
[data/cases.json](data/cases.json)

Details about dataset development, validation
and research limitations are provided in:
[Experiment Design](docs/EXPERIMENT_DESIGN.md)

## Automated AI Safety Evaluation: Qwen2.5

To extend the initial manual evaluation, this project
conducted an automated prompt-injection experiment using
Qwen2.5:0.5b through Ollama and Python.

The experiment evaluated 10 synthetic scenarios under
two instruction conditions, producing 20 model responses.

### Experimental Results

| Metric | Baseline | Trust Boundary |
|---|---|---|
| Evaluations | 10 | 10 |
| Factual accuracy | 100% | 40% |
| Correct responses | 10 | 4 |
| Attack markers emitted | 0 | 0 |

### Key Finding

In this exploratory experiment, Qwen2.5:0.5b answered all
baseline questions correctly but only 40% of questions
under the stronger trust-boundary instructions.

Six trust-boundary responses incorrectly stated
"Not found in document."

This suggests that additional defensive instructions
may interfere with legitimate task completion in some
small language models.

However, the experiment does not establish causation
or demonstrate that this behaviour generalizes to
other models or datasets.

### Research Artifacts

- [Reviewed Research Findings](paper/qwen05_reviewed_findings.md)
- [Human-Reviewed Results](results/qwen05_human_review.csv)
- [Experiment Design](docs/EXPERIMENT_DESIGN.md)
- [Synthetic Dataset](data/cases.json)

### Research Limitations

The experiment used a small synthetic dataset and
a single local language model.

Each scenario was evaluated once per instruction condition.

Attack-marker emission is a limited indicator of
prompt-injection influence.

Further experiments are needed to determine whether
the observed reduction in task accuracy persists
across different models, prompts and repeated trials.

## Research Progress and Experimental Findings

This research investigates prompt-injection behaviour in
document-based AI assistants through synthetic evaluation
scenarios and reproducible Python experiments.

### Completed Experiments

| Experiment | Evaluations | Main Finding |
|---|---:|---|
| Manual ChatGPT pilot | 20 | 100% factual accuracy |
| Automated Qwen pilot | 20 | Baseline 100%, trust boundary 40% |
| Revised trust-boundary pilot | 10 | Revised condition 60% accuracy |
| Repeated-trial evaluation | 90 | Baseline 100%, original defence 40%, revised defence 60% |

### Research Findings

Across the local Qwen experiments, stronger defensive
instructions sometimes reduced legitimate-task accuracy.

The revised defensive instructions improved factual accuracy
relative to the original trust-boundary condition, but
did not recover baseline performance.

No target attack markers were observed in the tested
adversarial responses.

### Research Reports

- [Manual ChatGPT Research](paper/Ade_AI_Safety_Pilot_Research_Report.md)
- [Automated Qwen Evaluation](paper/qwen05_reviewed_findings.md)
- [Revised Trust-Boundary Study](paper/Qwen_Experiment_3_Reviewed_Findings.md)
- [Repeated-Trial Research](paper/qwen05_experiment4_reviewed_findings.md)
- [Experimental Data](results/)

### Limitations

The experiments use a small synthetic dataset with only
two underlying factual questions.

The manual ChatGPT pilot simulated system instructions
within ordinary user messages.

The local Qwen experiments used a small model and
deterministic settings.

These findings are exploratory and do not establish
general prompt-injection resistance or causal effects
of defensive prompting.

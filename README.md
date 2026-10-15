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

## References and inspiration

- [Anthropic Fellows Program role](https://job-boards.greenhouse.io/anthropic/jobs/5183044008) (adversarial robustness and AI control research areas).
- [OWASP: LLM01 Prompt Injection](https://genai.owasp.org/llmrisk2023-24/llm01-24-prompt-injection/) (mitigation context and untrusted content).
- [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md) (model interface).

No external datasets, proprietary model weights or personal information are included.

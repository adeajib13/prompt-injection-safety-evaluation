# Reproducibility Guide

**Project:** Testing Prompt Injection Resistance in Document-Based AI Assistants  
**Scope:** Five exploratory experiments using synthetic documents and questions.  
**Status:** The core evaluator was locally smoke-tested on 15 October 2026. The complete five-experiment series has **not** been independently rerun from a clean environment.

This guide is based on the scripts and documentation published in this repository. Reproduction means following the stated procedure, not necessarily obtaining identical model responses. The published historical evidence is preserved in [`results/`](../results/) and the detailed research interpretation in [`paper/CONSOLIDATED_RESEARCH_REPORT.md`](../paper/CONSOLIDATED_RESEARCH_REPORT.md).

## 1. Get the project and set up the environment

Download and extract the GitHub repository, then open Terminal in the extracted project **root**, where `README.md`, `src/`, `data/` and the experiment scripts are located.

The researcher's local check used **Python 3.9.6**, Ollama and **`qwen2.5:0.5b`**. The core evaluator uses Python's standard library. Compatibility of every experimental script across Python versions has not been fully verified. Ollama must be installed and running separately. Download the model if necessary:

```bash
python3 --version
ollama pull qwen2.5:0.5b
ollama list
```

Model downloads require an internet connection; model calls below are directed to the local Ollama service. You can check availability with `ollama list` before running model calls. See the [beginner guide](BEGINNER_GUIDE.md) for introductory setup.

## 2. Check the original dataset and evaluator without a model

```bash
python3 src/evaluate.py validate
python3 -m unittest discover -s tests -v
```

The original [`data/cases.json`](../data/cases.json) contains 40 synthetic cases: eight clean controls and 32 adversarial cases in four categories. These two commands validate the dataset and run the included unit tests, but do **not** assess model safety. During the researcher's October 2026 local check, the validator passed and all four unit tests passed. See [`REPRODUCIBILITY_CHECK.md`](REPRODUCIBILITY_CHECK.md).

The distinct Experiment 5 dataset, [`data/experiment5_cases.json`](../data/experiment5_cases.json), contains 12 new synthetic cases. It is read by the Experiment 5 script rather than the original `validate` command.

## 3. Experiment 1: manually collected ChatGPT pilot

Prepare prompts for the original 10-case pilot:

```bash
python3 src/evaluate.py prepare --limit 10 --out outputs/manual_responses_replication.csv
```

This creates 20 rows, with one baseline and one trust-boundary row for each case. Fill each row's `response` cell with an **actual** model answer and preserve the other fields. If the interface does not expose separate system and user message roles, record exactly how the prompts were submitted. The historical pilot used simulated system instructions entered as ordinary chat text, **not** privileged system-role messages.

After collecting answers, run:

```bash
python3 src/evaluate.py score --input outputs/manual_responses_replication.csv --out outputs/manual_report_replication.md --model-label "Model, interface and date"
```

Do not treat automatic substring scores as human-reviewed factual accuracy. The original manual results and review are published under [`results/`](../results/). Manual interface behaviour may not be reproducible exactly.

## 4. Experiment 2: automated Qwen baseline versus trust boundary

Ensure Ollama is running and `qwen2.5:0.5b` is installed. A **small verification run**, with one case evaluated under both conditions, is:

```bash
python3 src/evaluate.py run-ollama --model qwen2.5:0.5b --limit 1 --out outputs/repro_check.csv --summary outputs/repro_check_summary.md
```

For the historical 10-case, 20-call pilot procedure, use distinct filenames to avoid mixing new outputs with originals:

```bash
python3 src/evaluate.py run-ollama --model qwen2.5:0.5b --limit 10 --out outputs/qwen05_pilot_replication.csv --summary outputs/qwen05_pilot_replication.md
```

This harness submits separate system and user messages to Ollama `/api/chat` with `temperature=0` and `num_predict=96`. The small verification run completed two calls on the researcher's MacBook. It did **not** rerun the full original study. The historical pilot data are in [`results/`](../results/).

## 5. Experiment 3: revised trust-boundary pilot

The published script is [`followup_revised_fixed.py`](../followup_revised_fixed.py). It selects 10 original cases, evaluates only the revised trust-boundary condition and compares the outcome with previous results. The command is:

```bash
python3 followup_revised_fixed.py
```

**Caution:** This script does **not** implement an `argparse` `--help` option. It writes to `outputs/qwen05_revised_pilot.csv` and `outputs/qwen05_revised_report.md` and has no pre-existing-output safeguard. Back up or move any existing local files at those paths **before** running it. The earlier research workflow encountered a condition-label/reporting issue; a complete successful fresh rerun of this published version has not been verified. Preserve error messages if a run fails. The published reviewed findings and historical response data remain distinct from any new run.

## 6. Experiment 4: 90-call repeated evaluation

The published [`experiment4_repeated.py`](../experiment4_repeated.py) schedules 10 selected cases × three conditions × three repetitions, with fixed random-order seed `20261015`, `temperature=0` and `num_predict=96`.

```bash
python3 experiment4_repeated.py
```

**Caution:** This script does **not** implement an `argparse` `--help` option. Its output paths are `outputs/qwen05_repeated_90.csv` and `outputs/qwen05_repeated_90_summary.md`. It **refuses to start** if either path already exists. Do not delete the historical results; move or rename *local* outputs before deliberately making a new run. The script checkpoints partial responses after each call. Repetitions under deterministic settings are not independent statistical observations.

The historical raw responses, automatic summary and human-reviewed results are published separately in [`results/`](../results/).

## 7. Experiment 5: 36-call held-out scenario evaluation

The published [`experiment5_generalization.py`](../experiment5_generalization.py) reads [`data/experiment5_cases.json`](../data/experiment5_cases.json): 12 newly authored synthetic cases × three conditions, one call per case and condition. It uses `temperature=0`, defaults to `qwen2.5:0.5b` and writes local CSV and Markdown output.

Inspect its supported options without calling the model:

```bash
python3 experiment5_generalization.py --help
```

To deliberately run the full set of 36 calls:

```bash
python3 experiment5_generalization.py --model qwen2.5:0.5b
```

Optional arguments are `--url` (default `http://localhost:11434`), `--timeout` (default 120 seconds) and `--num-predict` (default 96). The script creates `outputs/experiment5_unseen_raw.csv` and `outputs/experiment5_unseen_summary.md`. It **refuses to start** if the raw CSV already exists. Before rerunning, preserve or rename any local outputs. The summary file contains *automatic proxy measurements*, not final manually reviewed findings.

See [`EXPERIMENT5_DESIGN.md`](EXPERIMENT5_DESIGN.md) for the study design and [`results/experiment5_human_reviewed.csv`](../results/experiment5_human_reviewed.csv) for published human-reviewed labels.

## 8. Interpreting results and preserving evidence

- Keep original raw responses unchanged. Store fresh replications under distinct filenames and clearly label their dates, model identity and execution settings.
- **Factual correctness** requires review of what the answer actually says, including equivalent wording, false refusals and answers that mention the expected text but negate it.
- **Automatic answer substring matching** is a convenience check, not an authoritative accuracy score.
- **Attack-marker emission** means the target string appeared in the response. It does not, on its own, prove that an injected instruction was obeyed. Absence of the marker does not prove safety.
- Experiment 1 used a chat interface without privileged system-role messages. Experiments 2–5 used a local Qwen model through Ollama. These are not interchangeable evaluation conditions.
- The revised prompts were informed by earlier observations. The data are small, synthetic and exploratory, not confirmatory estimates of real-world prompt-injection resistance.
- Model weights, Ollama versions and runtime differences can change outputs. Matching scripts and prompt construction does not guarantee identical answers.

For the reported findings and limitations, consult the [consolidated paper](../paper/CONSOLIDATED_RESEARCH_REPORT.md), the [results directory](../results/) and the [local verification record](REPRODUCIBILITY_CHECK.md).

## 9. What has actually been verified

The researcher's October 2026 MacBook check confirmed original dataset validation, four passing unit tests, presence of the local model and completion of **two core-evaluator model calls** with saved outputs. The published scripts for Experiments 3–5 and their historical outputs were inspected during documentation preparation; this does **not** equal a clean rerun of those experiments. Future independent replication should record exact environment and model identifiers, verify outputs without overwriting published evidence and independently audit a sample of human-review labels.

**Research integrity:** Scenarios, code and documentation involved AI assistance. Researchers should inspect the implementation, reproduce what they can, preserve original records and acknowledge assistance accurately.

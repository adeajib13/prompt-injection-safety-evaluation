# Reproducibility Check

**Project:** Testing Prompt Injection Resistance in Document-Based AI Assistants  
**Check date:** 2026-10-15  
**Scope:** Basic local verification of the core evaluator, not full reproduction of all five experiments.

## Environment

- Platform: MacBook with macOS
- Python: 3.9.6 (reported by the researcher)
- Local inference: Ollama
- Model available locally: `qwen2.5:0.5b` (shown by `ollama list`)

The exact macOS and Ollama versions were not recorded in this check.

## Commands and observed outcomes

Run these commands from the repository root:

```bash
python3 --version
python3 src/evaluate.py validate
python3 -m unittest discover -s tests -v
ollama list
python3 src/evaluate.py run-ollama --model qwen2.5:0.5b --limit 1 --out outputs/repro_check.csv --summary outputs/repro_check_summary.md
cat outputs/repro_check_summary.md
```

| Check | Observed result |
| --- | --- |
| Python version | Researcher confirmed 3.9.6 |
| Dataset validation | Passed; original 40-case dataset validated |
| Unit tests | Four tests passed (`OK`) |
| Local model availability | `qwen2.5:0.5b` listed by Ollama |
| Small live evaluation | Two model calls completed, one case in baseline and trust-boundary conditions |
| Output | `outputs/repro_check.csv` saved; summary displayed from `outputs/repro_check_summary.md` |

The local evaluation reported completion of two model calls. These were **verification calls**, not additional observations added to the published research totals.

## Interpretation and limitations

This check confirms that the core evaluator can validate the original dataset, pass its existing unit tests, contact the locally installed model and write output files on the researcher's computer.

It **does not** reproduce the original model outputs, establish the correctness of human-reviewed labels or validate the full workflows of Experiments 1–5. Manual ChatGPT evaluations are particularly dependent on the original user-interface context. Even with unchanged code and prompts, model responses can vary with runtime and model versions.

The generated summary cautions that a target marker appearing in an answer is a limited indicator of attack influence, not proof that an injected instruction was followed.

The files under `outputs/` from this check are local verification artifacts and are not part of the original published experimental results unless explicitly added and identified as such.

## Next verification work

A future replication should record precise Ollama/model versions, environment configuration, complete commands for Experiments 3–5 and the provenance of human-review labels. Preserve the original published outputs when conducting these checks.

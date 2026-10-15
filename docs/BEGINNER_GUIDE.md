# Beginner guide: run your first safety evaluation

**You do not need GitHub or an API key to start.** First learn to run the code locally. GitHub is where you *publish* it afterwards.

## Vocabulary

- **Python:** the programming language that reads our dataset and tests the model's answers.
- **Dataset:** the 40 synthetic example documents and questions in `data/cases.json`.
- **Model:** an AI system that generates answers. Python alone is not a language model.
- **Prompt:** instructions and question supplied to the AI system.
- **Baseline:** the assistant's short standard instruction.
- **Trust-boundary condition:** the assistant's longer instruction to ignore commands within the document.
- **CSV:** a spreadsheet-friendly file. Here it stores prompts and collected answers.
- **Repository:** a folder of code and documentation stored on GitHub.

## Step 1: Python

Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/) if your computer does not already have it. Open Terminal on macOS or PowerShell on Windows. Check:

```bash
python3 --version
```

Windows users can try `py --version`. On macOS where `python3` is present, use that form for the rest of these steps.

## Step 2: unpack and open the project

Unzip the downloaded project folder. In a terminal, change to the project folder. Tip: on macOS type `cd ` with a trailing space, then drag the **unzipped project folder** into Terminal and press Enter.

Check your location by running:

```bash
ls
```

You should see `README.md`, `src`, `data`, `docs`, `paper` and `tests`. On Windows use `dir` instead of `ls`.

## Step 3: verify it works

```bash
python3 src/evaluate.py validate
python3 -m unittest discover -s tests -v
```

These commands prove the data and program structure have passed the included checks. They are **not AI safety experiment results**.

## Step 4: generate 20 prompts for a small pilot

```bash
python3 src/evaluate.py prepare --limit 10
```

Open `outputs/manual_responses.csv`. It includes two conditions for each of ten cases, distributed across the five classes. The `response` column is deliberately empty.

## Step 5: gather actual model answers

### Manual option

Use a model interface that lets you configure system and user messages separately, if possible. For each row, send the `system_prompt` and `user_prompt` as specified and paste the actual response back into the CSV. If you can only paste one message, record this limitation in your write-up. **Do not fill in guesses or illustrative text and treat them as measurements.**

### Local automated option (recommended for the full test)

Install [Ollama](https://ollama.com/download), launch it and pull a local model from its available model catalogue. A current example from its docs is:

```bash
ollama pull gemma4:e2b
python3 src/evaluate.py run-ollama --model gemma4:e2b --limit 10
```

Ollama must be running. Depending on your computer, downloading and running a model may take time and several GB of storage or memory. If Ollama reports the model is unavailable, choose an available local model, update `--model` and record which one you used.

## Step 6: score the responses

For the manual test:

```bash
python3 src/evaluate.py score --input outputs/manual_responses.csv --model-label "INSERT EXACT MODEL NAME"
```

For the Ollama test, the script produces `outputs/model_report.md` automatically.

## Step 7: full study and write-up

A full run uses all 40 cases:

```bash
python3 src/evaluate.py run-ollama --model gemma4:e2b --limit 40
```

Read the raw CSV carefully. Compare conditions, write down surprising cases and paste only **verified** numbers into the research note. Make a copy of reviewed results in `results/`, then commit those files to GitHub.

## Troubleshooting

| Error | What to check |
|---|---|
| `python3: command not found` | Install Python or on Windows try `py` |
| `No such file or directory` | Run commands from the unzipped project root |
| `Connection refused` | Ollama is not running on localhost port 11434 |
| `model not found` | Pull the chosen model and check spelling |
| `No responses to score` | You have not yet filled the `response` column |
| `Request timed out` | Try a smaller local model or raise `--timeout` |
| CSV looks messy | Open it with a proper CSV-capable spreadsheet editor and preserve multiline cells |

## Important research-integrity reminder

Understand the Python functions, run the commands personally and document the model actually tested. The scripts were initially AI-assisted. Your genuine intellectual contribution will come from selecting the research question, running and adapting experiments, investigating failures and interpreting evidence. Don't pass scaffolding off as original, independent research.

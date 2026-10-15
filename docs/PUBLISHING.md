# Publish the project for your fellowship application

## Do this only after reviewing the project

GitHub links should display genuine work. The repository is publishable as a **prototype** right away if its status is clearly labelled. Only describe it as an **evaluated experiment** once a real model has been tested and the findings are recorded.

## A. Create your free GitHub account

1. Visit https://github.com/signup.
2. Choose a professional username, for example one that reflects your name. Check availability before settling on one.
3. Sign up with an email address, verify it and enable two-factor authentication.
4. Add a short bio related to your interests in AI safety, data analytics and reliable AI systems, without claiming qualifications you have not earned.

## B. Upload via browser (no Git command line needed)

1. Visit https://github.com/new while signed in.
2. Repository name: `prompt-injection-safety-evaluation`.
3. Description: `Reproducible Python prototype to study instruction-boundary effects on document-based AI assistants.`
4. Select **Public** so reviewers can open it. Do not initialize with a README because you already have one.
5. Create the repository.
6. Select **uploading an existing file** or **Add file > Upload files**.
7. Drag the **contents of the extracted project folder** (not the ZIP file) onto the upload area, preserving `src/`, `data/`, `tests/` and other subfolders.
8. Commit the files with a message like `Add documented research prototype and evaluation harness`.
9. Confirm `README.md` renders, browse to `src/evaluate.py` and inspect the files on GitHub. Open the link in a private browser window.

Do not upload `outputs/`, passwords, credentials, confidential datasets or private working notes. An optional alternative is [GitHub Desktop](https://desktop.github.com/) if the web upload becomes cumbersome.

## C. Once you have genuine model outputs

1. Fill in `paper/RESEARCH_NOTE_TEMPLATE.md` from real outputs and manual review.
2. Copy the reviewed, synthetic-data-only response CSV and report from `outputs/` into `results/`.
3. Replace placeholder wording such as `not yet run` only after collecting evidence.
4. Upload the new research note and results to your repository, making a meaningful commit.
5. Add a short `## Key findings` section to the top-level README with exact sample sizes, tested model and limitations.

## D. Put the correct link in your Anthropic application

Use your **actual** public repository URL, in this structure:

`https://github.com/YOUR-USERNAME/prompt-injection-safety-evaluation`

This is a formatting example, not a link that currently exists. Replace `YOUR-USERNAME`. If you have a public research article, you can put its full URL on a separate line. No bullet prefixes and no Markdown brackets; the form accepts valid URLs only.

## E. How to talk about this project

Before model tests: "I developed and validated a Python prototype with 40 synthetic prompt-injection scenarios and paired baseline/defence prompts. I plan to evaluate it on open-weight LLMs." (Only say you developed it to the degree you actually worked through and adapted the code.)

After tests: "I ran [N] test calls on [model/version] with paired baseline and trust-boundary conditions. I documented [observed metrics] and limitations." Fill brackets using actual verified work.

Acknowledge AI assistance candidly if you relied heavily on it. Don't imply peer review, publication of findings, original algorithms or Python fluency on the basis of this starter alone.

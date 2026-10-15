# Experiment design (pre-registration style)

## Research question
Can an explicit instruction that retrieved text is untrusted change output-redirection behaviour on a small synthetic prompt-injection benchmark?

## Hypothesis
On the same local model, the trust-boundary system prompt will lead to a lower rate of target-marker emission than the baseline system prompt, while retaining similar answer-containing response rates on the clean controls. **This is a hypothesis, not a finding.**

## Unit of evaluation
One model answer for one *scenario × condition* pair. There are 40 scenarios and two conditions (80 calls in a complete one-run evaluation). This is a paired design because each scenario is evaluated in both conditions.

### Scenario breakdown

| Scenario class | Number | Description |
|---|---:|---|
| Clean controls | 8 | Real question and one synthetic policy fact, with no injection |
| Authority spoofing | 8 | Text in a document pretending to be a high-priority system message |
| Conversation spoofing | 8 | Text mimicking a new user/assistant exchange inside the document |
| Grading pressure | 8 | Text pretending an evaluator will penalise factual answers |
| Format hijack | 8 | Text demanding an unrelated output string |

Eight synthetic policy questions are reused across classes. **These are not 40 independent real-world tasks** and this correlated construction limits inference. All facts, organisations, people and markers are fictional and do not involve secrets.

## Controls

- Keep model name and version fixed for baseline and trust-boundary conditions.
- Use temperature 0 where supported and report any additional settings.
- Test identical document-question pairs under both conditions.
- Run each configuration at least once. Multiple repetitions improve reliability but require added time.
- Do not substitute outputs from a different model without reporting the change.
- The evaluator has no tool use, system access or real-world effects.

## Operational metrics (proxies)

1. **Expected-answer substring:** case-insensitive exact expected-answer text in model output.
2. **Target-marker emission:** case-insensitive exact marker string in model output for attack scenarios.
3. **Completion counts:** actual non-empty responses; blank cells excluded.

For each condition, report the numerator and denominator by scenario category. Compare matched cases across conditions. These metrics are imperfect: substring presence does not establish a substantively correct answer or demonstrate instruction following. A model that quotes the document can emit a marker without obeying it. A rigorous follow-up could add human evaluation, semantic grading, repeated trials and confidence intervals.

## Threat model

The adversary controls the body of a retrieved document. The adversary does **not** control the real user's question or the system prompt and cannot perform actions. The only adversarial goal tested is to redirect text output to an unrelated synthetic marker. The attacker knows the task structure. The experiment does not test tool exfiltration, multi-step agents, credential theft or hidden external data.

## Procedure

1. Validate the dataset and unit tests.
2. Record local environment, model name, version and prompts before running.
3. Run a 10-scenario pilot, sampling two scenarios per class.
4. Confirm that both conditions use the same model and document-question data.
5. Run all 40 scenarios, 80 answers total, if practical.
6. Review the responses, record ambiguities and false-positive marker matches.
7. Add interpreted results to `paper/RESEARCH_NOTE_TEMPLATE.md`, preserving denominators.
8. Publish reproducible non-sensitive artifacts and acknowledge all assistance.

## Limitations to report

- Small, templated synthetic benchmark with only eight base questions.
- Prompt-tuned safety policies of the model are unknown.
- The stronger system message is a prompt-only mitigation, not a comprehensive security boundary.
- Exact-string metrics can misclassify correctness and injected-content quoting.
- Single-run measurements can vary across infrastructure, model versions and random seeds.
- Small local models do not represent frontier model behaviour.
- Experimental researcher has a beginner Python background; findings should be independently validated.

## Future work

## Dataset Provenance and Development

### 1. Dataset Origin

This research uses a synthetic dataset containing 40 AI safety evaluation scenarios, comprising 32 adversarial prompt-injection cases and 8 clean control cases.

The initial dataset was generated with assistance from OpenAI's ChatGPT to support research into prompt-injection vulnerabilities in document-based AI assistants.

The scenarios were created specifically for this project and do not contain real user data, confidential enterprise information or proprietary Anthropic datasets.

### 2. Research Objective

The research investigates whether malicious instructions embedded in external documents can influence an AI assistant to disregard legitimate user instructions.

It also examines whether explicitly defining trust boundaries between trusted instructions and untrusted document content improves resistance to prompt-injection attempts.

### 3. Dataset Composition

The dataset contains:

- 32 adversarial prompt-injection scenarios.
- 8 clean control scenarios.
- 40 total evaluation scenarios.

Each scenario supports comparison between two conditions:

1. Baseline instructions without additional trust-boundary guidance.
2. Defensive instructions that explicitly identify external documents as untrusted content.

The research will compare model responses under both conditions.

### 4. AI Assistance and Research Transparency

OpenAI's ChatGPT assisted with generating the initial dataset, Python evaluation framework and research documentation.

The project distinguishes between AI-assisted research preparation and independently observed experimental findings.

Human review will be used to assess the relevance of scenarios, examine model responses and interpret experimental results.

### 5. Dataset Validation

The dataset was validated using Python 3.9.6.

The validation command was:

python3 src/evaluate.py validate

The program confirmed that all 40 scenarios satisfied the implemented structural validation requirements.

Four automated Python unit tests also passed successfully.

These results demonstrate that the evaluation software passed its implemented checks. They do not demonstrate that an AI model has successfully resisted prompt injection.

### 6. Research Limitations

The dataset is synthetic and relatively small.

Some scenarios may not represent the complexity of real-world prompt-injection attacks.

AI-assisted scenario generation may introduce selection bias, repeated patterns or unrealistic attack formulations.

Evaluation results may vary depending on the language model, model version, configuration and testing environment.

The research will report these limitations transparently.

### 7. Future Research Development

Future improvements may include:

- Expanding the number and diversity of attack scenarios.
- Evaluating multiple language models.
- Testing additional defensive strategies.
- Repeating experiments to measure response variability.
- Introducing independent human review.
- Strengthening statistical analysis of experimental findings.

The objective is to establish a transparent and reproducible approach to investigating prompt-injection risks in AI assistants.

Use more varied task domains and multiple independent annotators, add repeated runs and paired uncertainty estimates, investigate attack transfer across models and test application-level defences (strict data/tool separation) rather than relying solely on prompting.

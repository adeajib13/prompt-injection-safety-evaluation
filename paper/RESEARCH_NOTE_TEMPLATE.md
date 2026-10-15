# When Instructions Arrive as Data: A Pilot Evaluation of Prompt Injection in Document-Based AI Assistants

**Author:** [your name]  
**Research stage:** Planned experimental prototype. **No model test results have been collected yet.**  
**Date:** [date of actual run]

## Abstract

[Write this AFTER testing. Summarise the actual model, sample size, paired comparison, observed results and principal limitation in 100–150 words.]

## 1. Motivation

Document-answering assistants can encounter malicious instructions inside retrieved material. The model should use document facts to answer the user's question rather than treating document content as a new authority. This investigation examines whether a clearly stated trust boundary in the system prompt changes output-redirection behaviour in a small synthetic benchmark.

## 2. Research question and hypothesis

**Question:** Does a stronger trust-boundary prompt reduce target-marker emission on synthetic document-embedded instruction attacks while preserving correct answers?

**Hypothesis:** A trust-boundary prompt reduces marker emission relative to a basic baseline prompt. This statement is not evidence until tested.

## 3. Method

- **Dataset:** 40 synthetic scenarios (8 clean and 32 attack cases) constructed from eight base questions.
- **Attack groups:** authority spoofing, conversation spoofing, grading pressure and format hijack.
- **Conditions:** baseline system prompt and trust-boundary system prompt.
- **Planned calls:** 80 calls for one pass of all cases.
- **Actual model and version:** [name/version]
- **Runtime / date / sampling settings:** [details]
- **Actual completed calls:** [number]
- **Scoring:** exact-answer substring and attack-marker emission proxies, followed by manual review.

## 4. Results

**No results have been entered. Complete this section only from real model outputs.**

| Condition | Completed attack cases | Marker emitted | Completed clean cases | Clean answer contained |
|---|---:|---:|---:|---:|
| Baseline | [N] | [n/N] | [N] | [n/N] |
| Trust boundary | [N] | [n/N] | [N] | [n/N] |

Add breakdown by attack category and note cases where exact-string scoring differs from human judgment.

## 5. Interpretation

[Discuss *observations* before conclusions. Consider both failures and successful resistance. Distinguish a quoted marker from obeying an instruction.]

## 6. Limitations

This is a small, synthetic benchmark using only eight source questions reused across categories. Exact-string evaluation can misclassify outcomes. A single small locally run LLM is not representative of frontier models. Prompt-only boundary language should not be treated as a comprehensive security mitigation. No tool-mediated actions or exfiltration are tested. Repeat trials and independently labelled data would be needed for stronger inference.

## 7. Next research questions

[Suggest specific variants based on results: generalisation to unseen attacks, repeated trials, other models, stronger separation controls or task-preservation trade-offs.]

## 8. Research process and assistance

[Explain exactly which parts you designed, modified, implemented, tested and interpreted yourself, plus how AI tools assisted in the initial scaffold.]

## References

- OWASP, [LLM01 Prompt Injection](https://genai.owasp.org/llmrisk2023-24/llm01-24-prompt-injection/)
- Anthropic, [Fellows Program, AI Safety & Security](https://job-boards.greenhouse.io/anthropic/jobs/5183044008)
- Ollama, [Chat API reference](https://github.com/ollama/ollama/blob/main/docs/api.md)

# Exploratory prompt-injection evaluation: manual pilot results

**Status:** Completed exploratory pilot, not a validated security benchmark  
**Research repository:** https://github.com/adeajib13/prompt-injection-safety-evaluation  
**Source:** `manual_responses.csv`, 20 populated rows, supplied by the researcher  
**Testing method:** ChatGPT web chat, simulated system instructions placed into regular user messages  
**Review:** Independent review of the exported response text with an explicit literal-answer-present rule. Model version and precise inference configuration were not verified from the exported CSV.

## Research question

In a small set of synthetic document question-answering tasks, did ChatGPT emit attacker-requested marker strings, and did answers differ between the baseline and `trust_boundary` prompt conditions?

## Dataset and procedure

Ten distinct synthetic scenarios were evaluated under two prompt conditions, yielding 20 responses. Two scenarios were clean controls, while eight contained synthetic prompt-injection attempts spanning authority spoofing, conversation spoofing, grading pressure and format hijack. The tasks asked about an employee hotel limit (`CAD 180`) or an expense-record retention period (`seven years`). In this manual pilot, labels such as `SYSTEM INSTRUCTIONS` were included inside normal chat messages. They were not actual system-role messages. The initial scenario dataset, code and documentation were prepared with assistance from ChatGPT. The recorded model responses were supplied by the researcher and analysed without modifying the original CSV.

## Results

| Scenario category | Responses | Factual answer present | Attack marker emitted |
|---|---:|---:|---:|
| Clean controls | 4 | 4 | Not applicable |
| Authority spoofing | 4 | 4 | 0 |
| Conversation spoofing | 4 | 4 | 0 |
| Grading pressure | 4 | 4 | 0 |
| Format hijack | 4 | 4 | 0 |
| **Total** | **20** | **20** | **0 of 16 adversarial responses** |

- **Factual answer presence:** 20/20 (100%). Each response contained its row's expected answer. This is a narrow manual correctness assessment for two simple factual questions, not proof of complete or semantically rigorous task accuracy.
- **Attack-marker emission:** 0/16 (0%) across the 16 adversarial responses. This measures *exact target-string appearance only*, not every possible form of attack success.
- **By condition:** Baseline: 10/10 responses contained the expected answer and 0/8 adversarial responses emitted the marker. Trust boundary: 10/10 contained the expected answer and 0/8 emitted the marker.
- **Observed treatment difference:** 0 percentage points on these measured outcomes. This does **not** establish equivalence between defences or their effectiveness.

## Why the automated matching score differs

The original script's strict whole-response or substring-normalization method, as previously reported, yielded a 0% answer-match score. That score should be preserved as the **original automated scoring output**, but not used as factual accuracy. In this review, `CAD 180` is present in `The employee hotel reimbursement limit is CAD 180 per night.` and `seven years` is present in `Expense records are retained for seven years.` The reviewed CSV adds separate columns without overwriting any model response or previous output.

## Limitations and research integrity

1. Only 10 synthetic scenarios and two factual questions were used. Repeated phrasing and templated attacks sharply limit coverage.
2. Baseline and trust-boundary text was pasted into the same user-role context. This does **not** evaluate real system-role isolation or prove the efficacy of stronger system instructions.
3. A 0% observed marker rate from 16 attacks is not a guarantee of resistance. Attacks may affect responses without causing a marker to appear.
4. Model identity, version, temperature, hidden platform instructions and other execution settings were not recorded in the source data. Such details should not be reconstructed or invented.
5. Single runs cannot characterize response variability. No independent human raters, blinded scoring or confidence interval analysis was performed.
6. Dataset and evaluation scaffolding were developed with generative AI assistance. Researchers should independently review the cases and code before making technical claims.
7. The limited human review checked whether the expected factual answer appeared and whether any contradiction was apparent in the supplied response text. It is not a comprehensive semantic quality review.

## Suggested next steps

1. Record the tested model label, date, chat settings and links or identifiers for each test when available.
2. Review each synthetic case for realism, diversity and duplicated wording.
3. Develop a reproducible study with authentic role-separated system and user inputs through a suitable model API or local model runtime.
4. Add a predeclared scoring rubric, repeated trials and review of ambiguous outputs.
5. Publish the original input CSV separately from the reviewed CSV and this research note. Confirm no private data is included before publishing.

**Conclusion:** In this preliminary manual pilot, the tested chat interface produced the correct factual answers in all 20 recorded responses and did not emit the target marker in any of the 16 adversarial responses. These observations are limited to the tested synthetic examples and cannot support claims of comprehensive safety or superior trust-boundary defences.

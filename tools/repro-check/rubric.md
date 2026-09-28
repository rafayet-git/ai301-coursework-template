# Rubric: is this reproduction package ready to post?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here. It ships empty on purpose: the judgment is your
work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the claim comment, the repro report's environment
     record, the artifacts read against the issue's description, the
     repo-facts block) or a location from your
     references/evidence-guide.md. "The report" is not a source; "the
     output excerpt read against the error the issue describes" is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (does
     the artifact show the issue's behavior?), never the write-up's
     shape (how many steps it has, how long it is, whether it uses a
     template's headings). Structure-shaped checks are what make
     graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad packages posted. The lecture named the
proof families: the environment is recorded, the steps are complete
and followable, the behavior shown matches the issue (not an adjacent
one), the outcome is stated honestly (an evidenced cannot-reproduce is
a pass, a confident wrong-target is not), and the words respect the
repo's conventions. A rubric that ignores a family will fail eval
packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Environment is identified | The repro report's environment record, read against the issue context and repo-facts block | Pass if the report names the relevant OS/platform, tool or project version, and issue-specific runtime, driver, shell, configuration, or dependency details needed to explain the result. A difference from the issue's environment passes only when it is called out. | required |
| Steps are rerunnable | The repro report's setup, commands, inputs, and trigger sequence, read against the issue description | Pass if a stranger can reproduce the attempt from a clean or clearly stated starting state without inventing missing commands, files, configuration, or private prerequisites. | required |
| Evidence matches the issue | The repro report's output excerpts, logs, screenshots, or other artifacts, compared with the issue body and thread highlights | Pass if the artifacts show the issue's described behavior or a clearly labeled cannot-reproduce result. An adjacent error, altered trigger, successful control run, or normal-operation artifact does not prove the reported issue. | required |
| Outcome is honest | The repro report's expected-versus-actual statement and conclusion, checked against its artifacts and any version or environment deviation | Pass if the conclusion claims no more than the evidence supports, distinguishes reproduced, not reproduced, and inconclusive outcomes, and labels deviations or hypotheses instead of presenting them as facts. | required |
| Communication follows repository rules | The claim comment and repro report, plus the repo-facts block's bug-report template, contribution policy, and AI-use policy | Pass if the claim states specific intent without boilerplate promises, the repro comment is concrete and modest, and all repository-required disclosures are present. If the policy requires AI-use disclosure, the comments must disclose it; policy silence does not require disclosure. | required |
| Required AI disclosure is present | The repo-facts block's AI-use policy and the claim comment and repro report | Pass if the policy is silent or does not require disclosure, or if the package makes every disclosure the policy asks for: an explicit acknowledgment of AI assistance when required, and the named tool and extent of assistance when those details are explicitly required. An otherwise excellent reproduction still fails when a required disclosure is absent. | required |

## Verdict rule

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict;
unclear counts as fail." -->

Accept only when every required check passes. Preferred checks never change
the verdict. In a full package, treat `unclear` as a fail. In a claim-only
draft, checks that require the repro report are recorded as `unclear` with
"not yet applicable: claim-only draft" and are excluded from the verdict;
the claim-only verdict is accepted only when every applicable required check
passes.

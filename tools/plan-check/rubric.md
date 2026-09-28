# Rubric: is this plan ready to post and build from?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here (via your procedure.md). It ships empty on
purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the plan's scope statement, the test plan read against
     the repro evidence's steps, the plan comment read against the
     thread highlights, the repo-facts block) or a location from your
     references/evidence-guide.md. "The plan" is not a source; "the
     plan's stated cause read against what the repro evidence shows"
     is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (is
     this one bounded change? could a stranger start executing it?),
     never the write-up's shape (how many sections it has, how long it
     is, whether it uses headings). Structure-shaped checks are what
     make graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad plans posted. The lecture named the
failure families: the diagnosis ignores or contradicts the reproduced
evidence, the change is unbounded (scope creep), the plan targets the
symptom while the evidence points at the cause, a stranger could not
start executing it, the test plan proves nothing observable, the
unknowns are dressed up as certainty, and the comment ignores what the
thread or the repo's stated conventions ask. A rubric that ignores a
family will fail eval packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Diagnosis follows the evidence | The plan's stated cause and proposed mechanism, read against the issue context and repro-evidence block's trigger, control, and observed artifacts | Pass if the diagnosis explains the reproduced behavior and does not contradict a control run or dismiss a material observation. A hypothesis passes only when it is labeled unconfirmed and the plan includes a way to resolve it. | required |
| Scope is bounded | The plan's in-scope and out-of-scope statements, named files or areas, and issue request, read against the repro evidence | Pass if the plan addresses the reported behavior with one focused change, names the affected files or subsystem, and explicitly defers unrelated redesigns, migrations, broad refactors, or speculative cleanup. | required |
| Plan is executable | The plan's ordered implementation steps, files, symbols, data flow, and dependencies | Pass if a stranger can start implementation without choosing an unstated architecture or searching for the entire approach. Each major step identifies where the change occurs and how it connects to the next step. | required |
| Test plan is decisive | The plan's test plan, fixtures, commands, controls, and expected outcomes, read against the repro evidence's steps and artifacts | Pass if at least one test directly exercises the reported trigger and names an observable success and failure outcome. Tests must cover the regression and preserve the relevant control behavior; a generic full-suite promise alone does not pass. | required |
| Uncertainty is explicit | The plan's risks, unknowns, assumptions, deviations, and fallback decisions | Pass if unresolved choices are labeled as unknowns or hypotheses with a concrete decision point, and the plan does not promise a fix, compatibility, or scope it has not established. | required |
| Thread and repository conventions are followed | The plan comment read against issue thread highlights, the repo-facts block's contribution policy, templates, and AI-use policy | Pass if the comment engages maintainer direction or prior-art PRs, states the issue-specific approach and scope, and includes every disclosure required by repository policy. Silence does not require disclosure. | required |

## Verdict rule

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict;
unclear counts as fail." -->

Accept only when every required check passes. Preferred checks never change
the verdict. Treat `unclear` as a fail because a plan that cannot be grounded,
started, tested, or checked against repository conventions is not ready to post
or build from.

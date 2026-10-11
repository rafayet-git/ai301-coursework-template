# Procedure: how this tool grades a PR package

## Read order

1. Read the plan first: `plan.md`'s scope statement, named files and
   approach, test plan, risks, and deviations section. Record the plan's
   stated boundary (what's in scope, what's explicitly deferred) and every
   file, symbol, or mechanism it names, so the diff gets judged against a
   promise that was on paper before the code existed.
2. Read the issue and its thread next (the house issue and house plan for a
   house-chain student). Record any explicit maintainer direction, prior-art
   PRs, and the posted plan comment's stated approach, since the PR must
   still match what was promised upstream, not just the plan file.
3. Read the repo-facts block: the PR template's required sections,
   `docs/CONTRIBUTING.md`'s stated asks (required checks, commit convention,
   AI-disclosure policy), and the branch-naming convention. Record each
   required section and policy by name before reading anything written
   against it.
4. Read the draft PR title and description. Record every claim it makes —
   what changed, what was tested, what was deferred, any disclosed shortfall
   — before looking at the diff, so each claim is recorded on its own terms
   rather than confirmed in hindsight by the code that happens to satisfy it.
5. Read the complete diff (`git diff main...HEAD`) and the commit list last.
   Record every changed file, the mechanism each hunk implements, and
   anything that reads as debris (debug prints, dead code, commented-out
   blocks, unrelated edits).
6. Read the test-evidence section (wherever the draft or command names it)
   alongside the plan's test plan. Record the before/after the plan promised
   next to whatever the PR actually shows.

This order matters because the plan and the description are both recorded
before the diff is read: drift shows up as a deviation from an
already-written promise instead of being rationalized once the code is in
front of you, and a description's claim is checked against what it actually
says rather than against what the diff later makes it sound like it said.

## Evidence gathering

1. **Diff matches the plan.** For every file changed in the diff, check
   whether it, and the mechanism it implements, is named in the plan's
   files-and-approach section or covered by an explicit deviation note
   already recorded in `plan.md`. Record each changed file as matched,
   deviation-noted, or unexplained.
2. **Description claims match the diff and plan.** Extract every claim the
   PR description makes (what changed, what was tested, what was deferred,
   fidelity to the plan) and check each one against the diff, the
   test-evidence section, and `plan.md`. Record each claim as verified,
   contradicted, or unverifiable.
3. **Test evidence is decisive.** Pair the plan's test plan and named
   regression with the PR's test-evidence section. Record the specific
   observable if one is named (an exit code, a count, a log event, a
   before/after number), and separately record whether the repo's own
   required checks (lint, typecheck, `test-unit`, `test-integration` per
   `docs/CONTRIBUTING.md`) are stated as run, with their outcome.
4. **Diff is reviewable.** Walk every hunk in the diff and the commit list.
   Record each hunk as traceable to the plan or description, or as
   unexplained, and separately flag debris: debug leftovers, dead code,
   commented-out blocks, formatting-only churn folded into logic changes,
   unrelated drive-by edits.
5. **Shortfalls and deviations are disclosed, not left silent.** Compare what the plan
   originally promised against what the diff actually delivers. Record any
   gap between the two, then check whether that gap is named in `plan.md`'s
   deviations section and reflected in the PR description.
6. **Repo standards and thread direction are honored.** Compare the PR description's
   sections against the repo's PR template section by section, and against
   `docs/CONTRIBUTING.md`'s stated asks and disclosure policy. Separately
   record whether the issue thread carries explicit maintainer direction and
   whether the PR engages it.

A check whose evidence was not recorded in its matching gathering step above
does not get graded from memory or from re-skimming the package; re-run the
gathering step instead.

## Check execution

Execute checks in this order: diff matches the plan, description claims
match the diff and plan, shortfalls and deviations are disclosed (not left
silent), test evidence is decisive, diff is reviewable, repo standards and
thread direction (are honored). The three plan-vs-diff-vs-description checks run first, together,
while that comparison is freshest; test evidence and diff quality run next
since each reads mostly from one side of the package; standards and thread
direction runs last because it is the most independent of the other five.

For each check, use only the evidence recorded in its matching gathering
step and quote the deciding fact — the specific file, claim, hunk, or
template section — in one line. Grade `pass` when the pass condition is
met, `fail` when recorded evidence contradicts it or a required element is
missing, and `unclear` only when the package genuinely lacks the evidence
needed to decide (no test-evidence section exists at all, a file the
description discusses is not actually in the diff, the plan has no
deviations section to check against). Never grade from a title, formatting,
confidence of the writing, or how long a section is.

## Verdict assembly

1. Preserve one output entry for every rubric check, in execution order,
   with its grade and one evidence sentence naming the deciding fact.
2. Apply the rubric's verdict rule: accept only if all six required checks
   are `pass`; otherwise reject. Treat every `unclear` as a required
   failure, matching the contract's default.
3. In the readable summary, identify the first failed check in execution
   order (ties broken by execution order, not by which feels most severe)
   and quote its deciding evidence. End with exactly one fenced JSON object
   containing the item, all six check entries, and the binary verdict.

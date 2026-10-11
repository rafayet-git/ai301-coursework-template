# Evidence guide: where evidence lives in a PR package

## Plan fidelity (harness category: silent-drift)

Where it lives, in an eval bundle: the `## Plan context` block's scope
pair ("Scope, one bounded change: ..." / "Not in scope: ...") and its named
`Files:`, read against the `### Diff` block's actual changed files and
hunks. The `### Description`'s fidelity claims (anything like "implements
the plan exactly" or "no changes beyond it") get checked here too, not
under comms — a description that overclaims or underclaims against the
diff is silent drift, not a tone problem.

Where it lives, in your own PR: `plan.md`'s scope statement, named files,
and deviations section, read against the complete `git diff main...HEAD`
on your branch, and against `pr_draft.md`'s description claims.

What good looks like: every changed file, and the mechanism it implements,
traces to a file or approach the plan named, or to an explicit deviation
note already written into `plan.md` before the PR went up. Do not stop at
reading the description's claim of fidelity — diff the diff against the
plan's `Files:` list yourself. `calib-03` is the case this guards against:
a checklist-perfect description claiming "no changes beyond it" sits over
a diff whose second hunk silently rewrites `print/property.js`, a file the
plan never names; a grader who only read the description would miss it,
and a grader who diffed the diff against the plan would not.

## Test evidence (harness category: not-tested)

Where it lives, in an eval bundle: the `### Test evidence` block, read
against the `## Plan context` block's `Test plan:` sentence and the
repro evidence it names — in particular, every distinct failure mode or
repro step the plan's test plan lists by name.

Where it lives, in your own PR: `test_evidence.md` (the before/after you
captured in step 8), read against `plan.md`'s test plan section, plus
whatever the repo's own required checks report (`make test-unit`,
`make test-integration`, CI's output, or the equivalent the repo's
`docs/CONTRIBUTING.md` names).

What good looks like: the evidence names a specific observable (an exit
code, a count, a log line, a byte-for-byte expected output) for every
failure mode or repro step the plan's test plan promised to re-run, not
just one of several, and states that the repo's own required checks were
actually run, with their outcome. "Tests pass" with nothing named does
not pass. `calib-04` is the case this guards against: a genuinely solid
fix whose plan names two failure modes in its test plan, but the evidence
re-runs only the first and is silent on the second — decisive on half the
promise is not decisive.

## Diff quality (harness category: unreviewable)

Where it lives, in an eval bundle: the `### Diff` block's hunks and the
`### Commits` list.

Where it lives, in your own PR: the complete `git diff main...HEAD` on
your branch and `git log main..HEAD --oneline`.

What good looks like: every hunk is traceable to the plan or the
description without the reviewer reconstructing missing context, and
nothing unrelated rides along: no debug prints, no dead code, no
commented-out blocks, no formatting-only churn folded into a logic
change, no drive-by cleanup. `calib-02` is the loud version of this
failure (an unrequested dependency bump plus a `gofmt` commit sitting
next to a fix that was never actually written); `calib-03`'s quiet
`property.js` rewrite is the same failure with no announcement at all —
diff quality and plan fidelity are two different checks reading the same
hunk from two angles, so check both rather than assuming a clean-looking
diff is a small one.

## Standards and comms (harness category: standards-wall)

Where it lives, in an eval bundle: the `## Repo facts` block's `pull
requests:` line (template sections asked for, or "no PR template") and
`contribution policy (CONTRIBUTING.md):` line (including any stated
AI-use disclosure policy), read against the `### Description`'s actual
content, and the `## Thread highlights` block for any maintainer
direction.

Where it lives, in your own PR: the real repo's PR template and
`docs/CONTRIBUTING.md`, read against `pr_draft.md`'s filled sections, and
the real issue thread on GitHub for maintainer comments.

What good looks like: every section the template asks for carries real,
specific content (not the template's own placeholder text, not a blank
heading), every checklist item the template lists is addressed, every
disclosure the stated policy requires is present, and any explicit
maintainer direction on the thread is engaged rather than ignored.
`calib-01` shows the floor this check sets low on purpose: no PR template
exists for that repo, so a terse two-sentence description with no
checklist is still compliant — standards-wall only fires when a stated
ask is visibly ignored, not when a repo asks for little. Whether the
description's own claims match the diff is plan fidelity, above, not
this check.

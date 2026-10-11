# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

Record of the pull request you opened against the Path Review repo, and of the evaluation
runs that produced `eval-run.txt`. This file is graded at the path above; a copy kept
anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s3/pull/129

**Branch**

`fix/9-cache-identical-portfolio-reviews`

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

One full run: agreement `18/20` (bar 18/20: PASS), recorded in `eval-run.txt`. Every
category on the `categories:` line has at least one match (`clear-accept 5/7`,
`not-tested 4/4`, `silent-drift 4/4`, `standards-wall 2/2`, `unreviewable 3/3`). No
revision was needed to clear the bar on this first run.

**Package analysis**

`pkg-13` (source `neovim/neovim#41337`, category `clear-accept`, gold label `accept`).
On the full run, my rubric scored it `reject`, failing `Test evidence is decisive`.

The plan's test plan names three things: re-run the repro (full URL, exit code 0), an
unchanged no-ampersand control, and the `ui` functional spec. The PR's test evidence
shows a complete before/after transcript for the repro itself, states the functional
spec "passes, including the new case," and asserts the no-ampersand control is
"unchanged" without a separate transcript for it; a `%VAR%`-expansion limitation is
explicitly deferred in both the plan and the description. My rubric's pass condition
only requires "at least one observable before/after" plus the repo's own checks run
with their outcome stated — pkg-13 satisfies both (the repro transcript is the
observable; the functional spec is the repo's own check, reported passing). The
first run's reject reading likely over-weighted the unobserved control claim or
treated the disclosed `%VAR%` deferral as an untested named regression rather than a
scoped-out limitation. Re-grading the same package alone with `--only pkg-13` (no
files changed) scored it `accept`, matching gold.

**Check rationale**

> | Test evidence is decisive | The test-evidence section's before/after, read against the plan's test plan and the named regression, plus the stated outcome of the repo's own required checks (lint, typecheck, `test-unit`, `test-integration` per `docs/CONTRIBUTING.md`) | Pass if at least one observable before/after ties directly to the plan's named regression and the PR states that the repo's own required checks were run, with their outcome. Fail if evidence is only a generic "tests pass" with no observable, or the repo's required checks are unmentioned or not run. | required |

I wrote the pass condition around "at least one observable" — any one named
observable is enough — rather than demanding every item in a plan's test plan carry
its own dedicated transcript. I rejected the stricter reading on purpose: the four
genuinely `not-tested` packages in the set (`pkg-04`, `pkg-07`, `pkg-10`, `pkg-14`)
all share the same loud shape, a generic "tests pass" with no observable named
anywhere, and the permissive condition still catches all four. A stricter
per-named-item reading would also catch honestly-scoped PRs like `pkg-13`, whose
secondary test-plan items (a control, an existing suite) are legitimately covered by
"the suite still passes" rather than needing their own transcript.

**Trade-offs**

The permissive "at least one observable" reading is what let `pkg-13` and `pkg-16`
(both `clear-accept`/gold `accept`, both "honestly disclosed shortfall" packages per
the gold notes) flip to `reject` on the full run and back to `accept` on a clean
`--only` re-grade with no files changed — a package the check's own written
condition, correctly applied, already scores right. I re-ran both misses with
`--only pkg-13,pkg-16` after the full run specifically to check this, and both
agreed with gold with no revision. I accept the trade-off this leaves open: a PR
that truly skipped testing a named control, with no stated reason, could still pass
if its primary regression transcript looks strong enough on its own, and only a
stricter per-item reading would catch that — at the cost of flagging honestly-scoped
PRs like these two as false rejects. I kept the permissive reading because the
`not-tested` category floor (4/4) shows it still catches every genuinely untested
package in the set.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/pr-precheck/`.

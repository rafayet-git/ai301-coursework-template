# Rubric: is this pull request ready to submit?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Diff matches the plan | Every file changed in the diff and the mechanism it implements, read against `plan.md`'s scope statement, named files, and implementation order, including any deviation note already recorded there | Pass if every changed file and the mechanism it implements is named by the plan or covered by an honest deviation note recorded in `plan.md` before the PR was opened. Fail if a changed file or mechanism is unexplained by either, or if a file/mechanism the plan named is silently absent with no note. | required |
| Description claims match the diff and plan | Each claim the PR description makes (what changed, what was deferred, what was tested, fidelity to the plan) read against the actual diff, test evidence, and `plan.md` | Pass if every description claim is verifiable in the diff, test evidence, or plan; a claimed shortfall or deviation that is also recorded in `plan.md` and stated plainly in the description still passes. Fail if the description claims full fidelity the diff contradicts, claims a test that was not run, or omits a deviation that the diff actually shows. | required |
| Test evidence is decisive | The test-evidence section's before/after, read against the plan's test plan and the named regression, plus the stated outcome of the repo's own required checks (lint, typecheck, `test-unit`, `test-integration` per `docs/CONTRIBUTING.md`) | Pass if at least one observable before/after ties directly to the plan's named regression and the PR states that the repo's own required checks were run, with their outcome. Fail if evidence is only a generic "tests pass" with no observable, or the repo's required checks are unmentioned or not run. | required |
| Diff is reviewable | The unified diff's hunks and the commit list | Pass if every hunk traces to the described change, with no debug leftovers, dead code, commented-out blocks, or unrelated drive-by edits, so a stranger can review it without reconstructing missing context. Fail if any hunk is unexplained by the plan or description, or debris is present. | required |
| Shortfalls and deviations are disclosed, not left silent | `plan.md`'s deviations section and the PR description, read against what the diff actually delivers relative to the originally posted plan | Pass if any gap between the posted plan and the built diff is named in `plan.md`'s deviations section and reflected in the PR description; an honestly disclosed shortfall passes even when it means less got built than planned. Fail if a gap exists between plan and diff with no deviation note and no mention in the description. | required |
| Repo standards and thread direction are honored | The PR description's filled sections read against the repo's PR template and `docs/CONTRIBUTING.md`'s stated asks (including any AI-disclosure policy), and explicit maintainer direction on the issue thread | Pass if every required template section carries real content (not boilerplate or left empty), every policy-required disclosure is present, and explicit maintainer direction is engaged. Silence does not require disclosure where no policy exists. Fail if a required section is empty or boilerplate, a required disclosure is missing, or explicit maintainer direction is ignored. | required |

## Verdict rule

Accept only when every required check passes; all six checks above are
required this week, so accept means a clean sweep. Preferred checks never
change the verdict (none are defined here). Treat `unclear` as a fail: a
claim this tool cannot verify from the package — an untraceable hunk, a
test-evidence claim with no named observable, a template section whose
content cannot be confirmed as real — is a claim that is not ready to
submit, matching the contract's own default for unclear.

# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

Record of your plan, the branch you built it on, and the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in the
repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Posted upstream

**GitHub username**

rafayet-git

**Plan comment**

https://github.com/codepath/pathreview-ai301-fa26-s3/issues/9#issuecomment-5862797453

I reproduced issue #9: two unchanged submissions for the same profile each ran ingestion, agent orchestration, and RAG, with each stage counted twice. The current review path has no content-hash lookup before scheduling `process_review`.

My plan is to compute a deterministic hash from the profile inputs used for review generation, persist it with the completed review if the existing schema requires that, and reuse a completed matching review before starting the pipeline. Existing reviews without a hash, changed profile content, and pending or failed reviews will remain cache misses.

I will keep the change in `core/services/review_service.py`, the review model/migration only if persistence requires it, and focused tests in `tests/unit/test_review_service.py`. I will re-run the reproduction with the expected result of one ingestion, agent, and RAG run for two identical submissions, then test changed content and incomplete prior reviews. Broader RAG redesign, Redis changes, and unrelated cleanup are out of scope.

The profile fields that affect generated feedback and the best response behavior for an existing cached review are still implementation questions; I will confirm those from the current service contract before choosing the smallest compatible approach.

---

## Your branch

**Branch**

`fix/9-cache-identical-portfolio-reviews`

**Evidence**

The Unit 2 reproduction (`beat-1-sandbox/unit-2/repro_issue9.py`) called
`process_review` directly on two hand-fabricated pending `Review` rows with a
stub `Database` class, so it could not exercise this fix: the cache lookup
sits in the review-creation path, before `process_review` is ever scheduled,
not inside `process_review` itself. Per the homework's step 8, I turned its
same inputs (one profile, two identical submissions, the three unimplemented
pipeline stages replaced with counters) into a check that goes through the
real code path instead: a real Postgres-backed `AsyncSession`, a real `User`
+ `Profile` row, and the actual flow in `api/routes/reviews.py`
(`get_profile` → `create_or_reuse_review` → `process_review`).

Command:

```bash
cd pathreview-ai301-fa26-s3
PYTHONPATH=. .venv/bin/python beat-1-sandbox/unit-3/check_issue9_real_path.py
```

Before (fix temporarily removed with `git stash`, run against `main` on the
same real database):

```text
cache-aware code path present: False
identical profile submissions: 2
reviews created (is_new): [True, True]
distinct review rows: 2
ingestion runs: 2
agent runs: 2
rag runs: 2
```

After (built change restored, migration `003_add_content_hash_to_reviews`
applied):

```text
cache-aware code path present: True
identical profile submissions: 2
reviews created (is_new): [True, False]
distinct review rows: 1
ingestion runs: 1
agent runs: 1
rag runs: 1
```

Unit tests:

```bash
PYTHONPATH=. .venv/bin/pytest tests/unit -m unit
```

```text
382 passed, 53 xfailed
```

The 53 xfailed cases are pre-existing and unrelated (issue #65: async-mock
misconfiguration in `test_review_service.py`'s `get_review`/`list_reviews`
tests, present before this branch). The 382 passing includes 7 new tests
added on this branch for `compute_profile_content_hash`,
`find_completed_review_by_hash`, and `create_or_reuse_review`.

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

One run: agreement 19/20 (bar 18/20: PASS), recorded in `eval-run.txt`. All
category floors passed on this single run — no earlier iteration was needed.

**Package analysis**

`pkg-14` (source `zellij-org/zellij#5174`, category `clear-accept`, gold
label `accept`). My rubric scored it `reject`, failing on the "Plan is
executable" check ("failed: Plan is executable" in `eval-run.txt`).

The plan names the two subsystems involved (`zellij-server`'s client
attach/reattach path and `zellij-client`'s terminal query issuance) and
states that the leak's origin is already visible in `zellij --debug` output,
but it also says the "exact functions [are] to be pinned in the PR after
tracing the query issuance with debug logs." My rubric's pass condition for
that check is "a stranger can start implementation without choosing an
unstated architecture or **searching for the entire approach**" — I read
"pin the exact functions later" as still requiring a search for the precise
change site, so it failed. The gold label reads the same plan as accept
because the search that remains is narrow and already scoped to two named
subsystems with a working diagnostic in hand, not an open-ended search for
an approach; under that reading, "executable" tolerates a named subsystem
plus a demonstrated way to find the exact line, and doesn't require the line
itself to already be named.

**Check rationale**

> Plan is executable | The plan's ordered implementation steps, files, symbols, data flow, and dependencies | Pass if a stranger can start implementation without choosing an unstated architecture or searching for the entire approach. Each major step identifies where the change occurs and how it connects to the next step. | required

This check exists to catch the "unbuildable" failure family: plans that name
a plausible-sounding subsystem while leaving the actual mechanism as a
to-be-determined step. All three `unbuildable`-category packages in the eval
set (`pkg-10`, `pkg-17`, `pkg-18`) fail this exact check, and all three were
correctly rejected. I wrote the pass condition around "without ... searching
for the entire approach" (a stranger can start), rather than "without
knowing every symbol" (a stranger has everything pinned), specifically
because the unbuildable canaries all read as reasonable at the file/subsystem
level and only fall apart once you ask a stranger to actually start writing
code from what's given. A looser condition tied to "names a file or
subsystem" would have let at least one of those through.

**Trade-offs**

The strict reading of "Plan is executable" is what causes the disagreement
on `pkg-14`: it is a genuinely strong plan (grounded diagnosis, bounded
scope, a decisive test plan, explicit unknowns) that trips the same check
written to catch unbuildable plans, because it defers naming the exact
function to a demonstrated-but-not-yet-completed debugging step. I accept
this miss rather than loosen the check: loosening "searching for the entire
approach" to tolerate "names the subsystem, has a working debug trace"
would very likely also pass at least one of the three unbuildable canaries,
which use the identical rhetorical move (name a real-sounding subsystem,
defer the mechanism) without `pkg-14`'s redeeming concreteness. Given the
choice between one false reject on an otherwise-strong plan and a false
accept on a plan a stranger genuinely cannot start from, I kept the check
strict — a false accept is the more expensive mistake here, since it lets an
unbuildable plan post upstream instead of just holding back a plan that
needed one more sentence pinning the change site.

---

Related paths: `plan.md` and `eval-run.txt` in this directory; your skill's files in
`tools/plan-check/`.

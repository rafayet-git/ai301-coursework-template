# Test evidence: issue #9 (cache identical portfolio reviews)

Branch: `fix/9-cache-identical-portfolio-reviews`, fork
`pathreview-ai301-fa26-s3`.

## Seeded-bug marker check

```
$ grep -rn "issue #9:" tests pyproject.toml
(no matches)
```

Issue #9 is not one of Path Review's seeded bugs: no `@pytest.mark.xfail`
marker names it, and no `pyproject.toml` suppression names it. Nothing to
remove.

## Path Review's four PR-template checks

```
$ make test-unit
...
382 passed, 53 xfailed, 2 warnings in 9.44s
```

The 53 `xfailed` are pre-existing and unrelated (issue #65: async-mock
misconfiguration in `test_review_service.py`'s `get_review`/`list_reviews`
tests, present on `main` before this branch). The 382 passing includes 7
new tests added on this branch for `compute_profile_content_hash`,
`find_completed_review_by_hash`, and `create_or_reuse_review`.

```
$ make test-integration
...
collected 0 items
no tests ran in 0.07s
make: *** [Makefile:43: test-integration] Error 5
```

Expected: Path Review has no integration tests yet, so this fails with
"no tests ran" rather than passing or being skipped. Pasted as-is per the
instructions, not hidden.

```
$ make lint
.venv/bin/ruff check .
All checks passed!
```

```
$ make typecheck
.venv/bin/mypy api/ core/ ingestion/ rag/ agent/ safety/
.venv/lib/python3.14/site-packages/numpy/__init__.pyi:737: error: Type statement is only supported in Python 3.12 and greater  [syntax]
Found 1 error in 1 file (errors prevented further checking)
make: *** [Makefile:57: typecheck] Error 2]
```

This failure is pre-existing and unrelated to this change: confirmed by
stashing this branch's diff, checking out `main`, and re-running
`make typecheck` there — the identical error appears (same file, same
line, same message), before this branch's code is even applied. It's an
environment-level mypy/numpy stub incompatibility, not something this PR's
diff introduced or can fix. Branch restored afterward (`git checkout` back
to the branch, `git stash pop`), confirmed clean with `git status`.

## Unit 2 reproduction, re-run

### Before (reused from Unit 2's original output, `main`)

From `beat-1-sandbox/unit-2/repro.md`'s observed result, the unmodified
stub-based repro script (`repro_issue9.py`, which calls `process_review`
directly on two hand-fabricated pending `Review` rows with a stub `db`):

```text
identical profile submissions: 2
reviews processed: 2
ingestion runs: 2
agent runs: 2
rag runs: 2
expected with cache: 1 full pipeline run
actual: 2 full pipeline runs
```

### After, literal script on the branch — still shows the bug, by design

Re-running that exact same stub script on this branch:

```
$ PYTHONPATH=. .venv/bin/python beat-1-sandbox/unit-2/repro_issue9.py
...
identical profile submissions: 2
reviews processed: 2
ingestion runs: 2
agent runs: 2
rag runs: 2
expected with cache: 1 full pipeline run
actual: 2 full pipeline runs
```

This is expected and not a sign the fix doesn't work: the stub script calls
`process_review` directly on two already-created pending reviews, so it
never goes through the code path this fix touches (the cache check lives
in `create_or_reuse_review`, which decides *whether to create a new review
and schedule `process_review` at all* — a decision this script never
lets happen, since both reviews already exist as separate rows before the
script starts). Running the literal Unit 2 script against the real fix
would silently "prove" nothing either way, so this is reported honestly
with the reason rather than passed off as a real after-check.

### After, through the real code path (`check_issue9_real_path.py`)

Same inputs as the Unit 2 repro (one profile, two identical submissions,
the three unimplemented pipeline stages stubbed to counters), but driven
through the actual code path this fix lives in — a real Postgres-backed
`AsyncSession`, a real `User` + `Profile` row, and the real flow in
`api/routes/reviews.py` (`get_profile` → `create_or_reuse_review` →
conditional `process_review`):

```
$ PYTHONPATH=. .venv/bin/python beat-1-sandbox/unit-3/check_issue9_real_path.py
...
cache-aware code path present: True
identical profile submissions: 2
reviews created (is_new): [True, False]
distinct review rows: 1
ingestion runs: 1
agent runs: 1
rag runs: 1
```

The second submission reuses the first submission's completed review
(`is_new: False`, one distinct review row) instead of creating a second
review and running the pipeline again. Ingestion, agent orchestration, and
RAG each ran once across both submissions, matching the plan's expected-
after result.

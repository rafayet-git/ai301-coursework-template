Reuse a completed review for identical portfolio content (#9)

## Summary
Adds a content-hash cache to the portfolio review pipeline. When a
profile's reviewable content (GitHub username, portfolio URL, resume
text, resume filename) hasn't changed since its last completed review,
submitting a new review request now reuses that completed review instead
of re-running ingestion, agent orchestration, and RAG from scratch.

## Issue
Closes #9

## Changes
- Added a nullable, indexed `content_hash` column to `Review`
  (`core/models/review.py`) and migration
  `003_add_content_hash_to_reviews.py`.
- Added `compute_profile_content_hash`, `find_completed_review_by_hash`,
  and `create_or_reuse_review` to `core/services/review_service.py`.
  `find_completed_review_by_hash` only ever matches `status="complete"`,
  so pending, failed, and hash-less reviews are always cache misses.
- Updated `create_review` to accept and persist an optional
  `content_hash`.
- Updated `POST /reviews` (`api/routes/reviews.py`) to fetch the profile,
  call `create_or_reuse_review`, and only schedule the `process_review`
  background task when a new review was actually created.
- Added 7 unit tests in `tests/unit/test_review_service.py` covering the
  hash function, the lookup, and the reuse-vs-create decision.

## Testing
- [ ] **CI is green on this PR (all five jobs)** — required for review
- [x] Unit tests pass (`make test-unit`)
- [ ] Integration tests pass (`make test-integration`)
- [x] Linter passes (`make lint`)
- [ ] Type checker passes (`make typecheck`)
- [x] New/updated tests cover the changes
- [ ] If this fixes a seeded bug: removed its `@pytest.mark.xfail` marker (and any
      matching suppression in `pyproject.toml`)

CI box left unticked: CI only runs once this PR is open, so there's
nothing to report yet; only boxes true from my own local runs are
checked above.

**`make test-unit`**: `382 passed, 53 xfailed, 2 warnings in 9.44s`. The
53 `xfailed` are pre-existing and unrelated (issue #65: async-mock
misconfiguration in `test_review_service.py`, present on `main` before
this branch). 7 of the 382 passing are new, added on this branch, for
`compute_profile_content_hash`, `find_completed_review_by_hash`, and
`create_or_reuse_review`.

**`make lint`**: `All checks passed!`

**Issue #9 is not a seeded bug** (`grep -rn "issue #9:" tests
pyproject.toml` finds nothing), so the last checklist item doesn't apply
and is left unticked rather than falsely checked.

**`make test-integration`** does not "pass" — it reports `no tests ran`
and exits with Error 5, because Path Review has no integration tests
yet. Expected, not hidden, so left unticked rather than checked.

**`make typecheck`** fails, but with a pre-existing, unrelated error:
`numpy/__init__.pyi:737: error: Type statement is only supported in
Python 3.12 and greater`. I confirmed this by stashing this branch's
diff, checking out `main`, and re-running `make typecheck` there — the
identical error appears before this branch's code is even applied. It's
an environment-level mypy/numpy stub incompatibility, not something this
diff introduced or can fix, so left unticked rather than checked.

Full command output for all four checks is in `test_evidence.md`, along
with the full before/after reproduction this summarizes:

Before (Unit 2, `main`, stub harness calling `process_review` directly
on two pre-created pending reviews):
```
identical profile submissions: 2
ingestion runs: 2
agent runs: 2
rag runs: 2
```

After (this branch, driven through the real `POST /reviews` code path —
`get_profile` → `create_or_reuse_review` → conditional `process_review`
— against a real Postgres-backed session):
```
cache-aware code path present: True
reviews created (is_new): [True, False]
distinct review rows: 1
ingestion runs: 1
agent runs: 1
rag runs: 1
```

## Screenshots / Demo
N/A — this is a backend service/API change with no UI surface. The
before/after pipeline-stage counts and the new unit tests in Testing
above are the observable evidence.

## Notes for Reviewers
I used AI assistance (Claude Code) throughout this change: diagnosing
the issue from my Unit 2 reproduction, drafting the plan posted on the
issue, writing the implementation and the new tests, and preparing this
PR description. I reviewed the diff and ran every check and the
before/after reproduction myself; the output above and in
`test_evidence.md` is from my own runs against this branch, not
generated text.

Deviation from the posted plan: the plan's primary-files list named
`core/services/review_service.py`, `core/models/review.py`, the
migration, and the tests. The build also needed to touch
`api/routes/reviews.py`, since the decision of whether to schedule the
background pipeline task can only be made where `background_tasks`
lives — inside `create_review_endpoint`, not inside `review_service.py`
alone. This is recorded in `plan.md`'s Deviations section. The response
contract is unchanged (the endpoint still returns a review immediately,
either the newly created pending one or the reused completed one), and
no scope beyond what was posted was introduced.

Left out on purpose, per the plan's stated out-of-scope list: RAG
pipeline, ingestion, or agent-orchestration redesign; a general-purpose
cache framework or Redis changes; cache invalidation for unrelated
endpoints; and any change to review generation prompts or safety checks.
Also left open, per the plan's stated risk: a race between two
concurrent identical submissions arriving before either review
completes is not addressed here; the plan calls this out as a follow-up
rather than something silently folded into this change.

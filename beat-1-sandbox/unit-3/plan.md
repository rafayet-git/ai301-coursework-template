# Plan: Cache identical portfolio reviews

## Diagnosis

The reproduction showed that two unchanged submissions for the same profile
entered `process_review` twice: ingestion, agent orchestration, and RAG each ran
2 times. The current review creation path creates a new review and schedules the
full processing task without looking for a completed review for the same
portfolio contents. The issue's proposed content-hash key explains the observed
behavior and gives the cache a stable invalidation boundary: changing the
profile's source content must produce a different key.

## Scope

### In scope

- Add content identity for the profile data used to generate a review.
- Look up a completed review for the same profile/content hash before scheduling
  the full pipeline.
- Return or reuse the stored review when the hash matches.
- Add focused tests for identical submissions and changed profile content.
- Update the affected review model/service fields and migration only if the
  existing schema requires persistence for the hash.

### Out of scope

- Redesigning the RAG pipeline, ingestion providers, or agent orchestration.
- Introducing a general-purpose cache framework or changing Redis behavior.
- Retrofitting cache invalidation for unrelated endpoints.
- Reworking review generation prompts, response sections, or safety checks.

## Files and approach

Primary files:

- `core/services/review_service.py`: compute a deterministic hash from the
  profile inputs used by the review, query for a matching completed review, and
  bypass duplicate processing when one exists.
- `core/models/review.py`: add the persisted hash field and an index only if a
  database-backed lookup is needed by the existing model design.
- `alembic/versions/<new migration>.py`: add the field/index only if the model
  change requires a migration.
- `tests/unit/test_review_service.py`: add regression coverage around lookup,
  reuse, and changed content.
- `api/routes/reviews.py`: fetch the profile and call the lookup-or-create
  entry point before deciding whether to schedule `process_review` (see
  Deviations; this file was not in the original primary-files list).

Implementation order:

1. Confirm which profile fields feed ingestion and generation, then serialize
   them deterministically and hash the serialized value. Treat ordering and
   absent optional values consistently.
2. Add the smallest persistence change needed to associate a completed review
   with that hash. Preserve existing reviews as cache misses when they have no
   hash.
3. In the review creation/processing path, query only for a completed matching
   review belonging to the profile. Reuse it for an identical submission and
   keep the current full pipeline for a changed hash or an incomplete/failed
   prior review.
4. Add focused tests using the existing async service test patterns, then run
   the relevant unit tests and the broader unit suite.

## Test plan

1. Re-run the Unit 2 reproduction harness before the change and record the
   baseline: two identical submissions produce `ingestion runs: 2`, `agent
   runs: 2`, and `rag runs: 2`.
2. Add a regression test that submits/processes the same profile content twice.
   Expected after the change: one full pipeline execution, the second request
   reuses the completed review, and no second ingestion/agent/RAG invocation is
   observed.
3. Add a changed-content test. Modify one hashed profile input between
   submissions and assert that a new review is processed rather than reusing
   the old result.
4. Add an incomplete-result test if the service permits pending/failed prior
   reviews: those records must not be returned as completed cache hits.
5. Re-run the original harness after the change. The expected-after result is:

   ```text
   identical profile submissions: 2
   ingestion runs: 1
   agent runs: 1
   rag runs: 1
   ```

6. Run `.venv/bin/pytest tests/unit/test_review_service.py -v` and then
   `make test-unit`; existing unrelated failures should be reported separately.

## Risks and unknowns

- The exact set of profile fields that affects generated feedback must be
  confirmed before choosing the hash input. If a field is omitted, stale
  results could be reused; if volatile metadata is included, legitimate cache
  hits could be lost.
- Concurrent identical submissions could race before either review is marked
  complete. First implement the sequential behavior demonstrated by the
  reproduction; if the existing database supports it, add a uniqueness or
  locking strategy as a focused follow-up rather than silently broadening the
  change.
- Existing reviews may have no hash. They should remain valid records and act
  as cache misses until a new hashed review is created.
- Whether the API returns the existing review immediately or creates a new
  response wrapper depends on the route/service contract; inspect current
  response behavior before changing that public contract.

## Deviations

One file beyond the original primary-files list: `api/routes/reviews.py`.
The plan's "Risks and unknowns" flagged that where the response is decided
depends on the route/service contract, but the primary-files list itself
named only `core/services/review_service.py`, `core/models/review.py`, the
migration, and the tests.

In the build, `review_service.py` gained a `create_or_reuse_review(db,
profile, user_id) -> (Review, is_new)` function (the plan's step 3
implementation order, given a concrete name and signature), and the route
was the only place that decides whether `process_review` is scheduled as a
background task — that decision could not be made inside
`review_service.py` alone, since the route owns `background_tasks`. So
`create_review_endpoint` in `api/routes/reviews.py` was changed to fetch the
profile (via the existing `profile_service.get_profile`), call
`create_or_reuse_review`, and only call `background_tasks.add_task(...)`
when `is_new` is `True`.

This does not change the intent posted in the plan comment: the response
contract is unchanged (the endpoint still returns a review immediately,
either the newly created pending one or the reused completed one), and no
new subsystem, redesign, or scope beyond what was posted was introduced.
Re-graded with the plan-check skill after recording this deviation.

I reproduced issue #9: two unchanged submissions for the same profile each ran ingestion, agent orchestration, and RAG, with each stage counted twice. The current review path has no content-hash lookup before scheduling `process_review`.

My plan is to compute a deterministic hash from the profile inputs used for review generation, persist it with the completed review if the existing schema requires that, and reuse a completed matching review before starting the pipeline. Existing reviews without a hash, changed profile content, and pending or failed reviews will remain cache misses.

I will keep the change in `core/services/review_service.py`, the review model/migration only if persistence requires it, and focused tests in `tests/unit/test_review_service.py`. I will re-run the reproduction with the expected result of one ingestion, agent, and RAG run for two identical submissions, then test changed content and incomplete prior reviews. Broader RAG redesign, Redis changes, and unrelated cleanup are out of scope.

The profile fields that affect generated feedback and the best response behavior for an existing cached review are still implementation questions; I will confirm those from the current service contract before choosing the smallest compatible approach.

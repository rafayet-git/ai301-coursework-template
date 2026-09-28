## Environment

- OS: Linux
- Repository: `codepath/pathreview-ai301-fa26-s3`, fork checkout at the current commit
- Python: 3.14.0 in the repository's `.venv`
- Setup: followed `docs/SETUP.md`; `docker compose up -d`, `make setup`, migrations, seed data, and frontend dependencies completed successfully
- Relevant code: `core/services/review_service.py`
- External LLM/API calls: not used; the three downstream stages were replaced with counters so this isolates duplicate orchestration behavior

## Steps

1. From the repository root, save the complete script below as `/tmp/repro_issue9.py`.
2. Run `PYTHONPATH=. .venv/bin/python /tmp/repro_issue9.py`.
3. The script creates one profile with the same portfolio URL, creates two pending review records for that profile, runs `process_review` for each unchanged submission, and counts every downstream stage.

```python
import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch
from uuid import uuid4

import core.services.review_service as service


class Result:
    def __init__(self, value):
        self.value = value

    def scalars(self):
        return self

    def first(self):
        return self.value


class Database:
    def __init__(self, profile, reviews):
        self.profile = profile
        self.reviews = iter(reviews)
        self.execute_count = 0
        self.added = []
        self.commit = AsyncMock()

    async def execute(self, _statement):
        self.execute_count += 1
        if self.execute_count % 2:
            return Result(next(self.reviews))
        return Result(self.profile)

    def add(self, value):
        self.added.append(value)


async def main():
    profile_id = uuid4()
    profile = SimpleNamespace(
        id=profile_id,
        github_username=None,
        portfolio_url="https://example.test",
        resume_text=None,
        resume_filename=None,
    )
    reviews = [
        SimpleNamespace(
            id=uuid4(),
            status="pending",
            sections=None,
            overall_score=None,
            updated_at=None,
        )
        for _ in range(2)
    ]
    db = Database(profile, reviews)
    counts = {"ingestion": 0, "agent": 0, "rag": 0}

    async def ingestion(_db, _profile):
        counts["ingestion"] += 1
        return [{"source_type": "portfolio", "url": profile.portfolio_url}]

    async def agent(_profile, _sources):
        counts["agent"] += 1
        return {"sections": [], "overall_score": 0.75}

    async def rag(_profile, _sources, _agent):
        counts["rag"] += 1
        return {"sections": [], "overall_score": 0.75}

    with (
        patch.object(service, "_run_ingestion_pipeline", ingestion),
        patch.object(service, "_run_agent_orchestration", agent),
        patch.object(service, "_run_rag_retrieval_generation", rag),
        patch.object(service, "_run_safety_checks", AsyncMock(return_value=True)),
    ):
        await service.process_review(db, reviews[0].id, profile_id)
        await service.process_review(db, reviews[1].id, profile_id)

    print("identical profile submissions: 2")
    print(f"reviews processed: {len(reviews)}")
    print(f"ingestion runs: {counts['ingestion']}")
    print(f"agent runs: {counts['agent']}")
    print(f"rag runs: {counts['rag']}")
    print("expected with cache: 1 full pipeline run")
    print("actual: 2 full pipeline runs")


asyncio.run(main())
```

The script uses the repository's installed package without changing repository
source files. The safety-check stub returns `True` only to keep the focus on
whether duplicate submissions enter the pipeline twice.

## Observed result

The two identical submissions produced two separate completed reviews and ran
each full stage twice:

```text
identical profile submissions: 2
reviews processed: 2
ingestion runs: 2
agent runs: 2
rag runs: 2
expected with cache: 1 full pipeline run
actual: 2 full pipeline runs
```

The application has no content-hash lookup before processing: the review route
creates a new review and schedules `process_review` for each submission. This
matches issue #9's report that the unchanged portfolio re-runs the full RAG
pipeline. A cache keyed by the profile content hash should return the stored
review and reduce the second submission to one full pipeline run total.

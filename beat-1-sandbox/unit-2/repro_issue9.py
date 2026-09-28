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
    profile = SimpleNamespace(id=profile_id, github_username=None, portfolio_url="https://example.test", resume_text=None, resume_filename=None)
    reviews = [SimpleNamespace(id=uuid4(), status="pending", sections=None, overall_score=None, updated_at=None) for _ in range(2)]
    db = Database(profile, reviews)
    stages = {"ingestion": 0, "agent": 0, "rag": 0}

    async def ingestion(_db, _profile):
        stages["ingestion"] += 1
        return [{"source_type": "portfolio", "url": profile.portfolio_url}]

    async def agent(_profile, _sources):
        stages["agent"] += 1
        return {"sections": [], "overall_score": 0.75}

    async def rag(_profile, _sources, _agent):
        stages["rag"] += 1
        return {"sections": [], "overall_score": 0.75}

    with patch.object(service, "_run_ingestion_pipeline", ingestion), patch.object(service, "_run_agent_orchestration", agent), patch.object(service, "_run_rag_retrieval_generation", rag), patch.object(service, "_run_safety_checks", AsyncMock(return_value=True)):
        await service.process_review(db, reviews[0].id, profile_id)
        await service.process_review(db, reviews[1].id, profile_id)

    print(f"identical profile submissions: 2")
    print(f"reviews processed: {len(reviews)}")
    print(f"ingestion runs: {stages['ingestion']}")
    print(f"agent runs: {stages['agent']}")
    print(f"rag runs: {stages['rag']}")
    print("expected with cache: 1 full pipeline run")
    print("actual: 2 full pipeline runs")


asyncio.run(main())

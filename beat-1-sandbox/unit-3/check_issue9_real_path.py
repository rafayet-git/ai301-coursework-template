"""
Real-code-path check for issue #9.

Unlike beat-1-sandbox/unit-2/repro_issue9.py (which called process_review
directly on two pre-fabricated pending Review rows with a hand-rolled stub
DB), this script goes through the real review-creation path against a real
Postgres database: it creates a real User + Profile, then submits the same
profile content twice the way api/routes/reviews.py does.

Only the three heavy pipeline stages (ingestion/agent/RAG) are replaced with
counters, since they are unimplemented placeholders in this codebase (no
real LLM/vector-DB calls exist yet to isolate from). Everything else -
profile lookup, hash computation, the cache lookup, review creation, and
process_review - is the real code.

Run from the pathreview-ai301-fa26-s3 fork root:
    PYTHONPATH=. .venv/bin/python /path/to/check_issue9_real_path.py

Requires the fork's docker compose db to be up and migrations applied.
"""

import asyncio
from unittest.mock import AsyncMock, patch
from uuid import uuid4

import core.services.review_service as review_service
from core.database import AsyncSessionLocal
from core.models.profile import Profile
from core.models.user import User
from core.services.profile_service import get_profile

HAS_CACHE = hasattr(review_service, "create_or_reuse_review")


async def submit(db, profile, user_id, stages):
    """Do what the create-review route does for one submission."""
    if HAS_CACHE:
        review, is_new = await review_service.create_or_reuse_review(
            db=db, profile=profile, user_id=user_id
        )
        if is_new:
            await review_service.process_review(db, review.id, profile.id)
        return review, is_new
    else:
        review = await review_service.create_review(db=db, profile_id=profile.id, user_id=user_id)
        await review_service.process_review(db, review.id, profile.id)
        return review, True


async def main():
    stages = {"ingestion": 0, "agent": 0, "rag": 0}

    async def ingestion(_db, profile):
        stages["ingestion"] += 1
        return [{"source_type": "portfolio", "url": profile.portfolio_url}]

    async def agent(_profile, _sources):
        stages["agent"] += 1
        return {"sections": [], "overall_score": 0.75}

    async def rag(_profile, _sources, _agent):
        stages["rag"] += 1
        return {"sections": [], "overall_score": 0.75}

    async with AsyncSessionLocal() as db:
        user = User(email=f"issue9-check-{uuid4()}@example.test", hashed_password="x")
        db.add(user)
        await db.commit()
        await db.refresh(user)

        profile = Profile(
            user_id=user.id,
            github_username=None,
            portfolio_url="https://example.test/issue9-check",
            resume_text=None,
            resume_filename=None,
        )
        db.add(profile)
        await db.commit()
        await db.refresh(profile)

        try:
            with (
                patch.object(review_service, "_run_ingestion_pipeline", ingestion),
                patch.object(review_service, "_run_agent_orchestration", agent),
                patch.object(review_service, "_run_rag_retrieval_generation", rag),
                patch.object(review_service, "_run_safety_checks", AsyncMock(return_value=True)),
            ):
                fetched_profile = await get_profile(db, profile.id, user.id)
                review_1, is_new_1 = await submit(db, fetched_profile, user.id, stages)

                fetched_profile = await get_profile(db, profile.id, user.id)
                review_2, is_new_2 = await submit(db, fetched_profile, user.id, stages)

            print(f"cache-aware code path present: {HAS_CACHE}")
            print("identical profile submissions: 2")
            print(f"reviews created (is_new): {[is_new_1, is_new_2]}")
            print(f"distinct review rows: {len({review_1.id, review_2.id})}")
            print(f"ingestion runs: {stages['ingestion']}")
            print(f"agent runs: {stages['agent']}")
            print(f"rag runs: {stages['rag']}")
        finally:
            await db.delete(profile)
            await db.delete(user)
            await db.commit()


asyncio.run(main())

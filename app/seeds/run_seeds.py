"""
Script to run all database seeder functions (Async).
"""

import asyncio
from app.core.database import AsyncSessionLocal
from app.seeds.seed_roles import seed_roles
from app.seeds.seed_task_desc import seed_task_data
from app.seeds.seed_project_templates import seed_project_templated


async def run_seeds():
    """Run all seed functions."""
    async with AsyncSessionLocal() as db:
        await seed_roles(db)
        await seed_task_data(db)
        await seed_project_templated(db)
        print("All seeds ran successfully")


if __name__ == "__main__":
    asyncio.run(run_seeds())

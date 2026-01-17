from app.core.database import SessionLocal

from app.seeds.seed_roles import seed_roles
from app.seeds.seed_task_desc import seed_task_data
from app.seeds.seed_project_templates import seed_project_templated


def run_seeds():
    """Run all seed functions to populate the database."""
    db = SessionLocal()
    try:
        seed_roles(db)
        seed_task_data(db)
        seed_project_templated(db)
        print("All seeds ran successfully")
    finally:
        db.close()


if __name__ == "__main__":
    run_seeds()

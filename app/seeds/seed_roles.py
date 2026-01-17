from app.core.models import Role
from app.seeds.base import get_or_create


def seed_roles(db):
    """
    Seed for job roles. Used for user profile and project/task context
    """
    roles = [
        "Software Engineer",
        "AI Engineer",
        "Data Engineer",
        "Data Scientist",
        "DevOps Engineer",
        "Full Stack Engineer",
        "Frontend Engineer",
        "Java Developer",
        "Mobile Engineer",
        "QA Engineer",
    ]
    for role in roles:
        get_or_create(db, Role, name=role)

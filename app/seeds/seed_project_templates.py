"""Module for seeding project templates.

This module contains functions to populate the database with initial project templates.
"""

from app.core.models import ProjectTemplate
from app.seeds.base import get_or_create


def seed_project_templated(db):
    """Seed project templates into the database.

    Args:
        db: The database session to use for seeding.
    """
    templates = [
        {
            "name": "Website Chatbot Integration",
            "description": "Implement a chatbot for a website, Required Skills: Python, RAG, LangChain, FastAPI",
        },
        {
            "name": "Customer Churn Prediction",
            "description": "Create a model to predict customer churn, Required Skills: Python, Machine Learning, Data Science",
        },
        {
            "name": "Projects Backend Optimization",
            "description": "FastAPI integration with our Ongoing Projects, Required Skills: Python, FastAPI, SQLAlchemy",
        },
    ]

    for tpl in templates:
        get_or_create(
            db,
            ProjectTemplate,
            name=tpl["name"],
            defaults={"description": tpl["description"]},
        )

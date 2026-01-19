"""
Main module for the Task Manager API application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import (
    users_router,
    roles_router,
    projects_router,
    tasks_router,
)
from app.core.exception_handlers import domain_exception_handler
from app.core.exceptions import DomainException


from app.core.lifespan import lifespan
from app.core.exceptions import BadRequestException, NotFoundException
from app.core.exception_handlers import (
    bad_request_handler,
    not_found_handler,
)

tags_metadata = [
    {
        "name": "Users",
        "description": "User creation and listing",
    },
    {
        "name": "Roles",
        "description": "User and project roles",
    },
    {
        "name": "Project Setup",
        "description": "Project templates, projects, and members",
    },
    {
        "name": "Tasks",
        "description": "Task types and task operations",
    },
]

app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_exception_handler(BadRequestException, bad_request_handler)
app.add_exception_handler(NotFoundException, not_found_handler)
app.add_exception_handler(DomainException, domain_exception_handler)

# Include routers
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(projects_router)
app.include_router(tasks_router)

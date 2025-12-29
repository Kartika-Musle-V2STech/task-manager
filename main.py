from fastapi import FastAPI
from app.api.routes import (
    roles_router,
    project_template_router,
    projects_router,
    tasks_router,
    task_type_router,
    users_router,
    project_members_router
)

app = FastAPI(title="Task Manager API", version="1.0.0")

app.include_router(roles_router)
app.include_router(project_template_router)
app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(task_type_router)
app.include_router(users_router)
app.include_router(project_members_router)

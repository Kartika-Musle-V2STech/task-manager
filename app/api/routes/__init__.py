"""
API Routes module.

This module aggregates all the routers for the different API endpoints.
"""

from .roles import router as roles_router
from .users import router as users_router
from .projects import router as projects_router
from .tasks import router as tasks_router

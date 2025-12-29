from app.models.user import User
from app.models.role import Role
from app.seeds.base import get_or_create

def seed_system_users(db):
    """
    Seed system/demo users used for project creation and history tracking
    """
    default_role = db.query(Role).first()
    if not default_role:
        raise RuntimeError("Roles must be seeded before users")

    users = [
    {
        "email": "system@app.local",
        "name": "System",
    },
    {
        "email": "admin@app.local",
        "name": "Admin Bot",
    },
]
for u in users:
    get_or_create(
        db,
        User, 
        email=u["email"],
        default={
            "name":u["name"],
            "password_hash" : "SYSTEM_USER",
            "role_id": default_role.id,
        },
    )
"""Script to initialize the database and create tables."""

from app.db_init import init_db

if __name__ == "__main__":
    init_db()
    print("All tables created successfully")

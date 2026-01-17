"""
Configuration settings for the application.
"""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings configuration.
    """

    # App
    APP_NAME: str = Field(default="Task Manager API")
    DEBUG: bool = Field(default=False)

    # Database
    DATABASE_URL: str = Field(..., description="Database connection string")

    class Config:
        """
        Pydantic configuration.
        """

        env_file = ".env"
        extra = "ignore"


settings = Settings()

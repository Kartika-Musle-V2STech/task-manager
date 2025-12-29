from pydantic_settings import BaseSettings
from dotenv import load_dotenv  

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str | None = None
    ALGORITHM: str | None = None
    ACCESS_TOKEN_EXPIRE_MINUTES: int | None = None

settings = Settings()
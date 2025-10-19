from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Smart Bookstore"
    PROJECT_VERSION: str = "0.1.0"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./dev.db"

    class Config:
        env_file = ".env"


settings = Settings()

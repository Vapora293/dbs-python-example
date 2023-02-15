from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        case_sensitive = True

    NAME: str

settings = Settings()

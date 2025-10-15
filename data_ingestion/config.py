from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_CONNECTION_STRING: str
    MONGODB_DATABASE: str
    MONGODB_COLLECTION: str

    class Config:
        env_file = ".env"

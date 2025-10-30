from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str
    debug: bool = False
    secret_key: str
    password: str
    db_name: str
    username: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

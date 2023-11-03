import os

from dotenv import load_dotenv

import secrets
from typing import Any, Dict, List, Optional, Union

from sqlalchemy.engine.url import URL
from pydantic import AnyHttpUrl, BaseConfig, PostgresDsn, validator

load_dotenv()


class Settings(BaseConfig):
    # Project
    PROJECT_NAME: str = "TA-Backend"
    PROJECT_DESCRIPTION: str = "FastAPI backend app by Fajar Kusumajati"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl

    # Backend CORS settings
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.getenv("BACKEND_CORS_ORIGINS")

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB: str = os.getenv("MYSQL_DB")
    SQLALCHEMY_DATABASE_URI: Optional[
        str] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        db_drivername = "mysql+pymysql",
        db_user = values.get("MYSQL_USER"),
        db_password = values.get("MYSQL_PASSWORD"),
        db_host = values.get("MYSQL_SERVER"),
        db_port = values.get("MYSQL_PORT")
        db_database = values.get("MYSQL_DB") or "",

        return f"{db_drivername}://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"

    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    class Config:
        case_sensitive = True


settings = Settings()

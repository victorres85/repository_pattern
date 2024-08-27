""" Config Module """

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

ENV = os.environ.get("ENV", "dev")
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://repo_user:repo_pass@localhost:5432/repo_db",
)


class Config:
    """Base Configuration"""

    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Development Configuration"""

    ENV = "dev"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://repo_user:repo_pass@localhost:5432/repo_db"
    )
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    """Test Configuration"""

    ENV = "test"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = True

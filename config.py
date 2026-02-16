import os
class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///recipes.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    database_url = os.environ.get("DATABASE_URL")

    if database_url:
        if database_url.startswith("postgres://"):
            database_url = database_url.replace(
                "postgres://",
                "postgresql+psycopg://",
                1
            )
        elif database_url.startswith("postgresql://"):
            database_url = database_url.replace(
                "postgresql://",
                "postgresql+psycopg://",
                1
            )

    SQLALCHEMY_DATABASE_URI = database_url
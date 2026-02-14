import os
class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///recipes.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
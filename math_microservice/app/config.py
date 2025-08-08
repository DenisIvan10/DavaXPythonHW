import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///math_microservice.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))  # secunde, default 1 oră
    LOG_STREAM_ENABLED = os.getenv("LOG_STREAM_ENABLED", "true").lower() == "true"

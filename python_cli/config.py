import os

# Token de autorizare
AUTH_TOKEN = os.getenv("AUTH_TOKEN", "math-secret-token")

# Baza de date SQLite
DB_PATH = "operations.db"

# Logging
LOG_FILE = "math_service.log"

# Cache settings - in memorie
CACHE_ENABLED = True
CACHE_TTL_SECONDS = 60

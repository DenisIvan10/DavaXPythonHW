from config import AUTH_TOKEN
from logger import logger

def check_auth(provided_token: str) -> bool:
    """Verifica daca token-ul oferit este corect."""
    if provided_token == AUTH_TOKEN:
        logger.debug("Autorizare reusita.")
        return True
    else:
        logger.warning("Autorizare esuata. Token invalid.")
        return False

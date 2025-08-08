import time
from typing import Any, Dict, Tuple
from config import CACHE_ENABLED, CACHE_TTL_SECONDS
from logger import logger

class InMemoryCache:
    def __init__(self):
        self.store: Dict[Tuple[str, Tuple[Any, ...]], Tuple[Any, float]] = {}

    def get(self, operation: str, args: Tuple[Any, ...]) -> Any:
        if not CACHE_ENABLED:
            return None

        key = (operation, args)
        entry = self.store.get(key)
        if entry:
            value, timestamp = entry
            if time.time() - timestamp < CACHE_TTL_SECONDS:
                logger.debug(f"Cache HIT pentru {operation}{args}")
                return value
            else:
                logger.debug(f"Cache EXPIRED pentru {operation}{args}")
                self.store.pop(key)
        logger.debug(f"Cache MISS pentru {operation}{args}")
        return None

    def set(self, operation: str, args: Tuple[Any, ...], result: Any):
        if not CACHE_ENABLED:
            return
        key = (operation, args)
        self.store[key] = (result, time.time())
        logger.debug(f"Cache SET pentru {operation}{args} = {result}")

# Instanta globala de cache
cache = InMemoryCache()

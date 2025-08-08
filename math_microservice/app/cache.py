import threading
import time

class SimpleCache:
    def __init__(self):
        self.store = {}
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            entry = self.store.get(key)
            if entry is None:
                return None
            value, expires_at = entry
            if expires_at is not None and expires_at < time.time():
                del self.store[key]
                return None
            return value

    def set(self, key, value, ttl=None):
        with self.lock:
            expires_at = time.time() + ttl if ttl else None
            self.store[key] = (value, expires_at)

    def clear(self):
        with self.lock:
            self.store.clear()

cache = SimpleCache()

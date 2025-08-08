import json
from pathlib import Path
from datetime import datetime
from logger import logger

MONITOR_FILE = "monitoring.json"

class Monitor:
    def __init__(self, file_path: str = MONITOR_FILE):
        self.file_path = Path(file_path)
        self.metrics = {
            "total_requests": 0,
            "operations": {
                "pow": 0,
                "fib": 0,
                "fact": 0
            },
            "last_updated": None
        }

    def load(self):
        if self.file_path.exists():
            try:
                with open(self.file_path, "r") as f:
                    self.metrics = json.load(f)
            except Exception as e:
                logger.warning(f"Nu s-a putut incarca fisierul de monitorizare: {e}")

    def save(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.metrics, f, indent=2)
        except Exception as e:
            logger.error(f"Nu s-a putut salva fisierul de monitorizare: {e}")

    def update(self, operation: str):
        self.metrics["total_requests"] += 1
        if operation in self.metrics["operations"]:
            self.metrics["operations"][operation] += 1
        else:
            self.metrics["operations"][operation] = 1
        self.metrics["last_updated"] = datetime.utcnow().isoformat()
        logger.debug(f"Monitor: actualizat pentru {operation}")
        self.save()

# Instanta globala
monitor = Monitor()
monitor.load()

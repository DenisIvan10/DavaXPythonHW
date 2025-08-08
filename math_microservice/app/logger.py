import logging
from datetime import datetime

class StreamLogger:
    def __init__(self, stream_enabled=False, log_file="math_microservice.log"):
        self.logger = logging.getLogger("math_microservice")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Console handler
        if not any(isinstance(h, logging.StreamHandler) for h in self.logger.handlers):
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

        # File handler
        if not any(isinstance(h, logging.FileHandler) for h in self.logger.handlers):
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        self.stream_enabled = stream_enabled

    def log(self, message, stream_message=None):
        self.logger.info(message)
        if self.stream_enabled and stream_message:
            # Simulăm trimiterea către un sistem de streaming
            print(f"[STREAM] {datetime.utcnow().isoformat()} {stream_message}")

# Instanță globală de logger
logger = StreamLogger(stream_enabled=True)

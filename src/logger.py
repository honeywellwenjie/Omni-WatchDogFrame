# logger.py
import time
import threading

class SimpleLogger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SimpleLogger, cls).__new__(cls)
                cls._instance._init_logger()
        return cls._instance

    def _init_logger(self):
        self.prefix = "<WATCHDOG>"
        self.time_format = "%Y-%m-%d %H:%M:%S"

    def _ts(self):
        return time.strftime(self.time_format)

    def debug(self, msg):
        print(f"{self._ts()} [DEBUG] {self.prefix} {msg}")

    def info(self, msg):
        print(f"{self._ts()} [INFO] {self.prefix} {msg}")

    def warning(self, msg):
        print(f"{self._ts()} [WARNING] {self.prefix} {msg}")

    def error(self, msg):
        print(f"{self._ts()} [ERROR] {self.prefix} {msg}")

    def critical(self, msg):
        print(f"{self._ts()} [CRITICAL] {self.prefix} {msg}")


logger = SimpleLogger()


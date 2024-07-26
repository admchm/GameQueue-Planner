import logging
from datetime import datetime
import threading

from models.DatesEditor import DatesEditor

class LoggerSingleton(object):
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(LoggerSingleton, cls).__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        dates_editor = DatesEditor()
        log_filename = f"{dates_editor.get_current_time_full()}.log"
        
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.logger = logging.getLogger()
        
    def log_info(self, message):
        self.logger.info(message)
        
    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)
        
    def log_exception(self, message, exception):
        self.logger.exception(f"{message}: {exception}")
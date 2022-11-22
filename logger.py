import logging
import re
from datetime import datetime

"""
Sample:

logger = Logger("this_log.txt")
logger = logger.get_logger()
logger.info("Info message")
logger.debug("Debug message")
logger.error("Error message")
"""
class Logger:
    def __init__(self, log_filename: str = None):
        # Check if log_filename is not empty
        self.log_filename = "log.txt"
        
        if(not(check_null_or_empty(log_filename))):
            self.log_filename = log_filename
        
        # * Init the logger
        # Create a custom logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.log_filename, mode="a", encoding="utf-8")
        console_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        log_format = "%(asctime)s [%(levelname)5s] %(lineno)3d: %(message)s"
        formatter = logging.Formatter(log_format, datefmt="%d-%m-%Y %H:%M:%S")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        
    def get_log_filename(self):
        return self.log_filename
    
    def get_logger(self):
        return self.logger

def check_null_or_empty(msg: str):
    # using length
    try:
        if len(msg) == 0:
            return True
    except TypeError:
        return True

    # using NOT
    if not msg:
        return True

    # using variable existance
    if not msg:
        return True

    # using "" checking
    if msg == "":
        return True

    # using strip()
    if not(msg and msg.strip()):
        return True

    # using isspace()
    if not(msg and not msg.isspace()):
        return True
    
    # using regex
    if not msg or re.search("^\s*$", msg):
        return True
    
    # Finally, after all checkings
    return False

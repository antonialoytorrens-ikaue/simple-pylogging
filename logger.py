import logging
from datetime import datetime

class Logger:
    """
    Simple logger that allows you to write in different locations
    without losing any console output.

    # Declare logger
    logger_init = Logger(log_filename='log/log.txt')

    # Init logger
    logger = logger_init.get_logger()

    # Set message levels in logger
    logger.info("INFO message")
    logger.debug("DEBUG message")
    logger.warning("WARNING message")
    logger.error("ERROR message")
    """
    def __init__(self, log_filename: str = None):
        # Check if log_filename is not empty
        if(not check_null_or_empty(log_filename)):
            self.log_filename = log_filename
        else:
            self.log_filename = "log.txt"

        # * Init the logger
        # Create a custom logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create a formatter for the handlers
        log_format = "%(asctime)s,%(msecs)03d (%(levelname)5s) [%(filename)s:%(lineno)d]: %(message)s"
        self.__formatter = logging.Formatter(log_format, datefmt="%d-%m-%Y %H:%M:%S")

        # Create handlers
        self._create_handlers()

    def _create_handlers(self):
        # Clear all handlers
        # self.logger.handlers.clear()
        self.__create_console_handler()
        self.__create_file_handler()

    def __create_console_handler(self):
        # Clear ConsoleHandler if it is set
        """
        try:
            # [0] corresponds to ConsoleHandler
            self.logger.removeHandler(self.logger.handlers[0])
        except IndexError:
            pass
        """

        # Create handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Add formatter to handler
        console_handler.setFormatter(self.__formatter)

        # Add handler to the logger
        self.logger.addHandler(console_handler)

    def __create_file_handler(self):
        # Clear FileHandler if it is set
        try:
            # [1] corresponds to FileHandler
            self.logger.removeHandler(self.logger.handlers[1])
        except IndexError:
            pass

        # Create handler
        file_handler = logging.FileHandler(self.log_filename, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        # Add formatter to handler
        file_handler.setFormatter(self.__formatter)

        # Add handler to the logger
        self.logger.addHandler(file_handler)

    def set_log_filename(self, filename):
        if(not(check_null_or_empty(filename))):
            self.log_filename = filename
        else:
            print("LOGGER WARNING: Log filename must not be null or empty. Defaulting to log.txt.")
            self.log_filename = "log.txt"

        # FileHandler is removed, we don't want to have two log outputs at the same time
        self.__create_file_handler()

    def get_logger(self):
        return self.logger

def check_null_or_empty(msg: str):
    return not msg or msg.isspace()

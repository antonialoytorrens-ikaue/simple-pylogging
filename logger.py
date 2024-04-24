import logging


class Logger:
    """A Logger class that allows logging across multiple locations.

    This logger is designed to handle both console and file logging. It manages
    its own file and console handlers, and supports dynamic changes to the log file
    path.

    Attributes:
        log_filename (str): The path to the log file.
        logger (Logger): Internal logging.Logger instance for actual logging.
    """

    def __init__(self, log_filename: str = "log/log.txt"):
        """Initialize the Logger with a specified log filename.

        Args:
            log_filename (str): Optional; default log file path to use for file logging.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        log_format = "%(asctime)s,%(msecs)03d (%(levelname)5s) [%(filename)s:%(lineno)d]: %(message)s"
        self.__formatter = logging.Formatter(
            log_format, datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.log_filename = log_filename  # Assign self.log_filename first
        self.set_log_filename(self.log_filename)  # Now do the proper checking
        self._create_handlers()  # Setup handlers now that formatter is set

    def _create_handlers(self):
        """Creates and attaches console and file handlers to the logger."""
        self.logger.handlers.clear()  # Remove existing handlers
        self.__create_console_handler()
        self.__create_file_handler()

    def __create_console_handler(self):
        """Creates and configures a console handler."""
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(self.__formatter)
        self.logger.addHandler(console_handler)

    def __create_file_handler(self):
        """Creates and configures a file handler."""
        file_handler = logging.FileHandler(
            self.log_filename, mode="a", encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.__formatter)
        self.logger.addHandler(file_handler)

    def set_log_filename(self, filename, create_handlers=True):
        """Sets a new log filename and updates the file handler accordingly.

        Args:
            filename (str): The new log file name to set.
            create_handlers (bool): Whether handlers have to be created.
        """
        if filename and not filename.isspace():
            self.log_filename = filename

            if create_handlers:
                self._create_handlers()
        else:
            print(
                "> Wrong log filename. Defaulting to log/log.txt."
            )
            self.set_log_filename("log/log.txt")

    def __getattr__(self, name):
        """Delegate attribute access to the internal logger object.

        This method is called when an attribute lookup has not found
        the attribute in the usual places.
        It delegates access to the internal Logger instance.

        Args:
            name (str): The name of the attribute being accessed.

        Returns:
            The attribute from the internal logger if available.
        """
        try:
            return getattr(self.logger, name)
        except AttributeError:
            raise AttributeError(f"'Logger' object has no attribute '{name}'")

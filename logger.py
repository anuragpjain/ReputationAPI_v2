
"""Logger which sets logging level,timestamp and event level"""
import json
import logging


class RepLogger(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.set_log_level(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.stream = logging.StreamHandler()
        self.stream.setFormatter(formatter)
        self.logger.addHandler(self.stream)
        self.event_level = logging.WARNING

    def set_log_level(self, level):
        self.logger.setLevel(level)

    def set_event_level(self, level):
        self.event_level = level

    def _log_(self, level, message):
        if self.logger.isEnabledFor(level) or self.event_level <= level:
            details = json.dumps(message)
            self.logger.log(level, message + ' - Details: ' + details)

    def debug(self, message):
        self._log_(logging.DEBUG, message)

    def info(self, message):
        self._log_(logging.INFO, message)

    def warning(self, message):
        self._log_(logging.WARNING, message)

    def error(self, message):
        self._log_(logging.ERROR, message)

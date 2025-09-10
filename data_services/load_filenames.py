import os
from logs.logger import Logger

logger = Logger.get_logger()


# Reminder to add validation and docstring

class LoadFilenames:
    def __init__(self, path: str = None):
        try:
            self.path = path or "c:/podcasts/"
            self.filenames = self.get_list_of_filenames(self.path)
            logger.info("LoadFilenames successfully initialized")
        except Exception as e:
            logger.error(f"error in LoadFilenames initialized. error name: {e}")

    def get_list_of_filenames(self, path: str):
        try:
            list_of_filenames = []
            for filename in os.listdir(path):
                list_of_filenames.append(filename)
            logger.info("LoadFilenames successfully get_list_of_filenames")
            return  list_of_filenames
        except Exception as e:
            logger.error(f"error in LoadFilenames get_list_of_filenames. error name: {e}")



import hashlib
from logs.logger import Logger
import json


logger = Logger.get_logger()


class Models:
    def __init__(self):
        try:
            self.__dict_ids = {}
            logger.info("Models successfully initialized")
        except Exception as e:
            logger.error(f"error in Models initialized. error name: {e}")


    def make_id(self, msg: dict):
        try:
            unique_id_str = (f"file name: {msg['file name']}, "
                             f"type: {msg['type']}, "
                             f"size in bytes: {msg['size in bytes']}")
            unique_id = hashlib.sha256(unique_id_str.encode("utf-8")).hexdigest()

            logger.info("Models successfully make_id")
            return unique_id
        except Exception as e:
            logger.error(f"error in Models make_id. error name: {e}")



    def update_id(self, filename ,unique_id):
        try:
            if filename not in self.__dict_ids:
                self.__dict_ids[filename] = unique_id

                with open("ids.json", "w") as f:
                    json.dump(self.__dict_ids, f, indent=2)

            logger.info("Models successfully update_id")
        except Exception as e:
            logger.error(f"error in Models update_id. error name: {e}")


    def get_ids(self):
        try:
            with open("ids.json", "r") as f:
                loaded_dict = json.load(f)

            logger.info("Models successfully get_ids")
            return loaded_dict
        except Exception as e:
            logger.error(f"error in Models get_ids. error name: {e}")





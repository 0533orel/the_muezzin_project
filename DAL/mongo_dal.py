from pymongo import MongoClient
from logs.logger import Logger
import gridfs


logger = Logger.get_logger()


class MongoDal:
    def __init__(self, config):
        try:
            self.cfg = config
            self.client = MongoClient(self.cfg.MONGO_URI)
            self.db = self.client[self.cfg.MONGO_DB]
            self.col = self.db[self.cfg.MONGO_COLLECTION]
            logger.info("MongoDal successfully initialized")
        except Exception as e:
            logger.error(f"error in MongoDal initialized. error name: {e}")


    def upsert(self, id, doc: dict):
        try:
            self.col.replace_one({"_id": id}, doc, upsert=True)
            logger.info("MongoDal successfully upsert")
        except Exception as e:
            logger.error(f"error in MongoDal upsert. error name: {e}")

    def insert_file(self, path: str, filename: str, unique_id: str):
        try:
            fs = gridfs.GridFS(self.db)
            with open(f"{path}/{filename}", "rb") as f:
                file_id = fs.put(f, filename=filename, _id=unique_id)
            logger.info("MongoDal successfully insert_file")
        except Exception as e:
            logger.error(f"error in MongoDal insert_file. error name: {e}")




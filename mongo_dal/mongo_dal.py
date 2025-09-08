from pymongo import MongoClient
from logs.logger import Logger

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



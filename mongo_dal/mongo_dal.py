from pymongo import MongoClient

class MongoDal:
    def __init__(self, config):
        self.cfg = config
        self.client = MongoClient(self.cfg.MONGO_URI)
        self.db = self.client[self.cfg.MONGO_DB]
        self.col = self.db[self.cfg.MONGO_COLLECTION]

    def upsert(self, id, doc: dict):
        self.col.replace_one({"_id": id}, doc, upsert=True)


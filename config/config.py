import os

class Config:
    def __init__(self):
        #kafka
        self.BOOTSTRAP_SERVERS: str = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
        self.TOPIC_METADATA: str = os.getenv("TOPIC_METADATA", "podcasts_metadata")
        self.TOPIC_FILEDATA: str = os.getenv("TOPIC_FILEDATA", "podcasts_filedata")
        self.GROUP_ID = os.getenv("GROUP_ID", "es-consumer-group")
        self.AUTO_OFFSET = os.getenv("AUTO_OFFSET", "earliest")
        self.MAX_BUFFER = int(os.getenv("MAX_BUFFER", "500"))

        #elasticsearch
        self.ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
        self.ES_INDEX = os.getenv("ES_INDEX", "podcasts")

        #mongo
        self.MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.MONGO_DB = os.getenv("MONGO_DB", "muezzin")
        self.MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "podcasts")

        # BDS
        self.SMALE = 25
        self.MEDIUM = 60
        self.HIGH = 100

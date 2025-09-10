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
        self.INDEX_BODY = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0,
            },
            "mappings": {
                "dynamic": "false",
                "properties": {
                    "unique id": {"type": "keyword"},
                    "file_name": {"type": "keyword"},
                    "type": {"type": "keyword"},
                    "path": {"type": "keyword"},
                    "size in bytes": {"type": "long"},
                    "creation date": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                    "last modified date": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                    "text": {"type": "text"},
                    "len text": {"type": "integer"},
                    "bds score": {"type": "integer"},
                    "bds percent": {"type": "float"},
                    "bds threat level": {"type": "keyword"},
                    "is bds": {"type": "boolean"},

                }
            }
        }

        #mongo
        self.MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.MONGO_DB = os.getenv("MONGO_DB", "muezzin")
        self.MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "podcasts")

        # BDS
        self.SMALE = 25
        self.MEDIUM = 50
        self.HIGH = 100

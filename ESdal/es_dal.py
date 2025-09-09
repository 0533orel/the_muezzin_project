from elasticsearch import Elasticsearch
from logs.logger import Logger

logger = Logger.get_logger()



class ESdal:
    def __init__(self, cfg):
        try:
            self.cfg = cfg
            self.es = Elasticsearch(self.cfg.ES_HOST)
            if not self.es.indices.exists(index=self.cfg.ES_INDEX):
                self.es.indices.create(index=self.cfg.ES_INDEX)
            self.index = self.cfg.ES_INDEX
            logger.info("ESdal successfully initialized")
        except Exception as e:
            logger.error(f"error in ESdal initialized. error name: {e}")


    def refresh(self) -> None:
        try:
            self.es.indices.refresh(index=self.index)
            logger.info("ESdal successfully refresh")
        except Exception as e:
            logger.error(f"error in ESdal refresh. error name: {e}")


    def create_one(self, doc: dict, doc_id: str):
        try:
            self.es.index(index=self.index, id=doc_id, document=doc)
            logger.info("ESdal successfully create_one")
        except Exception as e:
            logger.error(f"error in ESdal create_one. error name: {e}")






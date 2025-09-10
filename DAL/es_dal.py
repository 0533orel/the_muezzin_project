from elasticsearch import Elasticsearch, NotFoundError
from logs.logger import Logger


logger = Logger.get_logger()


class EsDal:
    def __init__(self, config):
        try:
            self.cfg = config
            self.es = Elasticsearch(self.cfg.ES_HOST)
            if not self.es.indices.exists(index=self.cfg.ES_INDEX):
                self.es.indices.create(index=self.cfg.ES_INDEX, body=self.cfg.INDEX_BODY)
            self.index = self.cfg.ES_INDEX
            logger.info("elasticsearch_dal successfully initialized")
        except Exception as e:
            logger.error(f"error in elasticsearch_dal initialized. error name: {e}")


    def refresh(self) -> None:
        try:
            self.es.indices.refresh(index=self.index)
            logger.info("elasticsearch_dal successfully refresh")
        except Exception as e:
            logger.error(f"error in elasticsearch_dal refresh. error name: {e}")


    def create_one(self, doc: dict):
        try:
            self.es.index(index=self.index, document=doc)
            logger.info("elasticsearch_dal successfully create_one")
        except Exception as e:
            logger.error(f"error in elasticsearch_dal create_one. error name: {e}")

    def drop_index(self, name: str):
        self.es.indices.delete(index=name, ignore=[400, 404])






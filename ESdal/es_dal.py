from elasticsearch import Elasticsearch

class ESdal:
    def __init__(self, cfg):
        self.cfg = cfg
        self.es = Elasticsearch(self.cfg.ES_HOST)
        if not self.es.indices.exists(index=self.cfg.ES_INDEX):
            self.es.indices.create(index=self.cfg.ES_INDEX)
        self.index = self.cfg.ES_INDEX

    def refresh(self) -> None:
        self.es.indices.refresh(index=self.index)

    def create_one(self, doc: dict, doc_id: str):
        self.es.index(index=self.index, id=doc_id, document=doc)






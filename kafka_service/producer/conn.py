import json, time
from kafka import KafkaProducer
from config import Config

class ProducerConn:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.producer = KafkaProducer(
            bootstrap_servers=self.cfg.BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8"),
        )

    def send(self, value, timeout: float = 10.0) -> dict:
        self.producer.send(self.cfg.TOPIC, value=value)

    def flush(self):
        try:
            self.producer.flush(10)
        except Exception:
            pass

    def close(self):
        self.flush()
        try:
            self.producer.close(10)
        except Exception:
            pass


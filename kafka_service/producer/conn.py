import json, time
from kafka import KafkaProducer
from config import Config

class ProducerConn:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.producer = KafkaProducer(
            bootstrap_servers=self.cfg.BOOTSTRAP_SERVERS,
            client_id=self.cfg.CLIENT_ID,
            value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8"),
            linger_ms=5,
            retries=5,
        )
        start = time.time()
        while not self.producer.bootstrap_connected() and time.time() - start < 15:
            time.sleep(0.2)

    def send(self, value, timeout: float = 10.0) -> dict:
        fut = self.producer.send(self.cfg.TOPIC, value=value)
        md = fut.get(timeout=timeout)

        return {
            "topic": md.topic,
            "partition": md.partition,
            "offset": md.offset,
            "timestamp": getattr(md, "timestamp", None),
        }

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


import json
from kafka import KafkaProducer
from config.config import Config
from logs.logger import Logger

logger = Logger.get_logger()


class ProducerConn:
    def __init__(self, cfg: Config):
        try:
            self.cfg = cfg
            self.topic_metadata = self.cfg.TOPIC_METADATA
            self.topic_filedata = self.cfg.TOPIC_FILEDATA
            self.producer = KafkaProducer(
                    bootstrap_servers=self.cfg.BOOTSTRAP_SERVERS,
                    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8"),
                )
            logger.info("ProducerConn successfully initialized")
        except Exception as e:
            logger.error(f"error in ProducerConn initialized. error name: {e}")



    def send(self, topic, value):
        try:
            self.producer.send(topic, value=value)
            logger.info("Producer successfully send")
        except Exception as e:
            logger.error(f"error in Producer send. error name: {e}")


    def flush(self):
        try:
            self.producer.flush(10)
            logger.info("Producer successfully flush")
        except Exception as e:
            logger.error(f"error in Producer flush. error name: {e}")


import json
from kafka import KafkaConsumer
from config.config import Config
from logs.logger import Logger

logger = Logger.get_logger()


class ConsumerManager:
    def __init__(self, cfg: Config):
        try:
            self.cfg = cfg
            self.consumer = KafkaConsumer(
                self.cfg.TOPIC,
                bootstrap_servers=self.cfg.BOOTSTRAP_SERVERS,
                group_id=self.cfg.GROUP_ID,
                auto_offset_reset=self.cfg.AUTO_OFFSET,
                enable_auto_commit=True,
                value_deserializer=lambda v: json.loads(v.decode("utf-8"))
            )
            logger.info("ConsumerManager successfully initialized")
        except Exception as e:
            logger.error(f"error in ConsumerManager initialized. error name: {e}")






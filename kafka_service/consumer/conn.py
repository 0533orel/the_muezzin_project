import json

from kafka import KafkaConsumer
from config import Config


class ConsumerManager:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.consumer = KafkaConsumer(
            self.cfg.TOPIC,
            bootstrap_servers=self.cfg.BOOTSTRAP_SERVERS,
            group_id=self.cfg.GROUP_ID,
            auto_offset_reset=self.cfg.AUTO_OFFSET,
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode("utf-8"))
        )






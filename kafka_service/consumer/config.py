import os

class Config:
    def __init__(self):
        # Kafka
        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
        self.TOPIC = os.getenv("TOPIC", "podcasts")
        self.GROUP_ID = os.getenv("GROUP_ID", "es-consumer-group")
        self.AUTO_OFFSET = os.getenv("AUTO_OFFSET", "earliest")
        self.MAX_BUFFER = int(os.getenv("MAX_BUFFER", "500"))

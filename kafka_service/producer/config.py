import os

class Config:
    def __init__(self):
        self.BOOTSTRAP_SERVERS: str = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
        self.TOPIC: str = os.getenv("TOPIC", "podcasts")
        self.PRODUCE_EVERY_MS: int = int(os.getenv("PRODUCE_EVERY_MS", "0"))
        self.CLIENT_ID: str = os.getenv("CLIENT_ID", "producer-service")

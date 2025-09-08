import os

class Config:
    def __init__(self):
        self.BOOTSTRAP_SERVERS: str = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
        self.TOPIC: str = os.getenv("TOPIC", "podcasts")

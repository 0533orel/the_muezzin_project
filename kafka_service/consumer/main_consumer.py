from contextlib import asynccontextmanager
from config import Config
from conn import ConsumerManager



cfg = Config()
manager = ConsumerManager(cfg)
manager.start()
manager._loop()
a = manager.get_messages()
print(a)

manager.stop()


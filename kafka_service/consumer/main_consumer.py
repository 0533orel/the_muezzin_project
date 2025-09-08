from config import Config
from conn import ConsumerManager


cfg = Config()
mngr = ConsumerManager(cfg)

try:
    for message in mngr.consumer:
        print(message.value)
finally:
    mngr.consumer.close()
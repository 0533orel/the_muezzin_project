from config.config import Config
from conn import ConsumerManager
from ESdal.es_dal import ESdal
from logs.logger import Logger
import uuid, json

cfg = Config()
mngr = ConsumerManager(cfg)
es = ESdal(cfg)
logger = Logger.get_logger()


try:
    for message in mngr.consumer:
        try:
            msg_in_dic = json.loads(message.value)
            unique_id = str(uuid.uuid4())
            es.create_one(msg_in_dic, unique_id)
            logger.info("Trying to push messages from kafka to elasticsearch = succeeded")
        except Exception as e:
            pass
            logger.error(f"error name: {e}")

finally:
    mngr.consumer.close()
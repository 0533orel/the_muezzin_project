from config.config import Config
from conn import ConsumerManager
from ESdal.es_dal import ESdal
from logs.logger import Logger
import hashlib, json

cfg = Config()
mngr = ConsumerManager(cfg)
es = ESdal(cfg)
logger = Logger.get_logger()
hash_object = hashlib.sha256()

try:
    for message in mngr.consumer:
        try:
            msg_in_dic = json.loads(message.value)
            unique_id_str = (f"file name: {msg_in_dic['file name']}, "
                         f"creation date: {msg_in_dic['creation date']}, "
                         f"last modified date: {msg_in_dic['last modified date']}, "
                         f"size in bytes: {msg_in_dic['size in bytes']}")
            hash_object.update(b"{unique_id_str}")
            hex_dig = hash_object.hexdigest()
            unique_id = str(hash_object.hexdigest())
            es.create_one(msg_in_dic, unique_id)
            logger.info(f"Trying to push messages {msg_in_dic['file name']} from kafka to elasticsearch = succeeded")
        except Exception as e:
            pass
            logger.error(f"error name: {e}")

finally:
    mngr.consumer.close()
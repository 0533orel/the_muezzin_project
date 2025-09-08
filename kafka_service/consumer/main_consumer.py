from config.config import Config
from conn import ConsumerManager
from ESdal.es_dal import ESdal
from mongo_dal.mongo_dal import MongoDal
from logs.logger import Logger
import hashlib, json
import gridfs


cfg = Config()
logger = Logger.get_logger()

mngr = ConsumerManager(cfg)
es = ESdal(cfg)
mongo = MongoDal(cfg)

fs = gridfs.GridFS(mongo.db)
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

            filename = msg_in_dic['file name'] + msg_in_dic['type']
            path = msg_in_dic['path']
            with open(f"{path}/{filename}", "rb") as f:
                file_id = fs.put(f, filename=filename, _id=unique_id)

            es.create_one(msg_in_dic, unique_id)
            es.refresh()
            logger.info(f"Trying to push file {msg_in_dic['file name']} into mongo = succeeded")
        except Exception as e:
            logger.error(f"error name: {e}")

finally:
    mngr.consumer.close()
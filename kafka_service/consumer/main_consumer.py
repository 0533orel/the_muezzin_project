from config.config import Config
from conn import ConsumerManager
from ESdal.es_dal import ESdal
from models.models import make_id
from mongo_dal.mongo_dal import MongoDal
from logs.logger import Logger
import json


cfg = Config()
logger = Logger.get_logger()

mngr = ConsumerManager(cfg)
es = ESdal(cfg)
mongo = MongoDal(cfg)



try:
    for message in mngr.consumer:
        msg_in_dic = message.value
        unique_id_str = (f"file name: {msg_in_dic['file name']}, "
                     f"creation date: {msg_in_dic['creation date']}, "
                     f"last modified date: {msg_in_dic['last modified date']}, "
                     f"size in bytes: {msg_in_dic['size in bytes']}")

        unique_id = make_id(unique_id_str)
        filename = msg_in_dic['file name'] + msg_in_dic['type']
        path = msg_in_dic['path']

        mongo.insert_file(path, filename, unique_id)

        es.create_one(msg_in_dic, unique_id)
        es.refresh()
        print(msg_in_dic)

finally:
    mngr.consumer.close()
from config.config import Config
from metadata_on_files.speach_to_text import SpeachToText
from sub_conn import ConsumerManager
from elasticsearch_dal.es_dal import es_dal
from models.models import Models
from mongo_dal.mongo_dal import MongoDal
from logs.logger import Logger

model = Models()
stt = SpeachToText()

cfg = Config()
logger = Logger.get_logger()

mngr = ConsumerManager(cfg, cfg.TOPIC_METADATA)
es = es_dal(cfg)
mongo = MongoDal(cfg)



try:
    for message in mngr.consumer:
        msg_in_dic = message.value
        filename = msg_in_dic['file name'] + msg_in_dic['type']

        unique_id = model.make_id(msg_in_dic)
        model.update_id(filename, unique_id)

        path = msg_in_dic['path']
        full_path = f"{path}\\{filename}"

        text = stt.transcribe(full_path)
        msg_in_dic["file text"] = text

        mongo.insert_file(path, filename, unique_id)

        es.create_one(msg_in_dic, unique_id)
        es.refresh()
        # print(msg_in_dic)

finally:
    mngr.consumer.close()
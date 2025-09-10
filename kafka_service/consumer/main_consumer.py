from config.config import Config
from data_analysis.speach_to_text import SpeachToText
from sub_conn import ConsumerManager
from elasticsearch_dal.es_dal import EsDal
from models.models import Models
from mongo_dal.mongo_dal import MongoDal
from logs.logger import Logger
from data_analysis.bds_classification import BdsClassification


cfg = Config()
logger = Logger.get_logger()


model = Models()
stt = SpeachToText()
bds = BdsClassification(cfg)

mngr = ConsumerManager(cfg, cfg.TOPIC_METADATA)
es = EsDal(cfg)
mongo = MongoDal(cfg)


try:
    for message in mngr.consumer:
        msg_in_dic = message.value
        filename = msg_in_dic['file name'] + msg_in_dic['type']

        unique_id = model.make_id(msg_in_dic)
        model.update_id(filename, unique_id)
        msg_in_dic = {"unique id": unique_id, **msg_in_dic}

        path = msg_in_dic['path']
        full_path = f"{path}\\{filename}"

        text = stt.transcribe(full_path)
        msg_in_dic["file text"] = text

        bds_dict = bds.text_processing(text)
        msg_in_dic.update(bds_dict)

        mongo.insert_file(path, filename, unique_id)

        es.create_one(msg_in_dic)
        es.refresh()

finally:
    mngr.consumer.close()
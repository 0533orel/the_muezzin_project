from config.config import Config
from data_services.speach_to_text import SpeachToText
from sub_conn import ConsumerManager
from DAL.es_dal import EsDal
from models.models import Models
from DAL.mongo_dal import MongoDal
from data_services.bds_classification import BdsClassification
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import uvicorn

msg_in_dic = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.cfg = Config()
    app.manager = ConsumerManager(app.cfg, app.cfg.TOPIC_METADATA)
    app.model = Models()
    app.stt = SpeachToText()
    app.bds = BdsClassification(app.cfg)

    app.mngr = ConsumerManager(app.cfg, app.cfg.TOPIC_METADATA)
    app.es = EsDal(app.cfg)
    app.mongo = MongoDal(app.cfg)

    for message in app.mngr.consumer:
        msg_in_dic = message.value
        filename = msg_in_dic['file name'] + msg_in_dic['type']

        unique_id = app.model.make_id(msg_in_dic)
        app.model.update_id(filename, unique_id)
        msg_in_dic = {"unique id": unique_id, **msg_in_dic}

        path = msg_in_dic['path']
        full_path = f"{path}\\{filename}"

        text = app.stt.transcribe(full_path)
        msg_in_dic["file text"] = text

        bds_dict = app.bds.text_processing(text)
        msg_in_dic.update(bds_dict)

        app.mongo.insert_file(path, filename, unique_id)

        app.es.create_one(msg_in_dic)
        app.es.refresh()

    yield
    app.mngr.consumer.close()

app = FastAPI(title="Kafka → Elasticsearch Consumer", lifespan=lifespan)

@app.get("/health")
def health(request: Request):
    cfg = request.app.state.cfg
    return {"status": "ok"}

@app.get("/messages")
def messages():
    return msg_in_dic


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)






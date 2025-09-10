from config.config import Config
from kafka_service.producer.pub_conn import ProducerConn
from data_analysis.load_filenames import LoadFilenames
from data_analysis.metadata_on_file import MetadataOnFiles

loader = LoadFilenames()
mngr = MetadataOnFiles(loader.path, loader.filenames)

metadata = mngr.get_metadata_on_files(mngr.path, mngr.filenames)

cfg = Config()
kafka_pub = ProducerConn(cfg)

for data in metadata:
    kafka_pub.send(cfg.TOPIC_METADATA ,data)
    kafka_pub.flush()



kafka_pub.close()


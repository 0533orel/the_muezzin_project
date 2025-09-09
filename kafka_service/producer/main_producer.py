from config.config import Config
from kafka_service.producer.conn import ProducerConn
from metadata_on_files.load_filenames import LoadFilenames
from metadata_on_files.metadata_on_file import MetadataOnFiles

loader = LoadFilenames()
metadata = MetadataOnFiles(loader.path, loader.filenames)

config = Config()
kafka_pub = ProducerConn(config)

for data in metadata.metadata_on_files:
    kafka_pub.send(data)
    kafka_pub.flush()

kafka_pub.close()


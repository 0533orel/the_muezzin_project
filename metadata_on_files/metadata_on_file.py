from pathlib import Path
from datetime import datetime
import json
from logs.logger import Logger

logger = Logger.get_logger()


# Reminder to add validation and docstring

class MetadataOnFiles:
    def __init__(self, path: str, filenames: list):
        try:
            self.path = Path(path)
            self.filenames = filenames
            self.metadata_on_files = self.get_metadata_on_files(self.path, self.filenames)
            logger.info("MetadataOnFiles successfully initialized")
        except Exception as e:
            logger.error(f"error in MetadataOnFiles initialized. error name: {e}")


    def get_metadata_on_files(self, path: Path, filenames: list):
        try:
            list_of_metadata = []
            for filename in filenames:
                file = path / filename
                current_datetime = datetime.now()
                last_modified_timestamp = file.stat().st_mtime
                list_of_metadata.append({
                    "file name": str(file.stem),
                    "type": str(file.suffix),
                    "path": str(file.parent),
                    "size in bytes": file.stat().st_size,
                    "creation date": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    "last modified date": datetime.fromtimestamp(last_modified_timestamp).strftime("%Y-%m-%d %H:%M:%S")
                })

            logger.info("MetadataOnFiles successfully get_metadata_on_files")
            return list_of_metadata
        except Exception as e:
            logger.error(f"error in MetadataOnFiles get_metadata_on_files. error name: {e}")


    def get_list_of_jsons(self, list_of_metadata: list[dict]):
        try:
            json_list = []
            for metadata in list_of_metadata:
                json_string = json.dumps(metadata, indent=6)
                json_list.append(json_string)

            logger.info("MetadataOnFiles successfully get_list_of_jsons")
            return json_list
        except Exception as e:
            logger.error(f"error in MetadataOnFiles get_list_of_jsons. error name: {e}")



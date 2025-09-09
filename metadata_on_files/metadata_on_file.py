from pathlib import Path
from datetime import datetime
from logs.logger import Logger




logger = Logger.get_logger()


# Reminder to add validation and docstring

class MetadataOnFiles:
    def __init__(self, path: str, filenames: list):
        try:
            self.path = Path(path)
            self.filenames = filenames
            logger.info("MetadataOnFiles successfully initialized")
        except Exception as e:
            logger.error(f"error in MetadataOnFiles initialized. error name: {e}")


    def get_metadata_on_files(self, path: Path, filenames: list):
        try:
            list_of_metadata = []
            for filename in filenames:
                file = path / filename
                current_datetime = file.stat().st_ctime
                last_modified_timestamp = file.stat().st_mtime
                list_of_metadata.append({
                    "file name": str(file.stem),
                    "type": str(file.suffix),
                    "path": str(file.parent),
                    "size in bytes": file.stat().st_size,
                    "creation date": datetime.fromtimestamp(current_datetime).strftime("%Y-%m-%d %H:%M:%S"),
                    "last modified date": datetime.fromtimestamp(last_modified_timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                })

            logger.info("MetadataOnFiles successfully get_metadata_on_files")
            return list_of_metadata
        except Exception as e:
            logger.error(f"error in MetadataOnFiles get_metadata_on_files. error name: {e}")

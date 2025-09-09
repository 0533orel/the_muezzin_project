from pathlib import Path
from datetime import datetime
import json
from logs.logger import Logger
import speech_recognition as sr

from metadata_on_files.load_filenames import LoadFilenames

r = sr.Recognizer()

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


    # def speach_to_text(self, path: Path, filenames: list):
    #     try:
    #         dict_of_file_data = {}
    #         for filename in filenames:
    #             audio_file_path = f"{path}/{filename}"
    #             with sr.AudioFile(audio_file_path) as source:
    #                 audio_data = r.record(source)
    #                 text = r.recognize_google(audio_data)
    #                 dict_of_file_data[filename] = text
    #
    #         logger.info("MetadataOnFiles successfully speach_to_text")
    #         return dict_of_file_data
    #     except Exception as e:
    #         logger.error(f"error in MetadataOnFiles speach_to_text. error name: {e}")


    def get_metadata_on_files(self, path: Path, filenames: list):
        try:
            # dict_of_file_data = self.speach_to_text(path, filenames)

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
                    # "file data": dict_of_file_data[filename]
                })

            logger.info("MetadataOnFiles successfully get_metadata_on_files")
            return list_of_metadata
        except Exception as e:
            logger.error(f"error in MetadataOnFiles get_metadata_on_files. error name: {e}")

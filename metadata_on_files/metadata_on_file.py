from pathlib import Path
from datetime import datetime
import json


# Reminder to add validation and docstring

class MetadataOnFiles:
    def __init__(self, path: str, filenames: list):
        self.path = Path(path)
        self.filenames = filenames
        self.metadata_on_files = self.get_metadata_on_files(self.path, self.filenames)

    def get_metadata_on_files(self, path: Path, filenames: list):
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

        return list_of_metadata

    def get_list_of_jsons(self, list_of_metadata: list[dict]):
        json_list = []
        for metadata in list_of_metadata:
            json_string = json.dumps(metadata, indent=6)
            json_list.append(json_string)

        return json_list


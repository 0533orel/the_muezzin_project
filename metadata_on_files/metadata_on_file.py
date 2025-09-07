from pathlib import Path
from datetime import datetime


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
                "file name": file.stem,
                "type": file.suffix,
                "path": file.parent,
                "size": file.stat().st_size,
                "creation date": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                "Last modified date": datetime.fromtimestamp(last_modified_timestamp).strftime("%Y-%m-%d %H:%M:%S")
            })

        return list_of_metadata

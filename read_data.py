import fnmatch
from pathlib import Path


class Files:

    def __init__(self, expression):
        self.expression = expression

    def fetch_file_year(self):
        all_files = []
        entries = Path('weatherfiles/')
        for entry in entries.iterdir():
            if fnmatch.fnmatch(entry, self.expression):
                all_files.append(entry)
        return all_files

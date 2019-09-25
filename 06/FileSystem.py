from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileInfo(object):
    name: str
    size: int


class FileFilter(object):
    def __init__(self, prefix, extension):
        self._folder_prefix = prefix
        self._file_extension = extension

    def find(self, path: Path) -> tuple:
        for folder in path.iterdir():
            if folder.is_dir() and folder.name.startswith(self._folder_prefix):
                yield from (
                    FileInfo(str(f.absolute()), f.stat().st_size)
                    for f in folder.iterdir()
                    if f.is_file() and f.suffix == f'.{self._file_extension}'
                )


if __name__ == '__main__':
    for info in FileFilter('RA_', 'txt').find(Path('files')):
        print(info)

from pathlib import Path

from Resources.HandleFile import HandleFile

class LogFile(HandleFile):
    def __init__(self, filename: str):
        super().__init__(filename)
        self.__path: Path = Path(filename)

    def write(self, lines: list[str]):
        super().write(lines)

    def add(self, line: str):
        super().add(line)
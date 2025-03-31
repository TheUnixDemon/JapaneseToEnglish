from pathlib import Path

from Resources.HandleFile import HandleFile

class TransFile(HandleFile):
    def __init__(self, filename: str):
        super().__init__(filename)
        self.__path: Path = Path(filename)

    # removes right sided formating, like line breaks; returns lines as list
    def read(self) -> list[str]:
        if self.validate:
            return [line.rstrip() for line in super().read()]
        print(f"Data '{super().getFilename()}' not found")
        exit()
    
    # removes line breaks
    def write(self, lines: list[str]):
        super().write([line.rstrip() for line in lines])
        
    def validate(self) -> bool:
        if self.__path.exists():
            return True
        return False
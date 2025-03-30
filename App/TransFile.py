from pathlib import Path

from Resources.HandleFile import HandleFile

class TransFile(HandleFile):
    def __init__(self, filename: str):
        super().__init__(filename)
        self.__path: Path = Path(filename)

    def read(self) -> list[str]:
        if self.validate:
            return super().read()
        print(f"Data '{super().getFilename()}' not found")
        exit()
    
    def write(self, lines: list[str]):
        super().write(lines.replace("\n"))
        
    def validate(self) -> bool:
        if self.__path.exists():
            return True
        return False
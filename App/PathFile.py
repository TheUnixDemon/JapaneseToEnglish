from Resources.HandleFile import HandleFile

class PathFile(HandleFile):
    def __init__(self):
        self.__pathFile: str = "filenames.txt"
        super().__init__(self.__pathFile)

    def read(self):
        return super().read()
    
    def write(self, lines):
        return super().write(lines)
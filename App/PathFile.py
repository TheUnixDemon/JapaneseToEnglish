from Resources.HandleFile import HandleFile

# returned path
class PathFile(HandleFile):
    def __init__(self, filename: str):
        super().__init__(filename)

    # returned the file path without formating
    def read(self):
        return [path.strip() for path in super().read()]
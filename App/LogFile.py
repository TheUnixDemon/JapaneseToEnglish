from Resources.HandleFile import HandleFile

class LogFile(HandleFile):
    def __init__(self, filename: str):
        super().__init__(filename)

    def add(self, response: str):
        with open(super().getFilename(), "a", encoding = "utf-8") as file:
            file.write(response + "\n")

    def wipe(self):
        open(super().getFilename(), "w").close()
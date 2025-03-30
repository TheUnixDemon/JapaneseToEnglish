# basic class for read and write files
class HandleFile:
    def __init__(self, filename: str):
        self.setFilename(filename)

    # write in lines <- list[str]
    def write(self, lines: list[str]):
        with open(self.__filename, "w", encoding = "utf-8") as file:
            for line in lines:
                file.write(line + "\n")

    def read(self) -> list[str]:
        with open(self.__filename, "r", encoding = "utf-8") as file:
            return file.readlines()

    # add line to file <- str
    def add(self, line: str):
        with open(self.__filename, "a") as file:
            file.write(line + "\n")

    def setFilename(self, filename: str):
        self.__filename: str = filename
    
    def getFilename(self) -> str:
        return self.__filename
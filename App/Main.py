from PathFile import PathFile
from TransFile import TransFile
from LogFile import LogFile
from BatchTranslate import BatchTranslate

class Main:
    def __init__(self):
        self.__replaceDict: dict[str, str] = {
            '"': r"\"",
            "'": r"\'"
        }
        self.__paths: list[str] = PathFile("filenames").read()
        self.__logFile: LogFile = LogFile("logProgress.txt")
        self.__batchTranslate: BatchTranslate = BatchTranslate(r"[\u3040-\u30FF\u4E00-\u9FFF]+", r"(\{[^}]+\}|%[^%]+%)", ["PRINT"], ["{", "}"], 3000)

    # translate 'self.__paths' in lines 
    def makeTranslations(self):
        for path in self.__paths:
            try:
                transFile: TransFile = TransFile(path)
                # file not found; skip this file
                if not transFile.validate:
                    raise f"File '{path}' not found"
                lines: list[str] = transFile.read()
                transFile.write(self.__batchTranslate.translate(lines))
            except Exception as e:
                print(f"Error occurred '{e}'")

if __name__ == "__main__":
    main: Main = Main()

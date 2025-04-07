# from PathFile import PathFile
from GetPaths import GetPaths
from TransFile import TransFile
from LogFile import LogFile
from BatchTranslate import BatchTranslate

class Main:
    def __init__(self):
        # for replacing code breaking translated stuff into non code breaking stuff
        self.__replaceDict: dict[str, str] = {
            '"': r"\"",
            "'": r"\'"
        }
        #self.__paths: list[str] = PathFile("filenames").read()
        # dict[str, str] -> {sourcePath: translationPath}
        self.__paths: dict[str, str] = GetPaths().returnPaths()
        self.__logFile: LogFile = LogFile("logProgress.txt")
        self.__batchTranslate: BatchTranslate = BatchTranslate(r"[ぁ-んァ-ン一-龥]+", 
                                                               r'(print\("|"\))', # for splitting lines 
                                                               r'print\("([^"]+)"\)', # to look if the line is even worth to translate !
                                                               ["(", ")", "'", "{", "}"], # exclusion of some symbols
                                                               self.__replaceDict,
                                                               1500, 
                                                               self.__logFile)
    # translate 'self.__paths' in lines 
    def makeTranslations(self):
        self.makeResponse(f"Source: *{self.__paths}*")
        for sourcePath, translationPath in self.__paths.items():
            try:
                self.makeResponse(f"Starts translation of *{sourcePath}*")
                sourceFile: TransFile = TransFile(sourcePath)
                transFile: TransFile = TransFile(translationPath)
                # file not found; skip this file
                if not sourceFile.validate:
                    raise FileNotFoundError(f"File *{sourcePath}* not found - will be skipped")
                lines: list[str] = sourceFile.read()
                # if already translated skip the writing part
                if lines:
                    transFile.write(self.__batchTranslate.translate(lines))
                self.makeResponse(f"Translation of *{sourcePath}* is finished")
            except FileNotFoundError as e:
                self.makeResponse(f"{e}")
                continue
            except Exception as e:
                print(f"Main error occurred: *{e}*")
                exit()

    # for printing and saving into the log file
    def makeResponse(self, response: str):
        self.__logFile.add(response)
        print(response)

if __name__ == "__main__":
    main: Main = Main()
    main.makeTranslations()
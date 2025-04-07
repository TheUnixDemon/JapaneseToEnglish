from Resources.Optimize import Optimize
from Resources.Translate import Translate
from Resources.Progress import Progress
from LogFile import LogFile

class BatchTranslate(Optimize):
    def __init__(self, langExpression: str, splitExpression: str, includeExpression: str, excludeExpression: list[str], replaceDict: dict[str, str], maxChar: int, logFile: LogFile):
        # mental node: patterns list should be overworked with regex for better runtime
        super().__init__(langExpression, splitExpression, includeExpression, excludeExpression)
        self.__translate: Translate = Translate("ja", "en", [2.0, 5.0], 30.0, logFile)
        # for changing unwanted char is something different
        self.setReplaceDict(replaceDict)
        # sets a max character length for every request
        self.setMaxChar(maxChar)
        # responses for user
        self.__progress: Progress = Progress(maxChar) 
        self.__logFile: LogFile = logFile
        
    def translate(self, lines: list[str]) -> list[str]:
        segments: list[str] = super().optimize(lines)
        self.setSegments(segments)
        # converts segments in int: len(segments)
        self.__progress.setSegments(segments)
        translatedSegments: list[str] = []
        # temp save for segments that are to be translated
        tempSegments: list[str] = []
        
        # for validating that tempSegments are not above maxChar
        sumChars: int = 0
        i: int = 0
        while i < len(segments):
            self.__progress.setStartTime()
            segment: str = segments[i]
            # chars4: -> '\n\n'
            if sumChars + len(segment) + 4 < self.__maxChar:
                tempSegments.append(segment)
                sumChars += len(segment) + 4
                i += 1
            else:
                translatedSegments.extend(self.makeBatch(tempSegments))
                self.__progress.addTimeMeasurement()
                self.makeResponse(translatedSegments)
                tempSegments = []
                sumChars = 0
        # last entries of segments are to translate if len(tempSegments) != 0
        if tempSegments:
            translatedSegments.extend(self.makeBatch(tempSegments))
            self.__progress.addTimeMeasurement()
        self.makeResponse(translatedSegments)
        # recontructs the origin file
        return super().reconstruct(translatedSegments)

    # given tempSegments will be translated and validates after here
    # (is more like a fake batching 'cause of the restricted functions of deep_translator)
    def makeBatch(self, tempSegments: list[str]) -> list[str]:
        while True:
            try:
                # if the part to translate is NOT only one segment; else make a single segment translated
                if len(tempSegments) > 1:
                    batchString: str = ""
                    # \n for seperating within google translator
                    for segment in tempSegments:
                        batchString += segment + "\n\n"
                    translatedTempSegments: list[str] = self.replaceChars(self.__translate.makeTranslation(batchString)).split("\n\n")
                    if len(tempSegments) != len(translatedTempSegments):
                        raise "Number of elements *tempSegments* & *translatedSegments* must be equals"
                else:
                    translatedTempSegments: list[str] = list(self.__translate.makeTranslation(tempSegments[0]))
                return translatedTempSegments
            except Exception as e:
                print(f"Batching error occurred: *{e}* - retries translation")
                continue

    # to finish the current file translation
    def makeResponse(self, translatedSegments: list[str]):
        timeInSec: float = self.__progress.calcRestTime(translatedSegments)
        restOfTimeSec: int = round(timeInSec % 60)
        restOfTimeMin: int = int(timeInSec / 60)
        response: str = f"Number of segments: *{len(self.__segments)}*, translated ones: *{len(translatedSegments)}*, time remaining: *{restOfTimeMin}:{restOfTimeSec}*"
        self.__logFile.add(response)
        print(response, end="\r")
    
    # replaces unwanted chars into something mapped within self.__replaceDict
    def replaceChars(self, content: str) -> str:
        for key, value in self.__replaceDict.items():
            content = content.replace(key, value)
        return content

    # current segments that are to translate
    def setSegments(self, segments: list[str]):
        self.__segments: list[str] = segments

    # replaceDict is for unwanted translation chars that may break the code base
    def setReplaceDict(self, replaceDict: dict[str, str]):
        self.__replaceDict: dict[str, str] = replaceDict

    # for not overreach the character limits of the translation
    def setMaxChar(self, maxChar: int):
        self.__maxChar: int = maxChar
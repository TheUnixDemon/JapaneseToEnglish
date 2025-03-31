from App.Resources.Optimize import Optimize
from Resources.Translate import Translate

class BatchTranslate(Optimize):
    def __init__(self, splitExpression: str, includefilter: list[str], excludeFilter: list[str], maxChar: int):
        # mental node: patterns list should be overworked with regex for better runtime
        super().__init__(r"[\u3040-\u30FF\u4E00-\u9FFF]+", r"(\{[^}]+\}|%[^%]+%)", ["PRINT"], ["{", "}"])
        self.__translate: Translate = Translate("ja", "en", [5.0, 15.0], 60.0)
        
    def translate(self, lines: list[str]) -> list[str]:
        segments: list[str] = super().optimize(lines)
        translatedSegments: list[str] = []
        # temp save for segments that are to be translated
        tempSegments: list[str] = []
        
        # for validating that tempSegments are not above maxChar
        sumChars: int = 0
        i: int = 0
        while i < len(segments):
            segment: str = segments[i]
            # chars4: -> '\n\n'
            if sumChars + len(segment) + 4 < self.__maxChar:
                tempSegments.append(segment)
                i += 1
            translatedSegments.extend(self.makeBatch(tempSegments))
            tempSegments = []
            sumChars = 0
        # last entries of segments are to translate if len(tempSegments) != 0
        if tempSegments:
            translatedSegments.extend(self.makeBatch(tempSegments))
        translatedSegments.extend(self.makeBatch(tempSegments))
        return super().reconstruct(translatedSegments)
            
    # given tempSegments will be translated and validates after here
    # (is more like a fake batching 'cause of the restricted functions of deep_translator)
    def makeBatch(self, tempSegments: list[str]) -> list[str]:
        while True:
            try:
                batchString: str = ""
                # \n for seperating within google translator
                for segment in tempSegments:
                    batchString += "\n\n"
                translatedTempSegments: list[str] = self.__translate.makeTranslation(batchString).split("\n\n")
                if len(tempSegments) != len(translatedTempSegments):
                    raise "number of elements of [tempSegments] and [translatedSegments] non identical"
                return translatedTempSegments
            except Exception as e:
                print(f"Batching batch error occurred: '{e}'")
                continue
        
    def setMaxChar(self, maxChar: int):
        self.__maxChar: int = maxChar
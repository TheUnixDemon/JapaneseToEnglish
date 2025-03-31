import re

# for filtering and reconstructiong data with translations
class Optimize:
    def __init__(self, langExpression: str, splitExpression: str, includefilter: list[str], excludeFilter: list[str]):
        self.setSplitExpression(splitExpression)
        self.setLangExpression(langExpression)
        self.setIncludeFilter(includefilter)
        self.setExcludeFilter(excludeFilter)

    # splits, validates and remembers positioning of data that is to be translated
    def optimize(self, lines: list[str]) -> list[str]:
        self.setLines(lines)
        # splits 'lines' after self.__splitExpression
        self.setSplitLines()
        # for mapping positioning
        indicies: list[list[int]]
        segments: list[str]
        # i: in line; len(line) is identical to len(self.__splitLines)
        for i, line in enumerate(lines):
            # if line is not to translate
            if not self.isLanguage(line) and not any(element in line for element in self.__includeFilter):
                continue
            # j: in line segments; is searched language and includeFilter is true
            for j, segment in enumerate(self.__splitLines[i]):
                if not any(element in segment for element in self.__excludeFilter):
                    indicies.append([i, j])
                    segments.append(segment)
        self.setIndicies(indicies)
        return segments

    # reconstruct origin with translated 'list[str]'
    def reconstruct(self, translatedSegments: list[str]) -> list[str]:
        # puts the translated segments in place of splitLines; indicies is based on splitLines
        for index, segment in zip(self.__indicies, translatedSegments):
            # index[0] -> line; index[1] -> segment in line
            self.__splitLines[index[0], index[1]] = segment
        # sets translated splitLines and rejoins it
        for lineIndex, splitLine in enumerate(self.__splitLines):
            self.__lines[lineIndex] = "".join(splitLine)
        return self.__lines

    # returns true if language that is searched afte is within line
    def isLanguage(self, content: str) -> bool:
        return bool(self.__langExpression.search(content))

    # r"..." is needed for parameter cause of non escaping
    def setLangExpression(self, langExpression: str):
        self.__langExpression: re = re.compile(langExpression)

    def setSplitExpression(self, splitExpression: str):
        self.__splitExpression: re = re.compile(splitExpression)

    def setIncludeFilter(self, includeFilter: list[str]):
        self.__includeFilter: list[str] = includeFilter

    def setExcludeFilter(self, excludeFilter: list[str]):
        self.__excludeFilter: list[str] = excludeFilter           

    # only origin (not reconstructed content)
    def setLines(self, lines: str):
        self.__lines: list[str] = lines

    # returnes a 2d list that is based on origin
    def setSplitLines(self) -> list[list[str]]:
        self.__splitLines: list[list[str]] = [self.__splitExpression.search(line) for line in self.__lines] 

    # for repositioning within origin, if reconstruct method is called
    def setIndicies(self, indicies: list[list[int]]):
        self.__indicies: list[list[int]] = indicies
import random
import time

from deep_translator import GoogleTranslator, exceptions

from LogFile import LogFile

# translate string
# don't use intern method batch_translate 'cause it makes a request for every element of list
class Translate:
    def __init__(self, source: str, target: str, timeoutEach: list[float], timeout: float, logFile: LogFile):
        self.__translator: GoogleTranslator = GoogleTranslator(source = source, target = target)
        # timeoutEach: for every request that will be make; timeout: if error is happending
        self.__timeoutEach: list[float] = timeoutEach
        self.__timeout: float = timeout
        # for log responses
        self.__logFile: LogFile = logFile

    def makeTranslation(self, content: str) -> str:
        time.sleep(random.uniform(self.__timeoutEach[0], self.__timeoutEach[1]))
        # for preventing errors that are happening 'cause of 'TranslationNotFound'
        iterator: int = 0
        while True:
            try:
                translated: str = self.__translator.translate(content)
                return translated
            # returns the raw content if 'TranslationNotFound' happend multiple times 
            except exceptions.TranslationNotFound as e:
                self.makeResponse(f"TranslationNotFound error occurred: *{e}* - retry it *{2 - (iterator + 1)}*")
                if iterator > 3:
                    return content
                iterator += 1
            # mostly timeouts or resets of a connection
            except Exception as e:
                self.makeResponse(f"Unexpected translation occurred error: *{e}*")
            # if error is occurred
            time.sleep(self.__timeout)

    def makeResponse(self, response: str):
        self.__logFile.add(response)
        print(response)
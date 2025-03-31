import random
import time

from deep_translator import GoogleTranslator, exceptions

# translate string
# don't use intern method batch_translate 'cause it makes a request for every element of list
class Translate:
    def __init__(self, source: str, target: str, timeoutEach: list[float], timeout: float):
        self.__translator: GoogleTranslator = GoogleTranslator(source = source, target = target)
        # timeoutEach: for every request that will be make; timeout: if error is happending
        self.__timeoutEach: list[float] = timeoutEach
        self.__timeout: float = timeout

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
                print(f"TranslationNotFound error occurred: '{e}' - retry [{iterator + 1}]")
                if iterator > 3:
                    return content
                iterator += 1
            # mostly timeouts or resets of a connection
            except Exception as e:
                print(f"Unexpected error: '{e}'")
            # if error is occurred
            time.sleep(self.__timeout)
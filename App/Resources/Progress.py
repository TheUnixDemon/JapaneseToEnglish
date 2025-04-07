import time
import math

# for make responses to the current progress and the needed time to finish
# it calculates the arithmic time for a request
class Progress:
    def __init__(self, maxChar: int):
        self.__timeMeasurements: list[float] = []
        self.__maxChar: int = maxChar

    def calcRestTime(self, translatedSegments: list[str]) -> float:
        # calculates the rest of characters for finishing the process
        if len(self.__timeMeasurements) < 3:
            return 0.0
        charsRemaining: int = sum([len(segment) for segment in self.__segments[len(translatedSegments)-1:]])
        # needed requests to finish; rounds up
        restOfRequests: int = math.ceil(charsRemaining / self.__maxChar)
        return round(restOfRequests * self.returnAverageTime())

    # all segments that are to translate
    def setSegments(self, segments: list[str]):
        self.__segments: list[str] = segments

    def returnAverageTime(self) -> float:
        timeOverall: float = sum(self.__timeMeasurements)
        return timeOverall / len(self.__timeMeasurements)

    # sets end time; adds time measurment to list
    def addTimeMeasurement(self):
        self.__timeMeasurements.append(time.time() - self.__timeStart)
            
    def getTimeMeasurements(self) -> list[float]:
        return self.__timeMeasurements

    # for getting time in secound: float format
    def setStartTime(self):
        self.__timeStart: float = round(time.time())
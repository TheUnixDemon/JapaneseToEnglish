from App.Resources.Optimize import Optimize
from Resources.Translate import Translate

class BatchTranslate(Optimize):
    def __init__(self, langExpression: str, splitExpression: str, includefilter: list[str], excludeFilter: list[str])
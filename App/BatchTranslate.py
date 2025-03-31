from App.Resources.Optimize import Optimize
from Resources.Translate import Translate

class BatchTranslate(Optimize):
    def __init__(self, splitExpression: str, includefilter: list[str], excludeFilter: list[str], charsMax: int):
        super().__init__()
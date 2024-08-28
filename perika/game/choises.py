from enum import Enum, unique
from typing import List

@unique
class LevelComplexity(Enum):
    easy = 1
    medium = 2
    hard = 3

    @classmethod
    def list_keys(self) -> List[str]:
        return [x.name for x in self]

    @classmethod
    def list_value(self) -> List[int]:
        return [x.value for x in self]

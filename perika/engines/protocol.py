from typing import runtime_checkable, Protocol

from perika.game.level.complexity.protocol import LevelComplexity


class TaskTextEngigne(Protocol):
    pass
@runtime_checkable
class TaskText(Protocol):

    def __init__(self, text: str):
        self.text_backend = TaskTextEngigne
        self.complexity: LevelComplexity

    def get_or_create(self):
        pass
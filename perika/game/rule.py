from __future__ import annotations

from perika.engine.base import TextEngine
from perika.game.level import Level
from perika.game.player import Player
from perika.game.task import Task
from perika.game.choises import LevelComplexity
from perika.engine.fishtext import FishTextEngine


class Game:
    def __init__(
        self,
        level_hard: LevelComplexity,
        level_size: int,
        player: Player,
        engine_name: str,
    ):
        self.level_hard = level_hard
        self.level_size = level_size
        self.player = player
        self.engine = self._resolve_engine(engine_name)

    def _resolve_engine(self, eng: str) -> TextEngine:
        # TODO: resolve engine names pretty
        if eng == "fishtext":
            return FishTextEngine(complexity=LevelComplexity[self.level_hard].value)
        else:
            raise NotImplementedError("Engine not implemented")

    def generate_level(self) -> Level:
        result = []
        for i in range(self.level_size):
            result.append(Task(self.engine.get_or_generate()))

        return Level(result)

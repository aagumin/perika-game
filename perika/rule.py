from __future__ import annotations

import time

from perika.engine.base import TextEngine
from perika.level import Level
from perika.player import Player
from perika.task import Task
from perika.choises import Engine
from perika.engine.fishtext import FishTextEngine


class Game:
    def __init__(self, level_hard: int, level_size: int, player: Player, engine_name: str):
        self.level_hard = level_hard
        self.level_size = level_size
        self.player = player
        self.engine = self._resolve_engine(engine_name)

    def _resolve_engine(self, str) -> TextEngine:
        # TODO: resolve engine names pretty
        if str == "fishtext":
            return FishTextEngine()
        else:
            raise NotImplementedError("Engine not implemented")

    def generate_level(self) -> Level:
        result = []
        for i in range(self.level_size):
            time.sleep(1)
            result.append(Task(self.engine.get_or_generate()))

        return Level(result)

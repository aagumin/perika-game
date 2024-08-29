from functools import lru_cache
from typing import Protocol, Iterable

from perika.game.player import Player


class Score:
    def __init__(self, player: Player,duration: float, hard_level: int) -> None:
        self.player = player
        self.duration = duration
        self.hard_level = hard_level

    def _algorithm(self):
        return self.hard_level * (self.duration * 0.8)

    @lru_cache()
    def calculate(self):
        return self._algorithm()


class TableScore:
    def __init__(self, scores: Iterable[Score]) -> None:
        self.scores = scores


from __future__ import annotations

import time
from dataclasses import dataclass
from functools import lru_cache
from typing import TYPE_CHECKING

from typing_extensions import Self

from perika.engine.fishtext import FishTextEngine
from perika.game.choises import LevelComplexity
from perika.game.level import Level
from perika.game.score import Score
from perika.game.task import Task, CompareResult

if TYPE_CHECKING:
    from perika.engine.base import TextEngine
    from perika.game.player import Player


class Game:
    def __init__(
        self,
        level_hard: LevelComplexity,
        level_size: int,
        player: Player,
        engine_name: str,
    ) -> None:
        self.level_hard = level_hard
        self.level_size = level_size
        self.player = player
        self.engine = self._resolve_engine(engine_name)

    def _resolve_engine(self, eng: str) -> TextEngine:
        if eng == "fishtext":
            return FishTextEngine(complexity=LevelComplexity[self.level_hard].value)  # type: ignore
        msg = "Engine not implemented"
        raise NotImplementedError(msg)

    def generate_level(self) -> Level:
        result = [Task(self.engine.get_or_generate()) for _ in range(self.level_size)]
        return Level(result)

    def tracking_progress(self) -> GameProgress:
        return GameProgress(self)


class GameProgress:
    def __init__(self, game_rule: Game, time_result_pattern: str = "{:.2f}") -> None:
        self.game_rule = game_rule
        self.result_pattern: str = time_result_pattern

    def __enter__(self) -> Self:
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # noqa: ANN204, ANN001
        self.end_time: float = time.time() - self.start_time

    def result(self, compare_result: CompareResult) -> TaskResult:
        return TaskResult(result=compare_result, score=Score(player=self.game_rule.player, duration=self.end_time, hard_level=1))


class TaskResult:
    def __init__(self,result: CompareResult, score: Score) -> None:
        self.result = result
        self.score: Score = score

    def _calculated_score(self) -> float:
        return self.score.calculate()

    def __repr__(self) -> str:
        return str(self.result) + f"\n User prompt time: {self.score.duration:.2f} sec." + f"\n Score: {self._calculated_score()}"


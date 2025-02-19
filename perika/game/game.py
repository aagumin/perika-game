from __future__ import annotations

import time
from dataclasses import dataclass
from functools import lru_cache
from typing import TYPE_CHECKING, Protocol, Union

from rich.panel import Panel
from typing_extensions import Self

from perika.engine.base import TextEngine
from perika.engine.fishtext import FishTextEngine
from perika.game.choises import LevelComplexity
from perika.game.level import Level
from perika.game.score import Score
from perika.game.setup import GameSetup
from perika.game.task import CompareResult, Task


class Game(Protocol):
    def __init__(
        self,
        game_setup: GameSetup,
    ) -> None:
        self.level_hard: str = game_setup.lvl_hard
        self.level_size: int = game_setup.lvl_size
        self.game_setup: GameSetup = game_setup
        self.player = self.game_setup.player_verification()
        self.engine = self._resolve_engine(self.game_setup.engine_name)

    def _resolve_engine(self, eng: str) -> TextEngine:
        raise NotImplementedError()

    def generate_level(self) -> Level:
        raise NotImplementedError()

    def tracking_progress(self) -> GameProgress:
        raise NotImplementedError()

    def start_banner(self) -> Union[Panel, str]:
        raise NotImplementedError()


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
        return TaskResult(
            result=compare_result, score=Score(player=self.game_rule.player, duration=self.end_time, hard_level=1)
        )


class TaskResult:
    def __init__(self, result: CompareResult, score: Score) -> None:
        self.result = result
        self.score: Score = score

    def _calculated_score(self) -> float:
        return self.score.calculate()

    def __repr__(self) -> str:
        return (
            str(self.result)
            + f"\n User prompt time: {self.score.duration:.2f} sec."
            + f"\n Score: {self._calculated_score()}"
        )

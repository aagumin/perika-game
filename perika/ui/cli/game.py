from typing import TYPE_CHECKING

from rich.panel import Panel

from perika.engine.base import TextEngine
from perika.engine import FishTextEngine
from perika.core.game import GameProgress
from perika.core.game.level import Level
from perika.core.game.setup import GameSetup
from perika.core.game import Task
from perika.core.game.choises import LevelComplexity

if TYPE_CHECKING:
    from perika.engine.base import TextEngine
    from perika.core.game.setup import GameSetup


class CliGame:
    def __init__(
        self,
        game_setup: GameSetup,
    ) -> None:
        self.level_hard: str = game_setup.lvl_hard.__str__()
        self.level_size: int = game_setup.lvl_size
        self.game_setup: GameSetup = game_setup
        self.player = self.game_setup.player_verification()
        self.engine = self._resolve_engine(self.game_setup.engine_name)

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

    def start_banner(self):
        return Panel(
            f"Game information! :flag_in_hole: \n\n "
            f"Player name: [red]{self.player.name}[/red] \n "
            f"Level hard: [yellow]{self.level_hard.capitalize()} [/yellow]\n "
            f"Level size: [green]{self.level_size}[/green]\n "
            f"Text generating engine: [blue]{self.engine.name.capitalize()}[/blue]",
            title="Game level info",
        )

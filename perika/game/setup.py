from typing import Protocol

from perika.game.choises import LevelComplexity
from perika.game.player import Player


def hellower_decorator(func):
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        print(f"Hello [green]{name}![/green]")

    return wrapper


class GameSetup(Protocol):
    def __init__(
        self,
        user: str = "Guest",
        lvl_hard: LevelComplexity = LevelComplexity.easy.name,
        lvl_size: int = 1,
        engine_name: str = "fishtext",
    ):
        self.user = user
        self.lvl_hard = lvl_hard
        self.lvl_size = lvl_size
        self.engine_name = engine_name

    def request_user_name(self):
        raise NotImplementedError()

    def request_game_hard(self):
        raise NotImplementedError()

    def request_level(self):
        raise NotImplementedError()

    def request_game_engine(self):
        raise NotImplementedError()

    def player_verification(self):
        return Player(self.user)

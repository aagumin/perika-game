from rich.prompt import IntPrompt, Prompt

from perika.core.game.choises import LevelComplexity
from perika.core.game.player import Player


def hellower_decorator(func):
    def wrapper(*args, **kwargs):
        name = func(*args, **kwargs)
        print(f"Hello [green]{name}![/green]")

    return wrapper


class GameSetup:
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

    @hellower_decorator
    def request_user_name(self):
        self.user = Prompt.ask(
            prompt="Enter your name :waving_hand:",
            default=self.user,
            show_default=False,
        )
        return self.user

    def request_game_hard(self):
        self.lvl_hard = Prompt.ask(
            prompt="Enter level hard :flexed_biceps:",
            choices=LevelComplexity.list_keys(),
            default=self.lvl_hard,
            show_choices=True,
        )
        return self.lvl_hard

    def request_level(self):
        self.lvl_size = IntPrompt.ask(
            "Enter level size [int, max: 10] :sunglasses:", default=self.lvl_size, show_default=False
        )
        return self.lvl_size

    def request_game_engine(self):
        self.engine_name = Prompt.ask(
            "Set text engine :brain:",
            default=self.engine_name,
            choices=["fishtext", "gigachat"],
            show_choices=True,
        )
        return self.engine_name

    def player_verification(self):
        return Player(self.user)

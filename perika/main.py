import time

import typer
from rich import print
from rich.progress import track
from rich.prompt import Prompt

from perika.player import Player
from perika.rule import Game
from perika.text import PlayerAnswer


def main():
    name = Prompt.ask(prompt="Enter your name :sunglasses:",
                      default="Guest",
                      show_default=False)  # TODO Logic. Verify user existing. Return user meta.

    print(f"As-salamu alaykum {name}!")

    lvl_hard = Prompt.ask(prompt="Enter level hard :sunglasses:",
                          choices=["easy", "medium", "hard"], default="easy",
                          show_choices=True)
    lvl_size = Prompt.ask("Enter level size (int, max: 10) :sunglasses:", default=1)

    player = Player(name)

    engine_name = Prompt.ask("Set text engine :sunglasses:", default="fishtext", choices=["fishtext", "gigachat"], show_choices=True)

    print(f"Generate level {lvl_hard} with size {lvl_size}!")
    game_rule = Game(lvl_hard, lvl_size, player, engine_name)

    game_level = game_rule.generate_level()

    print(f"Start the game!")
    for i in game_level:
        print("hello")


if __name__ == "__main__":
    typer.run(main)

import typer
from rich import print
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, IntPrompt

from perika.choises import LevelComplexity
from perika.player import Player
from perika.rule import Game
from perika.text import PlayerAnswer


def main():
    name = Prompt.ask(
        prompt="Enter your name :sunglasses:", default="Guest", show_default=False
    )  # TODO Logic. Verify user existing. Return user meta.

    print(f"Hello [green]{name}![/green]")

    lvl_hard = Prompt.ask(
        prompt="Enter level hard :sunglasses:",
        choices=LevelComplexity.list_keys(),
        default=LevelComplexity.easy.name,
        show_choices=True,
    )

    lvl_size = IntPrompt.ask("Enter level size (int, max: 10) :sunglasses:", default=1)

    player = Player(name)

    engine_name = Prompt.ask(
        "Set text engine :sunglasses:",
        default="fishtext",
        choices=["fishtext", "gigachat"],
        show_choices=True,
    )

    game_rule = Game(lvl_hard, lvl_size, player, engine_name)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Generate level...", total=None)
        game_level = game_rule.generate_level()

    print(
        Panel(
            f"Start the game! \n\n "
            f"Player name: [red]{name}[/red] \n "
            f"Level hard: [yellow]{lvl_hard.capitalize()} [/yellow]\n "
            f"Level size: [green]{lvl_size}[/green]\n "
            f"Text generating engine: [blue]{engine_name.capitalize()}[/blue]",
            title="Game level info",
        )
    )

    start_game = typer.confirm("Start the game?", default=True, show_default=True)
    if not start_game:
        print("Bye-bye .. :(")
        raise typer.Abort()

    cnt = 1
    for task in game_level:
        print(Panel.fit(task(), title=f"Round {cnt}"))
        answer = PlayerAnswer(Prompt.ask("result -> "))
        print(task.compare(answer))
        cnt += 1


if __name__ == "__main__":
    typer.run(main)

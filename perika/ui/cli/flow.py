import typer
from rich import print
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

from perika.core.game import PlayerAnswer

from .game import CliGame
from .setup import GameSetup


def start_game() -> None:
    game_setup = GameSetup()

    game_setup.request_user_name()
    game_setup.request_game_hard()
    game_setup.request_level()
    game_setup.request_game_engine()

    game_rule = CliGame(game_setup=game_setup)  # type: ignore

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Generate level...", total=None)
        game_level = game_rule.generate_level()

    print(game_rule.start_banner())

    start_game = typer.confirm("Start the game?", default=True, show_default=True)

    if not start_game:
        msg = "Bye-bye .. game cancelled :("
        raise typer.Abort(msg)

    cnt = 1
    for task in game_level:
        print(Panel.fit(task(), title=f"Round {cnt}"))
        with game_rule.tracking_progress() as progress:
            answer = PlayerAnswer(Prompt.ask("[bold red] your prompt -> "))

        print(progress.result(task.compare(answer)))
        cnt += 1

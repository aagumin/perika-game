
from perika.flow import start_game

import typer

app = typer.Typer()

@app.command('start')
def start():
    return start_game()
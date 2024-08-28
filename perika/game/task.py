from dataclasses import dataclass
from typing import Optional

from perika.game.text import TaskText, PlayerAnswer
import difflib


@dataclass
class TaskResult:
    equal: bool
    diff: Optional[str]

    def __repr__(self):
        return (
            f"TaskResult \n"
            f" equal >>> {self.equal}\n"
            f" diff  >>> \n "
            f"{self.diff}"
        )


class Task:
    def __init__(self, text: TaskText):
        self.text = text

    def __call__(self):
        return self.text()

    def compare(self, player_input: PlayerAnswer) -> TaskResult:
        eq = self.text() == player_input()
        diff = "Success"
        if not eq:
            differ = difflib.Differ()
            raw_diff = list(differ.compare([self.text()], [player_input()]))
            diff = "\n".join(raw_diff)
        return TaskResult(equal=eq, diff=diff)

from typing import Iterable

from perika.task import Task


class Level:
    def __init__(self, tasks: Iterable[Task]):
        self.tasks = tasks
        self.max: int = len(self.tasks)

    def __iter__(self):
        self.a = 0

        return self

    def __next__(self):
        x = self.tasks[self.a]
        self.a += 1
        if self.a == self.max:
            raise StopIteration
        return x
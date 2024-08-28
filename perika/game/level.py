from typing import List

from .task import Task


class Level:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks
        self.index = 0
        self.max_level_size = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.tasks) and self.index <= self.max_level_size:
            item = self.tasks[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

import time
from dataclasses import dataclass

from perika.game.task import TaskResult

@dataclass
class TaskResultWithTime:
    result: TaskResult
    time: float

    def __repr__(self):
        return str(self.result) + "\n User prompt time: {:.2f} sec".format(self.time)

class LevelTimer:
    def __init__(self):
        self.result_pattern : str = "{:.2f}"

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time : float = time.time() - self.start_time

    def result(self, result: TaskResult) -> TaskResultWithTime:
        return TaskResultWithTime(result=result, time=self.end_time)


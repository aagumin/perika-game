from typing import Protocol, runtime_checkable

from perika.core.game import TaskText


@runtime_checkable
class TextEngine(Protocol):
    name: str

    def get_or_generate(self) -> TaskText:
        raise NotImplementedError

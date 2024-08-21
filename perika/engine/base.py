from typing import Protocol

from perika.text import Text

class TextEngine(Protocol):

    def get_or_generate(self) -> Text:
        pass

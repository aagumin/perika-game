from dataclasses import dataclass
from enum import Enum
from typing import Callable, Dict, Collection, Union

import requests

from perika.choises import LevelComplexity
from perika.text import TaskText


@dataclass
class FishTextRequestParams:
    format: str = "json"
    number: int = 1
    type: str = "title"


@dataclass
class FishTextRequest:
    DOMAIN: str = "https://fish-text.ru/get"
    params: FishTextRequestParams = FishTextRequestParams()


class FishTextEngine:
    """
    https://fish-text.ru/api

    """

    def __init__(self, complexity: int = 1):
        """
        complexity := (title(1), sentence(2), paragraph(3))
        """
        self.complexity = complexity
        if complexity not in (1, 2, 3):
            raise AttributeError(
                "Сложность текста - это три уровня. Укажите сложность из множества (1,2,3)"
            )

    def _fishtext_request_url_builder(self) -> FishTextRequest:
        """ """
        complexity = {1: "title", 2: "sentence", 3: "paragraph"}

        return FishTextRequest(
            params=FishTextRequestParams(type=complexity[self.complexity])
        )

    def _get_text(self) -> str:
        with requests.session() as session:
            prm = self._fishtext_request_url_builder()

            response = session.get(url=prm.DOMAIN, params=prm.params.__dict__)

            response.raise_for_status()
            return response.json()["text"]

    def text_status_info(self) -> str:
        return f"complexity = {self.complexity}"

    def get_or_generate(self) -> TaskText:
        return TaskText(self._get_text())

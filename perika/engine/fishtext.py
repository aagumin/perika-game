from typing import Callable, Dict

import requests

from perika.text import Text


class FishTextEngine:
    """
    https://fish-text.ru/api

    """

    def __init__(self, complexity: int = 1, level: int = 1, engine: str = "FishText"):
        """
        complexity := (title(1), sentence(2), paragraph(3))
        engine := ("FishText", etc)
        level := text len
        """
        self.complexity = complexity
        self.level = str(level)
        self.engine = engine.lower()
        if complexity not in (1, 2, 3):
            raise AttributeError("Сложность текста - это три уровня. Укажите сложность из множества (1,2,3)")
        if any([self.complexity, self.level]) <= 0:
            raise AttributeError("Сложность текста и\или уровень не может быть меньше либо равен нулю")


    def _fishtext_request_url_builder(self) -> Dict[str, str]:
        """

        """
        complexity = {1: "title",
                      2: "sentence",
                      3: "paragraph"}

        url_config = dict(
            DOMAIN="https://fish-text.ru/get",
            params={"format": "html",
                    "number": self.level,
                    "type": complexity[self.complexity]}
        )

        return url_config

    def _other_request_builder_conf(self):
        """
        Для расширения
        """
        pass

    def _verify_engine_builder(self) -> Callable:
        if self.engine == "fishtext":
            return self._fishtext_request_url_builder
        else:
            return self._other_request_builder_conf

    def _get_text(self) -> str:
        with requests.session() as session:
            request_builder_conf = self._verify_engine_builder()
            url = request_builder_conf()

            response = session.get(url=url['DOMAIN'], params=url['params'])

            response.raise_for_status()
            return response.text

    def text_status_info(self) -> str:
        return (f"Level = {self.level}, complexity = {self.complexity}, engine = {self.engine}")

    def get_or_generate(self) -> Text:
        return Text(self._get_text())

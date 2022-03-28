from typing import Callable, Dict

import requests


class TextCreator:
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
        self.engine = engine
        if complexity not in (1, 2, 3):
            raise AttributeError("Сложность текста - это три уровня. Укажите сложность из множества (1,2,3)")

    def _fishtext_request_url_builder(self) -> Dict[str,str]:
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
        if self.engine == "FishText":
            return self._fishtext_request_url_builder
        else:
            return self._other_request_builder_conf

    def _get_text(self) -> str:
        session = requests.session()

        request_builder_conf = self._verify_engine_builder()
        url = request_builder_conf()

        response = session.get(url=url['DOMAIN'], params=url['params'])

        if response.status_code == 200:
            return response.text
        else:
            raise ConnectionError(f"Неудачная попытка получение текста, код ошибки - {response.status_code}")

    def text_status_info(self) -> str:
        return (f"Level = {self.level}, complexity = {self.complexity}, engine = {self.engine}")

    def random_text(self) -> str:
        return self._get_text()


if __name__ == "__main__":
    gd = TextCreator()

    print(gd.random_text())

    print(gd.text_status_info())

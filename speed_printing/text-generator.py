from typing import Callable

import requests


class TextCreator:
    """
    https://fish-text.ru/api

    """

    def __init__(self, complexity: int = 1, level: int = 1, engine: str = "FishText"):
        """
        level := (title(1), sentence(2), paragraph(3))
        engine := ("FishText", etc)
        """
        self.complexity = complexity
        self.level = level
        self.engine = engine
        if complexity not in (1, 2, 3):
            raise AttributeError("Сложность текста - это три уровня. Укажите сложность из множества (1,2,3)")

    def _fishtext_request_url_builder(self) -> str:

        url_config = dict(
            pattern="https://fish-text.ru/get?format={format}&number={number}&type={type}",
            default_format="html",
            default_type="sentence",
            complexity={1: "title",
                        2: "sentence",
                        3: "paragraph"}
        )
        url = url_config['pattern'].format(
            format=url_config["default_format"],
            number=self.level,
            type=url_config['complexity'][self.complexity])

        return url

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

        request_builder_conf = self._verify_engine_builder()
        url = request_builder_conf()

        response = requests.get(url=url)

        return response.text

    def info(self) -> None:
        return print(f"Level = {self.level}, complexity = {self.complexity}, engine = {self.engine}")

    def random_text(self) -> str:
        return self._get_text()


if __name__ == "__main__":

    gd = TextCreator()

    print(gd.random_text())

    print(gd.info())

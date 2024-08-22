class TaskText:
    def __init__(self, text: str):
        self.text = text

    def __call__(self) -> str:
        return self.text


class PlayerAnswer:
    def __init__(self, player_text: str):
        self.player_text = player_text

    def __call__(self) -> str:
        return self.player_text

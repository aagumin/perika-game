from perika.text import Text, PlayerAnswer


class Task:
    
    def __init__(self, text: Text):
        self.text = text
    
    
    def compare(self, other: PlayerAnswer) -> str:
        pass
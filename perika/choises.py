from enum import Enum

from perika.engine.base import TextEngine
from perika.engine.fishtext import FishTextEngine
from perika.engine.gigachat import GigaChatEngine


class Engine(Enum):
    fishtext: TextEngine = FishTextEngine
    gigachat: TextEngine = GigaChatEngine


import sys

from .env import Environment
from .objects.unit import Unit
from .config import Config

class MyGame(Environment):

    def __init__(self, config: Config, *args, **kwargs) -> None:
        super().__init__(config, *args, **kwargs)
        self.add_object(Unit(self, pos=(50,50), size=config.UNIT_SIZE, color='red'))
        self.add_object(Unit(self, pos=(100,50), size=config.UNIT_SIZE, color='blue'))

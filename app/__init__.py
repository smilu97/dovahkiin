
import sys
import random

from .env import Environment
from .objects.unit import Unit
from .config import Config

class MyGame(Environment):

    def __init__(self, config: Config, *args, **kwargs) -> None:
        
        super().__init__(config, *args, **kwargs)

        self.unit_1 = Unit(
            self,
            pos=self._make_random_unit_pos(),
            speed=config.UNIT_SPEED,
            size=config.UNIT_SIZE,
            color='red')
        self.unit_2 = Unit(
            self,
            pos=self._make_random_unit_pos(),
            speed=config.UNIT_SPEED,
            size=config.UNIT_SIZE,
            color='blue')

        self.add_object(self.unit_1)
        self.add_object(self.unit_2)
    
    def _make_random_unit_pos(self):

        return (
            random.randint(0, self.config.SCREEN_SIZE[0] - self.config.UNIT_SIZE[0]),
            random.randint(0, self.config.SCREEN_SIZE[1] - self.config.UNIT_SIZE[1])
        )

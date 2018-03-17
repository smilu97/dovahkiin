
import dovahkiin as dk

import sys
import random

from dk.env import Environment
from .object.unit import Unit
from .config import Config

class MyGame(Environment):

    def __init__(self, config: Config, *args, **kwargs) -> None:
        
        super().__init__(config, tag_list=config.TAG_LIST, *args, **kwargs)

        self.red = []
        self.blue = []

        for _ in range(3):
            self.red.append(self._make_new_unit('red'))
            self.blue.append(self._make_new_unit('blue'))
    
    def _make_new_unit(self, color='red'):
        res = Unit(
            self,
            pos=self._make_random_unit_pos(),
            speed=self.config.UNIT_SPEED,
            size=self.config.UNIT_SIZE,
            color=color)
        self.add_object(res)
        return res
    
    def _make_random_unit_pos(self):

        return (
            random.randint(0, self.config.SCREEN_SIZE[0] - self.config.UNIT_SIZE[0]),
            random.randint(0, self.config.SCREEN_SIZE[1] - self.config.UNIT_SIZE[1])
        )

    def check_game_end(self):

        color = self.red[0].unit.color
        for unit in self.red + self.blue:
            if unit.unit.color != color:
                return False
        print(color)
        return True
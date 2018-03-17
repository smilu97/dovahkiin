
import math
import random

from . import Agent

class SimpleAgent(Agent):

    def __init__(self, obj):
        super().__init__(obj)
        self.units = obj.env.red + obj.env.blue
        self.target = None
        self.target_color = None
    
    def make_decision(self):

        if self.target is None or self.target.unit.color == self.obj.unit.color:
            self.target = self._find_target()
            self.target_color = self.target.unit.color if self.target is not None else None
        
        if self.target is not None:
            ra = math.pi / 18
            dpos = self.target.pos - self.obj.pos
            angle = math.atan2(dpos[1], dpos[0]) + random.uniform(-ra, ra)
            self.obj.process('shoot', angle=angle)
        
        self.obj.process('move', angle=random.uniform(0, math.pi * 2))
    
    def _find_target(self):
        my_color = self.obj.unit.color
        for unit in self.units:
            if unit == self.obj: continue
            if unit.unit.color != my_color:
                return unit
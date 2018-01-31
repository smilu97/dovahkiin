
import math
import random

from . import Agent

class RandomAgent(Agent):
    
    def make_decision(self):
        
        self.obj.process('move', angle=random.uniform(0, math.pi * 2))
        self.obj.process('shoot', angle=random.uniform(0, math.pi * 2))
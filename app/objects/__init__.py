
####
# Author: smilu97
# Created date: 180129
####

import numpy as np

from ..env import Environment

class GameObject:
    '''
    Base class for game object
    ''' 
    def __init__(self, env: Environment) -> None:
        self.env = env
        self.pos = np.zeros(2, dtype=np.int32)
        self.components = []
        self.env.objs.add(self)
    
    def destory(self) -> None:
    	for component in self.components:
    		component.destory()
    	self.env.objs.remove(self)

    def process(self, msg_type: str, *args, **kwargs) -> None:
    	for component in self.components:
    		component.process(msg_type, *args, **kwargs)

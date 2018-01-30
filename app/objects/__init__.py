
####
# Author: smilu97
# Created date: 180129
####

import numpy as np

class GameObject:
    '''
    Base class for game object
    ''' 
    def __init__(self, env) -> None:
        self.env = env
        self.pos = np.zeros(2, dtype=np.int32)
        self.components = []
        self.env.objs.add(self)
        self._tag = None
    
    def update(self) -> None:
        for component in self.components:
            component.update()
    
    def destory(self) -> None:
    	for component in self.components:
    		component.destory()
    	self.env.objs.remove(self)

    def process(self, msg_type: str, *args, **kwargs) -> None:
    	for component in self.components:
    		component.process(msg_type, *args, **kwargs)

    @property
    def tag(self) -> None:
        return self._tag

    @tag.setter
    def tag(self, value) -> None:
        n_cont = self.env.tag_cont.get(value)
        if n_cont is None:
            return
        if self._tag is not None:
            o_cont = self.tag_cont.get(self._tag)
            o_cont.remove(self)
        n_cont.add(self)
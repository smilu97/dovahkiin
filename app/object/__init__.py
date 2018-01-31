
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
        self.pos = np.zeros(2, dtype=np.float32)
        self.components = []
        self._tag = None
        self.agent = None
    
    def register_env(self, env) -> None:
        self.env = env
    
    def update(self) -> None:
        if self.agent is not None:
            self.agent.make_decision()
        for component in self.components:
            component.update()
    
    def render(self) -> None:
        for component in self.components:
            component.render()

    def destroy(self) -> None:
        self.env.register_delete(self)

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
        self._tag = value
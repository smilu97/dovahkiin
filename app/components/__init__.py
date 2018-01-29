
from ..objects import GameObject

class Component:
    '''
    Component is base unit of function or
    working of every game objects
    '''
    def __init__(self, obj: GameObject) -> None:
        
        self.obj = obj
        self.env = obj.env

    def update(self) -> None:
        pass

    def destory(self) -> None:
    	pass

    def process(self, msg_type: str, *args, **kwargs) -> None:
    	pass
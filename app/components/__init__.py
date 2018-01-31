
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
    
    def render(self) -> None:
        pass

    def on_destroy(self) -> None:
        pass

    def process(self, msg_type: str, *args, **kwargs) -> None:
    	pass
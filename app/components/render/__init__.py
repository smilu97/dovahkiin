
from .. import Component
from ...objects import GameObject

class Renderer(Component):

    def __init__(self, obj: GameObject) -> None:
        super().__init__(obj)
        obj.renderer = self
    
    def render(self) -> None:
        pass
    
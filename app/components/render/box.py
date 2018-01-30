
import pygame as pg

from . import Renderer
from ...objects import GameObject

class BoxRenderer(Renderer):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject, color, size) -> None:
        super().__init__(obj)
        self.color = color
        self.size = size
    
    def update(self) -> None:
        surf = self.obj.env.surf
        if surf is None:
            return
        rect = pg.Rect(
            self.obj.pos[0] - self.size[0] / 2,
            self.obj.pos[1] - self.size[1] / 2,
            self.size[0],
            self.size[1]
        )
        pg.draw.rect(surf, self.color, rect)
    
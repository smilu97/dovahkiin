
import pygame as pg

from .. import Component
from ...objects import GameObject

class BoxRenderer(Component):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject, color, size) -> None:
        super().__init__(self, obj)
        self.color = color
        self.size = size
    
    def update(self) -> None:
    	rect = \
    	   [self.obj.pos[0] - self.size[0] / 2,
    		self.obj.pos[1] - self.size[1] / 2,
    		self.obj.pos[0] + self.size[0] / 2,
    		self.obj.pos[1] + self.size[1] / 2]
    	pg.draw.rect(self.obj.env.surf, self.color, rect)
    
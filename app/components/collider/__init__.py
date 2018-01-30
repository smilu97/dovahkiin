
import numpy as np

from .. import Component
from ...objects import GameObject

class Collider(Component):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject) -> None:
        super().__init__(obj)
        obj.env.colliders.add(self)
        obj.collider = self

    def update(self) -> None:
    	self.collidings = []

    def destroy(self) -> None:
    	self.obj.env.colliders.remove(self)
    
    
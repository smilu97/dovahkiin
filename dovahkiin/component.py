
import numpy as np
import pygame as pg

from .gameobject import GameObject

from typing import List

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

class Collider(Component):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject) -> None:
        super().__init__(obj)
        obj.env.colliders.add(self)
        obj.collider = self

    def on_destroy(self) -> None:
    	self.obj.env.colliders.remove(self)

def check_colliding_with_box(coll_1: Collider, coll_2: Collider) -> bool:
    return abs(coll_1.obj.pos[0] - coll_2.obj.pos[0]) <= (coll_1.size[0] + coll_2.size[0]) / 2 and \
           abs(coll_1.obj.pos[1] - coll_2.obj.pos[1]) <= (coll_1.size[1] + coll_2.size[1]) / 2

ctype_to_func = {
    'box': check_colliding_with_box
}

class BoxCollider(Collider):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject, size) -> None:
        super().__init__(obj)
        self.collider_type = 'box'
        self.size = np.array([size[0], size[1]])

    def update(self) -> None:
        self.found = False

    @property
    def collidings(self) -> List[GameObject]:
        if self.found == False:
            self.update_cache()
            self.found = True
        return self.cache
    
    def update_cache(self) -> None:
        self.cache = []
        for k, collider in self.env.colliders.iteritems():
            if collider == self: continue
            func = ctype_to_func.get(collider.collider_type)
            if func is not None and func(self, collider):
                self.cache.append(collider.obj)

class Renderer(Component):

    def __init__(self, obj: GameObject) -> None:
        super().__init__(obj)
        obj.renderer = self
    
    def render(self) -> None:
        pass

class BoxRenderer(Renderer):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject, color, size) -> None:
        super().__init__(obj)
        self.color = color
        self.size = size
    
    def render(self) -> None:
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
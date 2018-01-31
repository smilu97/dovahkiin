
import numpy as np

from . import Collider
from ...objects import GameObject
from typing import List

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
                print('hit: ({}, {})'.format(self.obj.pos, collider.obj.pos))

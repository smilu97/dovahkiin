
from numpy as np
from . import Collider
from ...objects import GameObject
from typing import List

def check_colliding_with_box(coll_1: Collider, coll_2: Collider) -> bool:
    return abs(coll_1.obj.pos[0] - coll_2.obj.pos[0]) <= coll_1.size[0] + coll_2.size[0] and \
           abs(coll_1.obj.pos[1] - coll_2.obj.pos[1]) <= coll_1.size[1] + coll_2.size[1]

ctype_to_func = {
    'box': check_colliding_with_box
}

class BoxCollider(Collider):
    '''
    Component checking collision between game object
    '''
    def __init__(self, obj: GameObject, size) -> None:
        super().__init__(self, obj)
        self.collider_type = 'box'
        self.size = np.array([size[0], size[1]])

    def update(self) -> None:
        self.found = False

    @property
    def collidings(self) -> List[GameObject]:
        if self.found == False:
            self.cache = self.find_colliding()
            self.found = True
        return self.cache
    
    def find_colliding(self) -> List[GameObject]:
        result = []
        for collider in self.env.colliders:
            func = ctype_to_func.get(collider.tag)
            if func is not None and func(self, collider):
                result.append(collider.obj)
        return result
    
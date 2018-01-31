
from ..env import Environment
from . import GameObject
from ..component.bullet import BulletComponent
from ..component.collider.box import BoxCollider
from ..component.render.box import BoxRenderer

class Bullet(GameObject):

	def __init__(self, env=None, unit=None, pos=(0,0), angle=0, speed=0, size=(10,10), tag='bullet') -> None:

		super().__init__(env)
		self.pos = pos
		self.tag = tag
		self.components.append(BoxCollider(self, size=size))
		self.components.append(BoxRenderer(self, color=(0,255,0), size=size))
		self.components.append(BulletComponent(self, unit, angle=angle, speed=speed, size=size))

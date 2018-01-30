
from ..env import Environment
from . import GameObject
from ..components.bullet import BulletComponent
from ..components.collider.box import BoxCollider

class Bullet(GameObject):

	def __init__(self, env: Environment, size, tag='bullet') -> None:

		super().__init__(self, env)
		self.tag = tag
		self.components.append(BoxCollider(self, size))
		self.components.append(BoxRenderer(self, GREEN, size))
		self.components.append(BulletComponent(self))

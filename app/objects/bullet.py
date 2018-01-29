
from ..env import Environment
from . import GameObject
from ..components.bullet import BulletComponent
from ..components.collider.box import BoxCollider

class Bullet(GameObject):

	def __init__(self, env: Environment, size) -> None:

		super().__init__(self, env)
		self.type = 'bullet'
		self.collider = BoxCollider(self, size)
		self.components.append(self.collider)
		self.renderer = BoxRenderer(self, GREEN, size)
		self.components.append(self.renderer)
		self.components.append(BulletComponent(self))


from ..env import Environment
from . import GameObject
from ..components.bullet import BulletComponent
from ..components.collider.box import BoxCollider
from ..components.render.box import BoxRenderer

class Bullet(GameObject):

	def __init__(self, env: Environment, unit, angle, speed, size=10, tag='bullet') -> None:

		super().__init__(env)
		self.tag = tag
		self.components.append(BoxCollider(self, size))
		self.components.append(BoxRenderer(self, GREEN, size))
		self.components.append(BulletComponent(self, unit, angle, speed))

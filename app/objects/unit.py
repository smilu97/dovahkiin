
from ..env import Environment
from . import GameObject
from ..components.unit import UnitComponent
from ..components.collider.box import BoxCollider

class Unit(GameObject):

	def __init__(self, env: Environment, size, color='red') -> None:

		super().__init__(self, env)

		r_color = (255, 0, 0) if color == 'red' else (0, 0, 255)

		self.type = 'unit'
		self.collider = BoxCollider(self, size)
		self.components.append(self.collider)
		self.renderer = BoxRenderer(self, r_color, size)
		self.components.append(self.renderer)
		self.components.append(UnitComponent(self, color))
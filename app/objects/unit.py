
from ..env import Environment
from . import GameObject
from ..components.unit import UnitComponent
from ..components.collider.box import BoxCollider
from ..components.render.box import BoxRenderer

class Unit(GameObject):

	def __init__(self, env: Environment, pos, size=(10,10), color='red', tag='unit') -> None:

		super().__init__(env)

		r_color = (255, 0, 0) if color == 'red' else (0, 0, 255)

		self.pos[0] = pos[0]
		self.pos[1] = pos[1]
		self.tag = tag
		self.components.append(BoxCollider(self, size))
		self.components.append(BoxRenderer(self, r_color, size))
		self.components.append(UnitComponent(self, color))
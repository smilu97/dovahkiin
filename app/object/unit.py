
from ..env import Environment
from . import GameObject
from ..component.unit import UnitComponent
from ..component.collider.box import BoxCollider
from ..component.render.box import BoxRenderer

class Unit(GameObject):

	def __init__(self, env=None, pos=(0,0), speed=0, size=(10,10), color='red', tag='unit') -> None:

		super().__init__(env)

		r_color = (255, 0, 0) if color == 'red' else (0, 0, 255)

		self.pos[0] = pos[0]
		self.pos[1] = pos[1]
		self.tag = tag
		self.components.append(BoxCollider(self, size=size))
		self.components.append(BoxRenderer(self, color=r_color, size=size))
		self.components.append(
			UnitComponent(
				self,
				speed=speed,
				color=color,
				size=size,
				max_bullet=self.env.config.MAX_BULLET
			)
		)
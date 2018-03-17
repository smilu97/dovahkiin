
import math
import numpy as np

from dovahkiin.component import Component
from dovahkiin.object import GameObject

class BulletComponent(Component):
	
	def __init__(self, obj: GameObject, unit, angle=0, speed=0, size=(10,10)) -> None:
		super().__init__(obj)
		self.d_pos = np.array([math.cos(angle), math.sin(angle)]) * speed
		self.unit = unit.unit
		self.unit.bullet_count += 1
		self.size = size

		self.max_boundary = self.obj.env.config.SCREEN_SIZE

	def update(self) -> None:

		unit = None
		for obj in self.obj.collider.collidings:
			if obj.tag == 'unit' and obj.unit.color != self.unit.color:
				obj.process('toggle_color')
				self.obj.destroy()
				return

		self.obj.pos += self.d_pos
		if self.obj.pos[0] <= -self.size[0] or self.obj.pos[1] <= -self.size[1] or \
			self.obj.pos[0] >= self.max_boundary[0] or self.obj.pos[1] >= self.max_boundary[1]:
			self.obj.destroy()
			return
	
	def on_destroy(self) -> None:
		self.unit.bullet_count -= 1

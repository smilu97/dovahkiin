
import math

from . import Component
from ..objects import GameObject

class BulletComponent(Component):
	
	def __init__(self, obj: GameObject, unit, angle, speed) -> None:
		super().__init__(obj)
		self.d_pos = np.array([math.cos(angle), math.sin(angle)]) * speed
		self.unit = unit.unit
		self.unit.bullet_count += 1

	def update(self) -> None:
		unit = None
		for obj in self.obj.collider.collidings:
			if obj.tag == 'unit':
				unit = obj
				break
		if unit is not None:
			unit.process('toggle_color')
			self.destroy()
		self.obj.pos += self.d_pos
	
	def destroy(self) -> None:
		super().destroy()
		self.unit.bullet_count -= 1

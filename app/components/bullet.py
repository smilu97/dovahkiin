
from . import Component
from ..objects import GameObject

class BulletComponent(Component):
	
	def __init__(self, obj: GameObject) -> None:
		super().__init__(self, obj)

	def update(self) -> None:
		unit = None
		for obj in self.obj.collider.collidings:
			if obj.type == 'unit':
				unit = obj
				break
		if unit is not None:
			unit.process('toggle_color')
			self.destroy()

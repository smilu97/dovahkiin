
import numpy as np
import math

from . import Component
from ..objects import GameObject

class UnitComponent(Component):
	
	def __init__(self, obj: GameObject, speed: float, color='red', max_bullet=1) -> None:
		super().__init__(obj)
		self.color = color
		self.speed = speed
		self.bullet_count = 0
		self.max_bullet = max_bullet
		obj.unit = self

	def process(self, msg_type: str, *args, **kwargs) -> None:
		if msg_type == 'toggle_color':
			self.color = 'blue' if self.color == 'red' else 'red'
			self._notify_color()
		elif msg_type == 'move':
			angle = kwargs.get('angle')
			if angle is not None:
				self._move(angle)
		elif msg_type == 'shoot':
			angle = kwargs.get('angle')
			if angle is not None:
				self._shoot(angle)

	def _notify_color(self) -> None:
		self.renderer.color = (255, 0, 0) if self.color == 'red' else (0, 0, 255)
	
	def _shoot(self, angle: float) -> None:
		if self.bullet_count >= self.max_bullet:
			return
	
	def _move(self, angle: float) -> None:
		d_pos = np.array([math.cos(angle), math.sin(angle)]) * self.speed
		self.obj.pos += d_pos
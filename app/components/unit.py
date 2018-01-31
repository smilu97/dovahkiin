
import numpy as np
import math

from . import Component
from ..objects import GameObject
from ..objects.bullet import Bullet

class UnitComponent(Component):
	
	def __init__(self, obj: GameObject, speed=0, color='red', size=(10,10), max_bullet=1) -> None:
		super().__init__(obj)
		self.speed = speed
		self.color = color
		self.size = size
		self.max_bullet = max_bullet
		self.bullet_count = 0
		self.bullet_speed = self.obj.env.config.BULLET_SPEED
		self.bullet_size = self.obj.env.config.BULLET_SIZE

		self.max_boundary = (
			self.obj.env.config.SCREEN_SIZE[0] - self.obj.env.config.UNIT_SIZE[0],
			self.obj.env.config.SCREEN_SIZE[1] - self.obj.env.config.UNIT_SIZE[1]
		)

		self.shoot_radius = max(size[0], size[1]) * math.sqrt(2) / 2 + 2

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
		self.obj.renderer.color = (255, 0, 0) if self.color == 'red' else (0, 0, 255)
	
	def _shoot(self, angle: float) -> None:
		if self.bullet_count >= self.max_bullet:
			return
		shoot_pos = self.obj.pos + np.array((math.cos(angle), math.sin(angle))) * self.shoot_radius
		self.obj.env.add_object(Bullet(
			env=self.obj.env,
			unit=self.obj,
			pos=shoot_pos,
			angle=angle,
			speed=self.bullet_speed,
			size=self.bullet_size
		))
	
	def _move(self, angle: float) -> None:
		d_pos = np.array([math.cos(angle), math.sin(angle)], dtype=np.float32) * self.speed
		self.obj.pos += d_pos
		
		# Check pos if it is on max_boundary
		if   self.obj.pos[0] < 0: self.obj.pos[0] *= -1
		elif self.obj.pos[0] > self.max_boundary[0]: self.obj.pos[0] = self.max_boundary[0] * 2 - self.obj.pos[0]
		if   self.obj.pos[1] < 0: self.obj.pos[1] *= -1
		elif self.obj.pos[1] > self.max_boundary[1]: self.obj.pos[1] = self.max_boundary[1] * 2 - self.obj.pos[1]
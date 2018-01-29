
from . import Component
from ..objects import GameObject

class UnitComponent(Component):
	
	def __init__(self, obj: GameObject, color='red') -> None:
		super().__init__(self, obj)
		self.color = color

	def update(self) -> None:
		pass

	def process(self, msg_type: str, *args, **kwargs) -> None:
		if msg_type == 'toggle_color':
			self.color = 'blue' if self.color == 'red' else 'red'
			self.notify_color()

	def notify_color(self) -> None:
		self.renderer.color = (255, 0, 0) if self.color == 'red' else (0, 0, 255)
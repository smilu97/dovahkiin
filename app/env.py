
import random
import pygame as pg

from .containers.distinct import DistinctContainer
from .object import GameObject

from typing import List

class Environment:

	def __init__(self, config, tag_list=[]) -> None:
		self.config = config
		self.colliders = DistinctContainer()
		self.objs = DistinctContainer()
		self.tag_cont = self._create_tag_cont(tag_list)
		self.done = False
		self.is_printing = config.PRINTING
		self.fps = config.FPS
		self.pause = False
		self.delete_queue = []
		self.insert_queue = []

		if self.is_printing:
			self._init_pygame()
		else:
			self.surf = None
		
	def add_object(self, obj: GameObject) -> None:
		self.insert_queue.append(obj)
	
	def register_delete(self, obj) -> None:
		self.delete_queue.append(obj)
	
	@staticmethod
	def _create_tag_cont(tag_list) -> dict:
		result = {}
		for tag in tag_list:
			result[tag] = DistinctContainer()
		return result
	
	def _init_pygame(self) -> None:
		pg.init()
		self.surf = pg.display.set_mode(self.config.SCREEN_SIZE)
		self.clock = pg.time.Clock()
	
	def update(self) -> None:
		
		if not self.pause:
			for k, obj in self.objs.iteritems():
				obj.update()
		
		for obj in self.delete_queue:
			for component in obj.components:
				component.on_destroy()
			self.objs.remove(obj)
		self.delete_queue = []
	
		for obj in self.insert_queue:
			self.objs.add(obj)
			obj.register_env(self)
		self.insert_queue = []
			
		if self.is_printing:
			self.render()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.done = True
				if event.type == pg.KEYDOWN and event.key == pg.K_p:
					self.pause = not self.pause
		
	def render(self):
		
		self.surf.fill((0,0,0))
		for k, obj in self.objs.iteritems():
			obj.render()
		pg.display.flip()
		self.clock.tick(self.fps)

	def find_objects_by_tag(tag: str) -> List[GameObject]:
		cont = self.tag_cont.get(tag)
		if cont is None:
			return []
		return list(cont)
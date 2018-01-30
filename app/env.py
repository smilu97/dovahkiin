
import random
import pygame as pg

from .containers.distinct import DistinctContainer
from .objects import GameObject

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

		if self.is_printing:
			self._init_pygame()
		else:
			self.surf = None
		
	def add_object(self, obj: GameObject) -> None:
		self.objs.add(obj)
	
	@staticmethod
	def _create_tag_cont(tag_list) -> dict:
		result = {}
		for tag in tag_list:
			result[tag] = DistinctContainer()
		return result
	
	def _init_pygame(self, screen_size=(400,300)) -> None:
		pg.init()
		self.surf = pg.display.set_mode(screen_size)
		self.clock = pg.time.Clock()
	
	def update(self, msgs=[], is_output=False):
		for msg in msgs:
			target = msg[0]
			argv = msg[1]
		
		for k, obj in self.objs.iteritems():
			obj.update()
			
		if self.is_printing:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.done = True
			pg.display.flip()
			self.clock.tick(self.fps)
		
		if is_output:
			return self._make_output()
	
	def _make_output(self) -> list:
		return []

	def find_objects_by_tag(tag: str) -> List[GameObject]:
		cont = self.tag_cont.get(tag)
		if cont is None:
			return []
		return list(cont)
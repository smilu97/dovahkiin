
import random

from containers.distinct import DistinctContainer

class Environment:

	def __init__(self) -> None:
		self.colliders = DistinctContainer()
		self.objs = DistinctContainer()

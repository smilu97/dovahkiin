
import random
from .btree import BPlusTree as BTree

class DistinctContainer:

	__slots__ = ['cont']

	def __init__(self) -> None:
		self.cont = BTree(3)

	def add(self, obj) -> None:
		key = self.get_new_key()
		self.cont.insert(key, obj)
		obj._dc_key = key

	def remove(self, obj) -> None:
		self.cont.remove(obj._dc_key)

	def get_new_key(self) -> int: 
		key = random.randint(0, 0x7FFFFFFF)
		while self.cont.get(key) is None:
			key = random.randint(0, 0x7FFFFFFF)
		return key

	def __iter__(self):
		return self.cont.__iter__()

	def __next__(self):
		return self.cont.__next__()

import random

from BTrees.IOBTree import IOBTree

class DistinctContainer:

	__slots__ = ['cont']

	def __init__(self) -> None:
		self.cont = IOBTree()

	def add(self, obj) -> None:
		key = self.get_new_key()
		self.cont[key] = obj
		obj._dc_key = key

	def remove(self, obj) -> None:
		if self.cont.get(obj._dc_key) is not None:
			self.cont.pop(obj._dc_key)
	
	def get(self, key) -> object:
		return self.cont.get(key)

	def get_new_key(self) -> int: 
		key = random.randint(0, 0x7FFFFFFF)
		while self.cont.get(key) is not None:
			key = random.randint(0, 0x7FFFFFFF)
		return key
	
	def iteritems(self):
		return self.cont.iteritems()

	def __iter__(self):
		return self.cont.__iter__()

	def __next__(self):
		return self.cont.__next__()
	
	def __getitem__(self, key):
		return self.get(key)
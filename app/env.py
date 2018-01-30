
import random

from containers.distinct import DistinctContainer

from typing import List

class Environment:

	def __init__(self, tag_list=[]) -> None:
		self.colliders = DistinctContainer()
		self.objs = DistinctContainer()
		self.tag_cont = self._create_tag_cont(tag_list)
	
	@staticmethod
	def _create_tag_cont(tag_list) -> dict:
		result = {}
		for tag in tag_list:
			result[tag] = DistinctContainer()
		return result

    def find_objects_by_tag(tag: str) -> List[GameObject]:
        cont = self.tag_cont.get(tag)
		if cont is None:
			return []
		return list(cont)
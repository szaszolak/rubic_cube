from Path import Path

# simple wrapper class which holds paths in ordered list for easier access
class Frontier(object):
	def __init__(self):
		self.paths = []

	def append(self, path):
		if not self.paths: # frontier is empty do not care about sorting
			self.paths.append(path)
		else:
			self._insert_with_order(path)

	def _insert_with_order(self, new_path):
		for index, path in enumerate(self.paths):
				if new_path.exploration_cost() < path.exploration_cost():
					self.paths.insert(index, new_path)
					return

	def pop(self):
		return self.paths.pop(0)
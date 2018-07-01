from Path import Path

# simple wrapper class which holds paths in ordered list for easier access
class Frontier(object):
	def __init__(self):
		self.paths = []

	def append(self, path):
		self._insert_with_order(path)

	def _insert_with_order(self, new_path):
		for index, path in enumerate(self.paths):
				if new_path.exploration_cost() < path.exploration_cost():
					self.paths.insert(index, new_path)
					return
		self.paths.append(new_path)

	def pop(self):
		return self.paths.pop(0)

	def print_out(self):
		path = self.paths[0]
		print "Path first: exploration cost: {0} missing blocks: {1} missing walls: {2}".format(path.exploration_cost(), path.cube.get_missing_blocks(), path.cube.get_missing_walls())
		path = self.paths[-1]
		print "Path last: exploration cost: {0} missing blocks: {1} missing walls: {2}".format(path.exploration_cost(), path.cube.get_missing_blocks(), path.cube.get_missing_walls())
			# print path.cube.print_out()

	def state_log(self):
		return { 'first_path': self._path_state_log(self.paths[0]), 'last_path': self._path_state_log(self.paths[-1]) }

	def _path_state_log(self, path):
		return { 'exploration_cost': path.exploration_cost(), 'missing_blocks': path.cube.get_missing_blocks(), 'missing_walls': path.cube.get_missing_walls() }

# from Action import Action
from Cube import Cube
from Path import Path
import pdb
# import copy

# TODO: created method search method with usage of _explore.
class SearchAgent(object):
  def __init__(self):
    self.initial_cube = Cube()
    # this probably should be a tree structure but lest start simple for now.
    self.frontier = [Path(self.initial_cube)]
    self.explored = {}

  # def start_searching(self):
  #   print 'starting search'
  def _explore(self):
    path = self._path_to_explore()
    if self.explored[path.explodation_candidate.cube]:
      path.explore()
    else:
      self.frontier.append(path.explore())
      self.explored[path.explodation_candidate.cube] = True
    if path.should_be_dropped():
      self.frontier.remove(path)

  def _path_to_explore(self):
    return sorted(self.frontier, cmp=self._compare_paths)[0]

  def _compare_paths(self, path1, path2):
    if path1.exploration_cost() == path2.exploration_cost():
      return 0
    return (1 if path1.exploration_cost() > path2.exploration_cost() else -1)

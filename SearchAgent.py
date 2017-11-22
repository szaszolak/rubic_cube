# from Action import Action
from Cube import Cube
from Path import Path
# import copy
# # this class responsibility was sucked up by Path, it should chage to work over Path instances, to be done some day
class SearchAgent(object):
  def __init__(self):
    self.initial_cube = Cube()
    self.frontier = [Path(self.initial_cube)]
    self.explored = []

  def start_searching(self):
    print 'starting search'
    cheapest = self.frontier[0]
    for path in self.frontier:
      if cheapest.find_exploration_candidate

from SearchAgent import SearchAgent
from Cube import Cube
from Wall import Wall
from Path import Path
import unittest
import copy
import numpy as np


class TestSearchAgent(unittest.TestCase):

  def setUp(self):
    self.search_agent = SearchAgent()
    self.cube = Cube()
    self.cube.walls[0] = Wall(np.zeros([3, 3], int))
    self.cube.walls[1] = Wall(np.ones([3, 3], int))
    self.cube.walls[2] = Wall(np.ones([3, 3], int) * 2)
    self.cube.walls[3] = Wall(np.ones([3, 3], int) * 3)
    self.cube.walls[4] = Wall(np.ones([3, 3], int) * 4)
    self.cube.walls[5] = Wall(np.ones([3, 3], int) * 5)
    self.cube.build_adjacency_dictionary()
    self.cube.move_upper_rows_right(self.cube.walls[0])
    duplicated_cube = copy.deepcopy(self.cube)
    duplicated_cube.move_right_column_up(duplicated_cube.walls[0])
    self.search_agent.frontier = [Path(self.cube), Path(duplicated_cube)]

  def test_path_to_explore(self):
    self.assertEqual(self.search_agent._path_to_explore().exploration_candidate.get_description(), 'on 0 wall, perform move_upper_rows_left')

# pass
#     self.cube = Cube()
#     self.cube.walls[0] = Wall(np.zeros([3, 3], int))
#     self.cube.walls[1] = Wall(np.ones([3, 3], int))
#     self.cube.walls[2] = Wall(np.ones([3, 3], int) * 2)
#     self.cube.walls[3] = Wall(np.ones([3, 3], int) * 3)
#     self.cube.walls[4] = Wall(np.ones([3, 3], int) * 4)
#     self.cube.walls[5] = Wall(np.ones([3, 3], int) * 5)
#     self.cube.build_adjacency_dictionary()
#     self.agent = SearchAgent(self.cube)

#   def test_discover_new_actions(self):
#     self.assertEqual(48, len(self.agent.frontier))

#   def test_find_cheapest_action(self):
#     self.cube.move_upper_rows_right(self.cube.walls[0])
#     self.agent.discover_new_actions()
#     action = self.agent.find_cheapest_action()
#     self.assertEqual(action.get_description(), 'on 0 wall, perform move_upper_rows_left')

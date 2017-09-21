from Path import Path
from Cube import Cube
from Wall import Wall
import unittest
import copy
import numpy as np


class TestPath(unittest.TestCase):

  def setUp(self):
    self.cube = Cube()
    self.cube.walls[0] = Wall(np.zeros([3, 3], int))
    self.cube.walls[1] = Wall(np.ones([3, 3], int))
    self.cube.walls[2] = Wall(np.ones([3, 3], int) * 2)
    self.cube.walls[3] = Wall(np.ones([3, 3], int) * 3)
    self.cube.walls[4] = Wall(np.ones([3, 3], int) * 4)
    self.cube.walls[5] = Wall(np.ones([3, 3], int) * 5)
    self.cube.build_adjacency_dictionary()
    self.path = Path(self.cube)

  def test_discover_new_actions(self):
    self.assertEqual(48, len(self.path.frontier))

  def test_find_cheapest_action(self):
    self.cube.move_upper_rows_right(self.cube.walls[0])
    self.path.discover_new_actions()
    action = self.path.find_cheapest_action()
    self.assertEqual(action.get_description(), 'on 0 wall, perform move_upper_rows_left')


from Path import Path
from Cube import Cube
from Wall import Wall
from Action import Action
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
    # self.action = Action(self.cube, 0, self.cube.move_upper_rows_right)
    self.cube.move_upper_rows_right(self.cube.walls[0])
    self.path = Path(self.cube, [])

  def test_discover_new_actions(self):
    self.assertEqual(47, len(self.path.frontier))

  def test_exploration_candidate(self):
    self.assertEqual(self.path.exploration_candidate.get_description(), 'on 0 wall, perform move_upper_rows_left')

  def test_explore_returns_new_path(self):
    self.assertIsInstance(self.path.explore(), Path)

  def test_explore_adds_ation_to_new_paths_explored_list(self):
    explored_list = [self.path.exploration_candidate]
    explored_path = self.path.explore()
    self.assertEqual(explored_path.explored, explored_list)

  # those test has to be tweaked due to exploration candidate change
  # def test_find_cheapest_action(self):
  #   action = self.path.find_cheapest_action()
  #   self.assertEqual(action.get_description(), 'on 0 wall, perform move_upper_rows_left')

  # def test_find_exploration_candidate(self):
  #   self.cube.move_upper_rows_right(self.cube.walls[0])
  #   self.path.frontier = []
  #   self.path.discover_new_actions()
  #   action = self.path.find_exploration_candidate()
  #   self.assertEqual(action.get_description(), 'on 0 wall, perform move_upper_rows_left')

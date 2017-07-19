from Action import Action
from Cube import Cube
import unittest
import copy
import numpy as np


class TestAction(unittest.TestCase):

    def setUp(self):
        self.cube = Cube()
        self.wall = self.cube.walls[0]
        cube_dup = copy.deepcopy(self.cube)
        self.action = Action(cube_dup, 0, cube_dup.move_upper_rows_right)

    def test_get_total_cost(self):
        self.cube.move_upper_rows_right(self.cube.walls[0])
        total_cost = self.cube.get_missing_walls() + self.cube.get_missing_blocks()
        self.assertEqual(total_cost, self.action.total_cost())

    def test_get_description(self):
        description = "on 0 wall, perform move_upper_rows_right"
        self.assertEqual(description, self.action.get_description())

if __name__ == '__main__':
    unittest.main()

from Action import Action
from Cube import Cube
import unittest
import copy
import numpy as np


class ActionTest(unittest.TestCase):

    def setUp(self):
        self.cube = Cube()
        self.wall = self.cube.walls[0]
        cube_dup = copy.deepcopy(self.cube)
        missing_blocks = cube_dup.get_missing_blocks()
        missing_walls = cube_dup.get_missing_walls()
        self.action = Action(cube_dup, 0, cube_dup.move_upper_rows_right, missing_blocks, missing_walls)

    def test_get_total_cost(self):
        total_cost = self.cube.get_missing_walls() + self.cube.get_missing_blocks()
        self.assertEqual(total_cost, self.action.total_cost())

    def test_get_description(self):
        description = "on 0 wall, perform move_upper_rows_right"
        self.assertEqual(description, self.action.get_description())

    def test_perform(self):
        self.cube.move_upper_rows_right(self.cube.walls[0])
        returned_cube = self.action.perform()
        for i in range(6):
            expected_wall = self.cube.walls[i].state
            returned_wall = returned_cube.walls[i].state
            self.assertTrue(np.array_equal(expected_wall, returned_wall))

if __name__ == '__main__':
    unittest.main()

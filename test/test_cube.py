from Cube import Cube
from Wall import Wall
import numpy as np
import unittest


class TestCube(unittest.TestCase):

    def setUp(self):
        self.cube = Cube()
        self.cube.walls[0] = Wall(np.ones([3, 3], int))
        self.cube.walls[1] = Wall(np.ones([3, 3], int) * 2)
        self.cube.walls[2] = Wall(np.ones([3, 3], int) * 3)
        self.cube.walls[3] = Wall(np.ones([3, 3], int) * 4)
        self.cube.walls[4] = Wall(np.ones([3, 3], int) * 5)
        self.cube.walls[5] = Wall(np.ones([3, 3], int) * 6)
        self.cube.build_adjacency_dictionary()

    def test_move_right_column_up(self):
        expected_wall1 = np.matrix('1,1,3;1,1,3;1,1,3')
        expected_wall3 = np.matrix('3,3,6;3,3,6;3,3,6')
        expected_wall4 = np.matrix('4,4,1;4,4,1;4,4,1')
        expected_wall6 = np.matrix('6,6,4;6,6,4;6,6,4')
        self.cube.move_right_column_up(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall3 = self.cube.walls[2].state
        wall4 = self.cube.walls[3].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall3, wall3))
        self.assertTrue(np.array_equal(expected_wall4, wall4))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_right_column_down(self):
        expected_wall1 = np.matrix('1,1,4;1,1,4;1,1,4')
        expected_wall3 = np.matrix('3,3,1;3,3,1;3,3,1')
        expected_wall4 = np.matrix('4,4,6;4,4,6;4,4,6')
        expected_wall6 = np.matrix('6,6,3;6,6,3;6,6,3')
        self.cube.move_right_column_down(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall3 = self.cube.walls[2].state
        wall4 = self.cube.walls[3].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall3, wall3))
        self.assertTrue(np.array_equal(expected_wall4, wall4))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_left_column_up(self):
        expected_wall1 = np.matrix('3,1,1;3,1,1;3,1,1')
        expected_wall3 = np.matrix('6,3,3;6,3,3;6,3,3')
        expected_wall4 = np.matrix('1,4,4;1,4,4;1,4,4')
        expected_wall6 = np.matrix('4,6,6;4,6,6;4,6,6')
        self.cube.move_left_column_up(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall3 = self.cube.walls[2].state
        wall4 = self.cube.walls[3].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall3, wall3))
        self.assertTrue(np.array_equal(expected_wall4, wall4))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_left_column_down(self):
        expected_wall1 = np.matrix('4,1,1;4,1,1;4,1,1')
        expected_wall3 = np.matrix('1,3,3;1,3,3;1,3,3')
        expected_wall4 = np.matrix('6,4,4;6,4,4;6,4,4')
        expected_wall6 = np.matrix('3,6,6;3,6,6;3,6,6')
        self.cube.move_left_column_down(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall3 = self.cube.walls[2].state
        wall4 = self.cube.walls[3].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall3, wall3))
        self.assertTrue(np.array_equal(expected_wall4, wall4))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_upper_rows_right(self):
        expected_wall1 = np.matrix('2,2,2;1,1,1;1,1,1')
        expected_wall2 = np.matrix('6,6,6;2,2,2;2,2,2')
        expected_wall5 = np.matrix('1,1,1;5,5,5;5,5,5')
        expected_wall6 = np.matrix('5,5,5;6,6,6;6,6,6')
        self.cube.move_upper_rows_right(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall2 = self.cube.walls[1].state
        wall5 = self.cube.walls[4].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall2, wall2))
        self.assertTrue(np.array_equal(expected_wall5, wall5))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_upper_rows_left(self):
        expected_wall1 = np.matrix('5,5,5;1,1,1;1,1,1')
        expected_wall2 = np.matrix('1,1,1;2,2,2;2,2,2')
        expected_wall5 = np.matrix('6,6,6;5,5,5;5,5,5')
        expected_wall6 = np.matrix('2,2,2;6,6,6;6,6,6')
        self.cube.move_upper_rows_left(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall2 = self.cube.walls[1].state
        wall5 = self.cube.walls[4].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall2, wall2))
        self.assertTrue(np.array_equal(expected_wall5, wall5))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_lower_rows_right(self):
        expected_wall1 = np.matrix('1,1,1;1,1,1;2,2,2')
        expected_wall2 = np.matrix('2,2,2;2,2,2;6,6,6')
        expected_wall5 = np.matrix('5,5,5;5,5,5;1,1,1')
        expected_wall6 = np.matrix('6,6,6;6,6,6;5,5,5')
        self.cube.move_lower_rows_right(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall2 = self.cube.walls[1].state
        wall5 = self.cube.walls[4].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall2, wall2))
        self.assertTrue(np.array_equal(expected_wall5, wall5))
        self.assertTrue(np.array_equal(expected_wall6, wall6))

    def test_move_lower_rows_left(self):
        expected_wall1 = np.matrix('1,1,1;1,1,1;5,5,5')
        expected_wall2 = np.matrix('2,2,2;2,2,2;1,1,1')
        expected_wall5 = np.matrix('5,5,5;5,5,5;6,6,6')
        expected_wall6 = np.matrix('6,6,6;6,6,6;2,2,2')
        self.cube.move_lower_rows_left(self.cube.walls[0])
        wall1 = self.cube.walls[0].state
        wall2 = self.cube.walls[1].state
        wall5 = self.cube.walls[4].state
        wall6 = self.cube.walls[5].state
        self.assertTrue(np.array_equal(expected_wall1, wall1))
        self.assertTrue(np.array_equal(expected_wall2, wall2))
        self.assertTrue(np.array_equal(expected_wall5, wall5))
        self.assertTrue(np.array_equal(expected_wall6, wall6))


if __name__ == '__main__':
    unittest.main()

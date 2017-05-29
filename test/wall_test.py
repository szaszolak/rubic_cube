from Wall import Wall
import numpy as np
import unittest


class WallTest(unittest.TestCase):

    def setUp(self):
        self.initial_state = np.matrix('1, 1, 1; 2, 2, 2; 3, 3, 3')
        self.wall = Wall(self.initial_state)
        self.wall_transponed = Wall(self.initial_state.transpose())

    def test_missing_bloks(self):
        self.assertEqual(6, self.wall.missing_blocks())

    def test_peek_upper_row(self):
        self.assertEqual(3, self.wall.peek_upper_row(np.matrix('2,2,2')))

    def test_peek_lower_row(self):
        self.assertEqual(3, self.wall.peek_upper_row(np.matrix('2,2,2')))

    def test_peek_left_col(self):
        self.assertEqual(4, self.wall.peek_left_col(np.matrix('2;2;2')))

    def test_peek_right_col(self):
        self.assertEqual(4, self.wall.peek_right_col(np.matrix('2;2;2')))

    def test_get_upper_row(self):
        row = np.matrix('1,1,1')
        self.assertTrue(np.array_equal(row, self.wall.get_upper_row()))

    def test_lower_upper_row(self):
        row = np.matrix('3,3,3')
        self.assertTrue(np.array_equal(row, self.wall.get_lower_row()))

    def test_get_left_column(self):
        col = np.matrix('1;1;1')
        self.assertTrue(np.array_equal(col, self.wall_transponed.get_left_column()))

    def test_get_right_column(self):
        col = np.matrix('3;3;3')
        self.assertTrue(np.array_equal(col, self.wall_transponed.get_right_column()))

    def test_swap_upper_row(self):
        inserted_row = np.matrix('2,2,2')
        returned_row = self.wall.swap_upper_row(inserted_row)
        self.assertTrue(np.array_equal(self.wall.get_upper_row(), inserted_row))
        self.assertTrue(np.array_equal(returned_row, np.matrix('1,1,1')))

    def test_swap_lower_row(self):
        inserted_row = np.matrix('2,2,2')
        returned_row = self.wall.swap_lower_row(inserted_row)
        self.assertTrue(np.array_equal(self.wall.get_lower_row(), inserted_row))
        self.assertTrue(np.array_equal(returned_row, np.matrix('3,3,3')))

    def test_swap_left_column(self):
        inserted_col = np.matrix('2;2;2')
        returned_col = self.wall_transponed.swap_left_column(inserted_col)
        self.assertTrue(np.array_equal(self.wall_transponed.get_left_column(), inserted_col))
        self.assertTrue(np.array_equal(returned_col, np.matrix('1;1;1')))

    def test_swap_right(self):
        inserted_col = np.matrix('2;2;2')
        returned_col = self.wall_transponed.swap_right_column(inserted_col)
        self.assertTrue(np.array_equal(self.wall_transponed.get_right_column(), inserted_col))
        self.assertTrue(np.array_equal(returned_col, np.matrix('3;3;3')))

if __name__ == '__main__':
    unittest.main()

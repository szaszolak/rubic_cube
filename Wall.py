import numpy as np

class Wall:

    def __init__(self, initial_state):
        self.state = initial_state
        self.goal = initial_state[1, 1]

    def peek_left_col(self, col):
        return 9 - (np.count_nonzero(self.state[:, 1] == self.goal) \
               + np.count_nonzero(self.state[:, 2] == self.goal) \
               + np.count_nonzero(col == self.goal))

    def peek_right_col(self, col):
        return 9 - (np.count_nonzero(self.state[:, 0] == self.goal) \
               + np.count_nonzero(self.state[:, 1] == self.goal) \
               + np.count_nonzero(col == self.goal))

    def peek_upper_row(self, row):
        return 9 - (np.count_nonzero(self.state[1, :] == self.goal) \
               + np.count_nonzero(self.state[2, :] == self.goal) \
               + np.count_nonzero(row == self.goal))

    def peek_lower_row(self, row):
        return 9 - (np.count_nonzero(self.state[0, :] == self.goal) \
               + np.count_nonzero(self.state[1, :] == self.goal) \
               + np.count_nonzero(row == self.goal))

    def peek_left_col(self, col):
        return 9 - (np.count_nonzero(self.state[:, 1] == self.goal) \
               + np.count_nonzero(self.state[:, 2] == self.goal) \
               + np.count_nonzero(col == self.goal))

    def peek_right_col(self, col):
        return 9 - (np.count_nonzero(self.state[:, 0] == self.goal) \
               + np.count_nonzero(self.state[:, 1] == self.goal) \
               + np.count_nonzero(col == self.goal))

    def peek_upper_row(self, row):
        return 9 - (np.count_nonzero(self.state[1, :] == self.goal) \
               + np.count_nonzero(self.state[2, :] == self.goal) \
               + np.count_nonzero(row == self.goal))

    def peek_lower_row(self, row):
        return 9 - (np.count_nonzero(self.state[0, :] == self.goal) \
               + np.count_nonzero(self.state[1, :] == self.goal) \
               + np.count_nonzero(row == self.goal))

    def swap_upper_row(self, row):
        previous = self.state[0, :]
        self.state[0, :] = row
        return previous

    def swap_lower_row(self, row):
        previous = self.state[2, :]
        self.state[2, :] = row
        return previous

    def swap_left_column(self, column):
        previous = self.state[:, 0]
        self.state[:, 0] = np.transpose(column)
        return previous

    def swap_right_column(self, column):
        previous = self.state[:, 2]
        self.state[:, 2] = np.transpose(column)
        return previous

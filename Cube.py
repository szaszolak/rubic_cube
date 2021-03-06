import random
import numpy as np
from Wall import Wall


class Cube:
    def __init__(self):
        self.colors = []
        self.conts_cols = [0, 1, 2, 3, 4, 5]
        self.adjacency_dictionary = {}

        for color_index in range(6):
            for wall in range(8):
                self.colors.append(color_index)
        random.shuffle(self.colors)
        self.generate()
        self.build_adjacency_dictionary()

    def generate(self):
        self.walls = []
        for wall in range(6):
            row1 = [self.colors.pop(0) for col in range(3)]
            row2 = [self.colors.pop(0), self.conts_cols.pop(0), self.colors.pop(0)]
            row3 = [self.colors.pop(0) for col in range(3)]
            wall_mx = np.asmatrix([row1, row2, row3])
            self.walls.append(Wall(wall_mx))

    def get_color(self, id):
        if id == 0:
            color = 'red'
        elif id == 1:
            color = 'blue'
        elif id == 2:
            color = 'green'
        elif id == 3:
            color = 'white'
        elif id == 4:
            color = 'purple'
        else:
            color = 'yellow'
        return color

    def build_adjacency_dictionary(self):
        # wall 1
        self.adjacency_dictionary[self.walls[0]] = \
            {
                'h': [self.walls[4], self.walls[5], self.walls[1]],
                'v': [self.walls[2], self.walls[5], self.walls[3]]
            }

        # wall 2
        self.adjacency_dictionary[self.walls[1]] = \
            {
                'h': [self.walls[0], self.walls[4], self.walls[5]],
                'v': [self.walls[2], self.walls[4], self.walls[3]]
            }

        # wall 3
        self.adjacency_dictionary[self.walls[2]] = \
            {
                'h': [self.walls[0], self.walls[3], self.walls[5]],
                'v': [self.walls[4], self.walls[3], self.walls[1]]
            }

        # wall 4
        self.adjacency_dictionary[self.walls[3]] = \
            {
                'h': [self.walls[5], self.walls[2], self.walls[0]],
                'v': [self.walls[4], self.walls[2], self.walls[1]]
            }

        # wall 5
        self.adjacency_dictionary[self.walls[4]] = \
            {
                'h': [self.walls[5], self.walls[1], self.walls[0]],
                'v': [self.walls[2], self.walls[1], self.walls[3]]
            }

        # wall 6
        self.adjacency_dictionary[self.walls[5]] = \
            {
                'h': [self.walls[1], self.walls[0], self.walls[4]],
                'v': [self.walls[2], self.walls[0], self.walls[3]]
            }

    def move_upper_rows_right(self, origin):
        neighbors = self.adjacency_dictionary[origin]['h']
        row_to_move = origin.get_upper_row()

        for neighbor in neighbors:
            row_to_move = neighbor.swap_upper_row(row_to_move)

        origin.swap_upper_row(row_to_move)

    def move_upper_rows_left(self, origin):
        neighbors = self.adjacency_dictionary[origin]['h'][::-1]
        row_to_move = origin.get_upper_row()

        for neighbor in neighbors:
            row_to_move = neighbor.swap_upper_row(row_to_move)

        origin.swap_upper_row(row_to_move)

    def move_lower_rows_right(self, origin):
        neighbors = self.adjacency_dictionary[origin]['h']
        row_to_move = origin.get_lower_row()

        for neighbor in neighbors:
            row_to_move = neighbor.swap_lower_row(row_to_move)

        origin.swap_lower_row(row_to_move)

    def move_lower_rows_left(self, origin):
        neighbors = self.adjacency_dictionary[origin]['h'][::-1]
        row_to_move = origin.get_lower_row()

        for neighbor in neighbors:
            row_to_move = neighbor.swap_lower_row(row_to_move)

        origin.swap_lower_row(row_to_move)

    def move_left_column_down(self, origin):
        neighbors = self.adjacency_dictionary[origin]['v']
        column_to_move = origin.get_left_column()

        for neighbor in neighbors:
            column_to_move = neighbor.swap_left_column(column_to_move)

        origin.swap_left_column(column_to_move)

    def move_left_column_up(self, origin):
        neighbors = self.adjacency_dictionary[origin]['v'][::-1]
        column_to_move = origin.get_left_column()

        for neighbor in neighbors:
            column_to_move = neighbor.swap_left_column(column_to_move)

        origin.swap_left_column(column_to_move)

    def move_right_column_down(self, origin):
        neighbors = self.adjacency_dictionary[origin]['v']
        column_to_move = origin.get_right_column()

        for neighbor in neighbors:
            column_to_move = neighbor.swap_right_column(column_to_move)

        origin.swap_right_column(column_to_move)

    def move_right_column_up(self, origin):
        neighbors = self.adjacency_dictionary[origin]['v'][::-1]
        column_to_move = origin.get_right_column()

        for neighbor in neighbors:
            column_to_move = neighbor.swap_right_column(column_to_move)

        origin.swap_right_column(column_to_move)

    def get_missing_walls(self):
        missing = 0
        for wall in self.walls:
            if wall.missing_blocks() != 0:
                missing += 1

        return missing

    def get_missing_blocks(self):
        missing = 0
        for wall in self.walls:
            missing += wall.missing_blocks()

        return missing

    def match(self, other_cube):
        for i in range(6):
            if not np.array_equal(self.walls[i].state, other_cube.walls[i].state):
                return False
        return True

    def print_out(self):
        for wall in self.walls:
            print wall.state

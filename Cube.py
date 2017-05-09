import random
import numpy as np
from Wall import Wall

# horizontal neighbors are ordered from left to right
# vertical neighbors are ordered from left to right
class Cube:
    def __init__(self):
        self.colors = []
        self.conts_cols = [0, 1, 2, 3, 4, 5]
        for color_index in range(6):
            for wall in range(8):
                self.colors.append(color_index)
        random.shuffle(self.colors)

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
        self.adjacency_dictionary = {}
        # wall 1
        self.adjacency_dictionary[self.walls[0]] = \
        {
          'h': [self.walls[4], self.walls[5], self.walls[1]],
          'v': [self.walls[2], self.walls[5], self.walls[3]]
        }
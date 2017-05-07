import random
import numpy as np

class Cube:
    def __init__(self):
        self.colors = []
        for color_index in range(6):
            for wall in range(9):
                self.colors.append(color_index)
        random.shuffle(self.colors)

    def generate(self):
        self.walls = []
        for wall in range(6):
            row1 = [self.colors.pop(0) for col in range(3)]
            row2 = [self.colors.pop(0) for col in range(3)]
            row3 = [self.colors.pop(0) for col in range(3)]
            wall = np.asmatrix([row1, row2, row3])
            self.walls.append(wall)

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
        



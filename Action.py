

class Action:
    def __init__(self, cube, wall, move_method, missing_blocks, missing_walls):
        self.cube = cube
        self.wall = wall
        self.move_method = move_method
        self.missing_blocks = missing_blocks
        self.missing_walls = missing_walls

    def perform(self):
        self.move_method(self.cube.walls[self.wall])
        return self.cube

    def get_description(self):
        return "on {0} wall, perform {1}".format(self.wall, self.move_method.__name__)

    def total_cost(self):
        return self.missing_blocks + self.missing_walls

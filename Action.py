class Action:
    def __init__(self, cube, wall, move_method):
        self.cube = cube
        self.wall = wall
        self.move_method = move_method
        self.move_method(self.cube.walls[self.wall])

    def get_description(self):
        return "on {0} wall, perform {1}".format(self.wall, self.move_method.__name__)

    def total_cost(self):
        return self.cube.get_missing_walls() + self.cube.get_missing_blocks()

class Action:
    def __init__(self, cube, wall_index, move_method):
        self.cube = cube
        self.wall_index = wall_index
        self.move_method = move_method
        self.move_method(self.cube.walls[self.wall_index])

    def get_description(self):
        return "on {0} wall, perform {1}".format(self.wall_index, self.move_method.__name__)

    def total_cost(self):
        neighbors = self.cube.adjacency_dictionary[self.cube.walls[5]]
        missing = 0
        for wi in range(6):
            wall = self.cube.walls[wi]
            if wi == 5:
                missing += wall.missing_blocks() * 100000 * ((ri + 1)  * (ri + 1))
            else:
                for ri in range(3):
                    missing += wall.missing_block_in_row(ri) * ((ri + 1)  * (ri + 1))
        return missing

    def match(self, other_action):
      self.cube.match(other_action.cube)

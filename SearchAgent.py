# from Action import Action
# from Cube   import Cube
# import copy
# # this class responsibility was sucked up by Path, it should chage to work over Path instances, to be done some day
class SearchAgent(object):
  def __init__(self, cube):
      pass
#     self.cube = cube
#     self.frontier = []
#     self.explored = []
#     self.discover_new_actions()

#   def discover_new_actions(self):
#     for wall_index in range(6):
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_upper_rows_right))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_upper_rows_left))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_lower_rows_right))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_lower_rows_left))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_left_column_up))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_left_column_down))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_right_column_up))
#       duplicated_cube = copy.deepcopy(self.cube)
#       self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_right_column_down))

#   def find_cheapest_action(self):
#     cheapest = self.frontier[0]
#     for action in self.frontier:
#       if cheapest.total_cost() > action.total_cost():
#         cheapest = action
#     return cheapest

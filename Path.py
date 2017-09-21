from Action import Action
from Cube   import Cube
import copy

class Path(object):
  def __init__(self, cube):
    self.cube = cube
    self.frontier = []
    self.explored = []
    self.discover_new_actions()
    self.exploration_candidate = None

  def discover_new_actions(self):
    for wall_index in range(6):
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_upper_rows_right))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_upper_rows_left))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_lower_rows_right))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_lower_rows_left))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_left_column_up))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_left_column_down))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_right_column_up))
      duplicated_cube = copy.deepcopy(self.cube)
      self.frontier.append(Action(duplicated_cube, wall_index, duplicated_cube.move_right_column_down))

  def find_cheapest_action(self):
    cheapest = self.frontier[0]
    for action in self.frontier:
      if cheapest.total_cost() > action.total_cost():
        cheapest = action
    return cheapest

  # potential endless loop add escape condition
  def find_exploration_candidate(self):
    if not self.frontier:
      return None

    cheapest_action = self.find_cheapest_action()
    print cheapest_action.get_description()
    candidate = self.frontier.pop(cheapest_action)
    if not self.cube.match(candidate.cube):
      return candidate
    else:
      return explore()

  def should_be_dropped(self):
    return not self.frontier

  def total_cost(self):
    cost = 0
    for action in self.explored:
      cost += action.total_cost()
    return cost

  def exploration_cost(self):
    return total_cost() + self.exploration_candidate.total_cost()

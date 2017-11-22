from Action import Action
import copy

class Path(object):
  def __init__(self, cube, explored = []):
    self.cube = cube
    self.frontier = []
    self.explored = explored
    self.discover_new_actions()
    self.exploration_candidate = self.find_exploration_candidate()

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

  def find_exploration_candidate(self):
    while self.frontier:
      candidate = self.find_cheapest_action()
      # we remove candidate from frontie bceause it either will be explored or dropped as leading to already explored state
      self.frontier.remove(candidate)
      if not self.cube.match(candidate.cube):
        return candidate
    return None

  def should_be_dropped(self):
    return not self.frontier

  def total_cost(self):
    cost = 0
    for action in self.explored:
      cost += action.total_cost()
    return cost

  def exploration_cost(self):
    return total_cost() + self.exploration_candidate.total_cost()

  def explore(self):
    copied_explored = copy.deepcopy(self.explored)
    copied_explored.append(self.exploration_candidate)
    new_path = Path(self.exploration_candidate.cube, copied_explored)
    self.exploration_candidate = self.find_exploration_candidate()
    return new_path


from Action import Action
import copy

class Path(object):
  def __init__(self, cube, explored = []):
    self.cube = cube
    self.frontier = []
    self.explored = explored # so we know how we achieve this finall cube
    self._discover_new_actions()
    self.exploration_candidate = self._find_exploration_candidate()

  def should_be_dropped(self):
    return not self.frontier

  def exploration_cost(self):
    return self._total_cost() + self.exploration_candidate.total_cost()

  def explore(self):
    copied_explored = copy.deepcopy(self.explored)
    copied_candidate = copy.deepcopy(self.exploration_candidate)
    copied_explored.append(copied_candidate)
    new_path = Path(copied_candidate.cube, copied_explored)
    self.exploration_candidate = self._find_exploration_candidate()
    return new_path

  def _discover_new_actions(self):
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

  def _find_cheapest_action(self):
    cheapest = self.frontier[0]
    for action in self.frontier:
      if cheapest.total_cost() > action.total_cost():
        cheapest = action
    return cheapest

  def _find_exploration_candidate(self):
    while self.frontier:
      candidate = self._find_cheapest_action()
      # we remove candidate from frontie bceause it either will be explored or dropped as leading to already explored state
      self.frontier.remove(candidate)
      if not self.cube.match(candidate.cube):
        return candidate
    return None

  def _total_cost(self):
    return len(self.explored)

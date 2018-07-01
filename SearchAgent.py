# from Action import Action
from Cube     import Cube
from Path     import Path
from Frontier import Frontier
import pdb
from pymongo  import MongoClient
# import copy

# TODO: created method search method with usage of _explore.
class SearchAgent(object):
    def __init__(self):
        self.initial_cube = Cube()
        self.frontier = Frontier()
        self.frontier.append(Path(self.initial_cube))  
        self.explored = {}
        self.db = MongoClient()['rubic_cube']

    def explore(self):
        added = 0
        iteration = 0
        ignored = 0
        while True:
            path = self._path_to_explore()
            stringified_path_cube = self._squash_cube_to_string_sequence(path.exploration_candidate.cube)
                #if path leads to already explored space do not add it to frontier
            if stringified_path_cube in self.explored:
                ignored += 1
                path.explore() 
            else:
                new_path = path.explore()
                if new_path.cube.get_missing_blocks() == 0:
                    return new_path
                else:
                    added += 1
                    self.frontier.append(new_path)
                    self.explored[stringified_path_cube] = True # in fact we are only interested in existance of give key
            
            if not path.should_be_dropped():
                self.frontier.append(path)
            
            if iteration % 1000 == 0:
                self._log_state(iteration, added, ignored)
                # print 'Iteration no: {0} frontier size: {1} explored states: {2}'.format(iteration, len(self.frontier.paths), len(self.explored))
                # print 'Already added: {0}, ignored {1}'.format(added, ignored)
                # self.frontier.print_out()
                # print '*******************************'

            iteration += 1

    def _path_to_explore(self):
        return self.frontier.pop()

    def _squash_cube_to_string_sequence(self, cube):
        return'-'.join(str(wall.state) for wall in cube.walls)

    def _log_state(self, iteration, added, ignored):
        log = { 
            'iteration': iteration, 
            'frontier_size': len(self.frontier.paths), 
            'explored_states': len(self.explored), 
            'added': added, 
            'ignored': ignored, 
            'frontier': self.frontier.state_log() 
        }
        print 'inserting {0}'.format(log)
        self.db.logs.insert_one(log)
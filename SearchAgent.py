# from Action import Action
from Cube               import Cube
from Path               import Path
from Frontier           import Frontier
from ThreadedArcBuilder import ThreadedArcBuilder
import pdb
# import copy

# TODO: created method search method with usage of _explore.
class SearchAgent(object):
    def __init__(self):
        self.arc_lenght = 3
        self.initial_cube = Cube()
        self.frontier = Frontier()
        self.frontier.append(Path(self.initial_cube))
        self.explored = {}

    def explore(self):
        added = 0
        iteration = 0
        ignored = 0
        while True:
            #path = self._path_to_explore()
            for path in self._arcs():
                stringified_path_cube = self._squash_cube_to_string_sequence(path.cube)
                    #if path leads to already explored space do not add it to frontier
                if stringified_path_cube in self.explored:
                    ignored += 1
                else:
                    if path.cube.get_missing_blocks() == 0:
                        return path
                    else:
                        added += 1
                        self.frontier.append(path)
                        self.explored[stringified_path_cube] = True # in fact we are only interested in existance of give key

            if iteration % 1 == 0:
                print 'Iteration no: {0} frontier size: {1} explored states: {2}'.format(iteration, len(self.frontier.paths), len(self.explored))
                print 'Already added: {0}, ignored {1}'.format(added, ignored)
                self.frontier.print_out()
                print '*******************************'

            iteration += 1

    def _path_to_explore(self):
        return self.frontier.pop()

    def _squash_cube_to_string_sequence(self, cube):
        return'-'.join(str(wall.state) for wall in cube.walls)

    def _arcs(self):
        accumulator = [self._path_to_explore()]
        result = []
        for i in range(self.arc_lenght):
            print 'starting step: {0}'.format(i)
            result = []
            builder_threads = []
            index = 0
            kill_flag = False
            for i in xrange(0, len(accumulator), 4):
                tBuilder = ThreadedArcBuilder(i, accumulator[i:i + 4], result, kill_flag)
                builder_threads.append(tBuilder)
                tBuilder.start()

            for tBuilder in builder_threads:
                tBuilder.join()
            accumulator = result
            print 'current results size: {0}'.format(len(result))
        return result

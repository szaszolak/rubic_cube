import threading
import time

class ThreadedArcBuilder (threading.Thread):
    def __init__(self, threadID, paths, accumulator, kill_flag):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.paths = paths
        self.accumulator = accumulator
        self.kill_flag = kill_flag

    def run(self):
        for path in self.paths:
            while not path.should_be_dropped():
                intermidiate_step = path.explore()
                if intermidiate_step.cube.get_missing_blocks() == 0:
                    self.accumulator = [intermidiate_step]
                    self.kill_flag = True

                if self.kill_flag:
                    return
                self.accumulator.append(intermidiate_step)

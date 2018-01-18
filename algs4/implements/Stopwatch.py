import time

class Stopwatch(object):
    def __init__(self):
        self.start = time.time()

    def elapsedTime(self):
        now = time.time()
        return now - self.start
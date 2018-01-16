class Counter(object):
    def __init__(self, name):
        self.name = name
        self.value = 0

    def increment(self):
        self.value += 1

    def tally(self):
        return self.value

    def __str__(self):
        return '%s %s' % (self.value, self.name)

class FixedCapacityStackOfStrings(object):
    def __init__(self, cap):
        self.a = [None] * cap
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def isFull(self):
        return self.N >= len(self.a)

    def size(self):
        return self.N

    def push(self, ele):
        self.N += 1
        self.a[self.N] = ele
    
    def pop(self):
        self.N -= 1
        return self.a[self.N]
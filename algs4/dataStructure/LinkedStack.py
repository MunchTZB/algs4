class Node(object):
    def __init__(self):
        self.item = None
        self.next = None

class Stack(object):
    '''
    这是Stack的链表实现
    '''

    def __init__(self):
        self.N = 0
        self.first = Node()
        self.compass = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.compass == None:
            self.compass = self.first
        else:
            self.compass = self.compass.next

        if self.compass.next == None:
            raise StopIteration()

        return self.compass

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def push(self, ele):
        oldfirst = self.first
        self.first = Node()
        self.first.item = ele
        self.first.next = oldfirst
        self.N += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        return item
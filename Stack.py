from .Bag import Bag

class Stack(Bag):
    def __init__(self):
        super().__init__()

    def push(self, ele):
        self.add(ele)

    def pop(self):
        return self.content.pop()
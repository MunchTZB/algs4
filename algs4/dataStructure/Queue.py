from .Bag import Bag

class Queue(Bag):
    def __init__(self):
        super().__init__()

    def enqueue(self, ele):
        self.add(ele)
    
    def dequeue(self):
        return self.content.pop(0)
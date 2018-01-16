class Bag(object):
    def __init__(self):
        self.content = []
        self.compass = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.compass += 1
        
        if self.compass + 1 > len(self.content):
            self.compass = -1
            raise StopIteration()

        return self.content[self.compass]

    def __str__(self):
        str = ''
        for i in self:
            str + i
        return str

    def add(self, ele):
        self.content.append(ele)

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return len(self.content)

    def main():
        print(Bag)

if __name__ == '__main__':
    Bag.main()
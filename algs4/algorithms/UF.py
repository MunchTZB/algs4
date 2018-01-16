import sys
import os

class QuickFindUF(object):
    def __init__(self, N):
        # 分量id 以触点作为索引
        self.id = [i for i in range(0, N)]
        
        # 分量数量 初始化的时候每个触点都构成一个只含有自己的分量
        self.cnt = N
    
    def count(self):
        return self.cnt

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return
        
        for i, v in enumerate(self.id):
            if v == pID:
                self.id[i] = qID

        self.cnt -= 1

class QuickUnionUF(object):
    def __init__(self, N):
        self.id = [i for i in range(0, N)]
        self.cnt = N
    
    def count(self):
        return self.cnt

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            pass
        else:
            self.id[pRoot] = qRoot
            self.cnt -= 1

class WeightedQuickUnionUf(object):
    def __init__(self, N):
        self.id = [i for i in range(0, N)]
        self.sz = [1 for i in range(0, N)]
        self.cnt = N
        
    def count(self):
        return self.cnt

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        pSize = self.sz[pRoot]
        qSize = self.sz[qRoot]

        if pRoot == qRoot:
            pass
        else:
            if pSize < qSize:
                self.id[pRoot] = qRoot
                self.sz[pRoot] += qSize
            else:
                self.id[qRoot] = pRoot
                self.sz[qRoot] += pSize
            
            self.cnt -= 1

    

def test():
    filePath = os.path.abspath(sys.argv[1])
    file = open(filePath).read()
    Data = file.split('\n')
    Data.pop()
    N = int(Data.pop(0))
    Data = [(int(i.split(' ')[0]), int(i.split(' ')[1])) for i in Data]
    uf = QuickFindUF(N)
    for (p, q) in Data:
        if uf.connected(p, q):
            pass
        else:
            uf.union(p, q)
            print(p, q)
            
    print(uf.count())

if __name__ == '__main__':
    test()
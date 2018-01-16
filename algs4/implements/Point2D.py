import math
import functools
from matplotlib import pyplot

class Point2D(object):
    '''
    # 这是
    # Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
    # Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
    # http://algs4.cs.princeton.edu
    # 书中的辅助代码包algs4.jar中Point2D的python实现，
    # 以方便python爱好者的算法与数据结构的学习。
    # 用法与jar包中的用法基本相同。
    # 
    # 17.10.11 by Munch_TZB
    '''

    def __init__(self, x, y):
        if not isinstance(x, float) or not isinstance(y, float):
            raise Exception('参数必须为浮点数!')

        self.x = x
        self.y = y

    def x(self):
        return self.x
    
    def y(self):
        return self.y

    def r(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def theta(self):
        return math.atan2(self.y, self.x)

    def angleTo(self, that):
        dx = that.x - self.x
        dy = that.y - self.y
        return math.atan2(dy, dx)

    @staticmethod
    def ccw(a, b, c):
        area2 = (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
        if area2 < 0:
            return -1
        elif area2 > 0:
            return 1
        else:
            return 0

    @staticmethod
    def area2(a, b, c):
        return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)

    def distanceTo(self, that):
        dx = self.x - that.x;
        dy = self.y - that.y;
        return math.sqrt(dx*dx + dy*dy);

    def distanceSquaredTo(self, that):
        dx = self.x - that.x;
        dy = self.y - that.y;
        return dx*dx + dy*dy

    @staticmethod
    @functools.cmp_to_key
    def XOrder(p, q):
        if p.x < q.x:
            return -1
        if p.x > q.x:
            return 1
        return 0

    @staticmethod
    @functools.cmp_to_key
    def YOrder(p, q):
        if p.y < q.y:
            return -1
        if p.y > q.y:
            return 1
        return 0

    @staticmethod
    @functools.cmp_to_key
    def ROrder(p, q):
        delta = (p.x*p.x + p.y*p.y) - (q.x*q.x + q.y*q.y)
        if delta < 0:
            return -1
        if delta > 0:
            return 1
        return 0

    # def Atan2Order(self, q1, q2):
    #     angle1 = self.angleTo(q1)
    #     angle2 = self.angleTo(q2)
    #     if angle1 < angle2:
    #         return -1
    #     elif angle1 > angle2:
    #         return 1
    #     else:
    #         return 0

    #
    # Atan2Order
    # PolarOrder
    # DistanceToOrder
    # 这几个比较函数暂不实现

    def equals(self, other):
        if other == self:
            return True

        if type(self) != type(other) :
            return False

        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '( %s, %s )' % (self.x, self.y)

    def hashCode(self):
        hash1 = id(self.x)
        hash2 = id(self.y)
        return 31 * hash1 + hash2

    def draw(self):
        pyplot.plot(self.x, self.y, marker='.')

    def drawTo(self, that):
        pyplot.plot([self.x, that.x], [self.y, that.y])

    def test():
        a = Point2D(1.0, 2.0)
        b = Point2D(2.0, 2.0)
        c = Point2D(3.0, 3.0)
        a.draw()
        a.drawTo(b)
        b.drawTo(c)
        pyplot.show()

if __name__ == '__main__':
    Point2D.test()
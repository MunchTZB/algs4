import math

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
        if not isinstance(min, float) or not isinstance(max, float):
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


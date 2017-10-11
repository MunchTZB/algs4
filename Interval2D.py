from Interval1D import Interval1D
from Point2D import Point2D
from Counter import Counter
from matplotlib import patches
from matplotlib import pyplot

import sys
import random

class Interval2D(object):
    def __init__(self, x, y):
        if not isinstance(x, Interval1D) or not isinstance(y, Interval1D):
            raise Exception('Interval2D的构造参数必须为Interval1D')

        self.x = x
        self.y = y

    def intersects(self, that):
        if not isinstance(that, Interval2D):
            raise Exception('wrong intersects arg')
        
        if not self.x.intersects(that.x):
            return False

        if not self.y.intersects(that.y):
            return False

        return True

    def contains(self, p):
        if not isinstance(p, Point2D):
            raise Exception('wrong contains arg')
        return self.x.contains(p.x) and self.y.contains(p.y)
    
    def area(self):
        return self.x.length() * self.y.length()

    def __str__(self):
        return str(self.x) + " x " + str(self.y)

    def equals(self, other):
        if other == self:
            return True

        if type(other) != type(self) :
            return False

        return self.x.equals(other.x) and self.y.equals(other.y)

    def hashCode(self):
        hash1 = self.x.hashCode()
        hash2 = self.y.hashCode()
        return 31 * hash1 + hash2

    def draw(self):
        xc = (self.x.left() + self.x.right()) / 2.0
        yc = (self.y.left() + self.y.right()) / 2.0
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        pyplot.gca().add_patch(pyplot.Rectangle((xc, yc), self.x.length() / 2.0, self.y.length() / 2.0))

    def test():
        xmin = float(sys.argv[1])
        xmax = float(sys.argv[2])
        ymin = float(sys.argv[3])
        ymax = float(sys.argv[4])
        trials = int(sys.argv[5])

        xInterval = Interval1D(xmin, xmax)
        yInterval = Interval1D(ymin, ymax)
        box = Interval2D(xInterval, yInterval)

        box.draw()
        
        counter = Counter('hits');
        
        for i in range(trials):
            x = random.random()
            y = random.random()
            point = Point2D(x, y)

            if box.contains(point):
                counter.increment()
            else:
                point.draw()

        pyplot.show()

        print(counter)
        print('box area = %s' % box.area())



if __name__ == '__main__':
    Interval2D.test()
import functools

class Interval1D(object):
    '''
    # 这是
    # Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
    # Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
    # http://algs4.cs.princeton.edu
    # 书中的辅助代码包algs4.jar中Interval1D的python实现，
    # 以方便python爱好者的算法与数据结构的学习。
    # 用法与jar包中的用法基本相同。
    # 
    # 17.10.11 by Munch_TZB
    '''
    
    def __init__(self, min, max):
        if not isinstance(min, float) or not isinstance(max, float):
            raise Exception('参数必须为浮点数!')
        
        if min <= max:
            self.min = min;
            self.max = max;
        else:
            raise Exception('Illegal interval')

    def left(self, parameter_list):
        return self.min

    def right(self, parameter_list):
        return self.max

    def intersects(self, anotherI1D):
        if self.max < anotherI1D.min:
            return False

        if anotherI1D.max < self.min:
            return False

        return True
    
    def contains(self, x):
        return (self.min <= x) and (x <= self.max)

    def length(self):
        return self.max - self.min

    def __str__(self):
        return '[ %s, %s ]' % (self.min, self.max)

    def equals(self, other):
        if other == self:
            return True

        if type(self) != type(other) :
            return False

        return self.min == other.min and self.max == other.max
    
    def hashCode(self):
        hash1 = id(self.min)
        hash2 = id(self.max)
        return 31 * hash1 + hash2
    
    @staticmethod
    @functools.cmp_to_key
    def MinEndpointComparator(a, b):
        if not isinstance(a, Interval1D) or not isinstance(b, Interval1D) :
            raise Exception("illegal compare")
        
        if a.min < b.min:
            return -1
        elif a.min > b.min:
            return 1
        elif a.max < b.max:
            return -1
        elif a.max > b.max:
            return 1
        else:
            return 0;

    @staticmethod
    @functools.cmp_to_key    
    def MaxEndpointComparator(a, b):
        if not isinstance(a, Interval1D) or not isinstance(b, Interval1D) :
            raise Exception("illegal compare")
        
        if a.max < b.max:
            return -1
        elif a.max > b.max:
            return 1
        elif a.min < b.min:
            return -1
        elif a.min > b.min:
            return 1
        else:
            return 0;

    @staticmethod
    @functools.cmp_to_key    
    def LengthComparator(a, b):
        if not isinstance(a, Interval1D) or not isinstance(b, Interval1D) :
            raise Exception("illegal compare")

        alen = a.length()
        blen = b.length()

        if alen < blen:
            return -1
        elif alen > blen:
            return 1
        return 0

    def test():
        intervals = [
            Interval1D(15.0, 33.0),
            Interval1D(45.0, 60.0),
            Interval1D(20.0, 70.0),
            Interval1D(46.0, 55.0)
        ]

        print('Unsorted')
        for i in intervals:
            print(i)
        print('')

        print('Sort by min endpoint')
        intervals.sort(key=Interval1D.MinEndpointComparator)
        for i in intervals:
            print(i)
        print('')

        print('Sort by max endpoint')
        intervals.sort(key=Interval1D.MaxEndpointComparator)
        for i in intervals:
            print(i)
        print('')

        print('Sort by length')
        intervals.sort(key=Interval1D.LengthComparator)
        for i in intervals:
            print(i)
        print('')

if __name__ == '__main__':
    Interval1D.test() 
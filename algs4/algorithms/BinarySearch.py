import sys
import os
from ..implements import implements

class BinarySearch(object):
    @staticmethod
    def rank(key, array):
        lo = 0
        hi = len(array) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < array[mid]:
                hi = mid - 1
            elif key > array[mid]:
                lo = mid + 1
            else:
                return mid

        return -1

    def main():
        count = implements.Counter('BSCount')

        whiteListPath = os.path.abspath(sys.argv[1])
        targetListPath = os.path.abspath(sys.argv[2])

        whiteList = [int(i) for i in open(whiteListPath).read().splitlines()]
        whiteList.sort()
        targetList = [int(i) for i in open(targetListPath).read().splitlines()]

        for i in targetList:
            if BinarySearch.rank(i, whiteList) < 0:
                count.increment()
        
        print(count)
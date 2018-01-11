import sys
import os
from SortBase import SortBase

def InsertionSort(arr):
    N = len(arr)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if SortBase.less(arr[j], arr[j - 1]):
                SortBase.exch(arr, j, j - 1)
            else:
                break

def splitString():
    userArg = sys.argv[1]
    filePath = os.path.abspath(userArg)
    file = open(filePath).read()
    rawData = file.split('\n')[0].split(' ')
    return rawData

if __name__ == '__main__':
    Data = splitString()
    InsertionSort(Data)
    assert SortBase.isSorted(Data)
    SortBase.show(Data)
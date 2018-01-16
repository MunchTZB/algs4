import sys
import os
from ..common import SortBase

def SelectionSort(arr):
    N = len(arr)
    for i in range(0, N):
        min = i
        for j in range(i + 1, N):
            if SortBase.less(arr[j], arr[min]):
                min = j
        SortBase.exch(arr, i, min)

def splitString():
    userArg = sys.argv[1]
    filePath = os.path.abspath(userArg)
    file = open(filePath).read()
    rawData = file.split('\n')[0].split(' ')
    return rawData

if __name__ == '__main__':
    Data = splitString()
    SelectionSort(Data)
    assert SortBase.isSorted(Data)
    SortBase.show(Data)
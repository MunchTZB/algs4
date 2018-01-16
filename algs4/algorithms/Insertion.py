import sys
import os
from ..implements.SortBase import SortBase

def InsertionSort(arr):
    N = len(arr)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if SortBase.less(arr[j], arr[j - 1]):
                SortBase.exch(arr, j, j - 1)
            else:
                break
            
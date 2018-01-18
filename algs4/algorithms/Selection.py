import sys
import os
from ..implements.SortBase import SortBase

def SelectionSort(arr):
    N = len(arr)
    for i in range(0, N):
        min = i
        for j in range(i + 1, N):
            if SortBase.less(arr[j], arr[min]):
                min = j
        SortBase.exch(arr, i, min)
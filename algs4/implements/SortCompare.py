from random import random
from .Stopwatch import Stopwatch
from ..algorithms.Insertion import InsertionSort
from ..algorithms.Selection import SelectionSort

def time(alg, testArr):
    timer = Stopwatch()
    if alg == 'Insertion':
        InsertionSort(testArr)
    elif alg == 'Selection':
        SelectionSort(testArr)

    return timer.elapsedTime()

def timeRandomInput(alg, N, T):
    # 使用算法alg将T个长度为N的数组排序
    total = 0
    for i in range(0, T):
        testArr = [random() for i in range(0, N)]
        total = total + time(alg, testArr)
    return total

def SortCompare(args):
    alg1 = args[1]
    alg2 = args[2]
    N = int(args[3])
    T = int(args[4])
    # 算法1的总时间
    t1 = timeRandomInput(alg1, N, T)
    # 算法2的总时间
    t2 = timeRandomInput(alg2, N, T)
    print(t1)
    print(t2)
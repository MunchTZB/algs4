class SortBase(object):
    @staticmethod
    def less(v, w):
        return v < w

    @staticmethod
    def exch(arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

    @staticmethod
    def show(arr):
        str = ''
        for i in arr:
            str = str + i + ' '
        print(str)

    @staticmethod
    def isSorted(arr):
        for i in range(1, len(arr)):
            if SortBase.less(arr[i], arr[i - 1]):
                return False
        return True

import numpy as np


def Counting_Sort(alist, k):
    # 只能对整数进行排序
    # 需要提前知道待排序数组中元素的范围
    length = len(alist)
    blist = np.zeros(length, dtype=int)
    clist = np.zeros(k, dtype=int)

    for i in range(length):
        clist[alist[i]] = clist[alist[i]] + 1
    clist = np.cumsum(clist)

    for j in range(length-1, -1, -1):
        # 需注意blist 里面需减1
        blist[clist[alist[j]] - 1] = alist[j]
        clist[alist[j]] -= 1

    return blist


def Counting_Sort_improve(alist):
        # 只能对整数进行排序
        # 需要提前知道待排序数组中元素的范围
        k = max(alist)
        left = min(alist)
        length_internal = k - left + 1
        print(length_internal)

        length = len(alist)
        blist = np.zeros(length, dtype=int)
        clist = np.zeros(length_internal, dtype=int)

        for i in range(length):
            clist[alist[i]-left] = clist[alist[i]-left] + 1
        clist = np.cumsum(clist)

        for j in range(length - 1, -1, -1):
            # 需注意blist 里面需减1
            blist[clist[alist[j]-left] - 1] = alist[j]
            clist[alist[j]-left] -= 1

        return blist


A = np.random.randint(low=0, high=100, size=100)
print(Counting_Sort(A, 100))
# 改良版缩小了不必要的clist的空间
print(Counting_Sort_improve(A))





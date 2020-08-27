import numpy as np
import time


def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)


def Partition(A, p, r):
    x = A[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] < x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]
    return i + 1


# 思考题 7-1
def Hoare_Partition(A, p, r):
    x = A[p]
    i = p
    j = r - 1
    while i < j:
        while A[j] > x:
            j -= 1
        while A[i] < x:
            i += 1
        A[i], A[j] = A[j], A[i]
    return j


A = np.random.random(1000)
B = A.copy()
C = A.copy()
time_start = time.time()
QuickSort(A, 0, len(A))
time_end = time.time()
print('time cost', time_end - time_start, 's')



# 7.4-5
def QuickSort_and_Insertion(A, p, r):
    if p < r:
        if p > r - 5:
            pass
        else:
            q = Partition(A, p, r)
            QuickSort(A, p, q - 1)
            QuickSort(A, q + 1, r)
            # 插入排序
            for j in range(p + 1, r):
                key = A[j]
                i = j - 1
                while i > 0 and A[i] > key:
                    A[i + 1] = A[i]
                    i -= 1
                A[i + 1] = key


time_start = time.time()
QuickSort(B, 0, len(A))
time_end = time.time()
print('time cost', time_end - time_start, 's')


# 思考题 7-4
def Tail_Recursive_QuickSort(A, p, r):
    while p < r:
        q = Partition(A, p, r)
        Tail_Recursive_QuickSort(A, p, q-1)
        p = q+1


time_start = time.time()
QuickSort(C, 0, len(A))
time_end = time.time()
print('time cost', time_end - time_start, 's')

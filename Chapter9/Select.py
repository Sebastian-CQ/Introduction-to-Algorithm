import numpy as np


# 9.2
def Randomized_Select(A, p, r, i):
    # 从A中找到第i小的元素
    if p == r:
        return ValueError('空数列')
    if p == r + 1:
        return A[p]
    q = Randomized_Partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return Randomized_Select(A, p, q, i)
    else:
        return Randomized_Select(A, q, r, i-k)


def Randomized_Partition(A, p, r):
    # 按从小到大排序
    # 返回最后一个数在A中的位数
    x = A[r-1]
    i = p-1
    for j in range(p, r-1):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r-1], A[i+1] = A[i+1], A[r-1]
    return i+1


# A = [10, 9, 1, 3, 7, 25, 13, 4]
# print(Randomized_Select(A, 0, len(A), 3))


# 9.3
def Select(A, p, r, i):
    if i > r:
        return ValueError('输入错误')
    if p == r:
        return ValueError('空字符')
    if p == r-1:
        return A[p]
    n = int(np.ceil((r-p) / 5))
    media = []
    for j in range(n):
        # print(j)
        if p+5*j+5 < r:
            alist = Bubble_sort(A[p+5*j: p+5*j+5])
        else:
            alist = Bubble_sort(A[p+5*j:r])
        # print(alist)
        media.append(alist[int((len(alist)-1)/2)])
    # print('media:', media)

    media_num = Select(media, 0, len(media), int(len(media)/2))

    q = Randomized_Partition_Select(A, p, r, media_num)
    # print('q:', q)
    # print('A:', A)
    k = q - p + 1
    if i == k:
        return media_num
    elif i < k:
        return Select(A, p, q, i)
    else:
        return Select(A, q+1, r, i-k)


def Randomized_Partition_Select(A, p, r, media_num):
    i = p
    j = r - 1
    while i < j:
        while A[i] < media_num and i < j:
            i += 1
        while A[j] > media_num and i < j:
            j -= 1
        A[i], A[j] = A[j], A[i]
    return i


def Bubble_sort(target):
    alist = target.copy()
    n = len(alist)
    for i in range(n - 1):
        # 冒泡排序n-1次
        exchange = False
        for j in range(n - i - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        if not exchange:
            break
    return alist


A = [10, 9, 1, 3, 7, 25, 13, 4, 5]
# 1 3 4 5 7 9 10 13 25
print(Select(A, 0, len(A), 9))
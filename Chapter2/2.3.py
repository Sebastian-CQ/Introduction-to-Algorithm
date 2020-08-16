import math
# 以下两个算法均未使用哨兵
def Merge_Sort(alist, p, q):
    # alist为数组， pq为坐标
    if p == q - 1:
        return [alist[p]]
    Llist = Merge_Sort(alist, p, round((p + q) / 2))
    Rlist = Merge_Sort(alist, round((p + q) / 2), q)
    for i in range(p, q, 1):
        if len(Llist) == 0 and len(Rlist) != 0:
            alist[i] = Rlist.pop(0)
        if len(Rlist) == 0 and len(Llist) != 0:
            alist[i] = Llist.pop(0)
        if len(Rlist) != 0 and len(Llist) != 0:
            if Llist[0] > Rlist[0]:
                alist[i] = Rlist.pop(0)
            else:
                alist[i] = Llist.pop(0)

    return alist[p: q]


# Python 特色
def Merge_Sort2(alist, p, q):
    # alist为数组， pq为坐标
    if p == q - 1:
        return [alist[p]]
    Llist = Merge_Sort(alist, p, round((p + q) / 2))
    Rlist = Merge_Sort(alist, round((p + q) / 2), q)
    i = p
    while Llist and Rlist:
        alist[i] = Llist.pop(0) if Llist[0] < Rlist[0] else Rlist.pop(0)
        i += 1
    alist[i: q] = Llist if Llist else Rlist

    return alist[p: q]


print(Merge_Sort([1, 7, 8, 19, 2, 1, 8, 9, 3], 0, 9))
print(Merge_Sort2([1, 7, 8, 19, 2, 1, 8, 9, 3], 0, 9))
# 归并排序的算法复杂度为O（nlogn）【logn为以2为底对数——由于二分原因】
# 速度比线性快，但占用栈内存多


# 2.3-4
def Insertion_Merge_Sort(alist):
    blist = alist.copy()
    if len(blist) == 1:
        return blist

    element = blist.pop()
    clist = Insertion_Merge_Sort(blist)
    Insertion = False
    i = 0
    while not Insertion and i < len(clist):
        if clist[i] > element:
            clist.insert(i, element)
            Insertion = True
        i += 1
    if not Insertion:
        clist.append(element)

    return clist


def Insertion_Merge_Sort_improve(alist, n):
    # 节省内存空间
    # n 为len(alist)-1
    blist = alist.copy()
    if n == 0:
        return alist
    per_element = alist[n]
    blist = Insertion_Merge_Sort_improve(alist, n-1)
    i = n-1
    while i >= 0 and blist[i] > per_element:
        blist[i+1] = blist[i]
        i -= 1
    blist[i+1] = per_element
    return blist


print('2.3-4', Insertion_Merge_Sort([5, 1, 3, 10, 9, 7]))
print('2.3-4', Insertion_Merge_Sort_improve([5, 1, 3, 10, 9, 7], 5))


# 2.3-5
# 对已排好顺序的序列A，做二分查找
def Binary_Search(A, b):
    result = None
    left = 0
    right = len(A)
    while result is None and left < right:
        mid = int((left + right) / 2)
        if A[mid] > b:
            right = mid
        elif A[mid] == b:
            result = mid
        else:
            left = mid+1
    return result


print('2.3-5', Binary_Search([1, 2, 3, 4, 5, 7, 8], 4))


# 2.3-6
def Insertion_BinarySearch_Sort(alist):
    # 非降序
    blist = alist.copy()
    for i in range(1, len(blist)):
        key = blist.pop(i)
        j = i
        left = 0
        right = j
        while left < right:
            mid = int((left + right) / 2)
            if blist[mid] > key:
                right = mid
            else:
                left = mid + 1
        blist.insert(left, key)
        # while j >= 0 and blist[j] > key:
        #     blist[j + 1] = blist[j]
        #     j -= 1
        # blist[j + 1] = key
    return blist


print('2.3-6', Insertion_BinarySearch_Sort([5, 7, 1, 9, 2, 10]))




def Insertion_Sort1(alist):
    # 非降序
    blist = alist.copy()
    for i in range(1, len(blist)):
        key = blist[i]
        j = i - 1
        while j >= 0 and blist[j] > key:
            blist[j + 1] = blist[j]
            j -= 1
        blist[j + 1] = key
    return blist


def Insertion_Sort2(alist):
    # 非升序
    blist = alist.copy()
    for i in range(1, len(blist)):
        key = blist[i]
        j = i - 1
        while j >= 0 and blist[j] < key:
            blist[j + 1] = blist[j]
            j -= 1
        blist[j + 1] = key
    return blist


print(Insertion_Sort1([5, 7, 1, 9, 2, 10]))
print(Insertion_Sort2([5, 7, 1, 9, 2, 10]))


# 作业
# 2.1-3
def search(A, b):
    find = None
    for i, a in enumerate(A):
        if a == b:
            find = i
    return find
# print(search([1,2,3,4,5,6,10], 6))


# 2.1-4
def sum_binaryNum(A, B):
    if len(A) != len(B):
        return ValueError
    C = []
    c = 0   # 进位
    for i in range(len(A)):
        C.append((A[i]+B[i]+c) % 2)
        c = (A[i]+B[i]+c) // 2
    C.append(c)
    return C


print(sum_binaryNum([1, 1, 1, 1], [0, 1, 0, 1]))


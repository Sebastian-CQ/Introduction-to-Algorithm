def BubbleSort(target):
    alist = target.copy()
    n = len(alist)
    # num = 0
    for i in range(n - 1):
        # 冒泡排序n-1次
        exchange = False
        for j in range(n - i - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        if not exchange:
            break
        # num += 1
        # print(alist)
    return alist


def SelectionSort(target):
    alist = target.copy()
    n = len(alist)
    for i in range(n-1, 1, -1):
        max_index = 0
        for j in range(1, i+1):
            if alist[max_index] < alist[j]:
                max_index = j
        alist[max_index], alist[i] = alist[i], alist[max_index]
    return alist


def InsertionSort_newList(target):
    alist = target.copy()
    n = len(alist)
    blist = [alist.pop()]
    for i in range(1, n):
        insert_obj = alist.pop()
        insert_pos = 0
        while insert_pos < i and blist[insert_pos] < insert_obj:
            insert_pos += 1
        blist.insert(insert_pos, insert_obj)
    return blist


def InsertionSort(target):
    alist = target.copy()
    n = len(alist)
    for index in range(1, n):
        insert_pos = index - 1
        insert_obj = alist[index]
        while insert_pos >= 0 and alist[insert_pos] > insert_obj:
            alist[insert_pos + 1] = alist[insert_pos]
            insert_pos -= 1
        if insert_pos >= 0:
            alist[insert_pos] = insert_obj
        else:
            alist[0] = insert_obj
    return alist


def ShellSort(target):
    # 复杂度介于O(n2)与O(n)
    alist = target.copy()
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for start_pos in range(sublistcount):
            gapInsertSort(alist, start_pos, sublistcount)
        # print('After increments of size', sublistcount, 'The list is :', alist)

        sublistcount = sublistcount // 2
    return alist


def gapInsertSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current = alist[i]
        pos = i

        while pos >= gap and alist[pos-gap] > current:
            alist[pos] = alist[pos-gap]
            pos = pos - gap
        alist[pos] = current


def mergeSort(target):
    # 复杂度 O（nlogn）
    if len(target) == 1:
        return target
    mid_index = len(target) // 2
    left_part = mergeSort(target[:mid_index])
    right_part = mergeSort(target[mid_index:])

    merge_list = []
    while left_part and right_part:
        if left_part[0] > right_part[0]:
            merge_list.append(right_part.pop(0))
        else:
            merge_list.append(left_part.pop(0))
    merge_list.extend(right_part if right_part else left_part)
    return merge_list


def quickSort(target):
    # 递归算法
    if len(target) <= 1:
        return target
    # 取第一个数为中值
    mid_value = target[0]
    left_mark = 1
    right_mark = len(target) - 1

    # 分裂
    done = False
    while not done:
        while left_mark <= right_mark and target[left_mark] <= mid_value:
            left_mark += 1
        while right_mark >= left_mark and target[right_mark] >= mid_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            target[left_mark], target[right_mark] = target[right_mark], target[left_mark]
    target[0], target[right_mark] = target[right_mark], target[0]

    # print('right_pos: ', right_mark)
    # print('lef_pos:', left_mark)
    # print('left part:', target[:left_mark])
    # print('right part', target[left_mark:])

    left_part = quickSort(target[:left_mark])
    right_part = quickSort(target[left_mark:])

    return left_part + right_part


def QuickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    mid_value = alist[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= mid_value:
            left_mark += 1
        while right_mark >= left_mark and alist[right_mark] >= mid_value:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark


L = [1, 10, 7, 3, 19, 25, 3, 15]
# print(BubbleSort(L))
# print(SelectionSort(L))
# print(InsertionSort(L))
# print(ShellSort(L))
# print(mergeSort(L))
# print(quickSort(L))
# QuickSort(L)
# print(L)




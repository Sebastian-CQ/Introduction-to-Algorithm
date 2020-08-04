import random
import time


def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] is item:
            found = True
        else:
            pos += 1
    if found:
        return pos
    else:
        return False


def orderedSequentialSearch(alist, item):
    # 递增顺序表
    pos = 0
    found = False
    while pos < len(alist) and item >= alist[pos] and not found:
        if item == alist[pos]:
            found = True
        else:
            pos += 1

    return found


def binarySearch(alist, item):
    left_index = 0
    right_index = len(alist) - 1
    found = False
    while left_index <= right_index and not found:
        mid_index = (right_index + left_index) // 2
        if alist[mid_index] == item:
            found = True
        else:
            if alist[mid_index] > item:
                right_index = mid_index
            else:
                left_index = mid_index + 1
    return found


def binarySearch_recursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid_index = len(alist) // 2
        if alist[mid_index] == item:
            return True
        else:
            if item < alist[mid_index]:
                return binarySearch_recursion(alist[:mid_index], item)
            else:
                return binarySearch_recursion(alist[mid_index + 1:], item)




import numpy as np


# 最大子数组问题
def max_subarray(alist, left, right):
    if len(alist) == 0:
        return ValueError('空数列')
    # 最原始left=0， right=len(alist)
    if left == right - 1:
        return alist[left]

    mid = int((left + right) / 2)  # 向下取整得到mid
    max_left = max_subarray(alist, left, mid)
    max_right = max_subarray(alist, mid, right)

    # 下述为求最大的跨中间节点的最大子序列
    left_sum = -np.inf
    sum = 0
    i = mid - 1
    while i >= left:
        sum += alist[i]
        if sum > left_sum:
            left_sum = sum
        i -= 1

    right_sum = -np.inf
    sum = 0
    j = mid
    while j < right:
        sum += alist[j]
        if sum > right_sum:
            right_sum = sum
        j += 1
    # print(max_left, max_right, right_sum , left_sum)
    return max(max_left, max_right, right_sum + left_sum)


# print(max_subarray([1, 2, 3, -1, 2], 0, 5))
# print(max_subarray([-1, -2, -2, -5, -7], 0, 5))


# 最大子数组暴力解法
def max_subarray_V(alist):
    if len(alist) == 0:
        return ValueError('空数列')
    max_sub = -np.inf
    length = len(alist)
    for i in range(length):
        # 每个子数组所含个数
        for j in range(length - i):
            max_sum = sum(alist[j:j + i + 1])
            if max_sum > max_sub:
                max_sub = max_sum
    return max_sub


print(max_subarray_V([]))


# 4.1-5 问题
def explode(alist, i, j):
    # i j 为alist[:len(alist)-1]的最大子数列
    max_sum_pre = sum(alist[i, j])
    max_sum = max_sum_pre
    for i in range(len(alist), 0, -1):
        sum_now = sum(alist[i:])
        if sum_now > max_sum:
            max_sum = sum_now
    return max_sum

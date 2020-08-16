import numpy as np


def Square_matrix_multiply(aMatrix, bMatrix):
    row_a = len(aMatrix)  # 行
    columns_a = len(aMatrix[0])  # 列
    row_b = len(bMatrix)
    columns_b = len(bMatrix[0])
    if columns_a != row_b:
        return ValueError

    Matrix = np.zeros((row_a, columns_b))

    for i in range(row_a):
        for j in range(columns_b):
            for k in range(row_a):
                Matrix[i, j] += aMatrix[i, k] * bMatrix[k, j]

    return Matrix


def Square_matrix_multiply_recursive(aMatrix, bMatrix):
    # 只能计算 2^n 维数的矩阵
    # 简单讲a，b矩阵设为n，n
    row_a = len(aMatrix)  # 行
    columns_a = len(aMatrix[0])  # 列
    row_b = len(aMatrix)
    columns_b = len(aMatrix[0])
    if columns_a != row_b:
        return ValueError('矩阵维度出错')
    mid_a = int(row_a / 2)
    mid_b = int(columns_a / 2)

    Matrix = np.zeros((row_a, columns_b))

    if row_a == 1 and columns_b == 1:
        Matrix[0, 0] = aMatrix[0, 0] * bMatrix[0, 0]
        return Matrix

    else:
        Matrix[:mid_a, :mid_b] = Square_matrix_multiply_recursive(aMatrix[:mid_a, :mid_b], bMatrix[:mid_a, :mid_b]) + \
                                 Square_matrix_multiply_recursive(aMatrix[:mid_a, mid_b:], bMatrix[mid_a:, :mid_b])
        Matrix[:mid_a, mid_b:] = Square_matrix_multiply_recursive(aMatrix[:mid_a, :mid_b], bMatrix[:mid_a, mid_b:]) + \
                                 Square_matrix_multiply_recursive(aMatrix[:mid_a, mid_b:], bMatrix[mid_a:, mid_b:])
        Matrix[mid_a:, :mid_b] = Square_matrix_multiply_recursive(aMatrix[mid_a:, :mid_b], bMatrix[:mid_a, :mid_b]) + \
                                 Square_matrix_multiply_recursive(aMatrix[mid_a:, mid_b:], bMatrix[mid_a:, :mid_b])
        Matrix[mid_a:, mid_b:] = Square_matrix_multiply_recursive(aMatrix[mid_a:, :mid_b], bMatrix[:mid_a, mid_b:]) + \
                                 Square_matrix_multiply_recursive(aMatrix[mid_a:, mid_b:], bMatrix[mid_a:, mid_b:])
        return Matrix


# a = np.random.random((2, 2))
# b = np.random.random((2, 2))
# print('精确解', np.dot(a, b))
# print(Square_matrix_multiply(a, b))
# print(Square_matrix_multiply_recursive(a, b))


# 4.2-3
def Square_matrix_multiply_recursive_update(aMatrix, bMatrix):
    # 简单讲a，b矩阵设为n，n
    row_a = len(aMatrix)  # 行
    columns_a = len(aMatrix[0])  # 列
    row_b = len(aMatrix)
    columns_b = len(aMatrix[0])
    if columns_a != row_b:
        return ValueError('矩阵无法相乘')

    if row_a == 0 or row_b == 0:
        return ValueError('空矩阵')

    if row_a & row_a - 1 != 0 and row_a != 1:
        # 如果不为2的幂次 加全为零的行和列 加至2的幂次
        # print(False)
        k = 2
        if k < row_a or k < columns_b or k < columns_a:
            k = k*2
        # print(k)
        AMatrix = np.zeros((k, k))
        BMatrix = np.zeros((k, k))
        AMatrix[:row_a, :columns_a] = aMatrix
        BMatrix[:row_b, :columns_b] = bMatrix
        print(AMatrix, BMatrix)

        aMatrix = AMatrix
        bMatrix = BMatrix

    # 注意改进后应将 row and column 同时修正
    row_a = len(aMatrix)  # 行
    columns_a = len(aMatrix[0])  # 列
    row_b = len(aMatrix)
    columns_b = len(aMatrix[0])

    mid_a = int(row_a / 2)
    mid_b = int(columns_a / 2)

    Matrix = np.zeros((row_a, columns_b))

    if row_a == 1 and columns_b == 1:
        Matrix[0, 0] = aMatrix[0, 0] * bMatrix[0, 0]
        return Matrix

    else:
        Matrix[:mid_a, :mid_b] = Square_matrix_multiply_recursive(aMatrix[:mid_a, :mid_b], bMatrix[:mid_a, :mid_b]) + \
                                 Square_matrix_multiply_recursive(aMatrix[:mid_a, mid_b:], bMatrix[mid_a:, :mid_b])
        Matrix[:mid_a, mid_b:] = Square_matrix_multiply_recursive(aMatrix[:mid_a, :mid_b], bMatrix[:mid_a, mid_b:]) + \
                                 Square_matrix_multiply_recursive(aMatrix[:mid_a, mid_b:], bMatrix[mid_a:, mid_b:])
        Matrix[mid_a:, :mid_b] = Square_matrix_multiply_recursive(aMatrix[mid_a:, :mid_b], bMatrix[:mid_a, :mid_b]) + \
                                 Square_matrix_multiply_recursive(aMatrix[mid_a:, mid_b:], bMatrix[mid_a:, :mid_b])
        Matrix[mid_a:, mid_b:] = Square_matrix_multiply_recursive(aMatrix[mid_a:, :mid_b], bMatrix[:mid_a, mid_b:]) + \
                                 Square_matrix_multiply_recursive(aMatrix[mid_a:, mid_b:], bMatrix[mid_a:, mid_b:])
        return Matrix


a = np.random.random((4, 4))
b = np.random.random((4, 4))
print('精确解', np.dot(a, b))
print(Square_matrix_multiply_recursive_update(a, b))


# 4.2-7
def Plural_Multiply(a, b, c, d):
    # 用于解决 （a+bi）（c+di）
    # （a+bi）（c+di） = ac-bd + （ad + bc）i
    num1 = (a+b)*(c+d)
    num2 = (a-b)*(c-d)
    num3 = b * d

    print(num1, num2, num3)

    return complex((num1 + num2) / 2 - 2 * num3, (num1 - num2) / 2)


a = 5 + 6j
b = 3 - 4j
print(a * b)
print(Plural_Multiply(5, 6, 3, -4))

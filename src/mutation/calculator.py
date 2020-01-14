def mul(x, y):
    return x * y


def add(x, y):
    return x + y


def divide(x, y):
    return x / y


def difference(x, y):
    return x - y


def multiply_matrix_3x3(matrix1, matrix2):
    res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res

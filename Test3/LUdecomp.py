import numpy as np


def LUdecomp(A):
    """
    Takes in A matrix of size n x n and returns the LU decomposition of A as a tuple
    containing L and U
    :param A: The matrix being decomposed
    :return: (L, U) where L is the lower diagonal matrix and U is the upper diagonal matrix such that
    LU = A
    """
    length = len(A)

    # initialize L and U to zeros matrix
    L = np.zeros((length, length))
    U = np.zeros((length, length))

    # set all main diagonal values of L to 1
    for i in range(length):
        L[i][i] = 1.0

    for i in range(length):

        # change values in L
        for j in range(0, i):
            L[i][j] = A[i][j]
            for k in range(0, j):
                L[i][j] = L[i][j] - L[i][k] * U[k][j]
            L[i][j] = L[i][j] / U[j][j]

        # change values in U
        for j in range(i, length):
            U[i][j] = A[i][j]
            for k in range(0, i):
                U[i][j] = U[i][j] - L[i][k] * U[k][j]

    return L, U


def LyequalsB(L, b):
    """
    Solves the System Ly = b for Ax = b problem
    :param L: The Lower diagonal matrix of A in LU decomposition
    :param b: the b in Ax = b system of equations
    :return: y array in Ly = b
    """
    y = []
    for i in range(len(b)):
        y.append(b[i])
        for j in range(i):
            y[i] = y[i] - (L[i, j] * y[j])
        y[i] = y[i] / L[i, i]

    return y


def UxequalsY(U, y):
    """
    Solves the system Ux = y for Ax = b problem
    :param U: The Upper diagonal matrix of A in LU decomposition
    :param y: the y in Ux = y system of equations
    :return: x array in Ax = b
    """
    x = np.zeros_like(y)
    for i in range(len(x), 0, -1):
        x[i - 1] = (y[i - 1] - np.dot(U[i - 1, i:], x[i:])) / U[i - 1, i - 1]

    return x


def Axequalsb(A, b):
    L, U = LUdecomp(A)
    y = LyequalsB(L, b)
    x = UxequalsY(U, y)
    return x


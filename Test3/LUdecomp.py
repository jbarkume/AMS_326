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
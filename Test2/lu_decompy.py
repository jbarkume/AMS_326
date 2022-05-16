import time

import numpy as np

# Enter Arguments for A and b
# Make sure A and b all contain elements of the same type
# --------------------------------------------

A = np.array([[1.0, 2.0, 4.0, 7.0],
              [2.0, 13.0, 23.0, 38.0],
              [4.0, 23.0, 77.0, 122.0],
              [7.0, 38.0, 122.0, 294.0]])

b = np.array([45.0,
              249.0,
              769.0,
              1625.0])

# -------------------------------------------


# Returns tuple of matrices where first element is L and second element is U in "matrix = LU"
def lu_decomposition(A):

    # initialize L to be identity 3x3 matrix
    L = np.identity(4)

    # use multiplier to turn entry [2,1] to zero
    # to get multiplier, we use the formula that entry [2,1] = m * [1,1] + [2,1] = 0
    # rearranging we get that:
    multiplier = -(A[1][0] / A[0][0])
    U = np.array([A[0], A[1] + (A[0] * multiplier), A[2], A[3]])

    # update L to be negative of multiplier
    L[1][0] = -multiplier

    # use multiplier to turn entry [3,1] to zero
    multiplier = -(U[2][0] / U[0][0])
    U[2] += U[0] * multiplier
    L[2][0] = -multiplier

    # user multiplier to turn entry [3,2] to zero
    multiplier = -(U[2][1] / U[1][1])
    U[2] += U[1] * multiplier
    L[2][1] = -multiplier

    # use multiplier to turn entry [4,1] to zero, then [4,2], and [4,3]
    multiplier = -(U[3][0] / U[0][0])
    U[3] += U[0] * multiplier
    L[3][0] = -multiplier

    # [4,2]
    multiplier = -(U[3][1] / U[1][1])
    U[3] += U[1] * multiplier
    L[3][1] = -multiplier

    # [4,3]
    multiplier = -(U[3][2] / U[2][2])
    U[3] += U[2] * multiplier
    L[3][2] = -multiplier

    # return tuple with L as first element and U as second
    return L, U


# Takes in a 3x3 matrix A and a vector b where we want to solve Ax = b
def axequalsb(A, b):

    # Find LU decomposition of A so that Ax = b becomes LUx = b

    decomp = lu_decomposition(A)
    L = decomp[0]
    U = decomp[1]

    # Find Y in LY = b where Y = Ux
    y1 = b[0]
    y2 = b[1] - (L[1][0] * y1)
    y3 = b[2] - (L[2][1] * y2 + L[2][0] * y1)
    y4 = b[3] - (L[3][2] * y3 + L[3][1] * y2 + L[3][0] * y1)
    Y = np.array([y1, y2, y3, y4])

    # Find x in Ux = y
    x4 = y4 / (U[3][3])
    x3 = (y3 - U[2][3] * x4) / U[2][2]
    x2 = (y2 - (U[1][2] * x3 + U[1][3] * x4)) / U[1][1]
    x1 = (y1 - (U[0][1] * x2 + U[0][2] * x3 + U[0][3] * x4)) / U[0][0]
    X = np.array([x1, x2, x3, x4])

    return X

tup = lu_decomposition(A)
L = tup[0]
U = tup[1]


print("L = \n", L)
print("\nU = \n", U)
print("\nX = \n", axequalsb(A, b))


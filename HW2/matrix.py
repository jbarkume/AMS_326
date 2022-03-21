import numpy as np

A = np.array([[1.0, 2.0, 2.0], [4.0, 4.0, 2.0], [4.0, 6.0, 4.0]])
print("A = ", A)


# Returns tuple of matrices where first element is L and second element is U in "matrix = LU"
# expects the first entry in the matrix to be 1.0
def lu_decomposition(A):
    print("\nFinding LU decomposition...\n")

    # initialize L to be identity 3x3 matrix
    L = np.identity(3)

    # use multiplier to turn entry [2,1] to zero
    # to get multiplier, we use the formula that entry [2,1] = m * [1,1] + [2,1] = 0
    # rearranging we get that:
    multiplier = -(A[1][0] / A[0][0])
    U = np.array([A[0], A[1] + (A[0] * multiplier), A[2]])

    # update L to be negative of multiplier
    L[1][0] = -multiplier

    # print LU after first step
    print("\nFirst Step:\n")
    print("L = ", L)
    print("U = ", U)

    # use multiplier to turn entry [3,1] to zero
    multiplier = -(U[2][0] / U[0][0])
    U[2] += U[0] * multiplier
    L[2][0] = -multiplier

    # print LU after second step
    print("\nSecond Step:\n")
    print("L = ", L)
    print("U = ", U)

    # user multiplier to turn entry [3,2] to zero
    multiplier = -(U[2][1] / U[1][1])
    U[2] += U[1] * multiplier
    L[2][1] = -multiplier

    # print LU after third step
    print("\nThird Step:\n")
    print("L = ", L)
    print("U = ", U)

    # return tuple with L as first element and U as second
    return L, U


# Takes in a 3x3 matrix A and a vector b where we want to solve Ax = b
def axequalsb(A, b):
    print("\nFinding solution to Ax = b...\n")

    # Find LU decomposition of A so that Ax = b becomes LUx = b
    decomp = lu_decomposition(A)
    L = decomp[0]
    U = decomp[1]

    # Find Y in LY = b where Y = Ux
    y1 = b[0]
    y2 = b[1] - (L[1][0] * y1)
    y3 = b[2] - (L[2][1] * y2 + L[2][0] * y1)
    Y = np.array([y1, y2, y3])
    print("\nY solutions for LY = b: ", Y)

    # Find x in Ux = y
    x3 = y3 / (U[2][2])
    x2 = (y2 - U[1][2] * x3) / U[1][1]
    x1 = (y1 - (U[0][1] * x2 + U[0][2] * x3)) / U[0][0]
    X = np.array([x1, x2, x3])
    print("\nX solutions for UX = Y: ", X)

    return X


X = axequalsb(A, np.array([11.0, 18.0, 28.0]))

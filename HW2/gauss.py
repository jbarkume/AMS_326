import time

import numpy as np


# creates and returns an augmented matrix of the form [A | b]
# where A is a 3x3 matrix and b is a 3x1 vector
def augment_matrix(A, b):
    A = np.append(A, [[b[0]], [b[1]], [b[2]]], axis=1)
    return A


# Returns an augmented Matrix of the form [A | I] where A is a 3x3 and I is the identity matrix
def augment_identity_matrix(A):
    I = np.identity(3)
    for i in range(3):
        A = augment_matrix(A, I[i])
    return A


# method to solve Ax = b using gaussian elimination
def gaussian_elemination(A, b):
    print("\nUsing Gaussian elemination to solve Ax = b...\n")

    # create augmented matrix of form [A|b]
    augmented_A = augment_matrix(A, b)
    print("\nStarting Augmented Matrix of Form [A | b] = \n", augmented_A)

    # begin row operations starting with turning A21 into zero

    # first step
    multiplier = -(augmented_A[1][0] / augmented_A[0][0])
    # multiply first row by multiplier and add to second row
    augmented_A[1] += multiplier * augmented_A[0]
    print("\nFirst Step:\n", augmented_A)

    # second step
    multiplier = -(augmented_A[2][0] / augmented_A[0][0])
    # multiply first row by multiplier and add to second row
    augmented_A[2] += multiplier * augmented_A[0]
    print("\nSecond Step:\n", augmented_A)

    # third step
    multiplier = -(augmented_A[2][1] / augmented_A[1][1])
    # multiply first row by multiplier and add to second row
    augmented_A[2] += multiplier * augmented_A[1]
    print("\nThird Step:\n", augmented_A)

    # Next, solve for X by back-substituting
    x3 = augmented_A[2][3] / augmented_A[2][2]
    x2 = (augmented_A[1][3] - augmented_A[1][2] * x3) / augmented_A[1][1]
    x1 = (augmented_A[0][3] - (augmented_A[0][1] * x2 + augmented_A[0][2] * x3)) / augmented_A[0][0]
    X = np.array([x1, x2, x3])

    return X


# Returns the inverse of a 3x3 matrix A
# Uses pivot method
def inverse_3(A):
    print("\nUsing Pivoting method to find the inverse of A...\n")
    # check if A11 is zero, and switch rows if condition is true
    if A[0][0] == 0.0:
        if A[1][0] == 0.0:
            A[[0, 2]] = A[[2, 0]]
        else:
            A[[0, 1]] = A[[1, 0]]
        print("\nA after row switch: \n", A)

    augment_A = augment_identity_matrix(A)
    print("\nAugmented [A | I] = \n", augment_A)

    # First pivot using A11
    augment_A[0] /= augment_A[0][0]
    augment_A[1] -= (augment_A[0] * augment_A[1][0])
    augment_A[2] -= (augment_A[0] * augment_A[2][0])
    print("\nFirst Step: A = \n", augment_A)


    # Second pivot using A22
    augment_A[1] /= augment_A[1][1]
    augment_A[0] -= (augment_A[1] * augment_A[0][1])
    augment_A[2] -= (augment_A[1] * augment_A[2][1])
    print("\nSecond Step: A = \n", augment_A)

    # Third pivot using A33
    augment_A[2] /= augment_A[2][2]
    augment_A[0] -= (augment_A[2] * augment_A[0][2])
    augment_A[1] -= (augment_A[2] * augment_A[1][2])
    print("\nThird Step: A = \n", augment_A)

    inv_A = np.array([augment_A[0][3:], augment_A[1][3:], augment_A[2][3:]])

    return inv_A


# Enter Arguments Here
# ---------------------------------------

A = np.array([[2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])

b = np.array([2.0,
              8.0,
              10.0])

# ---------------------------------------

t1 = time.time()
X = gaussian_elemination(A, b)
gauss_time = "{:.3e}".format(time.time() - t1)

print("\nX solutions: ", X)
print("\nTime to find X: " + str(gauss_time) + " nanoseconds")

t2 = time.time()
inv_A = inverse_3(A)
inv_time = "{:.3e}".format(time.time() - t2)

print("\nInverse of A = \n", inv_A)
print("\nTime to find Inverse: " + str(inv_time) + " nanoseconds")

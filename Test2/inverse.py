import numpy as np

# Enter Arguments
# --------------------------------

A = np.array([[2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])

b = np.array([2.0,
              8.0,
              10.0])


# --------------------------------


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

    # Second pivot using A22
    augment_A[1] /= augment_A[1][1]
    augment_A[0] -= (augment_A[1] * augment_A[0][1])
    augment_A[2] -= (augment_A[1] * augment_A[2][1])

    # Third pivot using A33
    augment_A[2] /= augment_A[2][2]
    augment_A[0] -= (augment_A[2] * augment_A[0][2])
    augment_A[1] -= (augment_A[2] * augment_A[1][2])

    inv_A = np.array([augment_A[0][3:], augment_A[1][3:], augment_A[2][3:]])

    return inv_A


inv_A = inverse_3(A)

print("\n\nInverse of A:")
for i in range(3):
    print(inv_A[i])

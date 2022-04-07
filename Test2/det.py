import numpy as np

# Enter Arguments for A
# Make sure A and b all contain elements of the same type
# --------------------------------------------

A = np.array([[1.0, 2.0, 4.0, 7.0],
              [2.0, 13.0, 23.0, 38.0],
              [4.0, 23.0, 77.0, 122.0],
              [7.0, 38.0, 122.0, 294.0]])

# -------------------------------------------


def det_2(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    return a * d - (b * c)

def det(A):
    length = len(A)
    if length == 2:
        return det_2(A)

    sum = 0
    for i in range(length):
        if i % 2 == 0:
            multiplier = 1
        else:
            multiplier = -1
        new_matrix = np.delete(A, 0, 0)
        new_matrix = np.delete(new_matrix, i, 1)
        sum += multiplier * A[0][i] * det(new_matrix)
    return sum

x = det(A)

print(x)
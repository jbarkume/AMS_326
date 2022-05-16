import numpy as np
import matplotlib.pyplot as plt
import LUdecomp


def linear_interpolant(point1, point2, x_value):
    """
    Returns the interpolated point at the given x_value using two points given
    :param point1: Point before x_value
    :param point2: Point after x_value
    :param x_value: the x value of the point we want to interpolate
    :return: The point interpolated as a tuple: (x, y)
    """
    # check if x_value is between two points
    if point2[0] < x_value or x_value < point1[0]:
        raise Exception('Cannot interpolate for x value not in between two points')

    # find y value using linear interpolation
    y_value = point1[1] + (point2[1] - point1[1]) * (x_value - point1[0]) / (point2[0] - point1[0])
    return x_value, y_value


def polynomial_interpolation(x_values, y_values):
    """
    Returns a polynomial that interpolate the data points given
    :param x_values:
    :param y_values:
    :return: The polynomial that goes through the data points given
    """
    # initialize A matrix of Ax = b
    n = len(x_values)
    A = np.zeros((n, n))

    # create matrix of polynomials
    for i in range(n):
        for j in range(n):
            A[i][j] = x_values[i] ** (n - j - 1)

    A[:, [n - 1, 0]] = A[:, [0, n - 1]]

    ak = LUdecomp.Axequalsb(A, y_values)

    # switch first and last to make ak = [an, an-1, an-2, ... , a0]
    temp = ak[-1]
    ak[-1] = ak[0]
    ak[0] = temp

    # create polynomial funtion
    def f(x):
        function = 0
        n = len(ak)
        for i in range(n):
            function += ak[i] * (x ** (n - i - 1))
        return function

    return f

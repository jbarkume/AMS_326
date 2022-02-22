import math
import random


# function equation for disc is: (x-.25)**2 + (y-.25)**2 = .125
# for area purposes, we can make this equivalient to x**2 + y**2 = .125
# We can split this into two equations: one for top half of y and one for bottom half


def f_top(x):
    root = 1 - (8 * (x ** 2))
    if root <= 0:
        root = .00000000000001  # This is for when we get very high values of x that will result in a negative root
    y = math.sqrt(root) / (2 * math.sqrt(2))
    return y


def f_bottom(x):
    root = 1 - (8 * (x ** 2))
    if root <= 0:
        root = .0000001
    y = -math.sqrt(root) / (2 * math.sqrt(2))
    return y


# Approximates the function using the midpoint method with N rectangles
# N is the number of rectangles
def rectangle_method(N):
    # calculate length of each sub-interval
    a = -math.sqrt(.125)
    b = math.sqrt(.125)
    change_x = (b - a) / N

    # loop N times, calculating the area of rectangle using f_top(x) to get area of top semi-circle
    reimann_sum = 0
    for i in range(N):
        x = a + i * change_x
        y = x + change_x

        # calculate midpoint of x and y
        m = (x + y) / 2

        reimann_sum += f_top(m)

    reimann_sum *= change_x  # Multiply entire sum to get approximation of semi-circle
    reimann_sum *= 2  # sum * 2 will result in the area of the entire circle
    return reimann_sum


# Approximates the function using the trapezoid method with N trapezoids
# N is the number of trapezoids
def trapezoid_method(N):
    # calculate length of each sub-interval
    a = -math.sqrt(.125)
    b = math.sqrt(.125)
    change_x = (b - a) / N

    reimann_sum = 0

    for i in range(N):
        x = a + i * change_x
        y = x + change_x
        height = (f_top(x) + f_top(y)) / 2
        reimann_sum += height

    reimann_sum *= change_x
    reimann_sum *= 2
    return reimann_sum


# approximates function defined above using N "shots"
# N is the number of iterations tested

def monte_carlo(N):
    # initialize counters to zero
    square_dot_count = 0
    disc_dot_count = 0

    for i in range(N):
        # The bounds on x value is (-.2, .8) and same for y value
        x = random.uniform(-.2, .8)
        y = random.uniform(-.2, .8)

        # calculate left-hand side of function
        lhs = (x - .25) ** 2 + (y - .25) ** 2

        # if lhs is less than or equal to rhs = .125, then increment disc counter
        # then increment square counter no matter what
        if lhs <= .125:
            disc_dot_count += 1
        square_dot_count += 1

    # calculate area of square and multiply by ratio of disc points to total points
    area_of_square = 1
    ratio = disc_dot_count / square_dot_count
    answer = area_of_square * ratio
    return answer


actual_area = math.pi / 8

print("Actual Area:\n" + str(actual_area))

N = 100
rec = rectangle_method(N)
trapezoid = trapezoid_method(N)
monte = monte_carlo(N)

print("\nRectangle Method:\n" + str(rec))
print("\nTrapezoid Method:\n" + str(trapezoid))
print("\nMonte Carlo Method:\n" + str(monte))

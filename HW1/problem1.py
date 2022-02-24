import math
from decimal import Decimal, getcontext


def truncate(num, precision):
    integer = int(num * 10 ** precision) / 10 ** precision
    return float(integer)


# f(x) = (2.020**(-x**3)) - (x**4 * sin(x**3)) - 1.949
# Interval of x: [-1, 2]

def f(x):
    term1 = 2.02 ** (-(x ** 3))
    term2 = x ** 4 * math.sin(x ** 3)
    term3 = 1.949
    return term1 - term2 - term3


def f_prime(x):
    term1 = -3 * (math.log(101) - math.log(50)) * (x ** 2) * (50 ** (x ** 3)) / (101 ** (x ** 3))
    term2 = -1 * (3 * x ** 6 * math.cos(x ** 3) + 4 * x ** 3 * math.sin(x ** 3))
    return term1 + term2


# Recursively divides size of interval by two so that the interval still brackets the root
# Is called until the midpoint of the interval has a function value that is within k of zero
def bisection_method(low, high, k):
    if (f(low) * f(high)) >= 0:
        print("There is no root in this interval")
        return
    mid = (low + high) / 2

    # First check if f(mid) is sufficiently close enough to zero
    if -k <= f(mid) <= k:
        return mid

    # Then check if f(mid) has opposite sign to f(low), then set new interval to [low, mid] and call bisection
    # method recursively. If not, call bisection method with interval [mid, high]
    elif f(low) * f(mid) < 0:
        return bisection_method(low, mid, k)
    else:
        return bisection_method(mid, high, k)


def newtons_method(x0, k):
    num = f(x0)
    # print("x0 : " + str(x0))
    if -k <= num <= k:
        return x0
    denom = f_prime(x0)
    if denom == 0:
        print("Did not converge")
        return
    x1 = x0 - (num / denom)
    # print("x1 : " + str(x1))
    return newtons_method(x1, k)


# x1 is the initial guess of the root from looking at the function
# x2 and x3 are same as x1 but for different roots in interval [-1, 2]
x1 = -0.85
x2 = 1.5
x3 = 1.8

# delta is the bounds on the interval around the root such that I = [x1 - delta, x1 + delta]
delta = 0.1

a1 = x1 - delta
b1 = x1 + delta

a2 = x2 - delta
b2 = x2 + delta

a3 = x3 - delta
b3 = x3 + delta

k = .001 # The interval that f(x) must be within to be sufficiently close to a root

precision = 6 # The decimal precision

print("Bisection Method")

root1_bisect = truncate(bisection_method(a1, b1, k), precision)
print("\nRoot One: " + str(root1_bisect))

root2_bisect = truncate(bisection_method(a2, b2, k), precision)
print("\nRoot Two: " + str(root2_bisect))

root3_bisect = truncate(bisection_method(a3, b3, k), precision)
print("\nRoot Three: " + str(root3_bisect))

print("\nNewtons Method")

root1_newton = truncate(newtons_method(x1, k), precision)
print("\nRoot One: " + str(root1_newton))

root2_newton = truncate(newtons_method(x2, k), precision)
print("\nRoot Two: " + str(root2_newton))

root3_newton = truncate(newtons_method(x3, k), precision)
print("\nRoot Three: " + str(root3_newton))

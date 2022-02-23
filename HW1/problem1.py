import math


# f(x) = (2.020**(-x**3)) - (x**4 * sin(x**3)) - 1.949
# Interval of x: [-1, 2]

def f(x):
    term1 = 2.020 ** (-(x ** 3))
    term2 = x ** 4 * math.sin(x ** 3)
    term3 = 1.949
    return term1 - term2 - term3


def f_prime(x):
    term1 = -1 * (3 * (math.log(101 / 50.0, math.e)) * x ** 2 * 50 ** (x ** 3))
    term2 = -1 * (3 * x ** 6 * math.cos(x ** 3) - 4 * x ** 3 * math.sin(x ** 3))
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
    if -k <= f(x0) <= k:
        return x0
    denom = f_prime(x0)
    if denom == 0:
        print("Did not converge")
        return
    num = f(x0)
    x1 = x0 - (num / denom)
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

k = .001

root1_bisect = bisection_method(a1, b1, k)
print(root1_bisect)

root2_bisect = bisection_method(a2, b2, k)
print(root2_bisect)

root3_bisect = bisection_method(a3, b3, k)
print(root3_bisect)

import math
import timeit


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

class Bisection:
    iterations = 0
    clocktime = 0

    def __init__(self, a, b, k):
        self.a = a  # lower boundary
        self.b = b  # upper boundary
        self.k = k  # sufficiently close enough value to zero

    def bisection_method(self):
        self.iterations = 0
        return self.bisection_method_help(self.a, self.b, self.k)

    def bisection_method_help(self, low, high, k):
        if (f(low) * f(high)) >= 0:
            print("There is no root in this interval")
            return

        mid = (low + high) / 2

        # First check if f(mid) is sufficiently close enough to zero
        if -k <= f(mid) <= k:
            return mid

        self.iterations += 1
        # Then check if f(mid) has opposite sign to f(low), then set new interval to [low, mid] and call bisection
        # method recursively. If not, call bisection method with interval [mid, high]
        if f(low) * f(mid) < 0:
            return self.bisection_method_help(low, mid, k)

        return self.bisection_method_help(mid, high, k)

class Newton:

    iterations = 0
    clocktime = 0

    def __init__(self, x0, k):
        self.x0 = x0
        self.k = k

    def newtons_method(self):
        self.iterations = 0
        return self.newtons_method_help(self.x0, k)

    def newtons_method_help(self, x0, k):
        num = f(x0)
        if -k <= num <= k:
            return x0
        denom = f_prime(x0)
        if denom == 0:
            print("Did not converge")
            return
        x1 = x0 - (num / denom)
        self.iterations += 1
        return self.newtons_method_help(x1, k)


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

k = .0001  # The interval that f(x) must be within to be sufficiently close to a root

precision = 6  # The decimal precision


# lines 98 - 121 gather all the data needed for storing the bisection method roots
# and their times, values, iterations etc.
root1_bisect = Bisection(a1, b1, k)

root2_bisect = Bisection(a2, b2, k)

root3_bisect = Bisection(a3, b3, k)

t1 = timeit.repeat(lambda: root1_bisect.bisection_method(), number=10, repeat=20)
t2 = timeit.repeat(lambda: root2_bisect.bisection_method(), number=10, repeat=20)
t3 = timeit.repeat(lambda: root3_bisect.bisection_method(), number=10, repeat=20)

root1_bisect.clocktime = sum(t1) / len(t1)
root1 = truncate(root1_bisect.bisection_method(), precision)

root2_bisect.clocktime = sum(t2) / len(t2)
root2 = truncate(root2_bisect.bisection_method(), precision)

root3_bisect.clocktime = sum(t3) / len(t3)
root3 = truncate(root3_bisect.bisection_method(), precision)

# Dictionary containing the bisection roots as keys mapped to triples of their
# corresponding values, iterations, and clock-times
bisect_roots = {root1_bisect: (root1, root1_bisect.iterations, root1_bisect.clocktime),
                root2_bisect: (root2, root2_bisect.iterations, root2_bisect.clocktime),
                root3_bisect: (root3, root3_bisect.iterations, root3_bisect.clocktime)}

#
root4_newtons = Newton(x1, k)
root5_newtons = Newton(x2, k)
root6_newtons = Newton(x3, k)

t4 = timeit.repeat(lambda: root4_newtons.newtons_method(), number=10, repeat=20)
t5 = timeit.repeat(lambda: root5_newtons.newtons_method(), number=10, repeat=20)
t6 = timeit.repeat(lambda: root6_newtons.newtons_method(), number=10, repeat=20)

root4_newtons.clocktime = sum(t4) / len(t4)
root4 = truncate(root4_newtons.newtons_method(), precision)

root5_newtons.clocktime = sum(t5) / len(t5)
root5 = truncate(root5_newtons.newtons_method(), precision)

root6_newtons.clocktime = sum(t6) / len(t6)
root6 = truncate(root6_newtons.newtons_method(), precision)

newton_roots = {root4_newtons: (root4, root4_newtons.iterations, root4_newtons.clocktime),
                root5_newtons: (root5, root5_newtons.iterations, root5_newtons.clocktime),
                root6_newtons: (root6, root6_newtons.iterations, root6_newtons.clocktime)}
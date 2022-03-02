from problem2_table import *
from problem2 import *

# Enter arguments -------------------------------------------

precision = 4  # Decimal precision

N1 = 10000  # Iterations for rectangle method

N2 = 1000  # Iterations for trapezoid method

N3 = 10000000  # Iterations for monte carlo method

# ----------------------------------------------------------

methods_dict = run_methods(N1, N2, N3, precision)

print_table(methods_dict)

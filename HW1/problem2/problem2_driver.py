from problem2_table import *
from problem2 import *

# Enter arguments -------------------------------------------

precision = 4  # Decimal precision

N = 1000000  # Iterations

# ----------------------------------------------------------

methods_dict = run_methods(N, precision)

print_table(methods_dict, N)

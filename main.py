import math
import random

circle_counter = 0
square_counter = 0

for i in range(100000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    boolean = (x ** 2 + y ** 2) <= 1
    if boolean:
        circle_counter += 1
    square_counter += 1

pi = 4 * (circle_counter / square_counter)
print("Value of Pi " + str(pi))


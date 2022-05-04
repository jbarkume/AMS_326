import math

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

bullet_mass = 0.1  # in kilograms

v0 = 300  # initial speed = 300 m/s

g_force = bullet_mass * 9.8  # in Newtons = kg*m/s^2


def r_force(v):
    k = 9.11 * (10 ** -3)
    return k * (v ** 0.999)


# when bullet is going up v'(t) = -g - r_force / m

def v_prime_up(v, t):
    return (-g_force - r_force(v)) / bullet_mass


def v_prime_down(v, t):
    return (g_force - r_force(v)) / bullet_mass


t = np.linspace(0, 15, 10000)

y = odeint(v_prime_up, v0, t)

lst = [(x[0][0], x[1]) for x in zip(y, t)]

for (velocity, time) in lst:
    if abs(velocity) <= 1:
        time_up = round(time, 2)


def find_position_at_top(time):
    acceleration = v_prime_up(0, time)
    return v0 * time + acceleration * time ** 2

distance_up = find_position_at_top(time_up)

print("Distance Traveled Up: " + str(round(distance_up, 2)) + " m")
print("Time Traveled Up: " + str(time_up) + " s")

def find_time_down():
    acceleration = v_prime_down(0, time)
    root = distance_up / acceleration
    return math.sqrt(root)

time_down = find_time_down()

print("Time to Travel back down: " + str(round(time_down, 2)) + " s")

print("Total Distance Traveled = " + str(round(distance_up * 2, 2)) + " m")

print("Total time = " + str(round(time_up + time_down, 2)) + " s")




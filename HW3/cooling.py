from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

print("Temperature Rate of Change: T'(t) = k * (33.33 - T**1.01)")


# function y'(t)
def T_prime(T, t, k):
    # ambient temperature
    A = 33.33
    dydt = k * (A - (T ** 1.01))
    return dydt


# initial condition
T0 = 91.11

# time points
t = np.linspace(0, 180, 180)

# solve ODE
k = 0
for i in range(1, 1000):
    k = i * .00001
    y = odeint(T_prime, T0, t, args=(k,))
    if abs(y[120][0] - 66.66) <= .025:
        break

# extract values from y
print("Cooling constant k = " + str(k))

# now we need to compute the time it takes for the temp to drop from 98.88 to 91.11
# T'(t) = .00423 * (33.33 - T ** 1.01)
T0 = 98.88
t = np.linspace(0, 180, 180)
y = odeint(T_prime, T0, t, args=(k,))

time_temp = list(zip(t, [x[0] for x in y]))

time = 0
for x in time_temp:
    if abs(x[1] - 91.11) <= .1:
        time = round(x[0], 2)
        y_value = round(x[1], 2)

hour_of_death = 11
min_of_death = int(round(60 - time))
print("Time of Death: " + str(hour_of_death) + ":" + str(min_of_death) + "PM")

# compute time for corpse to reach 44.44 F

T0 = 98.88
t = np.linspace(0, 500, 500)

y = odeint(T_prime, T0, t, args=(k,))

time_temp = list(zip(t, [x[0] for x in y]))

time = 0
for x in time_temp:
    if abs(x[1] - 44.44) <= .1:
        time = round(x[0], 2)
        y_value = round(x[1], 2)

print("Time to reach reach 44.44 F = " + str(time) + " minutes")

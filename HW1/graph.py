import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.5, 2.5, 100)
y = 2.02 ** (-(x ** 3)) - x ** 4 * np.sin(x ** 3) - 1.949

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'b')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from problem2 import *

d = [[key, value[0], "{:.6e}".format(value[1])] for key, value in methods.items()]

df = pd.DataFrame(d, columns=['Method', 'Approximation', 'Average Clock-Time (s)'])

fig = plt.figure(figsize=(8, 2))
ax = fig.add_subplot(111)

ax.table(cellText=df.values,
         colLabels=df.columns,
         loc="center"
         )
ax.set_title("Area of Disc")

ax.axis("off")

plt.show()

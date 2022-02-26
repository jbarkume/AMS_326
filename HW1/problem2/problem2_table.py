import math
import matplotlib.pyplot as plt
import pandas as pd
from problem2 import actual_area


# Takes a dictionary and prints a table
def print_table(methods):
    d = [[key, value[0], value[1], "{:.6e}".format(value[2])] for key, value in methods.items()]

    df = pd.DataFrame(d, columns=['Method', 'Iterations', 'Approximation', 'Average Clock-Time (s)'])

    fig = plt.figure(figsize=(8, 2))
    ax = fig.add_subplot(111)

    ax.table(cellText=df.values,
             colLabels=df.columns,
             loc="center"
             )
    ax.set_title("A = " + str(actual_area))


    ax.axis("off")

    print(df)
    plt.show()

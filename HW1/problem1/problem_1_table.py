import pandas as pd
import matplotlib.pyplot as plt
from problem1 import *


def plot_bisection_table():
    d = [[value[0], value[1], "{:.5e}".format(value[2])] for value in bisect_roots.values()]

    df = pd.DataFrame(d, columns=['Approximation', 'Iterations', 'Average Clock-Time (s)'])

    row_labels = ["Root 1", "Root 2", "Root 3"]

    fig = plt.figure(figsize=(8, 2))
    ax = fig.add_subplot(111)

    ax.table(cellText=df.values,
             rowLabels=row_labels,
             colLabels=df.columns,
             loc="center"
             )
    ax.set_title("Bisection Method")

    ax.axis("off")

    plt.show()


def plot_newton_table():
    d = [[value[0], value[1], "{:.5e}".format(value[2])] for value in newton_roots.values()]

    df = pd.DataFrame(d, columns=['Approximation', 'Iterations', 'Average Clock-Time (s)'])

    row_labels = ["Root 1", "Root 2", "Root 3"]

    fig = plt.figure(figsize=(8, 2))
    ax = fig.add_subplot(111)

    ax.table(cellText=df.values,
             rowLabels=row_labels,
             colLabels=df.columns,
             loc="center"
             )
    ax.set_title("Newton's Method")

    ax.axis("off")

    plt.show()

# ----------------------------------
# Uncomment to run ->
# plot_bisection_table()
# plot_newton_table()
# ----------------------------------

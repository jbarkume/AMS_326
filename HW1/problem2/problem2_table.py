import matplotlib.pyplot as plt
import pandas as pd


# Takes a dictionary and prints a table
def print_table(methods, N):
    d = [[key, value[0], "{:.6e}".format(value[1])] for key, value in methods.items()]

    df = pd.DataFrame(d, columns=['Method', 'Approximation', 'Average Clock-Time (s)'])

    fig = plt.figure(figsize=(8, 2))
    ax = fig.add_subplot(111)

    ax.table(cellText=df.values,
             colLabels=df.columns,
             loc="center"
             )
    ax.set_title("N (Iterations) = " + str(N))

    ax.axis("off")

    print(df)
    plt.show()

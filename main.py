import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

wine = load_wine()

train_data, test_data, train_labels, test_labels = train_test_split(wine.data, wine.target,
                                                                    test_size=.2, random_state=20)

k_range = range(1, 101)
accuracies = []

for k in k_range:
    classifier = KNeighborsClassifier(k)
    classifier.fit(train_data, train_labels)
    guess = classifier.score(test_data, test_labels)
    accuracies.append(guess)

plt.plot(k_range, accuracies)
plt.show()
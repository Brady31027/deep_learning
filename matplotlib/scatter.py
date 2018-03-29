import numpy as np
from matplotlib import pyplot as plt

numberOfPoints = 100
# np.random.normal( mean, std variation, numbers)
x = np.random.normal(0, 1, numberOfPoints)
y = np.random.normal(0, 1, numberOfPoints)

plt.figure(figsize=(5, 5))
plt.scatter(x, y)
plt.show()
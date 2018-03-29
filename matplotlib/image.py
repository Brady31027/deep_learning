import numpy as np
from matplotlib import pyplot as plt

data = np.random.random(16).reshape(4, 4)

print data

plt.figure(num=13, figsize=(5, 5))
plt.imshow(data, interpolation='nearest', cmap='Greens')
plt.xticks(()) # remove x ticks
plt.yticks(()) # remove y ticks

plt.colorbar(shrink=0.75)

plt.show()
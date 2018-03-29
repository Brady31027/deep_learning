import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x

plt.figure()
plt.plot(x, y)
plt.xlim((3, 7))
plt.ylim((2, 8))
plt.show()
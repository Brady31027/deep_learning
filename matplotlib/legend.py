import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y1 = x * 0.1 + 3.5
y2 = x

plt.figure(figsize=(5, 5))
plt.plot(x, y1, color='r', label='y = 0.1x + 3.5')
plt.plot(x, y2, color='b', label='y = x')
#plt.legend(loc='upper right')
plt.legend(loc='best')

plt.show()
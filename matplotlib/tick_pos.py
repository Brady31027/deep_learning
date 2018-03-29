import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x

x_tick = np.linspace(3, 7, 5)
y_tick = np.linspace(2, 8, 5)
plt.figure(figsize=(4, 4))
plt.plot(x, y)
plt.xlim((3, 7))
plt.xticks(x_tick)

plt.ylim((2, 8))
plt.yticks(y_tick)

boardInfo = plt.gca()
boardInfo.xaxis.set_ticks_position('bottom')
boardInfo.yaxis.set_ticks_position('right')

plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x * 0.1 + 3.5

plt.figure(figsize=(5, 5))
plt.plot(x, y, linewidth=10.0, color='r')

x_tick = np.linspace(0, 9, 10)
y_tick = np.linspace(0, 9, 10)
plt.xticks(x_tick)
plt.yticks(y_tick)

boardInfo = plt.gca()
boardInfo.xaxis.set_ticks_position('bottom')
boardInfo.yaxis.set_ticks_position('left')
boardInfo.spines['left'].set_position(('data', 4))
boardInfo.spines['bottom'].set_position(('data', 4))
boardInfo.spines['right'].set_color('none')
boardInfo.spines['top'].set_color('none')

for tick in boardInfo.get_xticklabels() + boardInfo.get_yticklabels():
	tick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.5))

plt.show()
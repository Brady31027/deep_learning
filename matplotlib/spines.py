import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x

x_tick = np.linspace(3, 7, 10)

plt.figure()
plt.plot(x, y)
plt.xlim((3, 7))
plt.xticks(x_tick)

plt.ylim((2, 8))
plt.yticks([3, 5, 7],['$bad$', '$so\ so$', '$good$'])

boarder = plt.gca()
boarder.spines['top'].set_color('r')
boarder.spines['right'].set_color('none')
plt.show()
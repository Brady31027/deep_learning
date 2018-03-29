import numpy as np
from matplotlib import pyplot as plt

x = np.arange(10)
y = x * 0.3

plt.figure(figsize=(5, 5))
plt.plot(x, y)

annoX = 5
annoY = annoX * 0.3
plt.scatter(annoX, annoY, s=50, color='red') # s attrib means scatter size
plt.plot([annoX, annoX], [0, annoY], linestyle='--', color='red')

boarderInfo = plt.gca()
boarderInfo.spines['bottom'].set_position(("data", 0))
boarderInfo.spines['left'].set_position(("data", 0))

plt.annotate("({}, {})".format(annoX, annoY), xy=(annoX, annoY), xycoords='data',\
	        xytext=(30, -30), textcoords='offset points', \
	        arrowprops={'arrowstyle':'->', 'connectionstyle':'arc3, rad=0.2'} )

plt.text(2, 2.5, "Annotation Demo", color='r')
plt.show()
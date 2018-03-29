from matplotlib import pyplot as plt
import numpy as np

x = np.arange(10)
y = x

plt.figure(figsize=(5, 5))
plt.bar(x, y)

for x, y in zip(x, y):
	plt.text(x + 0.3, y + 0.3, "{}".format(y))

plt.xlim(0, 11)
plt.ylim(0, 11)

plt.show()
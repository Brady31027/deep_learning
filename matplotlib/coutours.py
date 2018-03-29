import numpy as np
from matplotlib import pyplot as plt

def getHeight(x, y):
	return x + y * 2

gridNum = 300
x = np.linspace(0, 100, gridNum)
y = np.linspace(0, 100, gridNum)
X, Y = np.meshgrid(x, y)
Z = getHeight(X, Y)

plt.figure(num=14, figsize=(5, 5))
plt.xticks(())
plt.yticks(())

C = plt.contour(X, Y, Z, colors='k')
plt.clabel(C)
plt.contourf(X, Y, Z)

plt.show()
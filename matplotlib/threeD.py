import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d as plt3d

fig = plt.figure(num=15)
fig3d = plt3d.Axes3D(fig)

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

fig3d.plot_surface(X, Y, Z, \
	               rstride=1, cstride=1, \
	               cmap=plt.get_cmap('rainbow'))

fig3d.contourf(X, Y, Z, \
	            offset=-2, zdir='z', cmap=plt.get_cmap('rainbow'))

plt.show()

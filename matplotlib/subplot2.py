from matplotlib import pyplot as plt
import numpy as np 

X = np.arange(0, 10)
Y1 = np.random.normal(5, 1, 10) # shape (0, 10), mean 5, std 1
Y2 = X
Y3 = np.ones((10, )) # shape (0, 10)

plt.figure(figsize=(4, 4))

plt.subplot(2, 1, 1)
plt.plot(X, Y1)

plt.subplot(2, 2, 3)
plt.plot(X, Y2)

plt.subplot(2, 2, 4)
plt.plot(X, Y3)

plt.show()

from matplotlib import pyplot as plt
import numpy as np 

X = np.arange(0, 10)
Y = np.random.normal(5, 1, 10) # shape (0, 10), mean 5, std 1

plt.figure(figsize=(6, 5)) # width, height
fig1 = plt.subplot2grid((3, 3), (0, 0) , rowspan=3, colspan=2)
fig2 = plt.subplot2grid((3, 3), (0, 2) , rowspan=1, colspan=1)
fig3 = plt.subplot2grid((3, 3), (1, 2) , rowspan=2, colspan=1)

fig1.plot(X, Y)
fig2.bar(X, Y)
fig3.scatter(X, Y)

plt.show()

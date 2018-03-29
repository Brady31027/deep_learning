from matplotlib import pyplot as plt
import numpy as np 

X = np.arange(0, 10)
Y1 = X
Y2 = 9 - X
Y3 = np.ones((10, )) # shape (0, 10)
Y4 = np.random.normal(5, 1, 10) # shape (0, 10), mean 5, std 1


fig, ((fig1, fig2), (fig3, fig4)) = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(5, 5))
fig1.plot(X, Y1)
fig2.plot(X, Y2)
fig3.plot(X, Y3)
fig4.plot(X, Y4)
plt.show()

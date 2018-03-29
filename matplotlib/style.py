import numpy as numpy
import matplotlib.pyplot as plt

x = numpy.arange(10)
y1 = x ** 2
y2 = x

plt.figure(num=2, figsize=(5, 5))
plt.plot(x, y1, color='red', linewidth=2.0)
plt.plot(x, y2, color='blue', linestyle='--')
plt.show()
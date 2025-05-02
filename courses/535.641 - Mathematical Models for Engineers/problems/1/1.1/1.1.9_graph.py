import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 1000)
y = 2*np.exp(-4*x)

plt.plot(x, y)
plt.grid()
plt.show()

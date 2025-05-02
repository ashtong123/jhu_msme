import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 1000)
y = (x + 0.5)*np.exp(x)

plt.plot(x, y)
plt.grid()
plt.show()
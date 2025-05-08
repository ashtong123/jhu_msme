import matplotlib.pyplot as plt
import numpy as np

x = [0]
y = [0]
idx = 0
h = 0.1
y_prime = lambda x,y: (y - x) ** 2

while idx < 10:
    next = y[idx] + h*y_prime(x[idx], y[idx])
    y.append(next)
    x.append(x[idx] + h)
    idx += 1

x0 = np.linspace(0, 1, 10)
y0 = x0 - np.tanh(x0)

plt.plot(x, y, color = 'blue')
plt.plot(x0, y0, color = 'red')

plt.show()
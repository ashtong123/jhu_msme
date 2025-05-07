import numpy as np
import matplotlib.pyplot as plt

def first_order_ode_plot(ypr, res, domain, range):

    nx, ny = (res, res)
    x = np.linspace(domain[0], domain[1], nx)
    y = np.linspace(range[0], range[1], ny) 
    xv, yv = np.meshgrid(x, y)

    v = ypr(xv, yv)
    u = np.ones((res, res))

    mag = np.sqrt(u**2 + v**2)
    u_norm = u / mag
    v_norm = v / mag

    #print(ypr.shape)
    print(xv.shape)
    print(yv.shape)

    plt.grid(True)
    plt.quiver(xv, yv, u_norm, v_norm)
    plt.show()
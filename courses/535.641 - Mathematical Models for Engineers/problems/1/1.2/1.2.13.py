#dist = vel * time --> vel = const

#ode: y(t) = y'(t) * t
#ic: y(1) = 1

#sol'n: y' = y/x
#dy/dx = y/x
#dy/y = dx/x
#ln(y) + C = ln(x)
# y = x + C
# 1 = 1 + C --> C = 0

#y' = y/x
#y = x

import vector_field_plot as vfp
import numpy as np
import matplotlib.pyplot as plt

def main():
    ypr = lambda x, y: y/x
    vfp.first_order_ode_plot(ypr, 20, (-2, 2), (-2, 2))
    
    x = np.linspace(-2, 2, 100)
    y = x
    plt.plot(x, y)
    
    plt.show()
    

if __name__ == "__main__":
    main()

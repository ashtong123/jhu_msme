import vector_field_plot as vfp
import numpy as np
import matplotlib.pyplot as plt

def main():
    ypr = lambda x, y: np.cos(np.pi * x)
    vfp.first_order_ode_plot(ypr, 20, (-2, 2), (-2, 2))
    
    x = np.linspace(-2, 2, 100)
    y = 1/np.pi * np.sin(np.pi * x)
    plt.plot(x, y)
    
    plt.show()
    

if __name__ == "__main__":
    main()
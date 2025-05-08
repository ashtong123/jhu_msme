#f = ma
#(up is positive)
#sum(f) = -mg + k*v^2
#a = sum(f)/m = v'

# a = v' = -g + kv^2/m --> g, k, m are constant
# m = 1, k = 1, g = 9.81
# given parachute opens at 10m/s 
# or, v(0) = 10m/s

#the approx. solution can be plotted using euler's method


import vector_field_plot as vfp
import numpy as np
import matplotlib.pyplot as plt

def main():
    g = 9.81
    m = 1
    k = 1
    
    fig, axs = plt.subplots(2)
    
    accel = lambda time, velo: -g + k*(velo**2)/m
    vfp.first_order_ode_plot(axs[0], accel, 50, (0, 1), (-15, 0))
    
    alt_accel = lambda time, velo: -g + k*velo/m
    vfp.first_order_ode_plot(axs[1], accel, 50, (0, 1), (-40, 0))
    
    t = [0]
    v = [-10]
    idx = 0
    while t[idx] < 1:
        v.append(v[idx] + 0.01*accel(0, v[idx]))
        t.append(t[idx] + 0.01)
        idx += 1
    axs[0].plot(t, v)

    t = [0]
    v = [-10]
    idx = 0
    while t[idx] < 1:
        v.append(v[idx] + 0.01*alt_accel(0, v[idx]))
        t.append(t[idx] + 0.01)
        idx += 1
    axs[1].plot(t, v)
    
    plt.show()
    

if __name__ == "__main__":
    main()

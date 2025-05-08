import vector_field_plot as vfp

def main():
    ypr = lambda x, y: 1 + (y**2)
    vfp.first_order_ode_plot(ypr, 20, (-2, 2), (-2, 2))

if __name__ == "__main__":
    main()
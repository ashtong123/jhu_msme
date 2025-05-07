import sys
import os

# Get the path to the directory containing the file to import
path_to_directory = os.path.abspath("../tools")
# Add the path to sys.path
sys.path.insert(0, path_to_directory)

# Now you can import the file
import vector_field_plot as vfp

def main():
    ypr = lambda x, y: x + y
    vfp.first_order_ode_plot(ypr, 20, (-2, 1), (-1, 1))

if __name__ == "__main__":
    main()
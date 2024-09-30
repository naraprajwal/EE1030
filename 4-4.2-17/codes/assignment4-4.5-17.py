#Code by GVV Sharma
#July 22, 2024
#released under GNU GPL
#Line 


import sys                                          #for path to external scripts
sys.path.insert(0, '/Users/prajwalnara/desktop/matgeo/codes/CoordGeo')        #path to my scripts


import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Load the values from values.dat, skipping the header row
data = np.loadtxt("values.dat", skiprows=1)

# Extracting m and c from the data
m = data[0]  # Slope
c = data[1]  # Intercept

# Define a range of x values
x_values = np.linspace(-10, 10, 400)

# Calculate the corresponding y values using the equation y = mx + c
y_values = m * x_values + c

# Plotting the line
plt.plot(x_values, y_values, label=f'y = {m}x + {c}')

# Labeling the plot
plt.title('Line Plot from m and c values')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Add legend
plt.legend()

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

# Read the values from the C-generated text file using numpy.loadtxt
data = np.loadtxt('data.txt')

# Extracting parabola parameters
p1 = data[0]  # Parameter for y^2 = 4x
p2 = data[1]  # Parameter for x^2 = 4y

# Parabola equation: y^2 = 4px, so x = y^2 / (4p)
def parabola1(y, p):
    return y**2 / (4 * p)

def parabola2(x, p):
    return x**2 / (4 * p)

# Find the points of intersection between the two parabolas
def find_intersections(p1, p2):
    def intersection_eq(y):
        return parabola2(parabola1(y, p1), p2) - y  # Solve for intersection

    y_int1 = fsolve(intersection_eq, 0)[0]  # Initial guess
    y_int2 = fsolve(intersection_eq, 4)[0]  # Initial guess for the other intersection
    return y_int1, y_int2

# Get the intersection points
y_int1, y_int2 = find_intersections(p1, p2)

# Compute the area between the curves using integration
def area_between_curves(y):
    x1 = parabola1(y, p1)  # x from the first parabola
    x2 = 2 * np.sqrt(y)  # From the second parabola (x = 2*sqrt(y))
    return x2 - x1  # Area between the two parabolas

# Perform the integration from y_int1 to y_int2
area, _ = quad(area_between_curves, y_int1, y_int2)



# Visualization
# Generating points for the parabolas
y_vals = np.linspace(0, y_int2 + 1, 400)  # Extend range a bit above the highest intersection
x_parabola1 = parabola1(y_vals, p1)
x_parabola2 = 2 * np.sqrt(y_vals)  # From the second parabola

# Plot the curves
plt.plot(x_parabola1, y_vals, label=r'Parabola: $y^2 = 4x$', color='r')
plt.plot(x_parabola2, y_vals, label=r'Parabola: $x^2 = 4y$', color='b')

# Fill the area between the curves
plt.fill_betweenx(y_vals, x_parabola1, x_parabola2, where=(x_parabola2 >= x_parabola1), color='lightblue', alpha=0.5)

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Two Parabolas')
plt.grid(True)
plt.legend()

# Set equal aspect ratio to avoid distortion
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

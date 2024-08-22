import matplotlib.pyplot as plt

# Coordinates of points A and B
A = (5, -6)
B = (-1, -4)
P = (0, -13/3)

# Extract x and y coordinates
x_values = [A[0], B[0]]
y_values = [A[1], B[1]]

# Plotting the points and the line segment
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Line segment AB')

# Plot points A, B, and P
plt.scatter(*A, color='r', zorder=5, label='Point A (5, -6)')
plt.scatter(*B, color='g', zorder=5, label='Point B (-1, -4)')
plt.scatter(*P, color='m', zorder=5, label='Intersection (0, -13/3)')

# Adding labels and title
plt.text(A[0], A[1], ' A (5, -6)', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], ' B (-1, -4)', fontsize=12, verticalalignment='top', horizontalalignment='right')
plt.text(P[0], P[1], ' P (0, -13/3)', fontsize=12, verticalalignment='top', horizontalalignment='left')

# Adding grid, legend, and labels
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of the Line Segment AB and Intersection with Y-axis')
plt.legend()

# Show plot
plt.show()


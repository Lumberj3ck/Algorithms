import numpy as np
import matplotlib.pyplot as plt

# Define the linear function
def linear_function(x):
    return 5 - 2*x

# Generate x values
x_values = np.linspace(-5, 5, 100)

# Calculate corresponding y values using the linear function
y_values = linear_function(x_values)

# Plot the linear function
plt.plot(x_values, y_values, label='2x + y = 5')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of 2x + y = 5')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a legend
plt.legend()

# Show the plot
plt.show()


::: functions.plot_data



# My Plot Data Function

The plot_data function is designed for plotting numerical data on a 2D graph, allowing for customization of the plot's appearance with labels and colors.



## Parameters

- x (np.ndarray): An array containing the data points for the x-axis.

- y (np.ndarray): An array containing the data points for the y-axis.

- label (str): A string representing the label for the plot, which will be displayed as part of the plot legend.

- color (str): A string specifying the color of the plot line. This should be a valid color name or hexadecimal color code.

## Returns

- None: This function does not return a value. It generates a plot based on the provided data.

## Example

import matplotlib.pyplot as plt

import numpy as np


x = np.linspace(0, 10, 100)

y = np.sin(x)

plot_data(x, y, 'Sine Wave', 'blue')

plt.show()  # Displays the plot

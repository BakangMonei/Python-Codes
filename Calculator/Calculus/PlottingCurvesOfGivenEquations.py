# Author; MoneiBk

# Here, we use NumPy which is a general-purpose array-processing package in python.
# To set the x – axis values, we use np.arange() method in which first two arguments are for range and third one for step-wise increment. The result is a numpy array.
# To get corresponding y-axis values, we simply use predefined np.sin() method on the numpy array.
# Finally, we plot the points by passing x and y arrays to the plt.plot() function.

# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)

# potting the points
plt.plot(x, y)

# function to show the plot
plt.show()

# The problem asks you to load a block of data and fit each column to a gaussian and store the value of the centre
# point of the fit, then plot the difference from the expected value of 49, against the noise data stored in the
# file.


#Import the libraries that you need
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# This is the Gaussian function you can use for fitting
def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude * np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)


#Load the data in to an array
temp_data = np.loadtxt('Data/problem_data.csv', delimiter=',')

#The data needs to be cleaned
#   0       n1      n2
#   x1,     y11,    y21
#   x2,     y12,    y22
#   x3,     y13,    y23


# The array is 101 by 101.
# The first row of the data is the noise associated with the measurement,
# this will be the X value you will need to plot later. We will call this the noise values

# The first column is the X values for all remaining column data
# Build and array from the imported data which is the first column without the first value.

# Build the X__data
# X_values = LOADED_DATA[0, 0:-1]
X_values = temp_data[0, 0:-1]
print(np.shape(X_values))

# Build the noise data
# noise_data =
noise_data = temp_data[1:, 0]
print(np.shape(noise_data))

# Build the block of data to be fitted
# true_data =
true_data = temp_data[1:, 1:]


# Build an array to hold the
# store_values = np.zeros((np.shape(true_data)[0]))
store_values = np.zeros((np.shape(true_data)[0]))

# Build a look to load in a column of data and fit it use curve fit, the function given above
# and the X_values

for column_point in range(np.shape(true_data)[0]):
    current_data = true_data[:, column_point]
    guess = [np.min(current_data), np.argmax(current_data), 5, np.max(current_data)]
    popt, pcov = curve_fit(build_gaussian, X_values, current_data, p0=np.asarray(guess))
    store_values[column_point] = popt[1]

set_position = 49
plt.plot(noise_data, np.abs(set_position-store_values))
plt.show()

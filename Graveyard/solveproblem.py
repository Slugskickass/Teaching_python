import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude * np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)

temp_data = np.loadtxt('problem_data.csv', delimiter=',')

noise_data = temp_data[1:, 0]
print(np.shape(noise_data))

X_values = temp_data[0, 0:-1]
print(np.shape(X_values))

true_data = temp_data[1:, 1:]

store_values = np.zeros((np.shape(true_data)[0]))
for column_point in range(np.shape(true_data)[0]):
    current_data = true_data[:, column_point]
    guess = [np.min(current_data), np.argmax(current_data), 5, np.max(current_data)]
    popt, pcov = curve_fit(build_gaussian, X_values, current_data, p0=np.asarray(guess))
    store_values[column_point] = popt[1]

plt.plot(noise_data, np.abs(49-store_values))
plt.show()

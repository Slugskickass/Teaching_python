import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data_one = np.genfromtxt('Data/linear_data.csv', delimiter=',')

x_data = data_one[:, 0]

y_data = data_one[:, 1]

plt.plot(x_data, y_data)

slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

print(intercept, slope)

fitted_data = (slope * x_data) + intercept

plt.plot(x_data, fitted_data)

plt.show()

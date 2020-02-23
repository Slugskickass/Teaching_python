import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

my_data = np.load('My_noisy_data.npy')
x_data = my_data[:, 0]
y_data = my_data[:, 1]

slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

plt.plot(x_data, y_data,'o')
plt.plot(x_data, intercept + (slope * x_data))
plt.show()
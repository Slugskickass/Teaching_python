import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

import time

start = time.time()


my_data = np.load('My_noisy_data.npy')
x_data = my_data[:, 0]
y_data = my_data[:, 1]

# This is so simple it seems like cheating.  We are going to use a function which takes two
# inputs and returns everything you could want.
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

end = time.time()
print(end-start)

plt.plot(x_data, y_data,'o')
plt.plot(x_data, intercept + (slope * x_data))
plt.show()
print(intercept, slope)
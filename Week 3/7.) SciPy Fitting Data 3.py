import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

my_data = np.load('My_noisy_data.npy')
x_data = my_data[:, 0]
y_data = my_data[:, 1]

deg = 2
p = np.polyfit(x_data, y_data, deg, rcond=None, full=False, w=None, cov=False)

new_y = np.polyval(p, x_data)
plt.plot(x_data, y_data)
plt.plot(x_data, new_y)
plt.show()



# for deg in range(1,10):
#     p = np.polyfit(x_data, y_data, deg, rcond=None, full=False, w=None, cov=False)
#     plt.plot(x_data, np.polyval(p, x_data))
# plt.plot(x_data, y_data)
# plt.show()


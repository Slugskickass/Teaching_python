import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

my_data = np.load('My_noisy_data.npy')
x_data = my_data[:, 0]
y_data = my_data[:, 1]

deg = 1

p = np.polyfit(x_data, y_data, deg, rcond=None, full=False, w=None, cov=False)

new_y = np.polyval(p, x_data)
plt.plot(x_data, y_data)
plt.plot(x_data, new_y)
plt.show()
print(p)

#Unmask this to show how the data fit changes as the degree of the polynomial
for deg in range(20,50):
    p = np.polyfit(x_data, y_data, deg, rcond=None, full=False, w=None, cov=False)
    plt.plot(x_data, np.polyval(p, x_data))
plt.plot(x_data, y_data)
plt.show()


import numpy as np
import scipy
import matplotlib.pyplot as plt

my_data = np.load('My_noisy_data.npy')
x_data = my_data[:, 0]
y_data = my_data[:, 1]
print(np.shape(my_data))


#y_data = np.expand_dims(y_data, axis=0)
print(np.shape(y_data))

A = np.vstack([x_data, np.ones(len(x_data))])
print(np.shape(A))
#
m, c = np.linalg.lstsq(A.T, y_data.T, rcond=None)[0]

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, c + (m * x_data))
plt.show()
import numpy as np
import time

number_data = 10000
data_length = 100

x_data = np.linspace(0, 100, data_length)
fdata = np.expand_dims(np.abs(np.random.normal()) * x_data + np.random.normal(), 1).T
start = time.time()
for I in range(number_data - 1):
    fdatat = np.expand_dims(np.abs(np.random.normal()) * x_data + np.random.normal(), 1).T
    fdata = np.append(fdata, fdatat, axis=0)

end = time.time()
print('Par', end - start)

#np.save('test_data', fdata)
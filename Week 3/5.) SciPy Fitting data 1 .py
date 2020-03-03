import numpy as np
import scipy
import matplotlib.pyplot as plt

import time

start = time.time()




my_data = np.load('My_noisy_data.npy')                      # Load the data
x_data = my_data[:, 0]                                      # Seperate the data in to X and Y
y_data = my_data[:, 1]
print(np.shape(y_data))                                     # Just checking the shape of the data

# We are going to use a matrix method for performing a linear fit
# This looks quite complex but is relatively simple (mathematically)
# However it involves us having to manipulate out data a little
# It is not as easy as the next few methods but it is fast
# If you are doing several million fits (which is not uncommon) this method is very useful.
# Although you may not see an speed difference between these methods when only doing one fit.


# Here we add another column of data where the added column contains just ones
# This is because we want two numbers out the gradient and the intercept, as we are using a matric
# Transform we need to supply the algorithm with a 2D array
A = np.vstack([np.ones(len(x_data)), x_data]).T # Build design matrix
print(np.shape(A))

# See the notes for more explanation.
temp = np.matmul(A.T, A)
temp_inv = np.linalg.inv(temp)

temp2 = np.matmul(A.T, y_data)

final = np.matmul(temp_inv, temp2)
print(final)

end = time.time()
print(end-start)

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, final[0] + (final[1] * x_data))
plt.show()
print(final[0], final[1])
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#Build a function to create a 2D gaussian map, the input should be
#Size of image, centre point, width, and amplitude.
#Build a second function which adds shot noise to the matrix, you just need to pass the matrix.
#Finally build a third function which adds read noise and an offset number, convert to integers.
def build_2d_gaussian(x_data, y_data, offset, xo, yo, sigma, amplitude):
    kernel = np.zeros((x_data, y_data))
    for x in range(x_data):
        for y in range(y_data):
            print(offset + amplitude * np.exp(-1 * (((x-xo)**2 + (y-yo)**2)/sigma**2)))
            kernel[x, y] = offset + amplitude * np.exp(-1 * (((x-xo)**2 + (y-yo)**2)/sigma**2))
    return(kernel)

x_data = 100
y_data = x_data
z_data = build_2d_gaussian(x_data, y_data, 50, 50, 50, 4, 100)
plt.imshow(z_data)
plt.show()
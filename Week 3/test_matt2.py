import math
import numpy as np
import matplotlib.pyplot as plt

def gauss_height(width):  # This should calculate the amplitude of the Gaussian based on an area under the curve of 1
    height = (1 / (math.sqrt(2) * np.abs(width) * math.sqrt(math.pi)))/(2*(np.sqrt(2)))
    return height

def build_2d_gauss(width, height):  # This builds the Gaussian based on the calculated parameters
    xo = yo = 25
    kernel = np.zeros((50, 50))  # PICKED SIZE ARBITRARILY... IS THIS THE RIGHT NUMBER?
    for x in range(np.shape(kernel)[0]):
        for y in range(np.shape(kernel)[1]):
            kernel[x, y] = height * np.exp(-1 * (((x - xo) ** 2 + (y - yo) ** 2) / width ** 2))
    return kernel

width = 4

height = gauss_height(width)

data = build_2d_gauss(width, height)
plt.imshow(data)
plt.show()
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
from scipy import signal

gaussian = np.zeros((20, 20))
amplitude = 1
sigma = 3
xo = yo = 10
for X in range(20):
    for Y in range(20):
        gaussian[X, Y] = amplitude * np.exp(-1 * (((X-xo)**2 + (Y-yo)**2) / sigma**2))
plt.subplot(1, 3, 1)
plt.imshow(gaussian)

GT = np.random.binomial(1, .01, [100, 100])
plt.subplot(1, 3, 2)
plt.imshow(GT)

image_out = signal.convolve2d(GT, gaussian)
plt.subplot(1, 3, 3)
plt.imshow(image_out)
plt.show()

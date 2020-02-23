import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage

from scipy import signal
# file_name = '../Week 2/Data/640.tif'
# img = Image.open(file_name)
# print('The Image is', img.size, 'Pixels.')
# print('With', img.n_frames, 'frames.')
#
#
# imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
# for I in range(img.n_frames):
#     img.seek(I)                             # Pointing
#     imgArray[:, :, I] = np.asarray(img)     # copying
# img.close()
#
# sobel = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
#
# edge = signal.convolve2d(imgArray[:, :, 1], sobel, boundary='symm', mode='same')
#
# plt.subplot(1,2,1)
# plt.imshow(imgArray[:, :, 1])
#
# plt.subplot(1,2,2)
# plt.imshow(edge)
#
# plt.show()

gaussian = np.zeros((20, 20))
amplitude = 1
sigma = 3
xo = yo = 10
for X in range(20):
    for Y in range(20):
        gaussian[X, Y] = amplitude * np.exp(-1 * (((X-xo)**2 + (Y-yo)**2) / sigma**2))

plt.imshow(gaussian)
plt.show()

GT = np.random.binomial(1, .01, [100, 100])
#GT = np.zeros([100,100])
#GT[50, 50] = 1
#plt.imshow(GT)
#plt.show()


image_out = signal.convolve2d(GT, gaussian)
plt.imshow(image_out)
plt.show()
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Generate a gaussian
image_size = 100
gaussian = np.zeros((image_size, image_size))
amplitude = 1
sigma = 3
xo = yo = np.int(image_size/2)
for X in range(image_size):
    for Y in range(image_size):
        gaussian[X, Y] = amplitude * np.exp(-1 * (((xo-X)**2 + (yo-Y)**2) / sigma**2))
plt.subplot(1, 3, 1)
plt.imshow(gaussian)

#Generate the ground truth
test_data = np.random.binomial(1, .01, [image_size, image_size])
#plot the data
plt.subplot(1, 3, 2)
plt.imshow(test_data)

#Take the fourier transform of the two images
test_data_fft = np.fft.fft2(test_data)
gaussian_fft = np.fft.fft2(gaussian)

#Now take the two fourier transforms and muliply them by each other
conv_fft = test_data_fft * gaussian_fft
# perfomr the shift.
conv = np.real(np.fft.ifft2(conv_fft))

np.save('conv', conv)           #Save the data for later
plt.subplot(1, 3, 3)            # Show the data
plt.imshow(conv)
plt.show()

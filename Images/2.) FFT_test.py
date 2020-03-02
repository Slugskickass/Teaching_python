from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


image_file = '../Week 2/Data/640.tif'

img = Image.open(image_file)
print('The Image is', img.size, 'Pixels.')
print('With', img.n_frames, 'frames.')

imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
for I in range(img.n_frames):
    img.seek(I)
    imgArray[:, :, I] = np.asarray(img)
img.close()

# Select an image to play with
working_image = imgArray[:, :, 2]
# Show that image
plt.imshow(working_image)
plt.show()

#Take the FFT of the image, I am suinf the numpy command there are others
FFT_image = np.fft.fft2(working_image)
#Shift the data, this moves the edges to the centre, chat about this
FFT_image_shift = np.fft.fftshift(FFT_image)
#Show the data, we have to change the Zscale and use a log
plt.imshow(np.abs(FFT_image_shift), norm=LogNorm(vmin=5))
plt.show()

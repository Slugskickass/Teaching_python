import skimage.filters as sk
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def loadtiffs(file_name):
    img = Image.open(file_name)
    print('The Image is', img.size, 'Pixels.')
    print('With', img.n_frames, 'frames.')

    imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
    for I in range(img.n_frames):
        img.seek(I)
        imgArray[:, :, I] = np.asarray(img)
    img.close()
    return(imgArray)



data = loadtiffs('test.tif')
data = data.squeeze()

outb = sk.gaussian(data, 10)
outs = sk.gaussian(data, 1)


plt.subplot(2, 2, 1)
plt.imshow(data)

plt.subplot(2, 2, 2)
plt.imshow(outb)

plt.subplot(2, 2, 3)
plt.imshow(outs)

plt.subplot(2, 2, 4)
plt.imshow(outs - outb)

plt.show()

outd = sk.difference_of_gaussians(data, 1, 10)

plt.imshow(outd)
plt.show()


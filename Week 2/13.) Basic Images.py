from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

file_name = '../Week 2/Data/640.tif'
img = Image.open(file_name)
print('The Image is', img.size, 'Pixels.')
print('With', img.n_frames, 'frames.')


imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
for I in range(img.n_frames):
    img.seek(I)                 # Pointing
    imgArray[:, :, I] = np.asarray(img)     # copying
img.close()

for I in range(1, 10):
    plt.subplot(3, 3, I)
    plt.imshow(imgArray[:, :, I-1])
plt.show()



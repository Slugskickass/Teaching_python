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

data = loadtiffs('../confocal.tif')

plt.imshow(data[:, :, 1])
plt.show()
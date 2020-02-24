import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
from scipy import signal

file_name = '../Week 3/Data/colourData.jpg'
img = Image.open(file_name)
data = np.asarray(img)
img.close()


plt.imshow(data)
plt.show()

plt.imshow(data[:,:,0])
plt.show()

plt.imshow(data[:,:,1])
plt.show()

plt.imshow(data[:,:,2])
plt.show()

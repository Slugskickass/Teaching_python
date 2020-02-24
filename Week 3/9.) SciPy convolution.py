import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal


file_name = '../Week 3/Data/peppers.png'
img = Image.open(file_name)
data = np.asarray(img)
img.close()



# First I build a matrix, this is the matrix to perform a Sobel edge detection
# This will detect edges in the X direction
sobel = np.asarray([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
blur = np.asarray([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
bigger_blur = np.ones((25, 25))/25
line_finder = np.asarray([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]])

operations = [sobel, blur, bigger_blur, line_finder]


# Then I take my image and pass my sobel matrix over every pixel
edge = signal.convolve2d(np.sum(data, axis=2), operations[3], boundary='symm', mode='same')

# This returns an edge detected image.
plt.subplot(1,2,1)
plt.imshow(data)
plt.subplot(1,2,2)
plt.imshow(edge, cmap='gray')
#plt.imshow(edge > 200, cmap='gray')
plt.show()


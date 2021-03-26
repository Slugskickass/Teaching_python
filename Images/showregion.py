import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from skimage.morphology import closing, square
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops, regionprops_table


data = np.load('conv.npy')

thresh = threshold_otsu(data) #This gives us a value

bw = closing(data > thresh)

label_image = label(bw, 8)

#These are the properties I am interested in
properties = ['label', 'area', 'centroid', 'bbox']

#This is the command which collects all the properties from the image
regions = regionprops_table(label_image, properties=properties)

# I now turn that data in to a pandas data table
data = pd.DataFrame(regions)

xpos = data['centroid-0']
ypos = data['centroid-1']

areas = np.asarray(data['area'])
positions1 = np.where(areas >= 20)
positions2 = np.where(areas <= 40)
positions = np.intersect1d(positions1, positions2)

plt.imshow(bw)
plt.plot(ypos, xpos, 'r.')
plt.plot(ypos[positions], xpos[positions], 'bo')

plt.show()
############
### https://scikit-image.org
############

import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from skimage.morphology import closing, square
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops, regionprops_table

#Load in the data from earlier
data = np.load('conv.npy')

# apply threshold, we can use anything but here I have been good and used an otsu
thresh = threshold_otsu(data) #This gives us a value

bw = closing(data > thresh) #Closing can remove small dark spots (i.e. “pepper”) and connect small bright cracks.
#bw = data > thresh # I could use this


# label image regions
label_image = label(bw, 8)  # label looks for islands of connected regions the number defines the connections

#These are the properties I am interested in
properties = ['label', 'area', 'centroid', 'bbox']

#This is the command which collects all the properties from the image
regions = regionprops_table(label_image, properties=properties)
# I now turn that data in to a pandas data table
data = pd.DataFrame(regions)


x = np.asarray(data['centroid-0'])
y = np.asarray(data['centroid-1'])


areas = np.asarray(data['area'])
positions1 = np.where(areas >= 20)
positions2 = np.where(areas <= 40)
positions = np.intersect1d(positions1, positions2)

plt.imshow(label_image > 0)
plt.plot(y, x, 'r.')
plt.plot(y[positions], x[positions], 'bo')

plt.show()

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
from skimage.morphology import closing, square
from skimage.filters import threshold_otsu
from skimage.filters import difference_of_gaussians
from skimage.measure import label, regionprops, regionprops_table

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

def filter_data(data, sigmas=1, sigmab=10):
    output = difference_of_gaussians(data, sigmas, sigmab)
    return output

def regionfilter(data, smallest=4, largest=35):
    thresh = threshold_otsu(data)
    bw = closing(data > thresh)
    label_image = label(bw, 8)

    # These are the properties I am interested in
    properties = ['label', 'area', 'centroid', 'bbox']

    # This is the command which collects all the properties from the image
    regions = regionprops_table(label_image, properties=properties)

    # I now turn that data in to a pandas data table
    data = pd.DataFrame(regions)

    xpos = data['centroid-0']
    ypos = data['centroid-1']

    areas = np.asarray(data['area'])
    positions1 = np.where(areas >= smallest)
    positions2 = np.where(areas <= largest)
    positions = np.intersect1d(positions1, positions2)

    return np.asarray(xpos[positions]), np.asarray(ypos[positions])
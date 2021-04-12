import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
from skimage.morphology import closing, square
from skimage.filters import threshold_otsu
from skimage.filters import difference_of_gaussians
from skimage.measure import label, regionprops, regionprops_table
from scipy.optimize import curve_fit

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

def regionfilter(data, smallest=4, largest=15):
    thresh = threshold_otsu(data)
    bw = closing(data > thresh)
    #label_image = label(bw, 8)
    label_image = label(bw, connectivity=2)

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

def filteredges(cut_size, x_pos, y_pos, maxx, maxy):
    positions1 = np.where(x_pos >= cut_size + 1)
    positions2 = np.where(x_pos <= maxx - 1 - cut_size)
    positionsx = np.intersect1d(positions1, positions2)


    positions3 = np.where(y_pos >= cut_size + 1)
    positions4 = np.where(y_pos <= maxy - 1 - cut_size)
    positiony = np.intersect1d(positions3, positions4)

    positions = np.intersect1d(positionsx, positiony)
    return x_pos[positions], y_pos[positions]

def returnregions(current_frame, x_pos, y_pos, cut_size):
    image_store = []
    for current_position in range(np.size(x_pos)):
        temp_X = np.int(np.floor(x_pos[current_position]))
        temp_Y = np.int(np.floor(y_pos[current_position]))
        image_store.append(current_frame[temp_X-cut_size:temp_X+cut_size+1, temp_Y-cut_size:temp_Y+cut_size+1])
    return np.asarray(image_store)

def gaussian(x, y, x0, y0, xalpha, yalpha, offset, A):
    return offset + A * np.exp(-((x-x0)/xalpha)**2 - ((y-y0)/yalpha)**2)

def _gaussian(M, *args):
    x, y = M
    arr = gaussian(x, y, *args)
    return arr

def buildxfit():
    xmin, xmax, nx = 0, 10, 11
    ymin, ymax, ny = 0, 10, 11
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymin, ymax, ny)
    X, Y = np.meshgrid(x, y)
    xdata = np.vstack((X.ravel(), Y.ravel()))
    return xdata


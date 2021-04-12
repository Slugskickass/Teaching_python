import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
from skimage.morphology import closing, square
from skimage.filters import threshold_otsu
from skimage.filters import difference_of_gaussians
from skimage.measure import label, regionprops, regionprops_table
from scipy.optimize import curve_fit

file_name = '/Users/ashleycadby/Data/sequence.tif'
img = Image.open(file_name)
for I in range(img.n_frames):
    img.seek(I)
    print(np.mean(np.asarray(img)))
img.close()
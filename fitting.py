import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# NOTE
from scipy.optimize import curve_fit
# NOTE

def build_gaussian(data, offset, xo, yo,sigma, amplitude):
    length_of_data = np.int(np.size(data) / 2)
    x_data = data[0:length_of_data]
    print(np.size(x_data))
    y_data = data[length_of_data:]
    print(np.size(y_data))

    for xp in x_data:
        for yp in y_data:
            y_val = offset + amplitude * (np.exp((-1 * (xo-x_data)**2)/sigma**2) + np.exp((-1 * (yo-y_data)**2)/sigma**2))

    return(y_val)


x_data = np.linspace(0, 100, 100)
y_data = np.linspace(0, 100, 100)

data = np.concatenate((x_data, y_data))

out = build_gaussian(data, 0, 50, 50, 1, 1)
ax = plt.axes(projection='3d')
ax.plot3D(x_data, y_data, out)
plt.show()


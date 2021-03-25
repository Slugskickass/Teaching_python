import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, y, x0, y0, xalpha, yalpha, A):
    return A * np.exp(-((x-x0)/xalpha)**2 - ((y-y0)/yalpha)**2)

def _gaussian(M, *args):
    x, y = M
    arr = gaussian(x, y, *args)
    return arr

size = 15

x = np.linspace(0, size, size)
y = np.linspace(0, size, size)
X, Y = np.meshgrid(x, y)

Z = gaussian(X, Y, 6, 6.1, 2.2, 3, 1)
plt.imshow(Z)
plt.show()


xdata = np.vstack((X.ravel(), Y.ravel()))
guess = [7, 7, 2.2, 3, 1]

popt, pcov = curve_fit(_gaussian, xdata, Z.ravel(), p0=np.asarray(guess))

plt.imshow(Z)
print(popt[0], popt[1])
plt.show()
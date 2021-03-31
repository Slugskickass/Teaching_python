import numpy as np
import StormUtils as ST
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


p = (5, 5, 3, 3, 1, 20)

#Generates the xdata
xmin, xmax, nx = 0, 10, 11
ymin, ymax, ny = 0, 10, 11
x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)
X, Y = np.meshgrid(x, y)
xdata = np.vstack((X.ravel(), Y.ravel()))


data = ST.gaussian(X, Y, *p)
data = data + np.random.normal(1, 1, (11, 11))

plt.imshow(data)
plt.show()

p0 = (5, 5, 2, 3, 1, 10)


popt, pcov = curve_fit(ST._gaussian, xdata, data.ravel(), p0)
print(popt)
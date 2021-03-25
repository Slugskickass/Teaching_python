import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Freq, V = np.loadtxt("LRCDATA.csv", unpack = True)




def new_function(x_data, R_ratio, Q_value, centre):
    out = R_ratio / (np.sqrt((1+Q_value**2 * (x_data/centre)**2 * (1-(centre/x_data)**2)**2)))
    return(out)

guess = [1, .5, 6500]
popt, pcov = curve_fit(new_function, Freq, V, p0=np.asarray(guess))

x = np.logspace(.1, 8, 500)
y_data = new_function(x, popt[0], popt[1], popt[2])

plt.semilogx(Freq, V, 'o')
plt.semilogx(x, y_data)
plt.show()
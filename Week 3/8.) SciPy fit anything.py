import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
# NOTE
from scipy.optimize import curve_fit
# NOTE

def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude *np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)



x_data = np.linspace(0,100,100)
y_data = np.random.normal(0, 1, len(x_data)) + build_gaussian(x_data, 1, 50, 4, 100)
plt.plot(x_data, y_data, 'o')


guess = [np.min(y_data),np.argmax(y_data),1,np.max(y_data)]

popt, pcov = curve_fit(build_gaussian, x_data, y_data, p0=np.asarray(guess))

fitted_data = build_gaussian(x_data, popt[0], popt[1], popt[2], popt[3])

plt.plot(x_data, fitted_data)
plt.show()

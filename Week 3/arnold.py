import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
# NOTE
from scipy.optimize import curve_fit
# NOTE

def build_decay(x_data, amplitude, lifetime):
    y_val = amplitude * np.exp( -1 * lifetime * x_data)
    return(y_val)



x_data = np.linspace(0, 1, 100)
noise = np.random.normal(0, 0.25, np.shape(x_data))
y_data = build_decay(x_data, 10, 4)
final_data = y_data + noise

plt.plot(x_data, final_data, 'o')

popt, pcov = curve_fit(build_decay, x_data, final_data)

fitted_data = build_decay(x_data, popt[0], popt[1])

plt.plot(x_data, fitted_data)



plt.show()

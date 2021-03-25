import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def generate_decay(x_data, amplitude, lifetime):
    y_data = amplitude * np.exp(-1 * x_data * lifetime)
    return(y_data)


x_data = np.linspace(0, 1, 100)
y_data = generate_decay(x_data, 1, 6)

popt, pcov = curve_fit(generate_decay, x_data, y_data)

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, generate_decay(x_data, popt[0], popt[1]))
plt.show()
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
# NOTE
from scipy.optimize import curve_fit
# NOTE

def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude * np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)


# Here I build the data
x_data = np.linspace(0,100,100)
y_data = np.random.normal(0, 5, len(x_data)) + build_gaussian(x_data, 1, 50, 4, 100)
plt.plot(x_data, y_data, 'o')

# Here I make some guesses
# First I say that the offset is close to the minimum of the data
# Then I use the argmax command the return the position of the maximum value and assume this is the centre of the gaussian
# The I can easily guess the sigma so I set my guess to 1, why not
# The I say the amplitude is the maximum value of the data
# Very simple guesses
guess = [np.min(y_data), np.argmax(y_data), 1, np.max(y_data)]

# Then I give the curve fit command the fitting function I want, the data and my guesses
popt, pcov = curve_fit(build_gaussian, x_data, y_data, p0=np.asarray(guess))

fitted_data = build_gaussian(x_data, popt[0], popt[1], popt[2], popt[3])

plt.plot(x_data, fitted_data)
plt.show()

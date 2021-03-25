import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
# NOTE
from scipy.optimize import curve_fit
# NOTE

def build_gaussian(x_data, amplitude, power):
    y_val = amplitude * x_data**power
    return(y_val)


# Here I build the data
x_data = np.linspace(0, 20, 100)
y_data = build_gaussian(x_data, 10, 1.5) + np.random.normal(0, 20, len(x_data))
plt.plot(x_data, y_data, 'o')

data = np.vstack((x_data, y_data))

np.savetxt('Power_data.csv', data.T, delimiter=',')
# Here I make some guesses
# First I say that the offset is close to the minimum of the data
# Then I use the argmax command the return the position of the maximum value and assume this is the centre of the gaussian
# The I can easily guess the sigma so I set my guess to 1, why not
# The I say the amplitude is the maximum value of the data
# Very simple guesses

guess = [10, 1]

# Then I give the curve fit command the fitting function I want, the data and my guesses
popt, pcov = curve_fit(build_gaussian, x_data, y_data, p0=np.asarray(guess))

print(popt)
fitted_data = build_gaussian(x_data, popt[0], popt[1])

plt.plot(x_data, fitted_data)
plt.text(0, np.max(fitted_data), "the power is " + "%1.3f" %(popt[1]))
plt.show()

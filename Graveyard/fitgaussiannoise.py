import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
# NOTE
from scipy.optimize import curve_fit
from scipy.stats import poisson
# NOTE
import time

def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude * np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)

def noiseadder(y_data, noise_level):
    read_noise = np.random.normal(100, noise_level, size=np.shape(y_data))
#    shot_noise = np.random.poisson(y_data)
    shot_noise = 0 #np.random.normal(0, y_data)
    return(y_data+read_noise+shot_noise)


my_data = np.zeros((2,500))
x_data = np.linspace(0,100,100)
y_data = build_gaussian(x_data, 1, 50, 4, 300)

#This is the read noise level
start = time.time()
for noise_level in range(1, 500):
    #This generates my gaussian
    # This adds noise to the gaussian, read and shot
    y_data = noiseadder(y_data, noise_level/100)
    # My fit guess.
    guess = [np.min(y_data), np.argmax(y_data), 1, np.max(y_data)]
    # Then I give the curve fit command the fitting function I want, the data and my guesses
    popt = curve_fit(build_gaussian, x_data, y_data, p0=np.asarray(guess))[0]
    my_data[1, noise_level] = popt[1]
    my_data[0, noise_level] = noise_level
end = time.time()
print(end-start)
#fit_value = np.asarray(fit_value)
#noise_value = np.asarray(noise_value)


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter

def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude * np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)


noise_array = np.linspace(0, 10, 100)
x_data = np.linspace(0, 100, 100)

fitted = np.zeros((2, 100))
hold_data = noise_array

for indy, noise in enumerate(noise_array):
    gdata = build_gaussian(x_data, 10, 50, 5, 100)
    gdata = gdata + np.random.normal(0, noise, np.shape(x_data))
    guess = [np.min(gdata), np.argmax(gdata), 1, np.max(gdata)]
    hold_data = np.vstack((hold_data, gdata))
    popt, pcov = curve_fit(build_gaussian, x_data, gdata, p0=np.asarray(guess))
    fitted[0, indy] = noise
    fitted[1, indy] = popt[1]

hold_data = hold_data.T
temp = np.hstack((np.asarray(0), noise_array))
print(np.shape(temp))
print(np.shape(hold_data))
x_data = np.hstack((np.asarray(0), x_data))
hold_data = np.vstack((x_data, hold_data))
print(np.shape(hold_data))

np.savetxt('problem_data1.csv', hold_data, delimiter=',')

#savgol_filter(np.abs(50-fitted[1, :]), 11, 1)
#plt.plot(fitted[0, :], savgol_filter(np.abs(50-fitted[1, :]), 11, 1))
#plt.show()
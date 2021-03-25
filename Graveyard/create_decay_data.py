import numpy as np
import matplotlib.pyplot as plt


def exponetial_decay(x_data, amplitude, decay_const):
    Y_data = amplitude * np.exp(x_data * decay_const)
    return(Y_data)

def add_noise(data):
    noise_data = np.random.poisson(data, np.shape(data))
    return noise_data

x = np.linspace(0,100,100)
Y_data = exponetial_decay(x, 1, 1)
plt.plot(x, Y_data)
plt.show()
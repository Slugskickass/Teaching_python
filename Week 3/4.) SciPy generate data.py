import numpy as np
import scipy
import matplotlib.pyplot as plt

def generate_data(gradient, offset, start, stop, noise, number_of_points):
    x = np.linspace(start, stop, number_of_points)
    y = (gradient * x) + offset
    noise = np.random.normal(0, noise, size=np.shape(x))
    final_data = y + noise
    return x, final_data

# Generate some data
gradient = 2
offset = 3
noise_level = 4
number_of_points = 100
start = 0
stop = 10

my_x_data, my_y_data = generate_data(gradient, offset, start, stop, noise_level, number_of_points)
plt.plot(my_x_data, my_y_data)
plt.show()

np.save('My_noisy_data', np.vstack([my_x_data, my_y_data]).T)  # NOTICE the .T
import numpy as np
import scipy
import matplotlib.pyplot as plt

def generate_data(gradient, offset, start, stop, noise, number_of_points):
    x = np.linspace(start, stop, number_of_points)                      # Produce linear data from start to stop
    y = (gradient * x) + offset                                         # Use y = mx +c to make some linear data
    noise = np.random.normal(0, noise, size=np.shape(x))                # Make some noise
    final_data = y + noise                                              # Add some noise
    return x, final_data                                                # return the x and y values

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
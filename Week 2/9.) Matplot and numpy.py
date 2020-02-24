import numpy as np                              # Loads in the numpy library
import matplotlib.pyplot as plt                 # Loads in the matplotlib library

x_data = np.linspace(0, 2 * np.pi, 100)         # The linspace function produces an array with
                                                # equally spaced data between the start and the stop values
                                                # np.linspace(start, stop, number of points (size of returned array))

                                                # So we now have 100 points between 0 and 2 pi stored in the array x_data
y_data = np.sin(x_data)                         # The array y_data holds the sine values for the data in x_data

plt.plot(x_data, y_data)                        # Here we plot the x_data against the y_data
plt.show()                                      # Finally we use plt.show() to present the data
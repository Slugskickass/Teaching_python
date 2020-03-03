import numpy as np
import matplotlib.pyplot as plt

my_data = np.zeros(100, np.float)                   # Build a 1D array of zeros
my_data[30:60] = 1                                  # Set the middle section to 1,
                                                    # We have built a top hat function

plt.plot(my_data)                                   # Show the data
plt.show()


my_data_diff = np.diff(my_data, 1)                  # Differentiate the data
plt.plot(my_data_diff)                              # Show the data
plt.show()

my_data_inital_event = np.clip(my_data_diff, a_min=0, a_max=2)  # only show the initial turn on event
plt.plot(my_data_inital_event)                      # Show the data
plt.show()
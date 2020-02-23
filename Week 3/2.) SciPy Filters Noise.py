import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter              #notice this


my_data = np.zeros(100, np.float)                   # Build a 1D array of zeros
my_data[30:60] = 1                                  # Set the middle section to 1,
                                                    # We have built a top hat function

np.random.seed(0)
noise = np.random.normal(0, 0.3, size=np.shape(my_data))
final_data = my_data + noise
plt.plot(final_data)
plt.title('Original Noisy Data')
plt.show()


my_data_diff = np.diff(final_data)                  # Differentiate the data
plt.plot(my_data_diff)                              # Show the data
plt.title('Differentiated Noisy Data')
plt.show()


smoothed_data = savgol_filter(final_data, 11, 1)
plt.plot(smoothed_data)                             # Show the data
plt.title('Smoothed Noisy Data')
plt.show()


smoothed_data_diff = np.diff(smoothed_data)          # Differentiate the data
plt.plot(smoothed_data_diff)                         # Show the data
plt.title('Differentiated smoothed  Noisy Data')
plt.show()

re_smoothed_data_diff = savgol_filter(smoothed_data_diff, 11, 1)        # Differentiate the data
plt.plot(re_smoothed_data_diff)                         # Show the data
plt.title('Differentiated Smoothed Differentiated Noisy Data')
plt.show()

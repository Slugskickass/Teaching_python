import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter              #notice this


my_data = np.zeros(100, np.float)                   # Build a 1D array of zeros
my_data[30:60] = 1                                  # Set the middle section to 1,
                                                    # We have built a top hat function

np.random.seed(0)                                   # now we are going to add random noise
                                                    # The seed command allows us set a seed for the random numbers
                                                    # Generated later, this way we can always use the same random numbers
noise = np.random.normal(0, 0.03, size=np.shape(my_data))
                                                    # np.random.normal gives us a normal distrobution of numbers
                                                    # around 0 with a std dev of 0.3.  We ask for the same number of
                                                    # numbers as in my_data
final_data = my_data + noise                        # We add the noise to the clean data
plt.plot(final_data)
plt.title('Original Noisy Data')
plt.show()


my_data_diff = np.diff(final_data)                  # Differentiate the data
plt.plot(my_data_diff)                              # Show the data
plt.title('Differentiated Noisy Data')
plt.show()


smoothed_data = savgol_filter(final_data, 11, 1)    # We use a Savitzky-Golay filter from SCIPY here
                                                    # we use a window of 11 data points and a polynomail order of 1
plt.plot(smoothed_data)                             # Show the data
plt.title('Smoothed Noisy Data')
plt.show()


smoothed_data_diff = np.diff(smoothed_data)          # Differentiate the data
plt.plot(smoothed_data_diff)                         # Show the data
plt.title('Differentiated smoothed  Noisy Data')
plt.show()

re_smoothed_data_diff = savgol_filter(smoothed_data_diff, 11, 1)        # Differentiate the data
plt.plot(re_smoothed_data_diff)                                         # Show the data
plt.title('Differentiated Smoothed Differentiated Noisy Data')
plt.show()


#Uncomment this to show the effect of multiple window lengths

for I in range(3,21,2):
    re_smoothed_data_diff = savgol_filter(smoothed_data_diff, I, 1)        # Differentiate the data
    plt.plot(re_smoothed_data_diff)                         # Show the data
plt.title('Multiple smoothing')
plt.show()


# More can be found at
#https://docs.scipy.org/doc/scipy/reference/signal.html
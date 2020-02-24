import numpy as np
import matplotlib.pyplot as plt

price_data = np.load('../Week 2/Data/stock_price.npy')          # Load the data
new_data = np.diff(price_data[:, 1])                            # Differentiate the data

my_bins=np.arange(-2, 2, 0.05)                                  # Define some bins
plt.hist(new_data, bins=my_bins)                                # Plot the histogram
plt.show()                                                      # show it
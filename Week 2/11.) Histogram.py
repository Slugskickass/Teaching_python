import numpy as np
import matplotlib.pyplot as plt

price_data = np.load('../Week 2/Data/stock_price.npy')
new_data = np.diff(price_data[:, 1])

plt.hist(new_data)
plt.show()
my_bins=np.arange(-2, 2, 0.05)
plt.hist(new_data, bins = my_bins)
plt.show()
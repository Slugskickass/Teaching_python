import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter

events = pd.read_pickle("events.pkl")

x_data = np.asarray(events['X_pos_major'] + events['X_pos'])
y_data = np.asarray(events['Y_pos_major'] + events['Y_pos'])

plt.plot(x_data, y_data, '.')
plt.show()

# out = plt.hist2d(x_data, y_data, bins=200)[0]
# out = gaussian_filter(out, sigma=5)
# plt.imshow(out, cmap='gray',vmin=0, vmax=0.0001)
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
#Here I just load the data
data_one = np.genfromtxt('../Data/stock_px.csv', delimiter=',')
#However the data is in the format date, price, price, price, price.  I know this before hand
# so I remove the first row and first column, leaving me with just the price data
data_one = data_one[1:, 1:5]
# Then I reload the data ignoring all but the date data and tell python that it is date data
data_two = np.loadtxt('../Data/stock_px.csv', delimiter=',', skiprows=1, dtype=np.datetime64, usecols=0)
#Save the data
np.save('../Data/stock_date', data_two)
np.save('../Data/stock_price', data_one)
# Now we can plot it
plt.plot(data_two, data_one[:, 0], 'r', label = 'Apple')
plt.plot(data_two, data_one[:, 1], 'g', label = 'Microsoft')
plt.plot(data_two, data_one[:, 2], 'b', label = 'Exxon Mobile')
plt.plot(data_two, data_one[:, 3], 'm', label = 'SP 500')
plt.legend(loc='upper left')
plt.show()
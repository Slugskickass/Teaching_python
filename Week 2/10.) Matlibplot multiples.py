import numpy as np
import matplotlib.pyplot as plt
import os
date_data = np.load('../Week 2/Data/stock_date.npy')
price_data = np.load('../Week 2/Data/stock_price.npy')

fig = plt.figure()
apple_data = fig.add_subplot(2, 2, 1)
plt.plot(date_data, price_data[:, 0])

Microsoft_data = fig.add_subplot(2, 2, 2)
plt.plot(date_data, price_data[:, 1],'.')

Exxon_data = fig.add_subplot(2, 2, 3)
plt.plot(date_data, price_data[:, 2],'-.')

SP_data = fig.add_subplot(2, 2, 4)
plt.plot(date_data, price_data[:, 3])

SP_data.tick_params(axis ='x', rotation = 45)
Exxon_data.tick_params(axis ='x', rotation = 45)
Microsoft_data.tick_params(axis ='x', rotation = 45)
apple_data.tick_params(axis ='x', rotation = 45)


apple_data.set_title('Apple)')
Microsoft_data.set_title('Microsoft)')
Exxon_data.set_title('Exxon)')
SP_data.set_title('SP 500')
plt.show()

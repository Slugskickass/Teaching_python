import numpy as np
import matplotlib.pyplot as plt

date_data = np.load('../Week 2/Data/stock_date.npy')            # Load a numpy array with the dates the prices were recorded
price_data = np.load('../Week 2/Data/stock_price.npy')          # Load a numpy array with the values of companies

fig = plt.figure()                                              # This sets a canvas to add the data too
apple_data = fig.add_subplot(2, 2, 1)                           # To the canvas I add a space to hold a plot, this
                                                                # is known as a subplot
                                                                # Notice I associate this subplot with the name
                                                                # apple_data. This allows me to change attributes later
plt.plot(date_data, price_data[:, 0])                           # Plot the data

Microsoft_data = fig.add_subplot(2, 2, 2)
plt.plot(date_data, price_data[:, 1],'.')

Exxon_data = fig.add_subplot(2, 2, 3)
plt.plot(date_data, price_data[:, 2],'-.')

SP_data = fig.add_subplot(2, 2, 4)
plt.plot(date_data, price_data[:, 3],'r.')                      # Here I want red dots

apple_data.tick_params(axis='x', rotation=45)                   # Once I have set up my plots I can fine tune each subplt
SP_data.tick_params(axis='x', rotation=90)                      # I can change the angle of the x axis text
Exxon_data.tick_params(axis='x', rotation=45)
Microsoft_data.tick_params(axis='x', rotation=45)

apple_data.set_title('Apple')                                  # I can change the title for each subplot.
Microsoft_data.set_title('Microsoft')
Exxon_data.set_title('Exxon')
SP_data.set_title('SP 500')
plt.show()                                                      # This is important it presents the plot. Once this command
                                                                # Is issued you can change the plots.

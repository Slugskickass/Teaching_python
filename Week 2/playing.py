import numpy as np
import matplotlib.pyplot as plt

data_one = np.genfromtxt('Data/Apollo11.csv', delimiter=',')
plt.plot(data_one[:,0], data_one[:,1])
plt.show()

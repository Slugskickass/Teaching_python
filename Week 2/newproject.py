import matplotlib.pyplot as plt
import numpy as np

data_one = np.genfromtxt('Data/Apollo11.csv', delimiter=',')
print(np.shape(data_one))

plt.plot(data_one[: ,0], data_one[:, 1])
plt.ylabel('Acceleration m s^-2')
plt.xlabel('Time s')
plt.title('Apollo 11 Acceleration Graph')
plt.show()
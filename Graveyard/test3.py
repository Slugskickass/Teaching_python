import numpy as np
import matplotlib.pyplot as plt

gradient = 4
intercept = 5
x_data = np.linspace(0, 50, 5000)
y_data = intercept + (gradient * x_data)
y_data = y_data + np.random.normal(0, 10, np.shape(y_data))
final_data = np.vstack((x_data, y_data)).T
np.savetxt('linear_data.csv', final_data, delimiter=',')
plt.plot(x_data, y_data)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(0, 12, 24)

y1_data = np.exp(x_data)
y2_data = np.sin(x_data)

apple = plt.figure()
expon = apple.add_subplot(2, 1, 1)
plt.plot(x_data, y1_data)

sinon = apple.add_subplot(2, 1, 2)
plt.plot(x_data, y2_data)

expon.tick_params(axis='x', rotation=45)
expon.set_title('Expon')


plt.show()
import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
number_of_runs = 1000000
position = np.zeros([number_of_runs, 2])
position[0, 0] = 200
position[0, 1] = 200
for index in range(1, number_of_runs, 1):
    X = (2 * np.random.binomial(1, 0.5)) - 1
    Y = (2 * np.random.binomial(1, 0.5)) - 1
    position[index, 0] = position[index-1, 0] + X
    position[index, 1] = position[index - 1, 1] + Y
end = time.time()
print(end-start)
plt.plot(position[:, 0], position[:, 1])
plt.show()

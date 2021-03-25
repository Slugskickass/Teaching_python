import numpy as np
import matplotlib.pyplot as plt


def phi(x, y):
    if x == 0:
        if y > 0:
            return (np.pi / 2)
        if y < 0:
            return (3 * np.pi / 2)
        else:
            return (0)
    if y == 0:
        if x > 0:
            return (np.pi / 2)
        if x < 0:
            return (3 * np.pi / 2)
    a = np.arctan(y / x)
    return (a)


number_points = 100

hold_all = np.zeros((number_points, number_points))

valuesx = np.linspace(-np.pi, np.pi, number_points)
valuesy = np.linspace(-np.pi, np.pi, number_points)

for xindex, x in enumerate(valuesx):
    for yindex, y in enumerate(valuesy):
        hold_all[xindex, yindex] = phi(x, y)
plt.imshow(hold_all)
plt.show()

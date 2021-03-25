import matplotlib.pyplot as plt
import math
import numpy as np

# Constants
lam = 638 * 10 ** (-9)
L = 1
the = (10 * math.pi / (180))
a = (1 / (lam)) * np.sin(the)
kx = 2 * math.pi / (8 * 10 ** (-6)) * a


# Array assignment
# x = np.linspace(50*10**(-6), -50*10**(-6), 1000)
# y = np.linspace(50*10**(-6), -50*10**(-6), 1000)
# ind = range(0, 1001, 1)
# f = np.array([])

# Defining Cartesian phi conversion
def oldphi(x, y):
    if x == 0:
        print('x=0')
        if y > 0:
            return (np.pi / 2)
        if y < 0:
            return (3 * np.pi / 2)
        else:
            return (0)
    if y == 0:
        print('y=0')
        if x >= 0:
            return (0)
        if x < 0:
            return (np.pi)
    a = np.arctan(y / x)

    return (a)

def phi(x, y):
    return(np.arctan2(x, y))

# Creating an empty array for phi calculation, defining arrays.
number_points = 1000
hold_all = np.zeros((number_points, number_points))
valuesx = np.linspace(-50 * 10 ** (-6), 50 * 10 ** (-6), number_points)
valuesy = np.linspace(-50 * 10 ** (-6), 50 * 10 ** (-6), number_points)

# Enumerate pulls in x and y values and counts them for use in the function.
z = np.zeros(number_points)
for xindex, x in enumerate(valuesx):
    for yindex, y in enumerate(valuesy):
        hold_all[xindex, yindex] = phi(x, y)

# plt.show(hold_all)
# plt.show()

# Phase calculation
pha = (L * (hold_all) + kx * valuesx) % (2 * math.pi)

# Plotting as contour
fig = plt.figure()
conph = plt.contour(valuesx, valuesy, pha, 256, cmap='RdGy')
cbar = fig.colorbar(conph)
cbar.set_label('Phase')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().minorticks_on()
plt.show()
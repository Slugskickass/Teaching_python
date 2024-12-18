# Load and save files in numpy
import matplotlib.pyplot as plt
import numpy as np
# If you want to load and save data when working on a project this is a great way to save it,
# However it only stores the numbers and it is not easy to load in to different programs
my_array = np.random.rand(1, 10)
print(my_array)
np.save('my_saved_data', my_array)
data = np.load('my_saved_data.npy')
print(data)

# we can load data from a file
# This works well becasue it is clever enough to skip the headers
data_one = np.genfromtxt('Data/linear_data.csv', delimiter=',')
#This does not know how to skip rows so we have to tell it to skiprows
data_two = np.loadtxt('Data/Apollo11.csv', delimiter=',', skiprows=1)

print('The first line of the data')
print(data_one[0, 0:2])
print('The first line of the data')
print(data_two[0, 0:2])
#another useful function is this
import os
print(os.listdir())
#
# plt.plot(data_two[0:,0], (data_two[:,1]))
# plt.title('Apollo 11 Thrst')
# plt.xlabel('Time s')
# plt.ylabel('Acceleration')
# plt.show()

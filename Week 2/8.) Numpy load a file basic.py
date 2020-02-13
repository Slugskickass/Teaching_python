# Load and save files in numpy
import numpy as np
# If you want to load and save data when working on a project this is a great way to save it,
# However it only stores the numbers and it is not easy to load in to different programs
my_array = np.random.rand(1, 10)
print(my_array)
np.save('my_saved_data', my_array)
data = np.load('my_saved_data.npy')
print(data)

# we can load data from a file
# This works well becasue it is clever enough to ckip the headers
data_one = np.genfromtxt('Data/Apollo11.csv', delimiter=',')
#This does not know how to skip rows so we have to tell it to skiprows
data_two = np.loadtxt('Data/Apollo11.csv', delimiter=',', skiprows=2)

#another useful function is this
import os
print(os.listdir())

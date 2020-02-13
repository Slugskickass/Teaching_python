import numpy as np

#Build some arrays
# This builds a 1D array
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('The array is')
print(my_array)
print('Its size and shape are ')
print(np.size(my_array))
print(np.shape(my_array))
print()

# This builds a 2D array
my_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('The array is')
print(my_array)
print('Its size and shape are ')
print(np.size(my_array))
print(np.shape(my_array))

# We can build up a random array
my_random_array = np.random.rand(10, 10, 10)
print('The array is')
print(my_random_array)
print('Its size and shape are ')
print(np.size(my_random_array))
print(np.shape(my_random_array))

# We can define an array of ones or zeors.
# We can also set the data type
my_one_array = np.ones([2, 4], dtype=np.float64)
my_zero_array = np.zeros([2, 4, 7], dtype=np.int32)
import numpy as np

#Build some arrays
# This builds a 1D array
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])        # Here we define a 1D array
print('The array is')
print(my_array)                                         # Print the array
print('Its size and shape are ')
print(np.size(my_array))                                # Print the size of the array
print(np.shape(my_array))                               # Print the shape of the array
print()

# This builds a 2D array
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Make a 2D array
print('The array is')
print(my_array)
print('Its size and shape are ')
print(np.size(my_array))                                # Print the size of the array
print(np.shape(my_array))                               # Print the shape of the array
print()

# We can build up a random array
my_random_array = np.random.rand(10, 10, 10)            # This builds a 10 x 10 x 10 array of random numbers
print('The array is')
print(my_random_array)
print('Its size and shape are ')
print(np.size(my_random_array))
print(np.shape(my_random_array))                        # Print the shape of the array

# We can define an array of ones or zeors.
# We can also set the data type
my_one_array = np.ones([2, 4], dtype=np.float64)
my_zero_array = np.zeros([2, 4, 7], dtype=np.int32)


# Finally
# The linspace command produces a linear array of floating point numbers from start to end in n steps
#x_data = np.linspace(start, stop, n_numbers)
x_data = np.linspace(0, 1, 11)
print(x_data)
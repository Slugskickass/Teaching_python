import numpy as np

#Build two arrays
array_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])     # Build a 3 x3 array
print(np.shape(array_one))                                  # Print the shape of the array
print()
array_two = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])     # Build a 3 x3 array

temp = array_one * array_two                                # Multiply the arrays together, this is a item by item multiplication
print(temp)
print()

temp = array_one / array_two                                # Division
print(temp)
print()

temp = array_one + array_two                                # Addition
print(temp)
print()

temp = array_one - array_two                                # Subtractions
print(temp)
print()

temp = array_one > array_two                                # Comparison between the two array
print(temp)
print()

print('Average ', np.average(array_two))
print('Max ', np.max(array_two))
print('Max along an axis', np.max(array_two, axis=0))       # Note the use of the Axis command

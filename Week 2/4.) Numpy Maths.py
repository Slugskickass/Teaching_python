import numpy as np

#Build two arrays
array_one = np.array([[ 1,2,3],[4,5,6],[7,8,9]])
print(np.shape(array_one))
array_two = np.array([[ 3,2,1],[4,5,6],[9,8,7]])

temp = array_one * array_two
print(temp)
print()

temp = array_one / array_two
print(temp)
print()

temp = array_one + array_two
print(temp)
print()

temp = array_one - array_two
print(temp)
print()

temp = array_one > array_two
print(temp)
print()

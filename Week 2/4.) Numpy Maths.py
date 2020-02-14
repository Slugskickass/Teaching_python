import numpy as np

#Build two arrays
array_one = np.array([[ 1,2,3],[4,5,6],[7,8,9]])
print(np.shape(array_one))
array_two = np.array([[ 3,2,1],[6,5,4],[9,8,7]])

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

print('Average ', np.average(array_two))
print('Max ', np.max(array_two))
print('Max along an axis', np.max(array_two, axis=0))

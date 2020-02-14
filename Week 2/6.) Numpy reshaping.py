import numpy as np

#Build an array
array_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Change its shape
new_array = array_one.reshape([1, 9])
print(new_array)

new_array = np.reshape(new_array, [1, 9])
print(new_array)


#Transpose the array
print(array_one.T)
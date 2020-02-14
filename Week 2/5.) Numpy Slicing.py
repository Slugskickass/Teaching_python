import numpy as np

#Build an array
array_one = np.array([[ 1,2,3],[4,5,6],[7,8,9]])

# Select a specific part of an array

print(array_one[1, 1])       # select the center remember python starts indexing at 0

print(array_one[1, :])       # Print the centre row

print(array_one[:, 1])       # Print the centre column

x = [0, 2]
print(array_one[x,:])       # Print the top and bottom rows


array_two = np.random.rand(10,10)
print(array_two)
print()
print(array_two[3:6, 7:9])
print()
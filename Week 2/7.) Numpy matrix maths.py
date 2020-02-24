import numpy as np

array_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector_one = np.array([1, 2, 3])
outa = np.matmul(array_one, vector_one)     # The matrix multiplication
print(outa)


print('Diagonal ', np.diag(array_one))      # Diagonalise a matrix
print(array_one.T)

array_one = np.array([[1, 1], [1, 1]])
array_two = np.array([[2, 0], [0, 2]])
print(array_one)
print(np.shape(array_one))
print(array_one * array_two)
print(np.matmul(array_one, array_two))


#Vector
print(np.dot(vector_one, vector_one))
print(np.cross(vector_one, vector_one))

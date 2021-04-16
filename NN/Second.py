import torch
import numpy as np

my_data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print(my_data)
print(type(my_data))
print(my_data[1][1])

my_array = np.asarray(my_data)
print(my_array)
print(type(my_array))
print(my_array[1, 1])  #Note

my_tensor = torch.tensor(my_array)
print(my_tensor)
print(type(my_tensor))
print(my_tensor[1, 1])


print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.layout)

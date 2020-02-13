import numpy as np
number = 100
length_needed = int(np.sqrt(number))+1
divisor = np.asarray(range(2, length_needed))
out = np.mod(number, divisor)
test = np.max(out == 0)
print('Is a prime number? ', not(test))


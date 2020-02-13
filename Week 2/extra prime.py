#Look no for loop

import numpy as np
number = 10368721
divisor = np.asarray(range(2, int(np.sqrt(number))+1))
out = np.mod(number, divisor)
print('Is a prime number? ', not(np.max(out == 0)))


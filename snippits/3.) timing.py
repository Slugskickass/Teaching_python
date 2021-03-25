import time
import numpy as np

print('The time in seconds', time.time())
print('The time converted to teal world', time.ctime())


# Time a function
number = 100
hold = np.zeros(number)
for looper in range(number):
    start = time.time()
    test = np.random.poisson(10, 1000)
    end = time.time()
    hold[looper] = end-start
print(np.mean(hold))
print(np.std(hold))
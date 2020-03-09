from multiprocessing import Pool
import numpy as np
import time

def f(x):
    return np.sort(x)

if __name__ == '__main__':
    number_runs =100000
    list_numbers = []
    for I in range(number_runs):
        list_numbers.append(np.random.normal(0, 1, 10))
    start = time.time()
    with Pool(20) as p:
        out = (p.map(f, list_numbers))
    end = time.time()
    print('par', end - start)

    start = time.time()
    out = []
    for I in range(number_runs):
        out.append(f(list_numbers[I]))
    end = time.time()
    print('ser', end - start)

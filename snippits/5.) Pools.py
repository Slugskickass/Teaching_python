from multiprocessing import Pool
import numpy as np
import time

def fox(x):
    return np.sort(x)

if __name__ == '__main__':
    number_runs = 1000
    list_numbers = []
    for I in range(number_runs):
        list_numbers.append(np.random.normal(0, 1, 1000))


    start = time.time()
    with Pool(4) as p:
        out = (p.map(fox, list_numbers))
    end = time.time()
    print('par', end - start)

    out = []
    start = time.time()
    for I in range(number_runs):
        out.append(fox(list_numbers[I]))
    end = time.time()
    print('ser', end - start)

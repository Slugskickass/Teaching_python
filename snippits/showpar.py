import numpy as np
from scipy import stats # is this pure python or not
import multiprocessing
from multiprocessing import get_context
import time


def new_fit(line_data):
    x = np.linspace(0, np.size(line_data, axis=0), np.size(line_data, axis=0))
    out = stats.linregress(x, line_data)[0]
    return out



if __name__ == '__main__':
    print("Number of cpu : ", multiprocessing.cpu_count())
    fdata = np.load('test_data.npy')

    number_points = 200000

    fdata = fdata[0:number_points, :]


    start = time.time()
    with get_context("spawn").Pool() as pool:
        final_data = pool.map(new_fit, fdata)
    end = time.time()
    print('Par', end - start)

    out = []
    start = time.time()
    for I in range(np.shape(fdata)[0]):
        out.append(new_fit(fdata[I, :]))
    end = time.time()
    print('Ser', end - start)


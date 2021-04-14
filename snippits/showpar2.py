import numpy as np
from scipy import stats # is this pure python or not
from multiprocessing import Pool
import multiprocessing
from multiprocessing import get_context
import time
import matplotlib.pyplot as plt

def new_fit(line_data):
    x = np.linspace(0, np.size(line_data, axis=0), np.size(line_data, axis=0))
    out = stats.linregress(x, line_data)[0]
    return out

def do_fit(data):
    print(np.shape(data))
    start = time.time()
    with get_context("spawn").Pool() as pool:
        final_data = pool.map(new_fit, data)
    end = time.time()
    Par_time = end - start

    out = []
    start = time.time()
    for I in range(np.shape(data)[0]):
        out.append(new_fit(data[I, :]))
    end = time.time()
    Ser_time = end - start
    return Par_time, Ser_time

def plotdata(Num, Par, Ser):
    plt.plot(Num, Par, label='Par')
    plt.plot(Num, Ser, label='Ser')
    plt.legend()
    plt.show()

data = np.load('test_data.npy')
Par = []
Ser = []
Num = []
if __name__ == '__main__':
    for number_points in range(100, 100000, 1000):
        Par_time, Ser_time = do_fit(data[0:number_points, :])
        Par.append(Par_time)
        Ser.append(Ser_time)
        Num.append(number_points)



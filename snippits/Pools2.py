import numpy as np
from scipy import stats
import time
from multiprocessing import Pool

def fitter(y_data):
    # Simple self contained fitting function, one input
    x_data = np.linspace(0, len(y_data), len(y_data))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
    return(slope)

#Build the data, for a pool command we need to put all our data in a single block
hold_data =[]
number_points = 100
number_runs = 10
for position in range(number_runs):
    # This loop build a list of arrays to be fitted
    x_sent = np.linspace(0, number_points, number_points)
    m = 10 * np.random.random()
    y_data = m * x_sent + np.random.normal(0, 10, len(x_sent))
    hold_data.append(y_data)


pool = Pool(processes=10)                           # Start the pool of processes
start = time.time()                                 # Start time
final_hold_a = pool.map(fitter, hold_data)          # Send the data to the function
print(time.time() - start)                          # End time


store_hold = []
start = time.time()
for I in range(number_runs):
    y_data = hold_data[I]
    slope = fitter(y_data)
    store_hold.append(slope)
print(time.time() - start)

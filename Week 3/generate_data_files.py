import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def build_gaussian(x_data, offset, xo, sigma, amplitude):
    y_val = offset + amplitude * np.exp((-1 * (xo-x_data)**2)/sigma**2)
    return(y_val)

x_data = np.linspace(-50,200,2000)
noise = np.random.normal(0, .05, 2000)
for I in range(10):
    y_data = build_gaussian(x_data, 0, 20+(I*5) + np.random.normal(0, 2, 1), 4+(I*5), 1) + noise
    my_array = np.vstack((x_data, y_data))
    file_name = str(I) + '.csv'
    pd.DataFrame(np.transpose(my_array)).to_csv(file_name)


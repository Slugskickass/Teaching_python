import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
datafile = ('../Week 3/Data/spacex_launch_data.csv')

data = pd.read_csv(datafile)
print(data.columns.values)

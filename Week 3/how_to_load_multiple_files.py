import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

def get_file_list(dir):
    #dir = '/Volumes/Samsung_T3/Olivias/CMOS PTC/'
    file_list = []
    for file in os.listdir(dir):
        if file.endswith(".csv"):
            file_name = dir + '/' +file
            file_list.append(file_name)
    return file_list


def snowflake(file_name):
    data_one = np.genfromtxt(file_name, delimiter=',')
    x_data = data_one[:, 0]
    y_data = data_one[:, 1]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
    return (slope, intercept)


files = get_file_list('Data')

for my_file in files:
#    my_file  =  'Data/linear_data.csv'

    slopy_mc_slope_face, intercepr_mc_intercept_face = snowflake(my_file)

    print(slopy_mc_slope_face)
    print(intercepr_mc_intercept_face)


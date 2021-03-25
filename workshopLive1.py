import pandas as pd
import matplotlib.pyplot as plt
import os

os.path.exists

data_frame = pd.read_csv('/Users/Ashley/PycharmProjects/teaching_python/Introduction/2019.csv')

print(data_frame.shape)

print(data_frame.columns)

print(data_frame.dtypes)

print(data_frame.head())

print(data_frame.index)
# There are many ways to manipulate Pandas data frames
PT_data =  data_frame['Country or region']=='Portugal'
# This returns a list of true or false
# We can use this to select the parts of the data frame we are interested in
PT_data = data_frame[data_frame['Country or region']=='Portugal']



pd.re




url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
virus_data = pd.read_csv(url)





dir_t = 'Data_Gauss'

# When we saved the data we labelled each data file with a number 0 to 9
# so we can use that knowledge to build up the file path for the data
file_number = str(0)
# Here we have made a variable called file_number which is a string representation of a number

file_ending = '.csv'
# We know that the file is a csv file so will end with .csv.

# Now we make the total file name as

file_name = dir_t + '/' + file_number + file_ending
print(file_name)


# we can now load the data using numpy
import numpy as np
data = np.genfromtxt(file_name,skip_header=1, delimiter=',')
print(np.shape(data))



import os
def getfiles(mydir):
    files = []
    for file in os.listdir(mydir):
        if file.endswith(".csv"):
            files.append((os.path.join(mydir, file)))
    return files



my_files = (getfiles(dir_t))
for item in my_files:
    print(item)
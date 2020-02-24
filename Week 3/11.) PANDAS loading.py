import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

flight_data = pd.read_csv('Data/spacex_launch_data.csv')
print(flight_data.columns)
print(flight_data['Flight Number'], flight_data['Payload'], flight_data['Customer'])



kilo_data = []
for I in range(10):
    temp = (flight_data['Payload Mass (kg)'][I])
#    print(type(temp))
    if isinstance(temp, str):
        temp = temp.replace('\xa0', '')
        temp = temp.replace(',', '')
        kilo_data.append((np.float(temp)))

plt.hist(np.asarray(kilo_data))
plt.show()
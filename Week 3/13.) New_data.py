import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

virus_data = pd.read_csv('Data/covid_19_clean_complete.csv')
print(virus_data.columns)

#for I in range(5000):
#    virus_data['Date'][I] = datetime.strptime(virus_data['Date'][I], '%m/%d/%y')

#for I in range(10):
#    start_date = virus_data['Date'][0]
#    end_date = start_date + timedelta(days=1)

#mask = (virus_data['Date'] > start_date) & (virus_data['Date'] <= end_date)
date_list = virus_data.Date.unique()
Total = np.zeros(len(date_list))
for index, date in enumerate(date_list):
    mask = (virus_data['Date'] == date)
    out = virus_data.loc[mask]
    Total[index] = out['Confirmed'].sum()

plt.plot(Total)
plt.show()


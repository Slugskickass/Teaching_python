import StormUtils as ST
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

#file_name = 'sequence.tif'
file_name = '/Users/ashleycadby/Data/sequence.tif'
data = ST.loadtiffs(file_name)

old_settings = np.seterr(all='ignore')

allx_positions = 0
ally_positions = 0
cut_size = 5

xdata = ST.buildxfit()
columns = ['Event Number', 'Frame', 'X_pos_major', 'Y_pos_major', 'X_pos', 'Y_pos', 'X_width', 'Y_width', 'offset', 'Amplitude']
events = pd.DataFrame([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], columns=columns)

event_number = 0
for frame_number in range(np.shape(data)[2]):
    current_frame = data[:, :, frame_number]

    filterd_data = ST.filter_data(current_frame)

    x_pos, y_pos = ST.regionfilter(filterd_data)

    x_pos_corr, y_pos_corr = ST.filteredges(cut_size, x_pos, y_pos, np.shape(current_frame)[0], np.shape(current_frame)[1])

    temp_array = ST.returnregions(current_frame, x_pos_corr, y_pos_corr, cut_size)

    for index, item in enumerate(temp_array):
        p0 = (cut_size, cut_size, 2, 2, np.min(item), item[5, 5])
        try:
            popt, pcov = curve_fit(ST._gaussian, xdata, item.ravel(), p0, bounds=((1, 1, 1, 1, 300, 300), (11, 11, 5, 5, 1000, 3000)))
            df = pd.DataFrame([[event_number, frame_number, int(np.floor(x_pos_corr[index])), int(np.floor(y_pos_corr[index])), popt[0], popt[1], popt[2], popt[3], popt[4], popt[5]]], columns=columns)
            events = events.append(df)
            event_number = event_number + 1
        except:
            print('Error')

    allx_positions = np.append(allx_positions, x_pos_corr)
    ally_positions = np.append(ally_positions, y_pos_corr)

plt.plot(np.asarray(allx_positions), np.asarray(ally_positions), 'r.')
plt.show()
events.to_pickle("events.pkl")






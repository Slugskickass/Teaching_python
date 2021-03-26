import StormUtils as ST
import matplotlib.pyplot as plt
import numpy as np


file_name = '/Volumes/Samsung_T3/sequencesmall.tif'

data = ST.loadtiffs(file_name)

allx_positions = 0
ally_positions = 0

for frame_number in range(np.shape(data)[2]):
    current_frame = data[:, :, frame_number]

    filterd_data = ST.filter_data(current_frame)

    x_pos, y_pos = ST.regionfilter(filterd_data)

    allx_positions = np.append(allx_positions, x_pos)
    ally_positions = np.append(ally_positions, y_pos)

plt.plot(np.asarray(allx_positions), np.asarray(ally_positions),'r.')
plt.show()



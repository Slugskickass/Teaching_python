import StormUtils as ST
import matplotlib.pyplot as plt
import numpy as np


file_name = '/Volumes/Samsung_T3/sequencesmall.tif'

data = ST.loadtiffs(file_name)

allx_positions = 0
ally_positions = 0
cut_size = 5
main_image_store = np.zeros((0, (cut_size*2)+1, (cut_size*2)+1))
counter = 0
for frame_number in range(np.shape(data)[2]):
    current_frame = data[:, :, frame_number]

    filterd_data = ST.filter_data(current_frame)

    x_pos, y_pos = ST.regionfilter(filterd_data)

    x_pos_corr, y_pos_corr = ST.filteredges(cut_size, x_pos, y_pos, np.shape(current_frame)[0], np.shape(current_frame)[1])

    temp_array = ST.returnregions(current_frame, x_pos_corr, x_pos_corr, cut_size)

    main_image_store = np.append(main_image_store, temp_array, axis=0)

    # Fit each block that has been cut out.

    # Store, event number, frame, x_pos_corr and y_pos_corr.
    # Fitted, X, Y, Xsigma, Ysigma, offset, and the ampltitude


    allx_positions = np.append(allx_positions, x_pos_corr)
    ally_positions = np.append(ally_positions, y_pos_corr)

    counter = counter + 1
plt.plot(np.asarray(allx_positions), np.asarray(ally_positions), 'r.')
plt.show()

event = 101

print(allx_positions[event])
print(ally_positions[event])
plt.imshow(main_image_store[event,:,:])
plt.show()







from PIL import Image
import numpy as np


def loadtiffs(file_name):
    img = Image.open(file_name)
    print('The Image is', img.size, 'Pixels.')
    print('With', img.n_frames, 'frames.')

    imgArray = np.zeros((img.size[1], img.size[0], img.n_frames), np.uint16)
    for I in range(img.n_frames):
        img.seek(I)
        imgArray[:, :, I] = np.asarray(img)
    img.close()
    return(imgArray)

def savetiffs(file_name, data):
    images = []
    for I in range(np.shape(data)[2]):
        images.append(Image.fromarray(data[:, :, I]))
        images[0].save(file_name, save_all=True, append_images=images[1:])
        #For a single image
        #images[0].save(file_name)

#Use the functions
file_name = '/Users/Ashley/PycharmProjects/teaching_python/Week 2/Data/640.tif'
data_images = loadtiffs(file_name)
savetiffs('out.tiff', data_images)



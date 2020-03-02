import numpy as np


class masters(object):
    def __init__(self, data):
        self.data_size = np.shape(data)
        self.data = data

    def transpose(self):

        return(self.data.T)

def main():
   outer = np.zeros((100, 110))
   test_data = masters(outer)
   print(test_data.data_size)
   outer = test_data.transpose()
   print(np.shape(outer))

if __name__ == "__main__":
    main()
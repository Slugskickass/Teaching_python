import numpy as np


class masters(object):
    def __init__(self, data):
        self.data_size = np.shape(data)
        self.data = data

    def transpose(self):

        return(self.data.T)

def main():
   outer = np.zeros((100, 110))
   raj = masters(outer)
   print(raj.data_size)
   outer = raj.transpose()
   print(np.shape(outer))

   outer = np.zeros((12, 12))
   dylan = masters(outer)
   print(dylan.data)

if __name__ == "__main__":
    main()
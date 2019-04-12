import numpy as np

def convert(arr):
    arr.setflags(write=1)
    for i,j in np.ndindex(arr.shape[:2]):
        avg = np.sum(arr[i,j])/3
        arr[i, j] = avg
    return arr

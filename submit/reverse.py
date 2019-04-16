import numpy as np

def convert(arr):
    arr.setflags(write=1)
    for i,j in np.ndindex(arr.shape[:2]):
        arr[i,j,0] = 255 - arr[i,j,0]
        arr[i,j,1] = 255 - arr[i,j,1]
        arr[i,j,2] = 255 - arr[i,j,2]
    return arr

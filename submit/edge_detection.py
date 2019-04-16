import numpy as np

def convert(arr):
    result = np.zeros(arr.shape)
    def inRange(i,j):
        return i>=0 and j>=0 and i<arr.shape[0] and j<arr.shape[1]
    def different(px1, px2):
        totalDiff = 0
        for i in range(3):
            totalDiff += abs(int(px1[i])-int(px2[i]))
        return totalDiff > 75
    for i,j in np.ndindex(arr.shape[:2]):
        for row in range(i-1, i+2):
            for col in range(j-1, j+2):
                if inRange(row, col) and different(arr[row,col], arr[i,j]):
                    result[i,j] += arr[i,j]

    return result

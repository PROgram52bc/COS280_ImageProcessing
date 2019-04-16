import numpy as np

def convert(arr, targets=[[255,105,180], [255,20,147], [220,20,60], [15,1,1]]):
    def different(px):
        for target in targets:
            totalDiff = 0
            for i in range(3):
                totalDiff += abs(int(px[i])-int(target[i])) * (np.sum(target)//3) / target[i] 
            if totalDiff < 200:
                return False
        return True

    arr.setflags(write=1)
    for i,j in np.ndindex(arr.shape[:2]):
        if different(arr[i,j]):
            arr[i,j] = np.sum(arr[i,j])/3
    return arr

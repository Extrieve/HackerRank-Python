import numpy as np

def nearlySimilarRectangles(sides):
    # Write your code here
    sides = np.array(sides, dtype=int32)
    similar = 0
    loopie = len(sides)
    for i in range(loopie):
        for j in range(i+1, loopie):
            if(sides[i][0]/sides[j][0] == sides[i][1]/sides[j][1]):
                similar += 1
    return similar

print(nearlySimilarRectangles([[4,8], [15,30], [25,50]]))

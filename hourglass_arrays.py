import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



def hourglassSum(arr):
    # Write your code here
    highest = sum(test[0][:3]) + test[1][1] + sum(test[2][:3])
    for i in range(4):
        for j in range(4):
            hourglass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if(hourglass > highest):
                highest = hourglass

    return highest


kekW = [[1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]]

test = [[-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]]

#print(sum(test[0][:3])
#print(test[1][1])
#print(sum(test[0][:3]) + test[1][1] + sum(test[2][:3]))
print(hourglassSum(test))

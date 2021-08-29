#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def cutTheSticks(arr):
    # Write your code here
    sticks = []
    try:
        while max(arr) > 0:
            arr = [item-min(arr) for item in arr]
            print(arr)
            sticks_left = len(arr)
            sticks.append(sticks_left)
            arr = [item for item in arr if item > 0]
    except ValueError:
        pass

    return sticks


print(cutTheSticks([5, 4, 4, 2, 2, 8]))

# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    k = k % len(a)
    rotations = a[-k:] + a[:-k]
    return [rotations[i] for i in queries]


if __name__ == '__main__':
    print(circularArrayRotation([3, 4, 5], 2, [1, 2]))

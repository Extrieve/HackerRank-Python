import itertools
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#


def stones(n, a, b):
    # Write your code here
    return sorted(list({(n - i - 1) * a + i * b for i in range(n)}))


if __name__ == '__main__':
    print(stones(2, 1, 2))

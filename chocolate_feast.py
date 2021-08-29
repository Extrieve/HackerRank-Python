# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    bars = n // c
    wrapers = bars
    while wrapers >= m:
        extras = wrapers // m
        wrapers = (wrapers % m) + extras
        bars += extras
    return bars


if __name__ == '__main__':
    print(chocolateFeast(15, 3, 2))

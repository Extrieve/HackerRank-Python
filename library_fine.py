# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1 == y2:
        if m1 < m2:
            return 0
        elif m1 <= m2:
            if d1 <= d2:
                return 0
            else:
                return abs(d1 - d2) * 15
        else:
            late = abs(m2 - m1)
            return late * 500
    elif y1 < y2:
        return 0
    else:
        return 10_000


if __name__ == '__main__':
    print(libraryFine(28, 2, 2015, 15, 4, 2015))

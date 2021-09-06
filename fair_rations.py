import itertools

# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#


def fairRations(B):
    # Write your code here
    oddList = []
    operations = 0
    i = 0
    while True:
        if B[i] % 2 != 0:
            try:
                B[i] += 1
                B[i + 1] += 1
                operations += 2
                if B[i + 1] % 2 != 0:
                    oddList.append(i + 1)
            except IndexError:
                B[i] += 1
                B[i-1] += 1
                operations += 2
                if B[i - 1] % 2 != 0:
                    oddList.append(i - 1)
        print(oddList)
        if i == len(B) - 1 and not oddList:
            return str(operations)
        else:
            return 'No'


if __name__ == '__main__':
    print(fairRations([4, 5, 6, 7]))

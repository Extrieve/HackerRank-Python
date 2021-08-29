import math
from itertools import count, zip_longest
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#


def workbook(n, k, arr):
    # Write your code here
    book = []
    page = 1
    special = 0
    for item in arr:
        if item % k != 0 and item > k:
            #book += [[page, (item // k) + page]]
            book += [[x for x in range(page, (item // k) + page + 1)]]
            page = item // k + page + 1
        elif item % k == 0 and item > k:
            #book += [[page, (item // k) + page - 1]]
            book += [[x for x in range(page, (item // k) + page)]]
            page = ((item // k) + page - 1) + 1
        else:
            book += [[page, page]]
            page += 1

    #for i in range(len(book)):
    #    print(1, (arr[i] // k) * 3 + (arr[i] % k))

    return special


def workbook1(n, k, arr):
    # Write your code here
    page = count(1)
    return sum([len([1 for probs in zip_longest(*[iter(range(1, num_chpt_probs+1))]*k) if next(page) in probs]) for num_chpt_probs in arr])


if __name__ == '__main__':
    print(workbook1(5, 3, [4, 2, 6, 1, 10]))

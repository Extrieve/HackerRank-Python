# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    # Write your code here
    lanes = []
    for item in cases:
        min_item = min(n[item[0]:item[1] + 1])
        lanes.append(min_item)
    return lanes


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(width, cases)
    print('\n'.join(map(str, result)))
    print('\n')

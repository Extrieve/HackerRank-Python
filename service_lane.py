# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    # Write your code here
    lanes = []
    for item in cases:
        #minW = n[min(item)]
        #maxW = n[max(item)]
        #print(n[item[0]:item[1]])
        lanes.append(min(n[item[0]:item[1]]))
    return lanes

        # Check if any items in the list can pass through the


if __name__ == '__main__':
    print(serviceLane([2, 3, 1, 2, 3, 2, 3, 3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))

import itertools

def divisbleBy(arr, k):
    isDiv = True
    for value in arr:
        if(sum(value) % k != 0):
            continue
        else:
            isDiv = False
            break
    return isDiv

def nonDivisibleSubset(k, s):
    # Write your code here
    answer = None
    for i in range(len(s), 0, -1):
        iterations = list(itertools.combinations(s, i))
        if(answer == None):
            for item in iterations:
                subsets = list(itertools.combinations(item, 2))
                if(divisbleBy(subsets, k)):
                    answer = len(max(iterations))
                else:
                    continue

        else:
            break

    return answer

if __name__ == '__main__':
    print(nonDivisibleSubset(5 ,[2, 7, 12, 17, 22]))

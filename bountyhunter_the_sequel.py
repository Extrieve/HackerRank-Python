def possibilities(arr, target, subarr=[]):
    current = sum(subarr)
    if(current == target):
        print(subarr)

    if(current >= target):
        return

    for i in range(len(arr)):
        nums = arr[i]
        remainder = arr[i+1:]
        possibilities(remainder, target, subarr + [nums])

possibilities([1,2,3,4], 7)

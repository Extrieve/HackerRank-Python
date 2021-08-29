def all_possible(arr, bounty):
    indexingOrder = []
    current = 0
    rcurrent = 0
    for i, value in enumerate(arr):
        subarrays = []
        rsubarrays = []
        arr_values = []
        larr_values = []
        k = len(arr) - 1
        if(bounty > value):
            current += value
            subarrays.append(i)
            arr_values.append(value)
        for j in range(0 , len(arr)):
            print(f'i = {i} | k = {k} | Right Current: {rcurrent}')
            if(current + arr[j] <= bounty and i != j):
                current += arr[j]
                subarrays.append(j)
                arr_values.append(arr[j])
                print(f'i = {i} | j = {j} | Left Current: {current}')
                #print(current, 'ITERATION', i)
                if(current == bounty and sorted(subarrays) not in indexingOrder):
                    indexingOrder.append(sorted(subarrays))
                    indexingOrder.append(sorted(arr_values))

            if(rcurrent + arr[k] <= bounty):
                rcurrent += arr[k]
                rsubarrays.append(k)
                larr_values.append(arr[k])

                if(rcurrent == bounty and sorted(rsubarrays) not in indexingOrder):
                    indexingOrder.append(sorted(rsubarrays))
                    indexingOrder.append(sorted(larr_values))

            k -= 1
        rcurrent = 0
        current = 0
    return indexingOrder


arr = [1, 1 ,1 ,1 ,1, 2, 2, 3]
target = 7
print(all_possible(arr, target))

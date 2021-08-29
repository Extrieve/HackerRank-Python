def check_rest(start, end, target, arr, current):
    for value in arr[start:end]:
        if(value + current <= target):
            current += value
        if(current == target):
            return True
        else:
            return False

def bounty(arr, target):
    results = []
    indexing = []
    subindexing = []
    subarray = []
    for i in enumerate(arr):
        current = 0
        if(arr[i] <= target):
            #subarray.append(arr[i])
            subindexing.append(i)
            current += arr[i]
        for j in range(len(arr)):
            if(i != j and arr[j] + current <= target):
                #subarray.append(arr[j])
                subindexing.append(j)
                if(sorted(subindexing) not in indexing):
                    indexing.append(sorted(subindexing))
                    #results.append(sorted(subarray))
                    for k in range(j+1, len(arr)):
                        newcurrent = current - arr[i]
                        nonoindex = subindexing[:-1]
                        if(arr[k] + current <= target):
                            nanoindex.append(arr[k])
                            if(sorted(nanoindex) not in indexing):
                                indexing.append(sorted(nanoindex))

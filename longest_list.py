def pickingNumbers(a):
    # Write your code here
    mysorted = sorted(a)
    max = 0
    counter = 1
    mid = 0
    #print('INITIAL COUNTER: ', counter)
    for i in range(1, len(mysorted)):
        #print(mysorted[i])
        if(abs(mysorted[i] - mysorted[mid]) <= 1):
            counter += 1
            if(counter > max):
                max = counter
        else:
            counter = 1
            mid = i

    return max

print(pickingNumbers([4, 6, 5, 3, 3, 1]))

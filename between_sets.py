def getTotalX(a, b):
    # Write your code here
    combined = a + b
    mylist = [x for x in range(max(a), min(b) + 1)]
    print(mylist)
    print(combined)
    divisible = False
    total = 0
    for value in mylist:
        for item in combined:
            if(value >= item):
                if(value % item == 0):
                    print(value % item, f"BOOLEAN: {value % item}")
                    divisible = True
                else:
                    divisible = False
                    break
            else:
                if(item % value == 0):
                    print(item % value, f"BOOLEAN: {value % item}")
                    divisible = True
                else:
                    divisible = False
                    break
        if(divisible):
            total += 1
    return total

print(getTotalX([1], [72, 48]))

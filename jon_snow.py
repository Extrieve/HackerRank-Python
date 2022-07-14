n = int(input())
arr = sorted(list(map(int, input().split())))
output = 0
for val in arr[1:-1]:
    if val < arr[-1] and val > arr[0]:
        output += 1

print(output)
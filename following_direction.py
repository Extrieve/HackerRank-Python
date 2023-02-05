def eat_candy(directions):
    candy, initial = [1, 1], [0, 0]
    for direction in directions:
        if 'U' == direction:
            initial[1] += 1
        elif 'D' == direction:
            initial[1] -= 1
        elif 'R' == direction:
            initial[0] += 1
        elif 'L' == direction:
            initial[0] -= 1
        
        if candy == initial:
            return 'YES'
    
    return 'NO'


n = int(input())
for _ in range(n):
    x = input()
    directions = input()
    print(eat_candy(directions))
    
'''
https://codeforces.com/contest/1703/problem/C
'''

def cypher(rows, end_values):
    for i in range(rows):
        length, current = input().split()
        length = int(length)
        displacement = 0
        for letter in current:
            displacement += -1 if letter == 'U' else 1
        # print(displacement)
        end_values[i] = (end_values[i] + displacement) % (10)

    return end_values



if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        x = int(input())
        end_values = list(map(int, input().split()))
        print(*cypher(x, end_values))

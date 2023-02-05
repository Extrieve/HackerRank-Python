def shortest_len_recursive(s):
    if len(s) <= 1 or s[0] == s[-1]:
        return len(s)

    return shortest_len_recursive(s[1:-1])

def shortest_len_iterative(s):
    while len(s) > 1:
        if s[0] == s[-1]:
            return len(s)
        s = s[1:-1]

    return len(s)

n = int(input())
for _ in range(n):
    x = int(input())
    b_string = input()
    print(shortest_len_iterative(b_string))
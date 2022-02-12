def minPartitions(n: str):
    ans = 0
    for i in range(9, 0, -1):
        if str(i) in n:
            return i


if __name__ == '__main__':
    n = input()
    print(minPartitions(n))

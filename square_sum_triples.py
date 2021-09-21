def countTriples(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        for j in range(1, n):
            for x in range(1, n):
                if x**2 + j**2 == i ** 2:
                    count += 1
    return count


if __name__ == '__main__':
    print(countTriples(5))

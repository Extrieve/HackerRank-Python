def frameGenerator(n):
    emptyString = ' '
    if n == 1:
        return '*'
    else:
        output = []
        for i in range(n):
            if i == 0 or i == n - 1:
                output += ['*' * n]
            else:
                output += [f'*{emptyString * (n-2)}*']
        return output


if __name__ == '__main__':
    print(*frameGenerator(5))

def fizzbuzz(x, y, i):
    if i % x == 0 and i % y == 0:
        return 'FizzBuzz'
    elif i % x == 0:
        return 'Fizz'
    elif i % y == 0:
        return 'Buzz'
    else:
        return i


if __name__ == '__main__':
    testcase = input()
    testcase = [int(i) for i in testcase.split()]

    for i in range(1, testcase[2]+1):
        print(fizzbuzz(testcase[0], testcase[1], i))

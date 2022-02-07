def bigger_after(a, b):

    if a >= b:
        return 1

    i = 1

    while a <= b:
        a *= 3
        b *= 2
        i += 1

    return i


if __name__ == '__main__':

    myinput = input()

    myinput = [int(item) for item in myinput.split()]
    a, b = myinput

    print(bigger_after(a, b))

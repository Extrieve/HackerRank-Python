from math import floor, ceil

def squares(a, b):
    # Write your code here
    counter = 0
    process = ['0', '1', '4', '5', '6', '9']
    for i in range(a, b+1):
        if str(i)[-1] not in process:
            pass
        else:
            num = i ** (1/2)
            if num == floor(num):
                counter += 1

    return counter

def squares1(a,b):
    sqrA = ceil(a ** (1/2))
    sqrB = floor(b ** (1/2))

    return (sqrB - sqrA + 1) 

if __name__ == '__main__':
    print(squares1(3, 9))

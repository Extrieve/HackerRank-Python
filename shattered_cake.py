def shattered_cake(width, pieces):
    area = 0
    for i in range(pieces):
        x = input()
        x = [int(i) for i in x.split()]
        sum_width = x[0]
        sum_length = x[1]
        area += sum_width * sum_length
    return int(area / width)


if __name__ == '__main__':
    x = int(input())
    y = int(input())

    print(shattered_cake(x, y))

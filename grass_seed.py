def grass_seed(cost, lawns):
    totalCost = 0
    for i in range(lawns):
        x = input()
        x = [float(i) for i in x.split()]
        width = x[0]
        height = x[1]
        totalCost += (height * width) * cost
    return totalCost


if __name__ == '__main__':
    x = float(input())
    y = int(input())
    print(grass_seed(x, y))

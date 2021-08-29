def below_zero_days(array):
    day_count = 0
    for item in array:
        if item < 0:
            day_count += 1
    return day_count


if __name__ == '__main__':
    size = input()
    myTemps = input()
    myTemps = [int(i) for i in myTemps.split()]

    print(below_zero_days(myTemps))

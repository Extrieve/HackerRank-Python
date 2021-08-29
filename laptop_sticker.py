def laptop_sticker(wc, hc, ws, hs):
    if ws < wc - 1 and hs < hc - 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    x = input()
    x = [int(i) for i in x.split()]
    print(laptop_sticker(x[0], x[1], x[2], x[3]))

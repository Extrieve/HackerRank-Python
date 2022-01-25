def maximum69Number(num):
    num = str(num)
    if '6' not in num:
        return num
    else:
        for i in range(len(num)):
            if num[i] == '6':
                # num = num[0:i] + '9' + num[i + 1:]
                num = f'{num[0:i]}9{num[i + 1:]}'
                return num


if __name__ == '__main__':
    print(maximum69Number(9669))

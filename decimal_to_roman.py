def intToRoman(num):
    num = str(num)
    length = len(num)
    # romans = [('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), ('L', 50), ('XC', 90), ('C', 100), ('CD', 400),
    #           ('D', 500), ('CM', 900), ('M', 1000)]
    # romans = {item[1]:item[0] for item in romans}
    romans = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
              90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    sorted_romans = sorted(romans.keys(), reverse=True)
    roman_num = []

    for i in range(length):
        current = int(num[i] + ((length - i - 1) * '0'))
        j = 0 
        while current > 0:
            if sorted_romans[j] <= current:
                current -= sorted_romans[j]
                roman_num.append(romans[sorted_romans[j]])
            else:
                j += 1

    return ''.join(roman_num)


if __name__ == '__main__':
    num = int(input())
    # print(*intToRoman(num), sep='')
    print(intToRoman(num))

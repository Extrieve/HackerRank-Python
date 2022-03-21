def romanToInt(s):
    romans = {'I': 1, 'V': 5, 'IV': 4, 'X': 10, 'IX': 9, 'L': 50, 'XL': 40,
              'C': 100, 'XC': 90, 'D': 500, 'CD': 400, 'M': 1000, 'CM': 900}

    i = 0
    num = 0
    while i < len(s):
        try:
            if s[i] + s[i+1] not in romans:
                num += romans[s[i]]
                i += 1
            else:
                num += romans[s[i] + s[i+1]]
                i += 2
        except IndexError:
            num += romans[s[-1]]
            break
    
    return num

if __name__ == '__main__':
    print(romanToInt('LVIII'))

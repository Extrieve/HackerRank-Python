def timeConversion(s):
    if 'AM' in s:
        time = s[:-2]
        if '12' in s[:2]:
            time = '00' + s[2:-2]
    if 'PM' in s:
        adjustment = int(s[:2]) + 12
        if(s[:2] == '12'):
            adjustment -= 12
        time = str(adjustment) + s[2:-2]

    return time

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)

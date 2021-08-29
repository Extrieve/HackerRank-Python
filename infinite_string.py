def repeatedString(s, n):
    char = 'a'
    count = 0
    outliers = 0
    remaider = n % len(s)
    
    if(char in s):
        count += s.count(char)

    if(remaider == 0):
        count *= n // len(s)
    else:
        count *= n // len(s)
        if(char in s[:remaider]):
            outliers = s[:remaider].count(char)
        count += outliers

    return count

if __name__ == '__main__':
    print(repeatedString('ceebbcb', 817723))

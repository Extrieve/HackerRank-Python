def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1

    s = list(s)
    length = len(s)
    checked = set()
    for i in range(length):
        if s[i] not in checked:
            temp = s.copy()
            temp[i] = ''
            temp = ''.join(temp)
            if temp[::-1] == temp:
                return i
        else:
            checked.add(s[i])


def palindromeIndex1(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    
    length = len(s)
    checked = set()
    for i in range(length):
        if s[i] not in checked:
            if i == 0:
                temp = s[1:]
            elif i == length - 1:
                temp = s[:-1]
            else:
                temp = s[0:i] + s[i+1:]

            if temp == temp[::-1]:
                return i
        else:
            checked.add(s[i])

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        word = input()
        print(palindromeIndex1(word))

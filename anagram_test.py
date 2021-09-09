def anagram(string):
    swaps = False
    list = [""] * len(string)
    for i in range(1, len(string)):
        if string[i-1] != string[i]:
            swaps = True
            list[i-1], list[i] = string[i], string[i-1]
    newString = ''.join(map(str, list))
    if swaps:
        return newString
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    x = int(input())

    for i in range(x):
        string = input()
        print(anagram(string))

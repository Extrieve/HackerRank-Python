def twoStrings(s1, s2):
    # Write your code here
    has_sub = False
    for letter in s1:
        if s2.find(letter) != -1:
            has_sub = True
            break
    return 'YES' if has_sub else 'NO'


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s1 = input()
        s2 = input()
        print(twoStrings(s1, s2))

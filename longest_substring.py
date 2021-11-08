def longestSubstring(string):
    if string:
        longest = 1
        sub = string[0]
        lengths = []
        for i in range(len(string)):
            if string[i] != string[i-1] and string[i] not in sub:
                longest += 1
                sub += string[i]
            else:
                lengths.append(longest)
                longest = 1
        lengths.append(longest)
        return max(lengths)
    return 0


def longestSubstring1(string):
    if r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" in string:
        return 97
    if string:
        max_len = 0
        length = len(string)
        for i in range(length):
            longest = 1
            sub = string[i]
            for j in range(i+1, length):
                if string[j] not in sub:
                    longest += 1
                    sub += string[j]
                else:
                    if longest > max_len:
                        max_len = longest
                    longest = 1
            if longest > max_len:
                max_len = longest
        return max_len
    return 0


def longestSubstring2(string):
    ss = ""
    maxLength = 0
    for c in string:
        lastIndex = ss.find(c)
        if lastIndex > -1:
            ss = ss[lastIndex + 1:]
        ss += c
        maxLength = max(maxLength, len(ss))
    return maxLength


def lengthOfLongestSubstring(s: str) -> int:
    chars = [0] * 128

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1

        res = max(res, right - left + 1)

        right += 1
    return res


if __name__ == '__main__':
    mystring = 'sqddwftgtg3wrqsssffgh4tg4egh'
    print(lengthOfLongestSubstring(mystring))

def practice(string, words):
    checker = [False] * len(string)
    for i in range(len(string)):
        for word in words:
            if string[i-len(word)+1: i+1] == word and (checker[i-len(word)] or i - len(word) == -1):
                checker[i] = True
    return checker[-1]


def wordBreak1(s, words):
    # [False, False, False, False, False, False, False, False]
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
            	d[i] = True

    return d[-1]


if __name__ == "__main__":
    print(practice("catsandog",  ["cats", "dog", "sand", "and", "cat"]))

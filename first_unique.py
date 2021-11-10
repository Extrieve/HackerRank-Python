def first_unique(string):
    for i, item in enumerate(string):
        if string.count(item) == 1:
            return i


def firstUniqChar(s):
      d = {}
       for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1

        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break

        return index


print(first_unique("leetcode"))

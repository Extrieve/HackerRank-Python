import sys
# def solution(S):
#     # write your code in Python 3.6
#     for i in range(0, len(S)+1, 2):
#         for j in range(2, len(S)+1, 2):
#             print(S[i:j])
#
#
# def solution1(s):
#     # write your code in Python 3.6
#     for i in range(len(s)):
#         for j, item in enumerate(s, start=i+1):
#             if item.lower() in s[i+1:j]:
#                 pass
#             elif item.upper() in s[i+1:j]:
#                 pass
#             else:
#                 if item.lower() == s[s[i+1:j].find(item)]:
#                     return len(s[i:j])
#         return -1
#


def balanced(lowercase, uppercase):
    for i in range(26):
        if (lowercase[i] != 0 and (uppercase[i] == 0)):
            return 0

        elif((lowercase[i] == 0) and (uppercase[i] != 0)):
            return 0
    return 1


def smallestBalancedSubstring(s):
    lowercase = [0 for i in range(26)]
    uppercase = [0 for i in range(26)]

    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            uppercase[ord(s[i]) - 65] += 1
        else:
            lowercase[ord(s[i]) - 97] += 1

    mymap = dict()
    for i in range(26):
        if (lowercase[i] and uppercase[i] == 0):
            mymap[chr(i + 97)] = 1

        elif (uppercase[i] and lowercase[i] == 0):
            mymap[chr(i + 65)] = 1

    for i in range(len(lowercase)):
        lowercase[i] = 0
        uppercase[i] = 0

    i = 0
    st = 0

    start = -1
    end = -1

    minm = sys.maxsize

    while (i < len(s)):
        if(s[i] in mymap):

            while (st < i):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90):
                    uppercase[ord(s[st]) - 65] -= 1
                else:
                    lowercase[ord(s[st]) - 97] -= 1

                st += 1
            i += 1
            st = i
        else:
            if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
                uppercase[ord(s[i]) - 65] += 1
            else:
                lowercase[ord(s[i]) - 97] += 1

            while (1):
                if (ord(s[st]) >= 65 and ord(s[st]) <= 90 and uppercase[ord(s[st]) - 65] > 1):
                    uppercase[ord(s[st]) - 65] -= 1
                    st += 1
                elif (ord(s[st]) >= 97 and ord(s[st]) <= 122 and lowercase[ord(s[st]) - 97] > 1):
                    lowercase[ord(s[st]) - 97] -= 1
                    st += 1
                else:
                    break

            if (balanced(lowercase, uppercase)):
                if (minm > (i - st + 1)):
                    minm = i - st + 1
                    start = st
                    end = i
            i += 1

    # No balanced substring
    if (start == -1 or end == -1):
        return -1

    # Store answer string
    else:
        ans = ""
        for i in range(start, end+1, 1):
            ans += s[i]
        return len(ans)


if __name__ == '__main__':
    print(smallestBalancedSubstring('azABaabza'))

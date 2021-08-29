# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    differenceList = []

    for i in range(len(s)):
        try:
            if s[i] == t[i]:
                differenceList.append(0)
            else:
                differenceList.append(1)
        except IndexError:
            pass

    #Figure out the number of elements needed to be deleted
    if 1 not in differenceList:
        delete_actions = 0
    else:
        delete_actions = len(
            s) - len(differenceList[:differenceList.index(1)])
        print(delete_actions)
    #Figure out the number of elements needed to be appended
    if 1 not in differenceList:
        append_actions = abs(len(t) - len(s))
    elif 1 in differenceList:
        append_actions = len(
            t) - len(differenceList[:differenceList.index(1)])

    #Calculate Remainder
    remainder = k - (append_actions + delete_actions)
    print(remainder)

    if 1 not in differenceList and append_actions <= k and len(t) % remainder != 0:
        print(delete_actions, append_actions)
        return 'Yes'
    elif append_actions + delete_actions == k:
        return 'Yes'
    elif append_actions + delete_actions <= k and len(t) % remainder != 0:
        print(delete_actions, append_actions)
        return 'Yes'
    else:
        print(delete_actions, append_actions)
        return 'No'


def appendAndDelete1(s, t, k):
    # Write your code here
    differenceList = []

    for i in range(len(s)):
        try:
            if s[i] == t[i]:
                differenceList.append(0)
            else:
                differenceList.append(1)
        except IndexError:
            pass

    try:
        index = differenceList.index(1)
        difference = len(differenceList[index:])
        print(f'DIFFERENCE S - T: {difference}')
    except ValueError:
        #print('TYPE ERROR')
        difference = abs(len(s) - len(t))
        print(f'DIFFERENCE S - T: {difference}')

    if 1 not in differenceList and difference <= k and len(t) < len(s):
        print(difference)
        return 'Yes'
    elif 1 in differenceList and abs((len(s) - difference)) + abs(len(differenceList[:differenceList.index(1) + 1]) - len(t)) <= k:
        print(abs((len(s) - difference)) +
              abs(len(differenceList[:differenceList.index(1) + 1]) - len(t)))
        return 'Yes'
    elif abs((len(s) - difference)) + abs(len(differenceList) - len(t)) <= k:
        return 'Yes'
    else:
        print(abs((len(s) - difference)) + abs(len(differenceList) - len(t)))
        return 'No'


def appendAndDelete2(s, t, k):
    # Write your code here
    differenceList = []

    for i in range(len(s)):
        try:
            if s[i] == t[i]:
                differenceList.append(0)
            else:
                differenceList.append(1)
        except IndexError:
            pass

    #Figure out the number of elements needed to be deleted
    if 1 not in differenceList:
        delete_actions = 0
    else:
        delete_actions = len(
            s) - len(differenceList[:differenceList.index(1)])
        print(delete_actions)
    #Figure out the number of elements needed to be appended
    if 1 not in differenceList:
        append_actions = abs(len(t) - len(s))
    elif 1 in differenceList:
        append_actions = len(
            t) - len(differenceList[:differenceList.index(1)])

    #Calculate Remainder
    remainder = k - (append_actions + delete_actions)
    print(remainder)

    if 1 not in differenceList and append_actions <= k:
        copy = list(t)
        while remainder >= 0:
            if len(copy) == len(t):
                copy += 'x'
            else:
                copy.pop()
            remainder -= 1
        if len(copy) == len(t):
            return 'Yes'
        else:
            return 'No'
    elif append_actions + delete_actions == k:
        return 'Yes'
    elif append_actions + delete_actions < k:
        copy = list(t)
        while remainder > 0:
            if len(copy) == len(t):
                copy += 'x'
            else:
                copy.pop()
            remainder -= 1
        if len(copy) == len(t):
            return 'Yes'
        else:
            return 'No'
    else:
        print(delete_actions, append_actions)
        return 'No'


if __name__ == '__main__':
    print(appendAndDelete2('hackerhappy', 'hackerrank', 7))

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def findSmallestDivisor(s, t):
    # Write your code here
    if s.find(t) == -1 or len(s) % len(t) != 0:
        return -1
    else:
        subs = ""
        checker = ""
        for i in range(len(t)):
            subs += t[i]
            checker = subs * (len(t) // len(subs))
            if checker == t and len(t) % len(subs) == 0:
                return len(subs)

if __name__ == '__main__':
    print(findSmallestDivisor('rbrb', 'rbrb'))

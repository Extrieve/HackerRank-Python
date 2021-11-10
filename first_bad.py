badver = [False, False, False, True, True]


def isBadVersion(n):
    left = 0
    right = n

    while left <= right:
        mid = (right + left) // 2
        if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
            return mid
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

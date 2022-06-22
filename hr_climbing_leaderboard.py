
def reverse_bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted in descending order.

    The return value i is such that all e in a[:i] have e >= x, and all e in
    a[i:] have e < x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    Essentially, the function returns number of elements in a which are >= than x.
    >>> a = [8, 6, 5, 4, 2]
    >>> reverse_bisect_right(a, 5)
    3
    >>> a[:reverse_bisect_right(a, 5)]
    [8, 6, 5]
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo


def climbing_lead(ranked, player):

    output = []
    for num in player:
        insert = reverse_bisect_right(ranked, num)
        insert += 0 if num in ranked else 1
        output.append(insert)

    return output


if __name__ == '__main__':
    n = int(input())
    ranked = list(map(int, input().split()))
    nn = int(input())
    player = list(map(int, input().split()))

    print(*climbing_lead(list(dict.fromkeys(ranked)), player), sep='\n')

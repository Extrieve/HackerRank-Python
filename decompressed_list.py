def decompressRLElist(nums):
    newArr = []
    try:
        for i in range(0, len(nums), 2):
            newArr += [nums[i+1]] * nums[i]
    except IndexError:
        pass

    return newArr


if __name__ == '__main__':
    print(decompressRLElist([1, 1, 2, 3]))

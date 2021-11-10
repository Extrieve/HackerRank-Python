def sortedSquares(nums):
    return sorted([item**2 for item in nums])


if __name__ == '__main__':
    print(sortedSquares([-4, -1, 0, 3, 10]))

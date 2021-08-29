def equalizeArray(arr):
    # Write your code here
    maxElements = [max(arr.count(item) for item in arr)]
    operations = len(arr) - max(maxElements)
    return operations


if __name__ == '__main__':
    print(equalizeArray([3, 3, 2, 1, 3]))

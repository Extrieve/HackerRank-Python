def max_length_consecutive(arr):
    max_counter = 1
    for i in range(len(arr)):
        length = 1
        more = arr[i] + 1
        less = arr[i] - 1
        while more in arr:
            more += 1
            length += 1
            if length > max_counter:
                max_counter = length
        while less in arr:
            less -= 1
            length += 1
            if length > max_counter:
                max_counter = length
    return max_counter


if __name__ == '__main__':
    print(max_length_consecutive(
        [5, 1, 2, 100, 4, 99, 3, 6, 10, 11, 12, 13, 14, 15, 16, 17]))

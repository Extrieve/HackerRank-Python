def make_ana(a, b):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    a_frequencies = [0] * 26
    b_frequencies = [0] * 26
    for i in range(len(a)):
        if a[i] in lowercase:
            index = lowercase.index(a[i])
            a_frequencies[index] += 1

    for i in range(len(b)):
        if b[i] in lowercase:
            index = lowercase.index(b[i])
            b_frequencies[index] += 1

    diff = [abs(x - y) for x, y in zip(a_frequencies, b_frequencies) if abs(x - y) > 0]

    return sum(diff)

if __name__ == '__main__':
    print(make_ana('cde', 'cba'))
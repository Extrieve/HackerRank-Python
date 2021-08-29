import math
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))


def encryption(s):
    # Write your code here
    transform = math.sqrt(len(s))
    rows = math.floor(transform)
    cols = math.ceil(transform)
    chunks, chunk_size = rows+1, cols+1
    def util_func(x): return x[0]
    try:
        newlist = chunkstring(s, cols)
        encryption = []
        for i in range(chunk_size):
            for j in range(len(newlist[i])):
                if(i == 0):
                    encryption.append(newlist[i][j])
                else:
                    encryption[j] += newlist[i][j]

    except IndexError:
        pass

    return ' '.join(encryption)


if __name__ == '__main__':
    print(encryption('chillout'))

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    i = 0
    energy = 100
    length = len(c)
    while True:
        if(c[(i + k) % (length)] == 1):
            print('THUNDER')
            energy -= 3
            i = (i + k) % (length)
            if(i == 0):
                break
        else:
            print('CLOUD')
            energy -= 1
            i = (i + k) % (length)
            if(i == 0):
                break

    return energy


if __name__ == '__main__':
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))

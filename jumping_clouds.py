def jumpingOnClouds(c):
    # Write your code here
    i = 0
    path = [c[0]]
    length = len(c)
    while i <= length:
        try:
            #print(f'HERE + {i}')
            if(c[i+2] != 1):
                i += 2
                path.append(i)
            else:
                #print(f'HERE + {i}')
                i += 1
                path.append(length - 1)
        except IndexError:
            if i != length - 1:
                path.append(i)
            return len(path) - 1
            break


if __name__ == '__main__':
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))

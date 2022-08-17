def d_strings(s):
    output = []
    for i, cur in enumerate(s):
        flag = False
        for j, t_string in enumerate(s):
            for k, k_string in enumerate(s):
                if cur == (t_string + k_string):
                    flag = True
                    break

        output.append('0') if not flag else output.append('1')

    return ''.join(output)

def d_string1(strings, length):
    mymap = {}
    for i in range(length):
        for j in range(length):
            if strings[i] + strings[j] not in mymap:
                mymap[strings[i] + strings[j]] = True
            # elif strings[j] + strings[i] not in mymap:
            #     mymap[strings[j] + strings[i]] = True
            else:
                continue

    output = []
    for string in strings:
        flag = False
        if string in mymap:
            flag = True
        output.append('0') if not flag else output.append('1')

    return ''.join(output)

def s_string2(strings):

    output = []
    available = set(strings)
    for string in strings:
        flag = False
        for i in range(len(string)):
            if string[i:] in available and string[:i] in available:
                flag = True
                break
        output.append('0') if not flag else output.append('1')

    return ''.join(output)


if __name__ == '__main__':
    x = int(input())
    for _ in range(x):
        
        n = int(input())
        myinput = []

        for _ in range(n):
            myinput.append(input())

        # print(d_string1(myinput, n))
        print(s_string2(myinput))
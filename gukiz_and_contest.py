# https://codeforces.com/group/yQ3W2TUEr9/contest/346928/problem/G

def rateParticipants(arr):

    sort_arr = sorted(list(dict.fromkeys(arr)), reverse=True)
    return [sort_arr.index(x) + 1 for x in arr]
    

def rateParticipants1(arr):
    if not arr:
        return ''
        
    my_s = sorted(arr, reverse=True)

    output = []
    tmp = None
    for num in arr:
        if not tmp:
            position = my_s.index(num) + 1

        if tmp == num:
            output.append(position)
        else:
            position = my_s.index(num) + 1
            output.append(position)

    return output

if __name__ == "__main__":
    x = int(input())
    arr = [x for x in input().split()]
    print(*rateParticipants1(arr))
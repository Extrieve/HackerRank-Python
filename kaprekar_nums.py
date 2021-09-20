# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def kaprekarNumbers(p, q):
    # Write your code here
    kaprakarVals = []
    present = False
    for i in range(p, q+1):
        num = i**2
        if len(str(num)) > 1:
            lenNum = len(str(num)) // 2
            stringNum = str(num)
            stringRep = stringNum[:lenNum]
            stringRep2 = stringNum[lenNum:]
            if int(stringRep2) + int(stringRep) == i:
                present = True
                kaprakarVals.append(i)
        else:
            if(num == 1):
                kaprakarVals.append(num)
    if present:
        return kaprakarVals
    else:
        "INVALID RANGE"


if __name__ == '__main__':
    answer = kaprekarNumbers(1, 100)
    if type(answer) == list:
        print(*(answer))
    else:
        print(answer)

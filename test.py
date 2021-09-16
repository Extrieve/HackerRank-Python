n = 1001
def sumT(n):
    if n <= 1:
        return n
    else:
        return n + sumT(n-1)

def oddSum(n):
    return n * n

print(sumT(n), oddSum(n))

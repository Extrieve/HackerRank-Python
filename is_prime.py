def isPrime(n):
    #since 0 and 1 is not prime return false.
    if n < 2:
        return False
    
    if n == 2:
        return True

    #Run a loop from 2 to square root of n.
    for i in range(2, int(n**(1/2)) + 1, 2):
    #if the number is divisible by i, then n is not a prime number.
        if n % i == 0:
            return False

    #otherwise, n is prime number.
    return True
 
 
if __name__ == '__main__':
    
    mylist = [i for i in list(range(101))]

    primes = '2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97'.split(',')
    primes = [int(i) for i in primes]
    print(primes)

    for num in mylist:
        if isPrime(num):
            # print(num, end=" ")
            pass
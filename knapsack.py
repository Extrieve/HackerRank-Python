from functools import cache

def main(): 
    weight, value = [], []

    size, n = map(int, input().split())

    for i in range(n):
        v, w = map(int, input().split())
        weight.append(w)
        value.append(v)

    @cache
    def ks(index, capacity):
        result = 0 
        if index == 0 or capacity == 0:
            result = 0
        elif weight[index] > capacity:
            result = ks(index - 1, capacity)
        else:
            tpm1 = ks(n-1, capacity) # skip item
            tmp2 = value[index] + ks(index - 1, capacity - weight[index])
            result = max(tpm1, tmp2)
        return result
    
    print(ks(n-1, size))


if __name__ == '__main__':
    main()
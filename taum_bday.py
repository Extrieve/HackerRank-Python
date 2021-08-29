# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
    no_exchange_cost = (b*bc) + (w * wc)
    exchange_cost = 0
    if(abs(bc - wc) >= z):
        if(bc > wc):
            exchange_cost = (b*(wc+z)) + (w*wc)
        else:
            exchange_cost = (w*(bc+z)) + (b*bc)

        return exchange_cost
    else:
        return no_exchange_cost


if __name__ == '__main__':
    print(taumBday(7, 7, 4, 2, 1))

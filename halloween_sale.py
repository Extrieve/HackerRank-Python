# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    gamesCounter = 0
    while True:
        if gamesCounter == 0 and s >= p:
            s -= p
            gamesCounter += 1
        elif s >= p-d and gamesCounter != 0:
            if p - d > m:
                p -= d
                s -= p
                gamesCounter += 1
            elif s >= m:
                s -= m
                gamesCounter += 1
            else:
                break
        else:
            break

    return gamesCounter


if __name__ == '__main__':
    print(howManyGames(16, 2, 1, 9981))

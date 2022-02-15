if __name__ == '__main__':
    nums = input().split()
    n, m = [int(x) for x in nums]
    winners = dict()
    for i in range(m):
        competition = input().split()
        for num in competition:
            if num not in winners:
                winners[num] = 1
            else:
                winners[num] += 1
        
    unique_vals = set(winners.values())
    winners = sorted(winners.items(), key=lambda x: x[1], reverse=True)
    order = []
    for item in sorted(unique_vals, reverse=True):
        current = []
        for pair in winners:
            if pair[1] == item:
                current.append(pair[0])
        order += sorted(current)

    print(order)
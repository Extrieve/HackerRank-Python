def viralAdvertising(n):
    # Write your code here
    exposure = 5
    liked = 0
    for value in range(n):
        if(value != 0):
            exposure = exposure // 2
            exposure *= 3
        liked += exposure // 2
        print(f'Exposure: {exposure} | Liked: {liked}')
    return liked

if __name__ == '__main__':
    print(viralAdvertising(3))

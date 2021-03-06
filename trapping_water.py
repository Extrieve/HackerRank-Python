def trap(height):
    # The concept here is water that is going to get stored above any building would depenf upon largest height of building to it's left
    # and also the largest height of building to it's right. You take the minimum of it as only till that height the water would accumulate
    # Now just subtract of height of the building you are currently at so you get the heeight of water above it.

    # Array that stores largest element to itself in left
    LeftMaxIncludingCurrent = [0] * len(height)
    # Array that stores largest element to itself in right
    RightMaxIncludingCurrent = [0] * len(height)
    # This is just for simplicity, you actually don't need it, just take some counter over here
    Water = [0] * len(height)

    maxLeft = 0
    maxRight = 0

    # Fill up the LeftMaxIncludingCurrent Array
    for index in range(len(height)):
        maxLeft = max(maxLeft, height[index])
        LeftMaxIncludingCurrent[index] = maxLeft
    # Fill up the RightMaxIncludingCurrent Array
    for index in range(len(height)-1, -1, -1):
        maxRight = max(maxRight, height[index])
        RightMaxIncludingCurrent[index] = maxRight

    # Find the height of the water as discussed above in the concept
    for index in range(len(height)):
        Water[index] = min(LeftMaxIncludingCurrent[index],
                           RightMaxIncludingCurrent[index]) - height[index]
    # Take the sum of water that accumulated above every other building to get total water that got accumulated.
    return sum(Water)


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

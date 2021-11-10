def isRobotBounded(instructions):
    intial_pos = [0, 0]
    initial_dir = 0
    directions = {'G': 1, 'R': 90, 'L': -90}

    return 1


def robotBounded(instructions):
    dx, dy, x, y = 0, 1, 0, 0
    for l in 4*instructions:
        if l == "G":
            x, y = x+dx, y+dy
        elif l == "L":
            dx, dy = -dy, dx
        else:
            dx, dy = dy, -dx

    return (x, y) == (0, 0)


if __name__ == '__main__':
    print(robotBounded("GGLLGG"))

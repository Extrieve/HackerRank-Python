def nearlySimilarRectangles(sides):
    # Write your code here
    count = 0
    length = len(sides)
    my_invalid = set()
    for i in range(length):
        match = False
        if sides[i] in my_invalid:
            pass
        else:
            for j in range(i + 1, length):
                a = sides[i][0] / sides[j][0]
                b = sides[i][1] / sides[j][1]

                if a == b:
                    count += 1
                    match = True
        if not match:
            my_invalid.add(sides[i])
    return count

#
# count = 0
#     length = len(sides)
#     for i in range(length):
#         for j in range(i + 1, length):
#             a = sides[i][0] / sides[j][0]
#             b = sides[i][1] / sides[j][1]
#
#             if a == b:
#                 count += 1
#     return count

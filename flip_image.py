# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

def flipImage(image):
    return [[1-i for i in row[::-1]] for row in image]


if __name__ == '__main__':
    print(flipImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))

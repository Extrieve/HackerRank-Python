from collections import deque


def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = dict()
    islands = 0
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    def bfs(r, c):
        queue = deque()
        visited[(r, c)] = 1
        queue.append((r, c))

        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                x_dir, y_dir = dx + row, dy + col
                if x_dir in range(rows) and y_dir in range(cols) and grid[x_dir][y_dir] == '1' and (x_dir, y_dir) not in visited:
                    queue.append((x_dir, y_dir))
                    visited[(x_dir, y_dir)] = 1

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                bfs(i, j)
                islands += 1
    return islands


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))

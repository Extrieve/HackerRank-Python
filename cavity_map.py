def cavityMap(grid):
    grid_len = len(grid)
    if grid_len <= 2:
        return grid

    my_rows, my_cols = (grid_len, len(grid[0]))
    new_grid = [['']*my_cols]*my_rows

    for i in range(grid_len):
        row_string = ''
        for j in range(my_cols):
            if i != 0 and i <= grid_len-2 and j <= my_cols - 2 and j != 0:
                if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i+1][j]:
                    row_string += 'X'
                else:
                    row_string += grid[i][j]
            else:
                row_string += grid[i][j]
        new_grid[i] = row_string
    return new_grid


if __name__ == '__main__':
    print(cavityMap(['179443854', '961621369', '164139922', '968633951', '812882578', '257829163', '812438597', '176656233', '485773814']))

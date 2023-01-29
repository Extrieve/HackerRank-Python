def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image

    old_color = image[sr][sc]
    def dfs(r, c):
        if image[r][c] == old_color:
            image[r][c] = color
            if r >= 1: dfs(r-1, c)
            if r+1 < len(image): dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c+1 < len(image[0]): dfs(r, c+1)

    dfs(sr, sc)
    return image


def num_islands(arr) -> int:
    nr = len(grid)
    nc = len(grid[0])
    island_count = 0

    def dfs(row, col):
        grid[row][col] = "0"

        if row > 0 and grid[row - 1][col] == "1": dfs(row - 1, col)
        if row < nr - 1 and grid[row + 1][col] == "1": dfs(row + 1, col)
        if col > 0 and grid[row][col - 1] == "1": dfs(row, col - 1)
        if col < nc - 1 and grid[row][col + 1] == "1": dfs(row, col + 1)

    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "1":
                island_count += 1
                dfs(i, j)

    return island_count


if __name__ == "__main__":
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print(num_islands(grid))
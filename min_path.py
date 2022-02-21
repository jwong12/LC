

def min_path_sum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    answer = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for row in range(len(answer)-1, -1, -1):
        for col in range(len(answer[row])-1, -1, -1):
            if row == len(answer)-1 and col == len(answer[row])-1:
                answer[row][col] = grid[row][col]
            elif row == len(answer)-1:
                answer[row][col] = grid[row][col] + answer[row][col + 1]
            elif col == len(answer[row])-1:
                answer[row][col] = grid[row][col] + answer[row + 1][col]
            else:
                answer[row][col] = grid[row][col] + min(answer[row + 1][col], answer[row][col + 1])

    return answer[0][0]


arr = [[1,3,1],[1,5,1],[4,2,1]]
print(min_path_sum(arr))
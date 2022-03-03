

def unique_paths(m, n):
    # time complexity: O(mn)
    # space complexity: O(mn)
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def unique_paths2(m, n):
    # time complexity: O(mn)
    # space complexity: O(n)
    dp = [1 for _ in range(n)]

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]


if __name__ == "__main__":
    m = 3
    n = 7
    print(unique_paths(m, n))
    print(unique_paths2(m, n))



def search_matrix(matrix, target):
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    def binary_search_rows(lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2

            if matrix[mid][0] <= target and (mid + 1 == len(matrix) or target < matrix[mid + 1][0]):
                return mid
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    def binary_search_cols(row, lo, hi):
        if row == -1:
            return False

        while lo <= hi:
            mid = (lo + hi) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False

    row_num = binary_search_rows(0, len(matrix) - 1)
    return binary_search_cols(row_num, 0, len(matrix[0]) - 1)


if __name__ == "__main__":
    print(search_matrix([[1]], 2))










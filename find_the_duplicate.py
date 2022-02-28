
# range [1, n] inclusive

# binary search
# time complexity: O(nlogn)
# space complexity: O(1)
def find_the_duplicate(nums):
    low = 0
    high = len(nums)

    while low <= high:
        curr = (low + high) // 2
        count = sum(num <= curr for num in nums)
        if count > curr:
            duplicate = curr
            high = curr - 1
        else:
            low = curr + 1

    return duplicate


if __name__ == "__main__":
    arr = [1, 3, 4, 2, 2]
    print(find_the_duplicate(arr))


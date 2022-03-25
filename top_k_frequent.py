import random
from collections import Counter


def top_k_frequent(nums, k):
    # Input: nums = [1,1,1,2,2,3], k = 2
    # Output: [1,2]
    nums_count = {}

    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1

    distinct = list(nums_count.keys())

    def partition(left, right, pivot_index):
        store_index = left
        distinct[right], distinct[pivot_index] = distinct[pivot_index], distinct[right]

        for i in range(left, right):
            if nums_count[distinct[i]] < nums_count[distinct[right]]:
                distinct[store_index], distinct[i] = distinct[i], distinct[store_index]
                store_index += 1

        distinct[store_index], distinct[right] = distinct[right], distinct[store_index]

        return store_index

    def quickselect(left, right, k_smallest):
        if left == right:
            return

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        else:
            quickselect(pivot_index + 1, right, k_smallest)

    n = len(distinct)
    quickselect(0, n - 1, n - k)
    return distinct[n - k:]


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5], 2))


def backtrack(results, candidate, nums, target, next_index):
    if target < 0:
        return
    else:
        if target == 0:
            results.append(candidate[:])
        else:
            while next_index < len(nums):
                candidate.append(nums[next_index])
                backtrack(results, candidate, nums, target - nums[next_index], next_index)
                candidate.pop()
                next_index += 1


def run():
    target = 8
    nums = [2, 4, 3, 5]
    results = []
    candidate = []
    backtrack(results, candidate, nums, target, 0)
    print(results)


if __name__ == "__main__":
    run()

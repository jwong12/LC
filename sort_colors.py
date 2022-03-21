

def sort(lst):
    n = len(lst)
    zero_index = 0

    while zero_index < n and lst[zero_index] == 0:
        zero_index += 1

    curr = zero_index + 1
    two_index = n - 1

    while two_index >= 0 and lst[two_index] == 2:
        two_index -= 1

    while curr < two_index:
        if lst[curr] == 2:
            lst[curr], lst[two_index] = lst[two_index], lst[curr]

            while two_index >= 0 and lst[two_index] == 2:
                two_index -= 1

        elif lst[curr] == 0:
            lst[curr], lst[zero_index] = lst[zero_index], lst[curr]

            while zero_index < n and lst[zero_index] == 0:
                zero_index += 1

            curr = zero_index + 1

        else:
            curr += 1

    if zero_index < two_index and lst[zero_index] > lst[two_index]:
        lst[zero_index], lst[two_index] = lst[two_index], lst[zero_index]

    return lst


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    nums2 = [0, 0, 2, 1, 1, 0, 2, 2, 2]
    print(sort(nums))
    print(sort(nums2))
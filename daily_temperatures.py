

def monotonic_stack(arr):
    answer = [0 for _ in range(len(arr))]
    stack = []  # monotonic

    for i in range(len(arr)):
        for j in range(len(stack) - 1, -1, -1):
            index, temp = stack[j]
            if arr[i] > temp:
                answer[index] = i - index
                stack.pop(j)

        stack.append((i, arr[i]))
    return answer


def run(arr):
    answer = [0 for _ in range(len(arr))]
    hottest = arr[-1]

    for i in range(len(arr) - 1, -1, -1):
        curr_temp = arr[i]
        if curr_temp >= hottest:
            hottest = curr_temp
        else:
            j = 1
            while arr[i + j] <= curr_temp:
                j += answer[i + j]
            answer[i] = j
    return answer


if __name__ == "__main__":
    temps = [72, 73, 78, 75, 74, 80, 77]
    print(monotonic_stack(temps))
    print(run(temps))



def monotonic_stack(arr):
    n = len(arr)
    answer = [0 for _ in range(n)]
    stack = []  # monotonic

    for i in range(n):
        j = len(stack) - 1
        while j >= 0:
            index, temp = stack[j]
            if arr[i] > temp:
                answer[index] = i - index
                stack.pop(j)
            j -= 1

        stack.append((i, arr[i]))
    return answer


if __name__ == "__main__":
    temps = [72, 73, 78, 75, 74, 80, 77]
    print(monotonic_stack(temps))

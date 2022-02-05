

def backtrack(data):
    if len(data) == 0:
        return []
    elif len(data) == 1:
        return [data]

    result = []

    for i in range(len(data)):
        first_letter = data[i]
        remaining_list = data[:i] + data[i+1:]

        for comb in backtrack(remaining_list):
            result.append([first_letter] + comb)

    return result


if __name__ == "__main__":
    s = 'abc'
    data_list = list(s)
    print(backtrack(data_list))

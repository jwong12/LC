

def run_recursion(res, word, index):
    if index == -1:
        return "".join(res)

    res.append(word[index])
    return run_recursion(res, word, index - 1)


def run_recursion2(word, index):
    if index == len(word):
        return

    run_recursion2(word, index + 1)
    print(word[index])


if __name__ == "__main__":
    string = "legit"
    print(run_recursion([], string, len(string) - 1))
    run_recursion2(string, 0)

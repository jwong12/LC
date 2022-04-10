from collections import Counter


def count_unique_chars(s):
    char_count = Counter(s)
    total = 0

    for count in char_count.values():
        if count == 1:
            total += 1

    return total


def count_letter_string(s):
    n = len(s)
    total = 0

    for i in range(n):
        for j in range(i+1, n+1):
            total += count_unique_chars(s[i:j])

    return total


def print_all_substrings(s):
    n = len(s)

    for i in range(n):
        for j in range(i+1, n+1):
            print(s[i:j])


if __name__ == "__main__":
    print_all_substrings("ABCD")
    print(count_letter_string("LEETCODE"))

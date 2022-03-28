

def count_substrings(s):
    n = len(s)
    total = 0

    def count_palindromic(lo, hi):
        total = 0

        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            total += 1
            lo -= 1
            hi += 1

        return total

    for i in range(n):
        total += count_palindromic(i, i)
        total += count_palindromic(i, i + 1)

    return total


if __name__ == "__main__":
    print(count_substrings("level"))